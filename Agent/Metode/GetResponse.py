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
        elif (data == b'GetRequestRam%'):
            #oid: 1.127.10.5.7
            conn.sendall(bytes("Ram % usage: " + MIB.getRamPercent(MIB.getData), "utf-8"))
            break
        elif (data == b'GetRequestRamGB'):
            #oid: 1.127.10.5.8
            conn.sendall(bytes("Ram GB usage: " + MIB.getRamGB(MIB.getData), "utf-8"))
            break
        elif (data == b'GetRequestCpu%'):
            #oid: 1.127.10.5.8
            conn.sendall(bytes("Cpu % usage: " + MIB.getCPUPercent(MIB.getData), "utf-8"))
            break
        else:
            conn.sendall(bytes("Invalid", "utf-8"))
            break

    #test