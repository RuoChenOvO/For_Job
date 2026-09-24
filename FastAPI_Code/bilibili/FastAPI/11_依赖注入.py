from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, Header, Path, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn

async def set_charet():
    print("set UTF-8 charset")

# 全局依赖注入
app = FastAPI(dependencies=[Depends(set_charet)])

async def verify(api_token:Optional[str] = Header(None,alias="api-token")):
    if not api_token:
        raise HTTPException(status_code=400,detail="Unauthorized")

# @app.get("/items")
# async def get_items(page_index:Optional[int] = 1,page_size:Optional[int] = 10):
#     return {"page_index":page_index,"page_size":page_size}

def total_param(total:Optional[int] = 1000):
    return total

def pageinfo_params(page_index:Optional[int] = 1,page_size:Optional[int] = 10,
                    total:Optional[int] = Depends(total_param)):
    return {
        "page_index":page_index,
        "page_size":page_size,
        "total":total
    }

class PageInfo:
    def __init__(self,page_index:Optional[int] = 1,page_size:Optional[int] = 10,
                 total:Optional[int] = Depends(total_param)):
        self.page_index = page_index
        self.page_size = page_size
        self.total = total

@app.get("/items")
async def get_users(page_info:dict = Depends(pageinfo_params)):
    return {"page_index":page_info.get("page_index"),
            "page_size":page_info.get("page_size"),
            "total":page_info.get("total")}

@app.get("/users",dependencies=[Depends(verify)])
async def get_users(page_info:PageInfo = Depends(PageInfo)):
    return {"page_index":page_info.page_index,
            "page_size":page_info.page_size,
            "total":page_info.total}

@app.get("/goods")
async def get_goods(page_info:PageInfo = Depends()):
    return {"page_index":page_info.page_index,"page_size":page_info.page_size}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("11_依赖注入:app", host="127.0.0.1", port=8000, reload=True)