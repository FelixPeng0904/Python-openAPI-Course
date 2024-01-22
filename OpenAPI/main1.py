from typing import Union
from fastapi import FastAPI
import redis
import os
from dotenv import load_dotenv
load_dotenv()
redis_conn = redis.Redis.from_url(os.environ.get('REDIS_HOST_PASSWORD'))

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/pico_w/{date}")
async def read_item(date:str ,address:str, celsius:float=0.0):
    print("日期:{date}")
    print("位置:{address}")
    print("攝氏:{celsius}")
    return {"狀態":"儲存成功！"}

