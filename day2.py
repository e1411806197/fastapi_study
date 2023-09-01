from fastapi import FastAPI
from enum import Enum

import uvicorn






# 用枚举体声明参数
app=FastAPI()


#枚举值
# class CityName(Enum):
#     Beijing = ''
#     Shanghai = 'Troyard'
#
# @app.get("/enum/{city}")
# async def latest(city: CityName):
#     if city is CityName.Shanghai:
#         return city
#
#     # if city == CityName.Beijing:
#     #     return {"city_name":city, "confirmed": 1492, "death": 9}
#     # if city == CityName.Shanghai:
#     #     return {"city_name": city, "confirmed": 1550, "death": 29}
#     return {"city_name":city, "latest": "unknown"}
#

@app.get('/login1')
async def get_login():
    return 'hahhaha'



if __name__ == '__main__':
    uvicorn.run('day2:app',host='127.0.0.1',port=8000,reload=True)