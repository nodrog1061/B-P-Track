from fastapi import FastAPI
from typing import Optional

from fastapi.params import Body
from app_functions import *
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

class add_device_body(BaseModel):
    RoomNumber: int


@app.post("/add_device/")
async def add_device(api_key: str = "null", data: add_device_body):


    return {apiKeyCheck(api_key)}
