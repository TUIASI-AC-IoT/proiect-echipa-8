import psutil
import self as self
import struct

import time
from tkinter import *
from tkinter import messagebox
class MIB():
    Name = "Agent"
    Temperature = 25
    getData = True


    def changeName(NewName):
        Name = NewName


    def getRamPercent(self):
        ramPercent = psutil.virtual_memory()[2]
        ramPercent = str(ramPercent)
        return ramPercent

    def getRamGB(self):
        ramGB = psutil.virtual_memory()[3]/1000000000
        ramGB = str(ramGB)
        return ramGB

    def getCPUPercent(self):
        cpuPercent = psutil.cpu_percent(4)
        cpuPercent = str(cpuPercent)
        return cpuPercent

    def checkTrap(self):
        while 1:
            ramPercent = psutil.virtual_memory()[2]

            print(ramPercent)
            if ramPercent > 50:
                messagebox.showerror('TRAP', 'Ram% mai mare decat 50%')
                break

            cpuPercent = psutil.cpu_percent(4)

            print(cpuPercent)
            if cpuPercent > 60:
                messagebox.showerror('TRAP', 'Cpu% mai mare decat 60%')
                break

            print("")

            time.sleep(5)
