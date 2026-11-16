"""Day2 自动验收。

运行（在 ljs_ws/ 目录下）：
    python check_day2.py

先只做 A 块（类封装），B 块（切分）可以明天再做。
没做完的部分会显示 SKIP，不会中断。
"""

import sys
import traceback

sys.path.insert(0, "src")

PASS, FAIL, SKIP = "[PASS]", "[FAIL]", "[SKIP]"
results = {"pass": 0, "fail": 0, "skip": 0}


def check(name: str, fn) -> None:
    try:
        fn()
    except NotImplementedError:
        print(f"{SKIP} {name}（还没实现）")
        results["skip"] += 1
    except AssertionError as exc:
        print(f"{FAIL} {name}")
        print(f"       {exc}")
        results["fail"] += 1
    except Exception as exc:  # noqa: BLE001
        print(f"{FAIL} {name}")
        print(f"       {type(exc).__name__}: {exc}")
        results["fail"] += 1
    else:
        print(f"{PASS} {name}")
        results["pass"] += 1


# ============================================================
# A 块：ArxivClient 类
# ============================================================
def test_a_class_exists() -> None:
    from ljs_ws.fetch import ArxivClient

    assert isinstance(ArxivClient, type), "ArxivClient 应该是一个类"


def test_a_constructor() -> None:
    from ljs_ws.fetch import ArxivClient

    c = ArxivClient()
    assert hasattr(c, "base_url"), "实例上应该有 base_url 属性"
    assert "arxiv.org" in c.base_url, f"base_url 看起来不对：{c.base_url}"


def test_a_custom_constructor() -> None:
    from ljs_ws.fetch import ArxivClient

    c = ArxivClient(timeout=5, delay=0)
    assert c.timeout == 5, f"timeout 没存住：{c.timeout}"
    assert c.delay == 0, f"delay 没存住：{c.delay}"


def test_a_search_returns_list_of_dict() -> None:
    from ljs_ws.fetch import ArxivClient

    c = ArxivClient(delay=0)
    papers = c.search('all:"retrieval augmented generation" AND cat:cs.CL', 2)
    assert isinstance(papers, list), f"应该返回 list，实际 {type(papers)}"
    assert len(papers) == 2, f"要了 2 篇，返回了 {len(papers)} 篇"
    for p in papers:
        assert isinstance(p, dict), "每个元素应该是 dict"
        for key in ("title", "summary", "id"):
            assert key in p, f"缺少字段 {key}，实际有 {list(p)}"
            assert isinstance(p[key], str) and p[key].strip(), f"{key} 不应该为空"


def test_a_pdf_url() -> None:
    """加分项：能拿到 PDF 链接（Day5 要用）。没做不算失败。"""
    from ljs_ws.fetch import ArxivClient

    c = ArxivClient(delay=0)
    papers = c.search('all:"retrieval augmented generation" AND cat:cs.CL', 1)
    p = papers[0]
    if "pdf_url" not in p:
        raise NotImplementedError("pdf_url 还没加（加分项，Day5 再补也行）")
    assert p["pdf_url"].startswith("http"), f"pdf_url 看起来不对：{p['pdf_url']}"


# ============================================================
# B 块：split_into_chunks
# ============================================================
SAMPLE = (
    "Retrieval augmented generation combines a retriever with a generator. "
    "The retriever finds relevant passages from a large corpus, and the "
    "generator conditions on them to produce an answer with citations. "
    "This approach reduces hallucination compared with feeding an entire "
    "document into the context window."
)


def test_b_short_text() -> None:
    from ljs_ws.text import split_into_chunks

    chunks = split_into_chunks("hello world", chunk_size=100, overlap=20)
    assert len(chunks) == 1, f"短文本应该只有 1 块，实际 {len(chunks)} 块"
    assert chunks[0] == "hello world", f"短文本应该原样返回，实际 {chunks[0]!r}"


def test_b_empty() -> None:
    from ljs_ws.text import split_into_chunks

    assert split_into_chunks("", chunk_size=100, overlap=20) == [], "空串应该返回 []"


def test_b_size_limit() -> None:
    from ljs_ws.text import split_into_chunks

    chunks = split_into_chunks(SAMPLE, chunk_size=100, overlap=20)
    assert len(chunks) > 1, f"这段文本按 100 字切应该多于 1 块，实际 {len(chunks)} 块"
    for i, c in enumerate(chunks):
        assert len(c) <= 100, f"第 {i} 块长度 {len(c)} 超过了 100"


def test_b_has_overlap() -> None:
    from ljs_ws.text import split_into_chunks

    chunks = split_into_chunks(SAMPLE, chunk_size=100, overlap=20)
    for i in range(len(chunks) - 1):
        a, b = chunks[i], chunks[i + 1]
        # 找 a 的后缀和 b 的前缀最长公共重叠
        best = 0
        for k in range(1, min(len(a), len(b)) + 1):
            if a[-k:] == b[:k]:
                best = k
        assert best > 0, f"第 {i} 块和第 {i+1} 块之间没有重叠"


def test_b_no_mid_word_cut() -> None:
    from ljs_ws.text import split_into_chunks

    chunks = split_into_chunks(SAMPLE, chunk_size=100, overlap=20)
    for i, c in enumerate(chunks):
        assert c == c.strip(), f"第 {i} 块首尾有空白没去掉"
        # 块的第一个字符不能紧接原文中的字母（说明切在了单词中间）
        pos = SAMPLE.find(c)
        assert pos != -1, f"第 {i} 块在原文里找不到，是不是改动了内容？"
        if pos > 0:
            prev = SAMPLE[pos - 1]
            assert not (prev.isalnum() and c[0].isalnum()), (
                f"第 {i} 块从单词中间开始了：...{SAMPLE[pos-3:pos]!r}|{c[:12]!r}..."
            )
        end = pos + len(c)
        if end < len(SAMPLE):
            nxt = SAMPLE[end]
            assert not (nxt.isalnum() and c[-1].isalnum()), (
                f"第 {i} 块切在单词中间结束了：...{c[-12:]!r}|{SAMPLE[end:end+3]!r}..."
            )


def test_b_covers_text() -> None:
    """所有块合起来要能覆盖原文（不丢内容）。"""
    from ljs_ws.text import split_into_chunks

    chunks = split_into_chunks(SAMPLE, chunk_size=100, overlap=20)
    for word in SAMPLE.split():
        assert any(word in c for c in chunks), f"单词 {word!r} 在所有块里都找不到，内容丢了"


def main() -> None:
    print("=" * 70)
    print("A 块：ArxivClient 类封装")
    print("=" * 70)
    for name, fn in [
        ("类 ArxivClient 存在", test_a_class_exists),
        ("构造函数默认参数", test_a_constructor),
        ("构造函数可传参 timeout / delay", test_a_custom_constructor),
        ("search() 返回 list[dict]，字段齐全", test_a_search_returns_list_of_dict),
        ("（加分项）返回 pdf_url", test_a_pdf_url),
    ]:
        check(name, fn)

    print()
    print("=" * 70)
    print("B 块：split_into_chunks 切分")
    print("=" * 70)
    for name, fn in [
        ("短文本原样返回", test_b_short_text),
        ("空串返回 []", test_b_empty),
        ("每块长度不超过 chunk_size", test_b_size_limit),
        ("相邻块有重叠", test_b_has_overlap),
        ("不切断单词", test_b_no_mid_word_cut),
        ("内容没有丢失", test_b_covers_text),
    ]:
        check(name, fn)

    print()
    print("=" * 70)
    print(f"通过 {results['pass']} | 失败 {results['fail']} | 跳过 {results['skip']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
