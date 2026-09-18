# 请求体 传参数
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    age: int
    pwd: str = None
    sex: str = '男'

@app.post("/users")
def create_user(user: dict):
    return user

@app.post("/users2")
def create_user(user: User):
    return user

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main05:app', host="127.0.0.1", port=8000, reload=True)