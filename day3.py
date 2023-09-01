import uvicorn
from fastapi import FastAPI

from typing import Union


app=FastAPI()


# 声明在参数中包含具体路径

@app.get('/files/{filepath:path}')
def read_path(filepath):
    return {'path':filepath}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 1):
    return fake_items_db[skip : skip + limit]





# 路径以外的参数默认处理为查询字符串的参数
@app.get('/xxx/')
async def get_kk(a,b):
    return {'a':a,'b':b}



# 处理可选参数

# 不声明任何默认值代表必选参数
@app.get('/sss/{r}')
def get_choice(r:str,s:Union[int,None]=None,p:bool=True):
    if s:
        return {'r':r,'p':p}
    else:
        return 'hhhhkkk'





if __name__ == '__main__':
    uvicorn.run('day3:app',host='127.0.0.1',port=8000,reload=True)
