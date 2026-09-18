# 路径参数
from fastapi import FastAPI

app = FastAPI()

@app.get("/args1/1")
def path_args1():
    return {"mseeage":"id1"}

@app.get("/args2/{id}")
def path_args2(id):
    return {"message":id}

@app.get("/args3/{id}")
def path_args3(id):
    return {"message2":id}

@app.get("/args4/{id}/{name}")
def path_args4(id:int,name):
    return {"message":id,"name":name}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main02:app', host="127.0.0.1", port=8000,reload=True)
