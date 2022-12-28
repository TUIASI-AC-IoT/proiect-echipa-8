import socket
from Agent.MIB import *

def SetResponse(OID,address, UDPAgent):

    while 1:
        if not OID: break
        if (OID[0:14] == b'SetRequestName'):
            # oid: 1.127.10.5.6
            MIB.Name=OID[14:len(OID)].decode("utf-8")
            MIB.changeName(MIB.Name)
            print("aici")
            print(MIB.Name)
            UDPAgent.sendto(bytes(MIB.Name, "utf-8"), address)
            #conn.sendall(bytes("Nume schimbat in :"+MIB.Name, "utf-8"))
            break
        else:
            UDPAgent.sendto(bytes("Invalid", "utf-8"), address)
            #conn.sendall(bytes("Invalid", "utf-8"))
            break
