from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

users = {
    # "x":{"id":1},
    "a":{"id":2,"username":"a"},
    "b":{"id":3,"username":"z","password":"bbb"},
    "c":{"id":4,"username":"c","password":"ccc","description":"default"},
    "d":{"id":5,"username":"d","password":"ddd","description":"user add"},
    "e":{"id":6,"username":"e","password":"eee","description":"user eee","fullname":"Ruochen"}
}

app = FastAPI()
class UerOut(BaseModel):
    id: int
    username: str
    # Optional 字段 作用：允许字段为空，设置默认值
    description: Optional[str] = "default"

@app.get("/users/{username}", response_model=UerOut)
async def read_user(username: str) -> UerOut:
    return users.get(username,{})

# response_model_include 参数,作用：包含指定字段
# response_model_exclude 参数,作用：排除指定字段
# response_model_exclude_unset = True 参数,作用：排除未设置的字段
@app.get("/users1/{username}", response_model=UerOut,response_model_include={"id","username"})
async def read_user(username: str) -> UerOut:
    return users.get(username,{})

@app.get('/users', response_model=list[UerOut])
async def read_users():
    return users.values()



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("09_响应模型2:app", host="127.0.0.1", port=8000, reload=True)