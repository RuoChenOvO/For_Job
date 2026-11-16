"""arXiv 检索客户端。

负责：拼查询 URL → 发请求 → 解析 Atom XML → 返回论文列表。
"""

import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

# Atom 标准的命名空间（见 XML 根节点的 xmlns 声明）
# 前缀 "a" 是我们自己起的别名，换成 "atom" 也一样
NS = {"a": "http://www.w3.org/2005/Atom"}

DEFAULT_BASE_URL = "http://export.arxiv.org/api/query"

# arXiv 建议请求间隔约 3 秒，太频繁会被限流
DEFAULT_DELAY = 3.0


class ArxivClient:
    """arXiv API 客户端。

    用法：
        client = ArxivClient()                      # 用默认配置
        papers = client.search('all:"RAG" AND cat:cs.CL', 5)

        client = ArxivClient(timeout=5, delay=0)    # 测试时关掉等待
    """

    def __init__(
        self,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = 30,
        delay: float = DEFAULT_DELAY,
    ) -> None:
        # 把配置存到 self 上，后面的方法就能读到
        # self 就是"当前这个实例自己"：不同实例的 timeout 互不干扰
        self.base_url = base_url
        self.timeout = timeout
        self.delay = delay

    # ---------- 内部方法（下划线开头表示"不对外，只给自己用"）----------

    def _build_url(self, query: str, max_results: int) -> str:
        """把查询表达式拼成完整 URL。

        quote() 必须调用：URL 里不能有空格，而且 & 和 = 是 URL 的
        语法字符，查询里如果出现会被服务器误当成参数分隔符。
        """
        return (
            f"{self.base_url}"
            f"?search_query={urllib.parse.quote(query)}"
            f"&start=0&max_results={max_results}"
        )

    def _fetch(self, url: str) -> str:
        """发 HTTP 请求，返回 XML 文本。"""
        if self.delay:
            time.sleep(self.delay)
        with urllib.request.urlopen(url, timeout=self.timeout) as resp:
            return resp.read().decode("utf-8")

    # ---------- 对外方法 ----------

    def search(self, query: str, max_results: int = 10) -> list[dict]:
        """按 arXiv 查询表达式检索。

        参数：
            query: 完整表达式，例如 all:"retrieval augmented generation" AND cat:cs.CL
                   只传裸关键词也能用，但匹配很松（"augmentation" 会带进
                   认知增强、事实核查之类的论文），检索质量差。
            max_results: 最多返回几篇

        返回：
            list[dict]，每项含 title / summary / id / pdf_url
        """
        raw = self._fetch(self._build_url(query, max_results))
        root = ET.fromstring(raw)

        papers = []
        for entry in root.findall("a:entry", NS):
            paper = {
                "title": entry.find("a:title", NS).text.strip(),
                "summary": entry.find("a:summary", NS).text.strip(),
                "id": entry.find("a:id", NS).text.strip(),
            }
            # PDF 链接在 <link title="pdf" href="..."/> 里，
            # 不在 <id> 里（<id> 是网页地址）。Day5 解析正文要用。
            for link in entry.findall("a:link", NS):
                if link.get("title") == "pdf":
                    paper["pdf_url"] = link.get("href")
                    break
            papers.append(paper)
        return papers


def search_arxiv(query: str, max_results: int = 10) -> list[dict]:
    """向后兼容的旧接口：老调用方（try_query.py 等）继续能用。

    新代码请直接用 ArxivClient。
    """
    return ArxivClient(delay=0).search(query, max_results)
