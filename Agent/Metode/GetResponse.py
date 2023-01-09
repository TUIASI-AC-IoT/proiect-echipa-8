from Agent.MIB import *
def GetResponse(OID,address, UDPAgent):

    while 1:
        if not OID: break
        print(OID)
        if (OID == b'2.16.840.1.113883.4.9.8.7.6.5'):
            # oid: GetRequestTemperatura
            UDPAgent.sendto(bytes(str(MIB.getTemperatura(MIB.getData,MIB.Temperature)), "utf-8"), address)
            break
        elif (OID == b'2.16.840.1.4.1.27385.3.9.6'):
            # oid: GetRequestName
            UDPAgent.sendto(bytes(str(MIB.Name), "utf-8"), address)
            break
        elif (OID == b'2.16.840.1.1.2021.255.3.56.9'):
            #oid: GetRequestRamPercent
            UDPAgent.sendto(bytes(str(MIB.getRamPercent(MIB.getData)), "utf-8"), address)
            break
        elif (OID == b'2.16.840.1.113733.3.4.3.2.1.1'):
            #oid: GetRequestRamGB
            UDPAgent.sendto(bytes(str(MIB.getRamGB(MIB.getData)), "utf-8"), address)
            break
        elif (OID == b'2.16.840.1.113883.3.72.5.9.1'):
            #oid: GetRequestCpuPercent
            UDPAgent.sendto(bytes(str(MIB.getCPUPercent(MIB.getData)), "utf-8"), address)
            break
        else:
            UDPAgent.sendto(bytes("Invalid", "utf-8"), address)
            break