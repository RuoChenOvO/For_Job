# 声明的参数不是路径参数时，路径操作函数会把该参数自动解释为“查询”参数。

from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

# 可选参数
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

# 查询参数类型转换
@app.get("/items1/{item_id}")
async def read_item(item_id: str, q: str | None = None,short: bool = False):
    item = {"item_id1": item_id}
    if q:
        item.update({"q": q})
    if short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item

# 多个路径和查询参数
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# 必选查询参数
@app.get("/items2/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('02_查询参数:app', host="127.0.0.1", port=8000, reload=True)