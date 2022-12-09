import psutil
import self as self
import struct
class MIB():
    Name = "Agent"
    Temperature = 25
    getData = True

    def changeName(NewName):
        Name = NewName

    def changeTemperature(NewTemperature):
        Temperature = NewTemperature

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
