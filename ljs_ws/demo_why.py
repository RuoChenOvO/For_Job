"""两个小实验，证明 NS 和 quote() 各自解决什么问题。

运行（在 ljs_ws/ 目录下）：
    python demo_why.py
"""

import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

QUERY = 'all:"retrieval augmented generation" AND cat:cs.CL'
BASE = "http://export.arxiv.org/api/query"


def fetch_xml(url: str) -> str:
    with urllib.request.urlopen(url) as resp:
        return resp.read().decode("utf-8")


def exp1_no_quote() -> None:
    """实验 1：不调用 quote()，直接把带空格的查询拼进 URL。"""
    print("=" * 78)
    print("实验 1：不调用 quote()")
    print("=" * 78)
    url = f"{BASE}?search_query={QUERY}&start=0&max_results=5"
    print("拼出来的 URL：")
    print("  " + url)
    print()
    print("注意：URL 里出现了空格，还有查询自带的 & 和引号。")
    print("真实请求会发生什么：")
    try:
        fetch_xml(url)
        print("  [意外] 没有报错")
    except Exception as exc:  # noqa: BLE001
        print(f"  [失败] {type(exc).__name__}: {exc}")
    print()


def exp1_with_quote() -> None:
    """实验 1 的对照组：调用 quote()。"""
    print("=" * 78)
    print("实验 1 对照组：调用 quote()")
    print("=" * 78)
    encoded = urllib.parse.quote(QUERY)
    url = f"{BASE}?search_query={encoded}&start=0&max_results=5"
    print("拼出来的 URL：")
    print("  " + url)
    print()
    print("空格变成 %20，& 变成 %26，引号变成 %22——全部被当成普通字符。")
    try:
        raw = fetch_xml(url)
        print(f"  [成功] 拿到 {len(raw)} 个字符的 XML")
    except Exception as exc:  # noqa: BLE001
        print(f"  [失败] {type(exc).__name__}: {exc}")
    print()


def exp2_namespace() -> None:
    """实验 2：解析 XML 时要不要带命名空间。"""
    print("=" * 78)
    print("实验 2：NS 字典去掉会怎样")
    print("=" * 78)
    url = f"{BASE}?search_query={urllib.parse.quote(QUERY)}&start=0&max_results=5"
    raw = fetch_xml(url)
    root = ET.fromstring(raw)

    print("XML 根节点的真实标签名：")
    print(f"  {root.tag}")
    print()

    ns = {"a": "http://www.w3.org/2005/Atom"}
    print("两种写法各找到多少个 <entry>：")
    print(f'  root.findall("a:entry", NS)  → {len(root.findall("a:entry", ns))} 个')
    print(f'  root.findall("entry")        → {len(root.findall("entry"))} 个')
    print()

    # 用 iterate 看看到底有哪些标签
    tags = [el.tag for el in root.iter() if el.tag.endswith("entry")]
    print("其实文件里 tag 完整长这样：")
    for t in set(tags):
        print(f"  {t}")
    print()
    print("说明：标签的真实名字是 {http://www.w3.org/2005/Atom}entry，")
    print('      不是 "entry"。NS 字典让 ElementTree 知道')
    print('      "a:entry" 等价于 "{http://www.w3.org/2005/Atom}entry"。')
    print()


def main() -> None:
    exp1_no_quote()
    exp1_with_quote()
    exp2_namespace()


if __name__ == "__main__":
    main()
