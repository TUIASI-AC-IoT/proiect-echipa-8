import socket

def SetResponse():

    while 1:
        if not data: break
        print(data)
        if (data == b'Temperatura'):
            # oid: 1.127.10.5.6
            conn.sendall(bytes("Temperatura: 25", "utf-8"))

        else:
            conn.sendall(bytes("Invalid", "utf-8"))
