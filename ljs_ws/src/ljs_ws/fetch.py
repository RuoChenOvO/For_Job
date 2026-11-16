import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

NS = {"a": "http://www.w3.org/2005/Atom"}


def search_arxiv(query: str, max_results: int = 10) -> list[dict]:
    """按 arXiv 查询表达式检索，返回 title / summary / id 列表。

    query 需要写完整表达式，例如：
        all:"retrieval augmented generation" AND cat:cs.CL

    注意：只传裸关键词也能跑，但匹配会很松（"augmentation" 会把
    认知增强、事实核查之类的论文一起带进来），检索质量差。
    """
    url = (
        "http://export.arxiv.org/api/query"
        f"?search_query={urllib.parse.quote(query)}"
        f"&start=0&max_results={max_results}"
    )
    with urllib.request.urlopen(url) as resp:
        raw = resp.read().decode("utf-8")
    root = ET.fromstring(raw)
    papers = []
    for entry in root.findall("a:entry", NS):
        papers.append({
            "title": entry.find("a:title", NS).text.strip(),
            "summary": entry.find("a:summary", NS).text.strip(),
            "id": entry.find("a:id", NS).text.strip(),
        })
    return papers
