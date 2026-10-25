import urllib.request
import xml.etree.ElementTree as ET

NS = {"a": "http://www.w3.org/2005/Atom"}


def search_arxiv(query: str, max_results: int = 10) -> list[dict]:
    """按关键词检索 arXiv，返回 title / summary / id 列表。

    TODO(W1 Day1): 下面的 urllib.parse.quote 需要 import urllib.parse，
    自己补上这一行，不要照抄就跑。
    """
    url = (
        "http://export.arxiv.org/api/query"
        f"?search_query=all:{urllib.parse.quote(query)}"
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
