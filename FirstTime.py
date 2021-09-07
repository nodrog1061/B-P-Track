import subprocess
import os

defaultFilename = "apiKeys.txt"
defaultNumber = 5


if os.path.isfile(defaultFilename):
    print("No Dump")
    exit()
else:
    print("First time dump done")
    subprocess.run(["python3", "keysCreate.py","-g", defaultNumber, "-du", defaultFilename],stdout=subprocess.PIPE, text=True)