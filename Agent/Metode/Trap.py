import time
import threading
from tkinter import *
from tkinter import messagebox
import socket

import psutil

def checkTrap():
    agentIp = socket.gethostname()
    conn = bytearray(agentIp, "utf-8")
    okRam=0
    okCPU=0

    UDPagent = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    while 1:
        ramPercent = psutil.virtual_memory()[2]

        print(ramPercent)
        if ramPercent > 50 and okRam==0:
            print("Trimite un pachet trap")
            UDPagent.sendto(str.encode("1.5.4.2"+str(ramPercent)), (conn, 162))
            okRam=1

        cpuPercent = psutil.cpu_percent(4)

        print(cpuPercent)
        if cpuPercent > 50 and okCPU==0:
            print("Trimite un pachet trap")
            UDPagent.sendto(str.encode("1.5.2.2"+str(cpuPercent)), (conn, 162))
            okCPU = 1

        print("")

        time.sleep(5)