from tkinter import messagebox
from tkinter import *
import socket


def SetRequest():

    window = Tk()
    window.title("Selectati informatia dorita")
    window.configure(width=100, height=300)

    # Buton Nume
    nameButton = Button(window, text="Nume", command=setRequestName)
    nameButton.place(x=35, y=50)

    # Buton Temperatura
    temperatureButton = Button(window, text="Temperatura", command=setRequestTemperatura)
    temperatureButton.place(x=20, y=100)

    # Buton Inapoi
    backButton = Button(window, text="Inapoi", command=window.destroy)
    backButton.place(x=35, y=250)

def introdusNume(inputtxt):
    nume = inputtxt.get("1.0", "end-1c")
    print(nume)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((socket.gethostname(), 161))
    except:
        messagebox.showerror("Error", "Nu s-a putut conecta la Agent")
    s.sendall(bytes("SetRequest", "utf-8"))
    s.sendall(bytes("Name", "utf-8"))

    s.sendall(bytes(nume, "utf-8"))
    data = s.recv(1024)
    print("Received", repr(data))
    s.close()
def setRequestName():

    #window pentru introdus numele
    window = Tk()
    window.title("Introduceti numele")
    window.configure(width=300, height=100)

    inputtxt = Text(window, height=10,
                    width=25,
                    bg="light yellow")
    inputtxt.pack()

    Display = Button(window, height=2,
                     width=20,
                     text="SetName",
                     command=lambda: introdusNume(inputtxt))
    Display.pack()




def setRequestTemperatura():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((socket.gethostname(), 161))
    except:
        messagebox.showerror("Error", "Nu s-a putut conecta la Agent")
    s.sendall(bytes("SetRequest", "utf-8"))
    s.sendall(bytes("Temperature", "utf-8"))
    s.sendall(bytes("20", "utf-8"))
    data = s.recv(1024)
    print("Received", repr(data))
    s.close()



#test