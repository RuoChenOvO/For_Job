from typing import Any

from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse, RedirectResponse
from pydantic import BaseModel, EmailStr

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.post("/items/")
async def create_item(item: Item) -> Item:
    return item


@app.get("/items/")
async def read_items() -> list[Item]:
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]

# response_model 参数
@app.post("/items1/", response_model=Item)
async def create_item(item: Item) -> Any:
    return item


@app.get("/items1/", response_model=list[Item])
async def read_items() -> Any:
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]

# 过滤响应模型的字段
class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

# 将 response_model 声明为不包含密码的 UserOut 模型
@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user

# 返回类型与数据过滤
class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

class UserIn(BaseUser):
    password: str

@app.post("/user1/")
async def create_user(user: UserIn) -> BaseUser:
    return user

# 其他返回类型注解
@app.get("/portal")
async def get_portal(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return JSONResponse(content={"message": "Here's your interdimensional portal."})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("09_响应模型:app", host="127.0.0.1", port=8000, reload=True)