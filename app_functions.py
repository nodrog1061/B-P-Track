import subprocess
import datetime
import pickle
import os

def apiKeyCheck(apiKey):
    check = subprocess.run(["py", "keysCreate.py","-c", apiKey],stdout=subprocess.PIPE, text=True)

    if 'True' in check.stdout:
        return True
    else:
        return False

def storeDataPT(room,pIn,pOut):
    fileName = f"{room}.pickle"

    date = datetime.datetime.now().strftime("%d")+"/"+datetime.datetime.now().strftime("%m")+","+datetime.datetime.now().strftime("%Y")+","+datetime.datetime.now().strftime("%X")

    if os.path.isfile(fileName):
        with open(fileName, "rb") as f:
            try:
                fromFile = pickle.load(f)

                pCur = int(fromFile[list(fromFile.keys())[0]][2] + pIn - pOut)

                DataForFile = {date : [pIn,pOut,pCur]}

                DataForFile.update(fromFile)
#{'start_time': 10:00:00; '05/20/21': [[], []]}
                return True

                with open(fileName, "wb") as b:
                    pickle.dump(DataForFile, b)
                    DataForFile = None
            except Exception:
                return False
    else:
        with open(fileName, "wb") as f:

            try:
                pCur = int(pIn - pOut)

                DataForFile = {date : [pIn,pOut,pCur]}

                pickle.dump(DataForFile, f)

                return True

            except Exception:
                    return False

def storeDataBT(room,binN,data):
    fileName = f"{room}-{binN}.pickle"

    date = datetime.datetime.now().strftime("%d")+"/"+datetime.datetime.now().strftime("%m")+","+datetime.datetime.now().strftime("%Y")
    time = datetime.datetime.now().strftime("%X")

    if os.path.isfile(fileName):
        with open(fileName, "rb") as f:
            try:
                fromFile = pickle.load(f)

                if fromFile[date]:
                    fromFile.update({date : })

                pCur = int(fromFile[list(fromFile.keys())[0]][2] + pIn - pOut)

                DataForFile = {date : [pIn,pOut,pCur]}

                DataForFile.update(fromFile)
#{'start_time': 10:00:00; '05/20/21': [[], []]}
                return True

                with open(fileName, "wb") as b:
                    pickle.dump(DataForFile, b)
                    DataForFile = None
            except Exception:
                return False
    else:
        with open(fileName, "wb") as f:

            try:
                pCur = int(pIn - pOut)

                DataForFile = {date : [pIn,pOut,pCur]}

                pickle.dump(DataForFile, f)

                return True

            except Exception:
                    return False