from Agent.MIB import *
from Host.SNMPPacket import encodeASN1


def GetResponse(OID,address, UDPAgent):

    while 1:
        if not OID: break
        print(OID)
        if (OID[1] == 1):
            # oid: GetRequestTemperatura
            encoded_message = encodeASN1(oid="1.1", text="Null", val=MIB.getTemperatura(MIB.getData,MIB.Temperature))
            UDPAgent.sendto(encoded_message, address)
            break
        elif (OID[1] == 2):
            # oid: GetRequestName
            encoded_message = encodeASN1(oid="1.2", text=MIB.Name, val=0)
            UDPAgent.sendto(encoded_message, address)
            break
        elif (OID[1] == 3):
            #oid: GetRequestRamPercent
            encoded_message = encodeASN1(oid="1.3", text="Null", val=MIB.getRamPercent(MIB.getData))
            UDPAgent.sendto(encoded_message, address)
            break
        elif (OID[1] == 4):
            #oid: GetRequestRamGB
            encoded_message = encodeASN1(oid="1.4", text="Null", val=MIB.getRamGB(MIB.getData))
            UDPAgent.sendto(encoded_message, address)
            break
        elif (OID[1] == 5):
            #oid: GetRequestCpuPercent
            encoded_message = encodeASN1(oid="1.5", text= "Null", val=MIB.getCPUPercent(MIB.getData))
            UDPAgent.sendto(encoded_message, address)
            break
        else:
            UDPAgent.sendto(bytes("Invalid", "utf-8"), address)
            break