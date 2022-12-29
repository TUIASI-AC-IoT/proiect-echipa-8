from Agent.MIB import *

def SetResponse(OID,address, UDPAgent):

    while 1:
        if not OID: break
        if (OID[0:19] == b'1.3.6.1.4.1.9.3.5.7'):
            MIB.Name=OID[19:len(OID)].decode("utf-8")
            MIB.changeName(MIB.Name)

            print(MIB.Name)
            UDPAgent.sendto(bytes(MIB.Name, "utf-8"), address)
            break
        else:
            UDPAgent.sendto(bytes("Invalid", "utf-8"), address)
            break