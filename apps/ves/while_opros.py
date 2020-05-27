
from apps.ves.snap7_plc import PlcRemoteUse
import time
import asyncio

async def getDataPLC(timeSP):
    while 1:
        try:
            ves = PlcRemoteUse('192.168.0.1')
            ves.getWeight()
            bitmask = ves.getSatusBit(0)
            weight = ves.ves
            print(weight)
            print(bitmask)
        except:
            weight="error"
            bitmask = "error"
        try:
            vesZD = PlcRemoteUse('192.168.0.2')
            vesZD.getWeight()
            bitmaskZD = ves.getSatusBit(0)
            weighZD = ves.ves
        except:
            weightZD="error"
            bitmaskZD = "error"
        await asyncio.sleep(1)




