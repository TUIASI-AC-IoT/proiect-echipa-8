from tkinter import *
from Host.Metode.GetRequest import GetRequest
from Host.Metode.SetRequest import SetRequest
from Host.Metode.ReceiveTrap import ReceiveTrap
import threading


window = Tk()


def startWindow():
    window.title("SNMP interface")
    window.configure(width=250, height=250)
    window.configure(bg='lightgrey')

    # Buton Get Request
    getRequestButton = Button(window, text="GetRequest", command=GetRequest)
    getRequestButton.place(x=40, y=200)

    # Buton Set Request
    setRequestButton = Button(window, text="Set Request", command=SetRequest)
    setRequestButton.place(x=140, y=200)

    threading.Thread(target=ReceiveTrap).start()
    window.mainloop()
