import socket



from Agent.MIB import *
def GetResponse(OID,address, UDPAgent):

    while 1:
        if not OID: break
        print(OID)
        if (OID == b'GetRequestTemperature'):
            # oid: 1.127.10.5.6
            UDPAgent.sendto(bytes(str(MIB.Temperature), "utf-8"), address)
            #conn.sendall(bytes("Temperatura: 25", "utf-8"))
            break
        elif (OID == b'GetRequestName'):
            # oid: 1.127.10.5.6
            UDPAgent.sendto(bytes(str(MIB.Name), "utf-8"), address)
            #conn.sendall(bytes(MIB.Name , "utf-8"))
            break
        elif (OID == b'GetRequestRam%'):
            #oid: 1.127.10.5.7
            UDPAgent.sendto(bytes(str(MIB.getRamPercent(MIB.getData)), "utf-8"), address)
            #conn.sendall(bytes("Ram % usage: " + MIB.getRamPercent(MIB.getData), "utf-8"))
            break
        elif (OID == b'GetRequestRamGB'):
            #oid: 1.127.10.5.8
            UDPAgent.sendto(bytes(str(MIB.getRamGB(MIB.getData)), "utf-8"), address)
            #conn.sendall(bytes("Ram GB usage: " + MIB.getRamGB(MIB.getData), "utf-8"))
            break
        elif (OID == b'GetRequestCpu%'):
            #oid: 1.127.10.5.8
            UDPAgent.sendto(bytes(str(MIB.getCPUPercent(MIB.getData)), "utf-8"), address)
            #conn.sendall(bytes("Cpu % usage: " + MIB.getCPUPercent(MIB.getData), "utf-8"))
            break
        else:
            UDPAgent.sendto(bytes("Invalid", "utf-8"), address)
            #conn.sendall(bytes("Invalid", "utf-8"))
            break



    #test