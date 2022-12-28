import time
import threading
from tkinter import *
from tkinter import messagebox
import socket

import psutil

def checkTrap():
    agentIp = socket.gethostname()
    conn = bytearray(agentIp, "utf-8")
    bufferSize = 1024

    UDPclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    while 1:
        ramPercent = psutil.virtual_memory()[2]

        print(ramPercent)
        if ramPercent > 50:
            UDPclient.sendto(str.encode("1.5.4.2"+ramPercent), (conn, 161))
            break

        cpuPercent = psutil.cpu_percent(4)

        print(cpuPercent)
        if cpuPercent > 60:
            UDPclient.sendto(str.encode("1.5.2.2"+str(cpuPercent)), (conn, 161))
            break

        print("")

        time.sleep(5)
        #



