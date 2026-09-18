# FastAPI 学习 Todo（目标：包一个模型对话接口）

> 总目标：写一个 `/chat` 接口（接 DeepSeek API 或 mock）+ pytest 测试 + Docker Compose 启动
> 教材：官方中文教程 https://fastapi.tiangolo.com/zh/tutorial/
> 原则：**只学下面勾选的必学项；选学项用到再翻；跳过项现在别碰**。每学一章，当天就把示例代码跑一遍（`uv run fastapi dev` + 浏览器开 `/docs` 调试）。

---

## 一、必学（核心 11 项，约 3–4 天）

- [ ] **1. 第一步** — https://fastapi.tiangolo.com/zh/tutorial/first-steps/
  - 学什么：装 FastAPI、写第一个 `GET /`、`fastapi dev` 启动
  - 验收：浏览器打开 http://127.0.0.1:8000/docs 能看到自动生成的接口文档（Swagger）

- [ ] **2. 路径参数** — https://fastapi.tiangolo.com/zh/tutorial/path-params/
  - 学什么：`@app.get("/items/{item_id}")`、类型自动校验、路径转换
  - 验收：写一个 `GET /chat/{session_id}`，故意传字符串当 id，看自动报错

- [ ] **3. 查询参数** — https://fastapi.tiangolo.com/zh/tutorial/query-params/
  - 学什么：`?limit=10&q=xx` 这种可选参数、默认值
  - 验收：`GET /chat/history?session_id=xx&limit=20` 能取到参数

- [ ] **4. 请求体（Pydantic）⭐ 最重要** — https://fastapi.tiangolo.com/zh/tutorial/body/
  - 学什么：`BaseModel` 定义 `ChatRequest(message: str, user_id: str)`，POST 自动解析+校验 JSON
  - 验收：用 `/docs` 发 `POST /chat`，body 故意少传字段，看自动报错
  - 为什么重要：这和 LLM function calling 的"结构化输出"是同一套东西

- [ ] **5. 响应模型** — https://fastapi.tiangolo.com/zh/tutorial/response-model/
  - 学什么：用 `response_model=ChatResponse` 规范返回结构（只暴露你该返回的字段）
  - 验收：返回 `{reply: str, tokens: int}`，多余字段不会漏出去

- [ ] **6. 异常处理** — https://fastapi.tiangolo.com/zh/tutorial/handling-errors/
  - 学什么：`HTTPException(status_code=404, detail=...)`，自定义错误
  - 验收：模型调用失败时接口返回 502/503 而不是直接崩溃

- [ ] **7. 依赖注入** — https://fastapi.tiangolo.com/zh/tutorial/dependencies/
  - 学什么：`Depends()` 把"获取数据库连接 / 拿 LLM client / 读 API key"抽成公共依赖，别在每个路由里重复写
  - 验收：把"初始化 DeepSeek client"写成一个依赖，`/chat` 和 `/chat/history` 都用它

- [ ] **8. 异步 async/await** — https://fastapi.tiangolo.com/zh/tutorial/async/
  - 学什么：为什么 LLM 调用要 `async def`、`await client.chat.completions.create(...)`
  - 验收：`/chat` 写成 async，高并发下多个请求不互相堵

- [ ] **9. CORS 跨域** — https://fastapi.tiangolo.com/zh/tutorial/cors/
  - 学什么：`CORSMiddleware` 允许本地前端/网页调用你的接口
  - 验收：前端 HTML 或另一个端口的页面能 fetch 通 `/chat`

- [ ] **10. 测试** — https://fastapi.tiangolo.com/zh/tutorial/testing/
  - 学什么：`TestClient(app)` + pytest，不用起服务器就能测
  - 验收：至少 3 个用例——正常问答、参数缺失报错、模型失败时的错误返回

- [ ] **11. 部署启动** — https://fastapi.tiangolo.com/zh/tutorial/deployment/
  - 学什么：`uvicorn` / `fastapi run` 正式启动方式（不是 dev 模式）
  - 验收：`fastapi run main.py` 启动，`/docs` 依然可访问

---

## 二、选学（用到再看，不用提前刷）

- [ ] **流式输出（StreamingResponse）** — 进阶指南 https://fastapi.tiangolo.com/zh/advanced/websockets/ 附近（搜 "StreamingResponse"）
  - 什么时候学：模型对话接口要"打字机效果"时——强烈建议学，LLM 应用面试常问

- [ ] **请求体嵌套模型** — https://fastapi.tiangolo.com/zh/tutorial/body-nested-models/
  - 什么时候学：RAG 接口要传 `{query: str, filters: {...}, top_k: int}` 这种复杂结构时

- [ ] **静态文件** — https://fastapi.tiangolo.com/zh/tutorial/static-files/
  - 什么时候学：想给项目配一个简单网页演示时

- [ ] **后台任务** — https://fastapi.tiangolo.com/zh/tutorial/background-tasks/
  - 什么时候学：想异步存对话历史、发日志不阻塞接口时

- [ ] **项目拆文件** — https://fastapi.tiangolo.com/zh/tutorial/bigger-applications/
  - 什么时候学：单文件超过 300 行、想按模块组织时

- [ ] **中间件** — https://fastapi.tiangolo.com/zh/tutorial/middleware/
  - 什么时候学：想统一打请求日志、计时时

---

## 三、明确跳过（现在别碰）

- ❌ **Security 全家桶**（OAuth2 / JWT / API Key / scopes）— 阶段 0 不做登录认证，面试前再补
- ❌ **SQL 数据库章节**（SQLAlchemy ORM）— 你有 MySQL 基础，项目用向量库就行，不写 CRUD 后端
- ❌ **请求头 / Cookie 参数、表单 / 文件上传** — 这个项目用不到
- ❌ **进阶指南里的高级配置** — 第一遍不需要

---

## 四、动手产出 checklist（阶段 0 验收标准）

- [ ] 一个项目目录：`chat-service/`，用 `uv`（或 venv）建虚拟环境
- [ ] `POST /chat`：入参 `{message, session_id}`，返回 `{reply, tokens, latency_ms}`
- [ ] 依赖注入统一管 DeepSeek client（key 从环境变量读，不写死）
- [ ] 异常处理：模型 API 报错 → 返回结构化错误而不是 500 裸异常
- [ ] `pytest`：≥3 个用例全部通过
- [ ] `Dockerfile` + `docker-compose.yml`，`docker compose up` 一键起服务
- [ ] README 写清楚：安装、启动、`/docs` 地址、示例请求

> 全部勾完 = 阶段 0 工程基础过关，可以进 W3 的 PyTorch / 大模型基础了。
