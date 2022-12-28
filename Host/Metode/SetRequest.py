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

    # Buton Inapoi
    backButton = Button(window, text="Inapoi", command=window.destroy)
    backButton.place(x=35, y=250)

def introdusNume(inputtxt):
    nume = inputtxt.get("1.0", "end-1c")
    print(nume)
    conn = socket.gethostname()

    UDPclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPclient.sendto(str.encode("SetRequestName"+nume), (conn, 161))

    data = UDPclient.recvfrom(1024)
    print("Received", repr(data))

def setRequestName():

    #window pentru introdus numele
    window = Tk()
    window.title("Introduceti numele")
    window.configure(width=300, height=100)

    inputtxt = Text(window, height=2,
                    width=10,
                    bg="light yellow")
    inputtxt.pack()

    Display = Button(window, height=2,
                     width=20,
                     text="SetName",
                     command=lambda: introdusNume(inputtxt))
    Display.pack()




#test