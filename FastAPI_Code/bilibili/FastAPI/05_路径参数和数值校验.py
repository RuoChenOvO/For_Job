from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# 按需对参数排序
@app.get("/items1/{item_id}")
async def read_items(q: str, item_id: int = Path(description="The ID of the item to get")):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

@app.get("/items2/{item_id}")
async def read_items(
    q: str, item_id: Annotated[int, Path(title="The ID of the item to get")]
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# 按需对参数排序的技巧
# Python 不会对这个 * 做任何事，但它会知道之后的所有参数都应该作为关键字参数（键值对）来调用，也被称为 kwargs。即使它们没有默认值。
@app.get("/items3/{item_id}")
async def read_items3(*, item_id: int = Path(title="The ID of the item to get"), q: str):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

@app.get("/items4/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")], q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# 数值校验：大于等于
# ge=1 后，item_id 必须是一个整数，且大于等于 1
@app.get("/items5/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=1)], q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# 数值校验：大于和小于等于
# gt：大于（greater than）
# le：小于等于（less than or equal）
@app.get("/items6/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", gt=0, le=1000)],
    q: str,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# 数值校验：浮点数、大于和小于
@app.get("/items7/{item_id}")
async def read_items(
    *,
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str,
    size: Annotated[float, Query(gt=0, lt=10.5)],
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if size:
        results.update({"size": size})
    return results

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("05_路径参数和数值校验:app", host="127.0.0.1", port=8000, reload=True)