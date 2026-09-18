from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World666"}

# 启动服务
# 1.通过命令:uvicorn filename:app_name --reload 启动服务，并自动加载代码内容
# 2.通过调试:fastapi dev filename
# 3.通过py运行:python filename.py
if __name__ == "__main__":
    import uvicorn
    # uvicorn.run('main01:app', host="127.0.0.1", port=8000, reload=True)
    uvicorn.run(app, host="127.0.0.1", port=8000)