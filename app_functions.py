import subprocess
import datetime
import pickle
import os
from tinydb import TinyDB, Query

db = TinyDB('db.json')

def apiKeyCheck(apiKey):
    check = subprocess.run(["python3", "keysCreate.py","-c", apiKey],stdout=subprocess.PIPE, text=True)

    if 'True' in check.stdout:
        return True
    else:
        return False

def addDevice (deviceId, roomNumber):
