import socket
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

        OID = data[0]
        address = data[1]
        if not OID: break
        print("OID este: " + OID.decode("utf-8"))

        if (OID[0:10] == b'2.16.840.1'):
            GetResponse(OID,address,UDPAgent)
        elif (OID[0:7] == b'1.3.6.1'):
            SetResponse(OID,address, UDPAgent)
        else:
            UDPAgent.sendto(bytes("Invalid", "utf-8"), address)
            break
