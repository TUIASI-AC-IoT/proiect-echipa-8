import socket

def GetRequestRun():
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
        if (data == b'Temperatura'):
            # oid: 1.127.10.5.6
            conn.sendall(bytes("Temperatura: 25", "utf-8"))

        else:
            conn.sendall(bytes("Invalid", "utf-8"))
    conn.close()