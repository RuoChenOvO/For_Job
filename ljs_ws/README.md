# ljs_ws —— arXiv 论文问答助手

> 大模型应用 8 周项目（W1: 2026-10-26 起）。规划见 `../ToDo/大模型应用学习规划_2026-10.md`。

## 简介

输入一个主题 → 从 arXiv 拉取论文 → 解析正文 → 切分 → 检索 → 带引用回答，并配套可一键复现的评测。

## 目录结构

```
ljs_ws/
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
├── data/                # 本地数据，不进版本库
└── src/ljs_ws/
    ├── __init__.py
    └── fetch.py         # arXiv API 检索（W1 Day1）
```

## 安装

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
cp .env.example .env          # 再填入自己的 key
```

## 使用

W1 Day1 验收命令：

```bash
python -c "from src.ljs_ws.fetch import search_arxiv; print(search_arxiv('retrieval augmented generation', 3))"
```

## 踩坑记录

- （W1 Day3）待填：高频词被 the / a / of 占满。

## 已知问题

- `fetch.py` 当前故意缺 `import urllib.parse`，Day1 补上后才可运行。

## 下一步

- W1 Day2：`ArxivClient` 类封装 + 手写 `split_into_chunks`
