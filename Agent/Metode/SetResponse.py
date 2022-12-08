import socket
from Agent.MIB import *

def SetResponse(conn,data):

    while 1:
        if not data: break
        if (data[0:14] == b'SetRequestName'):
            # oid: 1.127.10.5.6
            MIB.Name=data[14:len(data)].decode("utf-8")
            MIB.changeName(MIB.Name)
            print(MIB.Name)
            conn.sendall(bytes("Nume schimbat in :"+MIB.Name, "utf-8"))
            break
        else:
            conn.sendall(bytes("Invalid", "utf-8"))
            break
