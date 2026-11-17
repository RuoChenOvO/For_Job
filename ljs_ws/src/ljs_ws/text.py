"""切分：把长文本切成有重叠的小块。

这是 RAG 流水线里最容易被低估的一步，面试高频追问。
不要用 LangChain 的 splitter，自己写。
"""


def split_into_chunks(text: str, chunk_size: int = 500, overlap: int = 100) -> list[str]:
    """把 text 切成若干块，相邻块之间保留 overlap 个字符的重叠。

    举例（chunk_size=8, overlap=2）：
        原文  ABCDEFGHIJKLMNOPQRST
        块1   ABCDEFGH               位置 0-7
        块2       GHIJKLMN           位置 6-13（G,H 是重叠）
        块3           MNOPQRST       位置 12-19（M,N 是重叠）

    参数：
        text: 原始文本
        chunk_size: 每块的最大字符数
        overlap: 相邻块重叠的字符数，必须小于 chunk_size

    返回：
        块的列表（已去掉首尾空白，不含空块）
    """
    # ---- 边界情况先处理掉，主循环就能专注在正常流程 ----
    if not text:
        return []
    if overlap >= chunk_size:
        raise ValueError(f"overlap({overlap}) 必须小于 chunk_size({chunk_size})")
    if len(text) <= chunk_size:
        return [text]

    chunks = []
    start = 0
    total = len(text)

    while start < total:
        end = start + chunk_size          # 理想终点

        if end >= total:
            end = total                   # 不够一块了，取到结尾
        else:
            # 终点如果落在单词中间，往回挪到最近的空格
            snapped = end
            while snapped > start and text[snapped - 1] != " ":
                snapped -= 1
            if snapped > start:           # 找到了空格才采纳，否则保持硬切
                end = snapped

        chunk = text[start:end].strip()
        if chunk:                         # 不要空块
            chunks.append(chunk)

        if end >= total:                  # 已经到底，结束
            break

        next_start = end - overlap        # 制造重叠

        # 起点同样不能落在单词中间：往后挪到下一个空格处
        probe = next_start
        while probe < end and text[probe] != " ":
            probe += 1
        if probe < end:
            next_start = probe

        if next_start <= start:           # 保险：起点必须前进，否则死循环
            next_start = start + 1
        start = next_start

    return chunks
