from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.post("/items")
async def create_item(item: Item):
    return item

# 使用模型
@app.post("/items1")
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

# 请求体 + 路径参数
@app.put("/items2/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.model_dump()}

# 请求体 + 路径 + 查询参数
@app.put("/items3/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('03_请求体:app', host="127.0.0.1", port=8000, reload=True)