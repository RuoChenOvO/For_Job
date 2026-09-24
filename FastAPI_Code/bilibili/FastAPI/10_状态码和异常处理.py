import pstats
from typing import Optional

from fastapi import FastAPI, HTTPException, Path, Request
from fastapi.responses import JSONResponse
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

class UserBase(BaseModel):
    id:Optional[int] = None
    username: str
    fullname:Optional[str] = None
    description: Optional[str] = None

class UserIn(UserBase):
    password: str

class UserOut(UserBase):
    ...

class ErrorMessage(BaseModel):
    error_code: int
    error_message: str

class UserNotFoundException(Exception):
    def __init__(self,username: str):
        self.username = username

@app.exception_handler(UserNotFoundException)
async def user_not_found_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(status_code=404,content={
        'error_code':404,
        'error_message':f"用户 {exc.username} 不存在"
        })



@app.post("/users",status_code=201,response_model=UserOut,responses={400:{"model":ErrorMessage}})
async def create_user(user: UserIn):
    if users.get(user.username,None):
        error_message = ErrorMessage(error_code=400,error_message=f"用户 {user.username} 已存在")
        return JSONResponse(status_code=400,content=error_message.model_dump())

@app.get("/users/{username}",status_code=200, response_model=UserOut)
async def get_user(username: str = Path(...,description="用户名")):
    user = users.get(username,None)
    if user :
        return user
    # raise HTTPException(status_code=404,detail="用户不存在")
    raise UserNotFoundException(username)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("10_状态码和异常处理:app", host="127.0.0.1", port=8000, reload=True)