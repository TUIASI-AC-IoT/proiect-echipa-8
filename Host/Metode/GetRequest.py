from tkinter import messagebox
from tkinter import *
import socket

def GetRequest():

    window = Tk()
    window.title("Selectati informatia dorita")
    window.configure(width=100, height=400)

    pressed = False


    #Buton Nume
    nameButton = Button(window, text="Nume", command=GetRequestName)
    nameButton.place(x=35, y=50)

    #Buton Temperatura
    temperatureButton = Button(window, text="Temperatura", command=GetRequestTemperatura)
    temperatureButton.place(x=20, y=100)

    #Buton Ram % Usage
    ramPercentButton = Button(window, text="Ram % Usage", command=GetRequestRamPercent)
    ramPercentButton.place(x=20, y=150)

    #Buton Ram Gb Usage
    ramGBButton = Button(window, text="Ram Gb Usage", command=GetRequestRamGB)
    ramGBButton.place(x=20, y=200)

    #Buton Cpu Usage
    cpuUsageButton = Button(window, text="Cpu Usage", command=GetRequestCpuUsage)
    cpuUsageButton.place(x=20, y=250)

    #Buton Inapoi
    backButton = Button(window, text="Inapoi", command=window.destroy)
    backButton.place(x=35, y=350)


    window.mainloop()

def GetRequestCpuUsage():
    agentIp = socket.gethostname()
    conn = bytearray(agentIp, "utf-8")

    bufferSize = 1024

    UDPclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    UDPclient.sendto(str.encode("2.16.840.1.113883.3.72.5.9.1"), (conn, 161))

    # s.sendall(bytes("GetRequest", "utf-8"))
    # s.sendall(bytes("Temperature", "utf-8"))
    data = UDPclient.recvfrom(bufferSize)[0]

    print("Received", data.decode())
def GetRequestRamPercent():
    agentIp = socket.gethostname()
    conn = bytearray(agentIp, "utf-8")

    bufferSize = 1024

    UDPclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    UDPclient.sendto(str.encode("2.16.840.1.1.2021.255.3.56.9"), (conn, 161))

    # s.sendall(bytes("GetRequest", "utf-8"))
    # s.sendall(bytes("Temperature", "utf-8"))
    data = UDPclient.recvfrom(bufferSize)[0]
    print("Received", data.decode())

def GetRequestRamGB():
    agentIp = socket.gethostname()
    conn = bytearray(agentIp, "utf-8")

    bufferSize = 1024

    UDPclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    UDPclient.sendto(str.encode("2.16.840.1.113733.3.4.3.2.1.1"), (conn, 161))

    # s.sendall(bytes("GetRequest", "utf-8"))
    # s.sendall(bytes("Temperature", "utf-8"))
    data = UDPclient.recvfrom(bufferSize)[0]
    print("Received", data.decode())
def GetRequestName():
    agentIp = socket.gethostname()
    conn = bytearray(agentIp, "utf-8")

    bufferSize = 1024

    UDPclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    UDPclient.sendto(str.encode("2.16.840.1.4.1.27385.3.9.6"), (conn, 161))

    # s.sendall(bytes("GetRequest", "utf-8"))
    # s.sendall(bytes("Temperature", "utf-8"))
    data = UDPclient.recvfrom(bufferSize)[0]
    print("Received", data.decode())

def GetRequestTemperatura():

    agentIp = socket.gethostname()
    conn = bytearray(agentIp, "utf-8")

    bufferSize = 1024

    UDPclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


    UDPclient.sendto(str.encode("2.16.840.1.113883.4.9.8.7.6.5"),(conn, 161))

    #s.sendall(bytes("GetRequest", "utf-8"))
    #s.sendall(bytes("Temperature", "utf-8"))
    data = UDPclient.recvfrom(bufferSize)[0]
    print("Received", data.decode())
#test