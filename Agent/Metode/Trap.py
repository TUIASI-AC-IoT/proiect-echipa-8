import time
import threading
from tkinter import *
from tkinter import messagebox

import psutil

def checkTrap():
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
        #



