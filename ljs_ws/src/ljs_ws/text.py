"""切分：把长文本切成有重叠的小块。

这是 RAG 流水线里最容易被低估的一步，面试高频追问。
不要用 LangChain 的 splitter，自己写。
"""


def split_into_chunks(text: str, chunk_size: int = 500, overlap: int = 100) -> list[str]:
    """把 text 切成若干块，相邻块之间保留 overlap 个字符的重叠。

    要求（写完跑 check_day2.py 验收）：
      1. 每块长度 <= chunk_size
      2. 相邻块有重叠，且重叠长度接近 overlap（允许因边界吸附而略有出入）
      3. 块的首尾不能落在单词中间——边界要吸附到空白处
      4. 文本比 chunk_size 短时，原样返回一个块
      5. 空字符串返回空列表

    提示：
      - 直接按字符切片 text[i:i+chunk_size] 会切断单词，需要"往回找最近的空格"
      - 下一次的起点 = 本次终点 - overlap
      - 注意别写出死循环（起点必须往前推进）

    参数：
        text: 原始文本
        chunk_size: 每块的最大字符数
        overlap: 相邻块重叠的字符数，必须小于 chunk_size

    返回：
        块的列表
    """
    # TODO(Day2-B): 在这里实现
    raise NotImplementedError("split_into_chunks 还没实现")
