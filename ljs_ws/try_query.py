"""检索质量对比：加引号（短语匹配） vs 不加引号（松散匹配）。

运行（在 ljs_ws/ 目录下）：
    python try_query.py

只打印标题，不打印摘要——摘要太长，终端里看不出差别。
"""

import sys
import time

sys.path.insert(0, "src")

from ljs_ws.fetch import search_arxiv  # noqa: E402

QUERIES = [
    ("不加引号（松散匹配）", "all:retrieval augmented generation AND cat:cs.CL"),
    ("加引号（短语匹配）", 'all:"retrieval augmented generation" AND cat:cs.CL'),
]


def show(label: str, query: str, n: int = 5) -> None:
    print("=" * 78)
    print(f"{label}")
    print(f"query = {query}")
    print("=" * 78)
    try:
        papers = search_arxiv(query, n)
    except Exception as exc:  # noqa: BLE001
        print(f"  [失败] {type(exc).__name__}: {exc}")
        return

    if not papers:
        print("  （没有结果）")
        return

    for i, p in enumerate(papers, start=1):
        title = " ".join(p["title"].split())  # arXiv 返回的标题里有换行，压平
        print(f"  {i}. {title}")
    print()


def main() -> None:
    for idx, (label, query) in enumerate(QUERIES):
        show(label, query)
        if idx < len(QUERIES) - 1:
            time.sleep(3)  # arXiv 要求请求间隔约 3 秒，别省


if __name__ == "__main__":
    main()
