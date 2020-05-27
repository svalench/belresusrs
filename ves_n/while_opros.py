
from apps.ves.snap7_plc import PlcRemoteUse
import time
from time import sleep
def getDataPLC(timeSP):
    while 1:
        try:
            ves = PlcRemoteUse('192.168.0.1')
            ves.getWeight()
            bitmask = ves.getSatusBit(0)
            weight = ves.ves
            print(weight)
        except:
            weight="error"
            bitmask = "error"
        try:
            vesZD = PlcRemoteUse('192.168.0.2')
            vesZD.getWeight()
            bitmaskZD = ves.getSatusBit(0)
            weighZDt = ves.ves
            print(weighZDt)
        except:
            weightZD="error"
            bitmaskZD = "error"
        sleep(timeSP)

