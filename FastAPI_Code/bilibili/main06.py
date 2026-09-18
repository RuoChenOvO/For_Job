# Python原生类型注解
from typing import Union,Optional,List
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id:int):
    return {"item_id": item_id}

@app.get("/items2/{item_id}")
def read_item2(item_id:str):
    return {"item_id": item_id}

@app.get("/items3/{item_id}")
def read_item3(item_id:Union[str,int]):
    return {"item_id": item_id}

@app.get("/items4/{item_id}")
def read_item4(item_id:Union[str,int]=110):
    # 这个不可用默认参数
    return {"item_id": item_id}

@app.get("/items5")
def read_item5(item_id:Union[str,int]=110):
    return {"item_id": item_id}

@app.get("/items6")
def read_item6(item_id:Union[int,None]=None):
    return {"item_id": item_id}

@app.get("/items7")
def read_item7(item_id:Optional[int]=None):
    return {"item_id": item_id}

@app.get("/items8")
def read_item8(item_ids:List):
    return {"item_id": item_ids}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main06:app', host="127.0.0.1", port=8000, reload=True)