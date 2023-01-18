import socket

from pyasn1.codec.ber import decoder

from Host.SNMPPacket import decodeASN1
from Metode.GetResponse import GetResponse
from Metode.SetResponse import SetResponse
from Metode.Trap import *
import threading


while 1:

    localIP = socket.gethostname()
    localport = 161
    bufferSize = 1024;

    UDPAgent = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    UDPAgent.bind((localIP, localport))

    print('Agentul este activ')

    threading.Thread(target=checkTrap).start()

    while 1:
        data = UDPAgent.recvfrom(bufferSize)

        oid = decodeASN1(data[0])
        text = oid[1]
        oid = oid[0]
        print("oid este ", oid)

        address = data[1]


        if (oid[0] == 1):
            GetResponse(oid,address,UDPAgent)
        elif (oid[0] == 2):
            SetResponse(oid,address, UDPAgent, text)
        else:
            UDPAgent.sendto(bytes("Invalid", "utf-8"), address)
            break
