import socket

def GetResponseRun(s):
    s.sendall(bytes("GetRequest", "utf-8"))
