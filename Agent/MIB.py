import psutil
import wmi

import time
from tkinter import *
from tkinter import messagebox
class MIB():
    Name = "Agent"
    Temperature= "Celsius"
    getData =True


    def getTemperatura(self,Temperature):
        w = wmi.WMI(namespace="root\OpenHardwareMonitor")
        temperature_infos = w.Sensor()
        for sensor in temperature_infos:
            if sensor.SensorType == u'Temperature':
                break
        if Temperature == "Celsius":
                    return sensor.Value
        elif Temperature == "Farenheit":
                    return (sensor.Value*1.8+32)
        elif Temperature == "Kelvin":
                    return (sensor.Value+273.15)
        return("nuuu")


    def changeTemperature(NewTemperature):
        Temperature=NewTemperature



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
