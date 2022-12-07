import socket


def SetResponse(conn,data):
    Name='Andrei'
    print(Name)
    while 1:
        if not data: break
        if (data[0:14] == b'SetRequestName'):
            # oid: 1.127.10.5.6
            Name=data[14:len(data)].decode("utf-8")
            print(Name)
            conn.sendall(bytes("Nume schimbat in :"+Name, "utf-8"))
            break
        else:
            conn.sendall(bytes("Invalid", "utf-8"))
            break
