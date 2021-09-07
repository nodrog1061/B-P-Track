from fastapi import FastAPI
from typing import Optional

from fastapi.params import Body
from app_functions import *
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

class addDeviceIn(BaseModel):
    RoomNumber: int
    DeviceId: int

class addDeviceOut(BaseModel):
    State: str

@app.post("/add_device/")
async def add_device(data: addDeviceIn, api_key: str = "null", responseModel=addDeviceOut):

    print(data.RoomNumber)
    return {"apiKey": apiKeyCheck(api_key),"roomNumber": data.RoomNumber}
