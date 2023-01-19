from tkinter import *
import socket
from Host.SNMPPacket import encodeASN1, decodeASN1


def GetRequest():

    window = Tk()
    window.title("Selectati informatia dorita")
    window.configure(width=100, height=400)

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
    encoded_message = encodeASN1(oid="1.5", text="Null", val=0)

    print(encoded_message.hex())

    agentIp = socket.gethostname()
    conn = bytearray(agentIp, "utf-8")

    bufferSize = 1024

    UDPclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    UDPclient.sendto(encoded_message, (conn, 161))

    data = UDPclient.recvfrom(bufferSize)[0]
    decoded = decodeASN1(data)
    text = decoded[2]
    print("Received", text)
def GetRequestRamPercent():
    encoded_message = encodeASN1(oid="1.3", text="Null", val=0)

    print(encoded_message.hex())

    agentIp = socket.gethostname()
    conn = bytearray(agentIp, "utf-8")

    bufferSize = 1024

    UDPclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    UDPclient.sendto(encoded_message, (conn, 161))

    data = UDPclient.recvfrom(bufferSize)[0]
    decoded = decodeASN1(data)
    text = decoded[2]
    print("Received", text)

def GetRequestRamGB():
    encoded_message = encodeASN1(oid="1.4", text="Null", val=0)

    print(encoded_message.hex())

    agentIp = socket.gethostname()
    conn = bytearray(agentIp, "utf-8")

    bufferSize = 1024

    UDPclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    UDPclient.sendto(encoded_message, (conn, 161))

    data = UDPclient.recvfrom(bufferSize)[0]
    decoded = decodeASN1(data)
    text = decoded[2]
    print("Received", text)
def GetRequestName():
    encoded_message = encodeASN1(oid="1.2", text="Null", val=0)

    print(encoded_message.hex())

    agentIp = socket.gethostname()
    conn = bytearray(agentIp, "utf-8")

    bufferSize = 1024

    UDPclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    UDPclient.sendto(encoded_message, (conn, 161))

    data = UDPclient.recvfrom(bufferSize)[0]
    decoded = decodeASN1(data)
    text = decoded[1]
    print("Received", text)

def GetRequestTemperatura():
    encoded_message = encodeASN1(oid="1.1", text="Null", val=0)

    print(encoded_message.hex())


    agentIp = socket.gethostname()
    conn = bytearray(agentIp, "utf-8")

    bufferSize = 1024

    UDPclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


    UDPclient.sendto(encoded_message,(conn, 161))


    data = UDPclient.recvfrom(bufferSize)[0]
    decoded = decodeASN1(data)
    text = decoded[2]
    print("Received", text)
