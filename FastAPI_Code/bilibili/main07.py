from fastapi import FastAPI,Query

app = FastAPI()

@app.get("/items1")
def read_item1(item_id: str = Query(123)):
    return {"item_id": item_id}

@app.get("/items2")
def read_item2(item_id: str = Query(...)):
    # ...表示必填参数
    return {"item_id": item_id}

@app.get("/items3")
def read_item3(item_id: str = Query(..., min_length=3, max_length=10)):
    return {"item_id": item_id}

@app.get("/items4")
def read_item4(item_id: int = Query(..., gt=3, lt=100)):
    # gt表示大于，lt表示小于
    return {"item_id": item_id}

@app.get("/items5")
def read_item5(item_id: int = Query(..., alias="id")):
    # alias表示参数的别名
    return {"item_id": item_id}

@app.get("/items6")
def read_item6(item_id: int = Query(..., description="The ID of the item to get")):
    # description表示参数的描述信息
    return {"item_id": item_id}

@app.get("/items7")
def read_item7(item_id: int = Query(..., deprecated=True)):
    # deprecated表示该参数已过时
    return {"item_id": item_id}

@app.get("/items8")
def read_item8(item_id: str = Query(..., regex="^a\d{2}$")):
    # regex表示参数需要匹配的正则表达式
    return {"item_id": item_id}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main07:app', host="127.0.0.1", port=8000, reload=True)