import socket
from Metode.GetResponse import GetResponse
from Metode.SetResponse import SetResponse
from Metode.Trap import *
import threading

#threading.Thread(target=checkTrap()).start()

#daemon = threading.Thread(target=checkTrap(), daemon=True, name='Monitor')
while 1:
    #test
    UDPport=161
    localIP = socket.gethostname()
    localport = 161
    bufferSize = 1024;

    UDPAgent = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    UDPAgent.bind((localIP, localport))

    print('Agentul este activ')

    while 1:
        data = UDPAgent.recvfrom(bufferSize)

        OID = data[0]
        address = data[1]
        #print(OID)
        if not OID: break
        print("OID este: " + OID.decode("utf-8"))

        if (OID[0:10] == b'GetRequest'):
            # oid: 1.127.10.5.6
            GetResponse(OID,address,UDPAgent)
        elif (OID[0:10] == b'SetRequest'):
            # oid: 1.127.10.5.6
            SetResponse(OID,address, UDPAgent)
        else:
            UDPAgent.sendto(bytes("Invalid", "utf-8"), address)
            #conn.sendall(bytes("Invalid", "utf-8"))
            break
