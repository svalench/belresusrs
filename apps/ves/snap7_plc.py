import json
import struct

import snap7
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import CreateView


class PlcRemoteUse():

    def __init__(self,address):
        self.client = snap7.client.Client()  # формирование обращения к соединению
        self.client.connect(address, 0,  1)  # подключение к контроллеру. Adress - IP адресс. Rack, slot - выставляються/смотрятся в TIA portal
        self.ves = 0
        self.db_read = 3
        self.db_write = 2
	


    def getVes(request):
        payload = {'success': True}
        return HttpResponse(json.dumps(payload), content_type='application/json')

    def tearDown(self):
        self.client.disconnect()
        self.client.destroy()

    def changeBit(self,byte,bit):
        byte=int(byte)
        bit=int(bit)
        bitsSet = [1,2,4,8,16,32,64,128]
        bitsReset = [254, 253, 251, 247, 239, 223, 191, 127]
        retVal = self.client.db_read(self.db_write, byte, 1)
        value = int.from_bytes(retVal[0:1], byteorder='little')
        bits=bin(value)
        bits= bits.replace("0b","")
        if(len(bits)<7):
            for i in range(8 - len(bits)):
                bits="0"+bits
        bits=bits[::-1]
        try:
            status = bits[bit]
        except:
            status=0
        if(status!="0"):
            ret = value & bitsReset[bit]
        else:
            ret = value | bitsSet[bit]
        a = (ret).to_bytes(2, byteorder='little')
        self.client.db_write(self.db_write, byte, a)
        return value

    def setBit(self,byte,bit):
        bitsSet = [1,2,4,5,6,32,64,128]
        retVal = self.client.db_read(self.db_write, byte, 1)
        value = int.from_bytes(retVal[0:1], byteorder='big')
        ret = value | bitsSet[bit]
        a = (ret).to_bytes(2, byteorder='little')
        self.client.db_write(self.db_write, byte, a)

    def resetBit(self, byte, bit):
        bitsReset = [254, 253, 251, 247, 239, 223, 191, 127]
        retVal = self.client.db_read(self.db_write, byte, 1)
        value = int.from_bytes(retVal[0:1], byteorder='big')
        ret = value & bitsReset[bit]
        a = (ret).to_bytes(2, byteorder='little')
        self.client.db_write(self.db_write, byte, a)

    def getWeight(self):
        value_db_tia = self.client.db_read(self.db_read, 0, 4)
        val = struct.unpack('>f', value_db_tia[0:4])
        self.ves=val[0]
        return val[0]
