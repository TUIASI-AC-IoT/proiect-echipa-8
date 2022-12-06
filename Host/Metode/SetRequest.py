from tkinter import messagebox
import socket


def SetRequestRun():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 161))
    s.sendall(bytes("SetRequest", "utf-8"))
    data = s.recv(1024)
    print("Received", repr(data))
    s.close()
