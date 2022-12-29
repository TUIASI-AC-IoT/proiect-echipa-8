import socket


def ReceiveTrap():


    while 1:
        agentIp = socket.gethostname()
        bufferSize = 1024
        conn = bytearray(agentIp, "utf-8")
        UDPclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

        UDPclient.bind((conn, 162))
        while 1:
            data = UDPclient.recvfrom(bufferSize)[0]
            if not data: break
            print("Received", data.decode())
            if data[0:7] == b'1.5.4.2':
                print("TRAP: RAM % IS: ", data[7:len(data)].decode())
                break
            elif data[0:7] == b'1.5.2.2':
                print("TRAP: CPU % IS: ", data[7:len(data)].decode())
                break
