import subprocess
import datetime
import pickle
import os

def apiKeyCheck(apiKey):
    check = subprocess.run(["python3", "keysCreate.py","-c", apiKey],stdout=subprocess.PIPE, text=True)

    if 'True' in check.stdout:
        return True
    else:
        return False