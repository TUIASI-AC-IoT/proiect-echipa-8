import socket
from Metode.GetResponse import GetResponseRun

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 161))
s.listen(1)
print('Asteapta Conexiuni')
conn, addr = s.accept()
print('Conectat la', addr)
while 1:
    data = conn.recv(1024)
    if not data: break
    print(data)
    if (data == b'GetRequest'):
        #GetResponse
        GetResponseRun(s)
    else:
        if(data == b'SetRequest'):
            #SetResponse
            conn.sendall(bytes("SetResponse", "utf-8"))
conn.close()
