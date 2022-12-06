from tkinter import *
from Host.Metode.GetRequest import GetRequestRun
from Host.Metode.SetRequest import SetRequestRun


window = Tk()


def startWindow():
    window.title("SNMP interface")
    window.configure(width=500, height=500)
    window.configure(bg='lightgrey')

    # Buton Get Request
    getRequestButton = Button(window, text="GetRequest", command=GetRequestRun)
    getRequestButton.place(x=75, y=400)

    # Buton Set Request
    setRequestButton = Button(window, text="Set Request", command=SetRequestRun)
    setRequestButton.place(x=175, y=400)


    window.mainloop()
