import socket
from Metode.GetResponse import GetResponse
from Metode.SetResponse import SetResponse
from Metode.Trap import *
import threading

threading.Thread(target=checkTrap()).start()
daemon = threading.Thread(target=checkTrap(), daemon=True, name='Monitor')
while 1:
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
        if (data[0:10] == b'GetRequest'):
            # oid: 1.127.10.5.6
            GetResponse(conn,data)
        elif (data[0:10] == b'SetRequest'):
            # oid: 1.127.10.5.6
            SetResponse(conn,data)
        else:
            conn.sendall(bytes("Invalid", "utf-8"))
            break

conn.close()
