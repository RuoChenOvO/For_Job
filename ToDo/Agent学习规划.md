# Agent 学习与求职规划 v2（2026.09 → 2027.02）

> 适用对象：燕山大学计算机研二学生，CS 基础扎实（408），Python 基础语法可用（类 / 装饰器 / 异步待练熟），DL/LLM/Agent 从零起步
> 目标：掌握 LLM 应用 + Agent 开发技能，2027 年 2 月（过年后）开始投递实习
> 总时长：20 周，每周约 15–18 小时
> 本版已融合 Codex 路线。资源优先级：
>
> **官方教程 > 内容仍在更新 > 有代码 > 有阶段项目**
>
> 。原则：
>
> **不把教程从头看到尾，只学指定部分并完成产出。**



***

## 一、方向建议（先读这段）

**主攻「LLM 应用 / Agent 开发工程师」方向，不碰「大模型算法」方向。**



1. **岗位需求大、门槛友好**：Agent 应用开发岗 JD 核心是 Python + LLM/Agent 原理 + RAG + LangChain/LangGraph，5 个月可系统补齐；算法岗要求顶会论文和微调经验，来不及。

2. **框架聚焦**：项目以 **LangGraph 为主**，OpenAI Agents SDK 用来理解另一种实现；**不同时深入 CrewAI / AutoGen / LlamaIndex Agent 等多个框架**。

3. 本路线足以支撑 Agent 实习，**不需要再购买零散课程**。



***

## 二、总体路线（20 周）



| 阶段                | 周次      | 主题                                    | 关键产出                                 |
| ----------------- | ------- | ------------------------------------- | ------------------------------------ |
| 并行线               | W1–20   | LeetCode（Hot100 为主）+ 每周复盘             | 算法功底 + GitHub 可见度                    |
| 阶段 0 工程基础         | W1–2    | 命令行 / Shell、Git、FastAPI、Docker        | FastAPI 模型对话接口 + 测试 + Docker Compose |
| 阶段 1 大模型基础        | W3–6    | PyTorch 基础、Transformer、Tokenizer、微调流程 | 手写简化 Attention + 流式生成                |
| 阶段 2 RAG          | W7–10   | 文档处理、向量库、混合检索、Rerank、评测               | 科研论文知识库（≥30 条评测集）                    |
| 阶段 3 Agent 核心     | W11–15  | Agent 原理、LangGraph、MCP、OpenAI SDK     | 科研 Agent（工具 + 人工确认）                  |
| 阶段 4 评测 / 监控 / 部署 | W16–18  | LangSmith 评测与可观测、Ragas、部署             | 评测报告 + 上线                            |
| 阶段 5 求职准备         | W19–20+ | LeetCode 冲刺、八股、简历、最终交付物               | 简历 + 2 个 GitHub 项目                   |

**时间线**：2026-09-15 启动 → 2027-02 投递日常实习 → 3–4 月暑期实习集中招聘窗口。



***

## 三、学习顺序与资源（按阶段）

> 每个阶段只学指定部分，完成阶段产出后再进入下一阶段。
>
> **全部阶段均为中文教程、以 B 站视频为主**
>
> （个别无专门视频的标注替代方案）；官方英文文档只用来查 API。

### 阶段 0：工程基础（W1–2）



