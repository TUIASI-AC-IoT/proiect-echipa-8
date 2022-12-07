from tkinter import messagebox
import socket

def GetRequest():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((socket.gethostname(), 161))
    except:
        messagebox.showerror("Error", "Nu s-a putut conecta la Agent")
    s.sendall(bytes("GetRequest", "utf-8"))
    #s.sendall(bytes("Temperature", "utf-8"))
    s.sendall(bytes("Name", "utf-8"))
    data = s.recv(1024)
    print("Received", repr(data))
    s.close()

#test