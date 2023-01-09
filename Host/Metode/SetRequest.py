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
    temperatureButton = Button(window, text="Temperatura", command=setRequestTemperature)
    temperatureButton.place(x=20, y=100)

    # Buton Inapoi
    backButton = Button(window, text="Inapoi", command=window.destroy)
    backButton.place(x=35, y=250)

def introdusNume(inputtxt):
    nume = inputtxt.get("1.0", "end-1c")
    print(nume)
    conn = socket.gethostname()

    UDPclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPclient.sendto(str.encode("1.3.6.1.4.1.9.3.5.7"+nume), (conn, 161))

    data = UDPclient.recvfrom(1024)[0]
    print("Received", data.decode())

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

def setRequestTemperature():
    # window pentru introdus numele
    window = Tk()
    window.title("Temperatura:")
    window.configure(width=100, height=300)

    # Buton Inapoi
    celsiusButton = Button(window, text="Celsius", command=temperatura1)
    celsiusButton.place(x=35, y=50)
    # Buton Inapoi
    farenheitButton = Button(window, text="Farenheit", command=temperatura2)
    farenheitButton.place(x=30, y=100)
    # Buton Inapoi
    kelvinButton = Button(window, text="Kelvin", command=temperatura3)
    kelvinButton.place(x=35, y=150)
    # Buton Inapoi
    backButton = Button(window, text="Inapoi", command=window.destroy)
    backButton.place(x=35, y=250)

def temperatura1():
    conn = socket.gethostname()
    temp="Celsius"
    UDPclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPclient.sendto(str.encode("1.3.6.1.4.1.9.3.7.7" + temp), (conn, 161))
    data = UDPclient.recvfrom(1024)[0]
    print("Received", data.decode())

def temperatura2():
    conn = socket.gethostname()
    temp="Farenheit"
    UDPclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPclient.sendto(str.encode("1.3.6.1.4.1.9.3.7.7" + temp), (conn, 161))
    data = UDPclient.recvfrom(1024)[0]
    print("Received", data.decode())

def temperatura3():
    conn = socket.gethostname()
    temp="Kelvin"
    UDPclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPclient.sendto(str.encode("1.3.6.1.4.1.9.3.7.7" + temp), (conn, 161))
    data = UDPclient.recvfrom(1024)[0]
    print("Received", data.decode())