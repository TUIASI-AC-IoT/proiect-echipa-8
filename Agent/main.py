import socket
from Metode.GetResponse import GetResponse
from Metode.SetResponse import SetResponse



#test
UDPport=161
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), UDPport))
s.listen(1)
print('Asteapta Conexiuni')
conn, addr = s.accept()
print('Conectat la', addr)
while 1:
    data = conn.recv(1024)
    if not data: break
    print(data)
    if (data == b'GetRequestTemperature'):
        # oid: 1.127.10.5.6
        GetResponse(conn,data)
        break
    if (data == b'GetRequestName'):
        # oid: 1.127.10.5.6
        GetResponse(conn, data)
        break
    else:
        conn.sendall(bytes("Invalid", "utf-8"))
        break

conn.close()
