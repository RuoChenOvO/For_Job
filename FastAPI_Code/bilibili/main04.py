# 查询参数
from fastapi import FastAPI

app = FastAPI()

@app.get("/query1")
def query_limit(page, limit):
    return {"page":page,"limit":limit}

@app.get("/query2")
def query_limit2(page:int, limit=None):
    if limit:
        return {"page":page,"limit":limit}
    return {"page":page}

@app.get("/query3/{page}")
def page_limit3(page:int,limit=None):
    if limit:
        return {"page":page,"limit":limit}
    return {"page":page}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main04:app', host="127.0.0.1", port=8000, reload=True)