| 资源                                                                                                                                                                                                                                             | 只学部分                         | 用途                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| MIT Missing Semester（中文版）：[https://missing-semester-cn.github.io/](https://missing-semester-cn.github.io/)                                                                                                                                     | 第 1、2、6、7 讲                  | 命令行、Shell、Git、调试（讲义无视频；Git 实操配 B 站视频：[https://www.bilibili.com/video/BV1wSjA6sEX5/](https://www.bilibili.com/video/BV1wSjA6sEX5/) ） |
| FastAPI 官方教程（中文）：[https://fastapi.tiangolo.com/zh/tutorial/](https://fastapi.tiangolo.com/zh/tutorial/) + B 站《FastAPI 从零到一》（北大教程）：[https://www.bilibili.com/video/BV1DSWSzvEew/](https://www.bilibili.com/video/BV1DSWSzvEew/)                 | 路径参数、请求模型、依赖注入、异常处理、异步接口、测试  | 后端基本功（视频 + 文档配套）                                                                                                                    |
| Docker（中文）：菜鸟教程 [https://www.runoob.com/docker/docker-tutorial.html](https://www.runoob.com/docker/docker-tutorial.html) + B 站《40 分钟 Docker 实战攻略》：[https://www.bilibili.com/video/BV1THKyzBER6/](https://www.bilibili.com/video/BV1THKyzBER6/) | 镜像、容器、Dockerfile、Compose、数据卷 | 容器化与部署                                                                                                                              |



* **W1 额外**：按《W1 执行清单.md》先做 Python 工程化热身 + 第一个 CLI 小工具 + Git 仓库（阶段 0 的台阶）

* **阶段产出**：用 FastAPI 写一个**模型对话接口**（可先接 DeepSeek API 或 mock），配上测试，通过 Docker Compose 启动

### 阶段 1：大模型基础（W3–6）



| 资源                                                                                                                                                                                                                                              | 只学部分                                                   | 用途         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ---------- |
| PyTorch 官方中文教程：[https://docs.pytorch.ac.cn/tutorials/](https://docs.pytorch.ac.cn/tutorials/) + B 站 刘二大人《PyTorch 深度学习实践》：[https://www.bilibili.com/video/BV1Y7411d7Ys](https://www.bilibili.com/video/BV1Y7411d7Ys)                             | Tensor、DataLoader、网络构建、Autograd、优化、模型保存                | 补上 DL 动手基础 |
| Hugging Face LLM Course（简体中文）：[https://huggingface.co/learn/llm-course/zh-CN/chapter1/1](https://huggingface.co/learn/llm-course/zh-CN/chapter1/1)                                                                                              | 第 1–3 章：Transformer 原理、Tokenizer、模型调用、微调流程（数据集与微调章节选学） | LLM 核心机制   |
| 动手学深度学习（D2L）注意力机制：[https://zh.d2l.ai/chapter\_attention-mechanisms/index.html](https://zh.d2l.ai/chapter_attention-mechanisms/index.html) + 李沐 B 站视频：[https://www.bilibili.com/video/BV1nA41157y4](https://www.bilibili.com/video/BV1nA41157y4) | 只用来补数学和原理，不完整学习全书                                      | 公式推导兜底     |



* **阶段产出**：手写简化版 Attention；调用开源模型完成流式生成；能解释 Token、Embedding、KV Cache、上下文窗口

### 阶段 2：RAG（W7–10）



| 资源                                                                                                                                                                                                                                        | 只学部分                                                                                                                                      | 用途                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Datawhale《动手学大模型应用开发》：[https://github.com/datawhalechina/llm-universe](https://github.com/datawhalechina/llm-universe)                                                                                                                    | 文档处理、向量库、RAG、FastAPI、检索优化、评测（中文主线，在线阅读：[https://datawhalechina.github.io/llm-universe/](https://datawhalechina.github.io/llm-universe/) ） | 中文主线教材                                                                                                     |
| LangChain 中文文档（RAG 部分）：[https://python.langchain.ac.cn/](https://python.langchain.ac.cn/) + B 站【吴恩达】LangChain Chat with Your Data（RAG 专项，中文）：[https://www.bilibili.com/video/BV1d5V26xEc8/](https://www.bilibili.com/video/BV1d5V26xEc8/) | 文档加载、切分、Embedding、向量库、检索工具、引用、安全问题                                                                                                        | 官方文档中文版 + 视频                                                                                               |
| Qdrant 中文文档：[https://qdrant.org.cn/documentation/](https://qdrant.org.cn/documentation/) + B 站《Qdrant 向量数据库入门》：[https://www.bilibili.com/video/BV142Gq6SEER/](https://www.bilibili.com/video/BV142Gq6SEER/)                               | 向量检索、过滤、混合检索、向量数据库原理                                                                                                                      | 向量库基本功（文档 + 视频）                                                                                            |
| B 站《大模型 RAG 全 76 集》第 8 章（RAG 评估 + Ragas 实战）：[https://www.bilibili.com/video/BV1p1TezKEXA/](https://www.bilibili.com/video/BV1p1TezKEXA/)                                                                                                  | 评测检索质量、回答相关性、忠实度                                                                                                                          | 评测入门（官方英文文档可查：[https://docs.ragas.io/en/stable/getstarted/](https://docs.ragas.io/en/stable/getstarted/) ） |



* **阶段产出**：**科研论文知识库**—— 支持 PDF、混合检索、Rerank、带出处回答，并建立至少 30 条评测集

### 阶段 3：Agent 核心（W11–15）



| 资源                                                                                                                                                                                                                                                                                                                                    | 只学部分                                                                              | 用途                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Hugging Face Agents Course（简体中文）：[https://huggingface.co/learn/agents-course/zh-CN/unit0/introduction](https://huggingface.co/learn/agents-course/zh-CN/unit0/introduction) + 视频补充：微软《AI Agents for Beginners》中文版（每节配视频）：[https://github.com/microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | Unit 1 Agent 原理、Unit 2.3 LangGraph、Unit 3 Agentic RAG、Unit 4 完整项目、Bonus 2 可观测性与评测 | 第一主线                                                                                                                                       |
| B 站《LangGraph 从零开始完整教程》：[https://www.bilibili.com/video/BV1zKx4zWEZP/](https://www.bilibili.com/video/BV1zKx4zWEZP/) + LangGraph 中文文档 [https://langgraph.com.cn/](https://langgraph.com.cn/)                                                                                                                                          | State、Memory、Human-in-the-loop、长期记忆、完整 Assistant                                  | 第二主线（视频为主，文档查 API）                                                                                                                         |
| B 站《MCP 入门到实战 67 集完整版》（赋范课堂）：[https://www.bilibili.com/video/BV1fdMgzPEAk/](https://www.bilibili.com/video/BV1fdMgzPEAk/)                                                                                                                                                                                                             | Client、Server、Tool、Resource、端到端应用（先看前 20–30 集）                                    | MCP 开发（官方英文课程可选：[https://huggingface.co/learn/mcp-course/unit0/introduction](https://huggingface.co/learn/mcp-course/unit0/introduction) ） |
| OpenAI Agents SDK 中文文档：[https://openai.github.io/openai-agents-python/zh/](https://openai.github.io/openai-agents-python/zh/)                                                                                                                                                                                                         | Quickstart、Tools、Guardrails、Handoffs、Human-in-the-loop、MCP、Tracing、Testing        | 第二种实现参考（暂无专门中文视频，文档为主，可配微软 AI Agents 课程理解）                                                                                                 |



* **框架选择**：项目以 LangGraph 为主，OpenAI Agents SDK 对照理解；不同时深入 CrewAI / AutoGen / LlamaIndex Agent

* **阶段产出**：**科研 Agent**—— 检索论文、调用 Python / 数据库工具、生成报告、保存状态，危险操作前请求人工确认

### 阶段 4：评测、监控与部署（W16–18）



| 资源                                                                                                                                                                                                                                                                    | 只学部分                              | 用途                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- | -------------------------------------------------------------------------------- |
| B 站《LangSmith 平台实战详解：追踪、线程、LLM 和人工评估体系》：[https://www.bilibili.com/video/BV1Tipdz1EoJ/](https://www.bilibili.com/video/BV1Tipdz1EoJ/) + 中文文档 [http://docs.autoinfra.cn/docs/guides/langsmith/walkthrough](http://docs.autoinfra.cn/docs/guides/langsmith/walkthrough)  | 数据集、离线评测、在线评测、规则评审、LLM-as-a-judge | 评测体系（视频 + 文档）                                                                    |
| B 站《LangSmith 快速入门》系列（AIDeepCoder）：[https://www.bilibili.com/video/BV1dQYLzBEXD/](https://www.bilibili.com/video/BV1dQYLzBEXD/) + CSDN 实操 [https://blog.csdn.net/qq\_73472828/article/details/160423487](https://blog.csdn.net/qq_73472828/article/details/160423487) | Trace、Token、延迟、工具调用、失败链路分析        | 可观测性（视频 + 文章）                                                                    |
| B 站《大模型 RAG 全 76 集》第 8 章：[https://www.bilibili.com/video/BV1p1TezKEXA/](https://www.bilibili.com/video/BV1p1TezKEXA/)                                                                                                                                                 | 完成 RAG 指标                         | 评测指标（官方英文：[https://docs.ragas.io/en/stable/](https://docs.ragas.io/en/stable/) ） |
| 复用阶段 0/2 技能                                                                                                                                                                                                                                                           | FastAPI + Docker 部署               | 上线                                                                               |



* **阶段产出**：评测报告 + 部署上线。项目至少统计：**任务成功率、引用正确率、工具调用成功率、平均耗时、Token 成本、失败类型**

### 阶段 5：求职准备（W19–20，并持续进行）



| 资源                                                                                                                 | 只学部分                         | 用途     |
| ------------------------------------------------------------------------------------------------------------------ | ---------------------------- | ------ |
| 力扣热题 100：[https://leetcode.cn/studyplan/top-100-liked/](https://leetcode.cn/studyplan/top-100-liked/)              | 完成 80–100 题，不追求困难题           | 算法冲刺   |
| 小林 coding：[https://xiaolincoding.com/](https://xiaolincoding.com/)                                                 | 操作系统、网络、数据库、Redis，面试前按专题查漏补缺 | 八股     |
| LangGraph 项目：[https://github.com/langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)                | 读 README 与 Issues            | 学习优秀工程 |
| OpenAI Agents SDK：[https://github.com/openai/openai-agents-python](https://github.com/openai/openai-agents-python) | 读 README 与 Issues            | 学习优秀工程 |



***

## 四、最精简学习顺序（可打印）

**PyTorch 官方中文 → Hugging Face LLM Course（简体中文）→ LLM Universe → HF Agents Course（简体中文）→ LangGraph 中文视频 → MCP 中文视频 → 评测与部署**



***

## 五、最终交付物（求职前备齐）



1. **两个 GitHub 项目**：科研论文知识库（RAG）+ 科研 Agent（阶段 2/3 产出打磨）

2. **一张架构图**（项目 README 中）

3. **一段 3 分钟演示视频**（录制真实运行）

4. **一份评测报告**（阶段 4 产出，含六项指标）

5. **一份针对 Agent/LLM 应用岗位的简历**（STAR 写法）



***

## 六、求职准备要点

**投递节奏**



* 2027-02（过年后）：投日常实习（门槛低、全年可进，积累经验的最佳跳板）

* 2027-03/04：大厂暑期实习集中招聘（字节 / 阿里 / 腾讯 / 百度 / 美团等），部分公司提前批更早开放，持续关注

* 研三 9 月：秋招正式批

**Agent 方向面试高频问题（自测清单）**



1. 讲一下你的 RAG 流程？检索质量怎么优化？（chunk 策略、embedding 选型、混合检索、重排序）

2. function calling 的原理？（LLM 输出结构化参数 → 调用工具 → 结果回填 → 继续生成）

3. ReAct 为什么这样设计？和 CoT 的区别？

4. 上下文窗口满了怎么办？（摘要 / 滑动窗口 / 检索压缩）

5. Token、Embedding、KV Cache、上下文窗口怎么解释？（阶段 1 产出）

6. 你的 Agent 怎么评测？（任务成功率、工具调用成功率、bad case 分析）

7. 手写一个最小 Agent 循环伪代码

8. 八股高频：TCP/UDP、HTTP/HTTPS、MySQL 索引、数据库事务、Redis、进程线程

**简历要点**



* 项目按 STAR 写，结果量化（如 "检索 Top-5 命中率从 60% 提到 85%"）

* 放部署链接 + GitHub 仓库 + demo 视频

* 每个项目能讲 10 分钟以上、能扛追问



***

## 七、每周时间模板（按 15–18h）



| 时间    | 内容                                |
| ----- | --------------------------------- |
| 周一至周五 | 每天 1–1.5h：0.5h LeetCode + 1h 阶段主线 |
| 周末    | 整块 6–8h：做项目、写文档、部署                |
| 周日晚   | 30min 复盘：本周产出 + 下周计划              |

> 阶段产出周（如 W5/W10）可临时降为每天 1 题，保产出优先。



***

## 八、风险与建议



1. **时间紧，优先级：项目产出 > 算法题 > 八股**。2 个能讲深讲透的项目 > 10 个半成品。

2. **别沉迷框架**：LangGraph + MCP + 手写 ReAct 核心逻辑为主；面试考原理，不考 API 拼写。

3. **API 成本可控**：DeepSeek / 通义等国产模型，正常学习每月几十元；本地可用 ollama + Qwen 兜底。

4. **阶段 0 若吃力**：优先保 FastAPI + Docker，Missing Semester 只看第 1、2 讲即可。

5. **日常实习是捷径**：研二下学期课少的话，2 月后边实习边学。

6. **每周写复盘**：学习笔记 = 简历素材 = 面试谈资。

7. **方向可微调**：若对算法产生兴趣，在阶段 5 加 LoRA 微调入门（Datawhale self-llm），主攻方向不变。



***

## 九、复盘模板（每周用）



```
本周进度（对照阶段计划）：

完成 / 未完成 / 卡点：

本周产出（代码/文档/题目数）：

下周计划：
```



***

## 参考来源



* MIT Missing Semester（中文版）：[https://missing-semester-cn.github.io/](https://missing-semester-cn.github.io/) （Git 视频：[https://www.bilibili.com/video/BV1wSjA6sEX5/](https://www.bilibili.com/video/BV1wSjA6sEX5/) ）

* FastAPI 官方教程（中文）：[https://fastapi.tiangolo.com/zh/tutorial/](https://fastapi.tiangolo.com/zh/tutorial/) （视频：B 站《FastAPI 从零到一》[https://www.bilibili.com/video/BV1DSWSzvEew/](https://www.bilibili.com/video/BV1DSWSzvEew/) ）

* Docker（中文）：菜鸟教程 [https://www.runoob.com/docker/docker-tutorial.html](https://www.runoob.com/docker/docker-tutorial.html) （视频：B 站《40 分钟 Docker 实战攻略》[https://www.bilibili.com/video/BV1THKyzBER6/](https://www.bilibili.com/video/BV1THKyzBER6/) ）

* PyTorch 官方中文教程：[https://docs.pytorch.ac.cn/tutorials/](https://docs.pytorch.ac.cn/tutorials/) （视频：B 站 刘二大人《PyTorch 深度学习实践》[https://www.bilibili.com/video/BV1Y7411d7Ys](https://www.bilibili.com/video/BV1Y7411d7Ys) ）

* Hugging Face LLM Course（简体中文）：[https://huggingface.co/learn/llm-course/zh-CN/chapter1/1](https://huggingface.co/learn/llm-course/zh-CN/chapter1/1)

* D2L 注意力机制（中文）：[https://zh.d2l.ai/chapter\_attention-mechanisms/index.html](https://zh.d2l.ai/chapter_attention-mechanisms/index.html) （视频：李沐 B 站 [https://www.bilibili.com/video/BV1nA41157y4](https://www.bilibili.com/video/BV1nA41157y4) ）

* Datawhale llm-universe：[https://github.com/datawhalechina/llm-universe](https://github.com/datawhalechina/llm-universe) （在线阅读：[https://datawhalechina.github.io/llm-universe/](https://datawhalechina.github.io/llm-universe/)）

* LangChain 中文文档（RAG 部分）：[https://python.langchain.ac.cn/](https://python.langchain.ac.cn/) （视频：B 站【吴恩达】LangChain Chat with Your Data [https://www.bilibili.com/video/BV1d5V26xEc8/](https://www.bilibili.com/video/BV1d5V26xEc8/) ）

* Qdrant 中文文档：[https://qdrant.org.cn/documentation/](https://qdrant.org.cn/documentation/) （视频：B 站《Qdrant 向量数据库入门》[https://www.bilibili.com/video/BV142Gq6SEER/](https://www.bilibili.com/video/BV142Gq6SEER/) ）

* Ragas 中文视频：B 站《大模型 RAG 全 76 集》第 8 章 [https://www.bilibili.com/video/BV1p1TezKEXA/](https://www.bilibili.com/video/BV1p1TezKEXA/) （官方英文文档：[https://docs.ragas.io/en/stable/](https://docs.ragas.io/en/stable/) ）

* Hugging Face Agents Course（简体中文）：[https://huggingface.co/learn/agents-course/zh-CN/unit0/introduction](https://huggingface.co/learn/agents-course/zh-CN/unit0/introduction) （视频补充：微软《AI Agents for Beginners》中文版 [https://github.com/microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) ）

* LangGraph 中文视频：B 站《LangGraph 从零开始完整教程》[https://www.bilibili.com/video/BV1zKx4zWEZP/](https://www.bilibili.com/video/BV1zKx4zWEZP/) + 中文文档 [https://langgraph.com.cn/](https://langgraph.com.cn/)

* MCP 中文视频：B 站《MCP 入门到实战 67 集完整版》[https://www.bilibili.com/video/BV1fdMgzPEAk/](https://www.bilibili.com/video/BV1fdMgzPEAk/) （官方英文课程：[https://huggingface.co/learn/mcp-course/unit0/introduction](https://huggingface.co/learn/mcp-course/unit0/introduction) ）

* OpenAI Agents SDK 中文文档：[https://openai.github.io/openai-agents-python/zh/](https://openai.github.io/openai-agents-python/zh/)

* LangSmith 中文文档（评测）：[http://docs.autoinfra.cn/docs/guides/langsmith/walkthrough](http://docs.autoinfra.cn/docs/guides/langsmith/walkthrough) （视频：B 站《LangSmith 平台实战详解》[https://www.bilibili.com/video/BV1Tipdz1EoJ/](https://www.bilibili.com/video/BV1Tipdz1EoJ/) ）

* LangSmith 中文实操（可观测性）：CSDN《Agent 可观测性实战：用 LangSmith 追踪每一步》[https://blog.csdn.net/qq\_73472828/article/details/160423487](https://blog.csdn.net/qq_73472828/article/details/160423487) （视频：B 站《LangSmith 快速入门》系列 [https://www.bilibili.com/video/BV1dQYLzBEXD/](https://www.bilibili.com/video/BV1dQYLzBEXD/) ）

* 力扣热题 100：[https://leetcode.cn/studyplan/top-100-liked/](https://leetcode.cn/studyplan/top-100-liked/)

* 小林 coding：[https://xiaolincoding.com/](https://xiaolincoding.com/)

* LangGraph：[https://github.com/langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)

* OpenAI Agents SDK：[https://github.com/openai/openai-agents-python](https://github.com/openai/openai-agents-python)