# 参数路径path
from fastapi import FastAPI,Path

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get('/items2/{item_id}')
def read_item2(item_id: int = Path(...)):
    return {"item_id": item_id}

@app.get('/items3/{item_id}')
def read_item3(item_id: int = Path(..., gt=18, lt=100)):
    return {"item_id": item_id}

@app.get('/items4/{item_id}')
def read_item4(item_id: str = Path(..., pattern="^a\d{2}$")):
    return {"item_id": item_id}

from enum import Enum
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get('/items5/{model_name}')
def items5(model_name: ModelName):
    return {"model_name": model_name}

from typing import Annotated
from pydantic import BeforeValidator
def validate(value):
    if not value.startswith('P-'):
        raise ValueError("Item must start with 'P-'")
    return value

# create a custom type with validation
Item = Annotated[str, BeforeValidator(validate)]
@app.get('/items6/{item_id}')
def read_item6(item_id: Item):
    return {"item_id": item_id}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main09:app', host="127.0.0.1", port=8000, reload=True)