from tkinter import *
import socket

from Host.SNMPPacket import encodeASN1, decodeASN1


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
    encoded_message = encodeASN1(oid="2.1", text=nume, val=0)
    UDPclient.sendto(encoded_message, (conn, 161))

    data = UDPclient.recvfrom(1024)[0]
    text = decodeASN1(data)[1]
    print("Numele a fost schimbat in ", text)

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
    encoded_message = encodeASN1(oid="2.2", text=temp, val=0)
    UDPclient.sendto(encoded_message, (conn, 161))
    data = UDPclient.recvfrom(1024)[0]
    text = decodeASN1(data)[1]
    print("Temperatura a fost schimbata in ", text)

def temperatura2():
    conn = socket.gethostname()
    temp="Farenheit"
    UDPclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    encoded_message = encodeASN1(oid="2.2", text=temp, val=0)
    UDPclient.sendto(encoded_message, (conn, 161))
    data = UDPclient.recvfrom(1024)[0]
    text = decodeASN1(data)[1]
    print("Temperatura a fost schimbata in ", text)

def temperatura3():
    conn = socket.gethostname()
    temp="Kelvin"
    UDPclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    encoded_message = encodeASN1(oid="2.2", text=temp, val=0)
    UDPclient.sendto(encoded_message, (conn, 161))
    data = UDPclient.recvfrom(1024)[0]
    text = decodeASN1(data)[1]
    print("Temperatura a fost schimbata in ", text)