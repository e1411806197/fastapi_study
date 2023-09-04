from fastapi import FastAPI
import uvicorn
from typing import Union
from enum import Enum
from pydantic import BaseModel

from fastapi import FastAPI
from pydantic import BaseModel



# 构建请求体  post

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item


@app.post("/itemxx/{item_id}")
async def create(item_id:int,item:Item,q:Union[int,None]=None):
    result = {"item_id": item_id, **item.model_dump()}
    return result


if __name__ == '__main__':
    uvicorn.run('day4:app',host='127.0.0.1',port=8000,reload=True)