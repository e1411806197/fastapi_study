# from typing import Union
#
# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
#
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
import uvicorn
from fastapi import FastAPI


app=FastAPI()


@app.get("/login")
def login():
    return "helloworld"

@app.get('/login/ttx')
def get_sum():
    return [2,3,4,5]

@app.get('/items/{items_id}')
async def get_ttt(items_id:int):
    return {'ffff':items_id}




# 顺序问题
@app.get('/iss/{iss_id}')
async def get_iss(iss_id:str):
    return {'kkkk':iss_id}

@app.get('/iss/mer')
async def gu_iss():
    return 'lpppp_hello'

if __name__ == '__main__':
    uvicorn.run('day1:app',host='127.0.0.1',port=8000,reload=True)