from Agent.MIB import *
from Host.SNMPPacket import encodeASN1


def SetResponse(OID,address, UDPAgent, text):

    while 1:
        if not OID: break
        if (OID[1] == 1):
            MIB.Name=text
            MIB.changeName(MIB.Name)

            print(MIB.Name)
            encoded_message = encodeASN1(oid="2.1", text=MIB.Name, val=0)
            UDPAgent.sendto(encoded_message, address)
            break
        elif(OID[1] == 2):
            MIB.Temperature = text
            MIB.changeTemperature(MIB.Temperature)
            print(MIB.Temperature)
            encoded_message = encodeASN1(oid="2.2", text=MIB.Temperature, val=0)
            UDPAgent.sendto(encoded_message, address)
            break
        else:
            UDPAgent.sendto(bytes("Invalid", "utf-8"), address)
            break