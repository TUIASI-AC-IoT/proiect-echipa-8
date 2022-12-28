import socket


def ReceiveTrap():
    agentIp = socket.gethostname()
    conn = bytearray(agentIp, "utf-8")
    bufferSize = 1024

    UDPclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    UDPclient.bind((conn, 161))

    while 1:
        data = UDPclient.recvfrom(bufferSize)[0]
        if data[0:7] == "1.5.4.2":
            print("TRAP: RAM % IS: ", data[7:len(data)].decode())
            break
        elif data[0:7] == "1.5.2.2":
            print("TRAP: CPU % IS: ", data[7:len(data)].decode())
            break
        break