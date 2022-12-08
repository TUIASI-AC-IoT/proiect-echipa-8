import socket
from Agent.MIB import *
def GetResponse(conn,data):

    while 1:
        if not data: break
        print(data)
        if (data == b'GetRequestTemperature'):
            # oid: 1.127.10.5.6
            conn.sendall(bytes("Temperatura: 25", "utf-8"))
            break
        elif (data == b'GetRequestName'):
            # oid: 1.127.10.5.6
            conn.sendall(bytes(MIB.Name , "utf-8"))
            break
        else:
            conn.sendall(bytes("Invalid", "utf-8"))
            break

    #test