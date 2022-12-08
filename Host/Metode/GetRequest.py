from tkinter import messagebox
from tkinter import *
import socket

def GetRequest():

    window = Tk()
    window.title("Selectati informatia dorita")
    window.configure(width=100, height=300)

    #Buton Nume
    nameButton = Button(window, text="Nume", command=GetRequestName)
    nameButton.place(x=35, y=50)

    #Buton Temperatura
    temperatureButton = Button(window, text="Temperatura", command=GetRequestTemperatura)
    temperatureButton.place(x=20, y=100)

    #Buton Inapoi
    backButton = Button(window, text="Inapoi", command=window.destroy)
    backButton.place(x=35, y=250)


    window.mainloop()


def GetRequestName():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((socket.gethostname(), 161))
    except:
        messagebox.showerror("Error", "Nu s-a putut conecta la Agent")
    s.sendall(bytes("GetRequest", "utf-8"))
    s.sendall(bytes("Name", "utf-8"))
    data = s.recv(1024)
    print("Received", repr(data))
    s.close()

def GetRequestTemperatura():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((socket.gethostname(), 161))
    except:
        messagebox.showerror("Error", "Nu s-a putut conecta la Agent")
    s.sendall(bytes("GetRequest", "utf-8"))
    s.sendall(bytes("Temperature", "utf-8"))
    data = s.recv(1024)
    print("Received", repr(data))
    s.close()
#test