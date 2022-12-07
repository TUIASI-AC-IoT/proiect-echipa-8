from tkinter import *
from Host.Metode.GetRequest import GetRequest
from Host.Metode.SetRequest import SetRequest


window = Tk()


def startWindow():
    window.title("SNMP interface")
    window.configure(width=500, height=500)
    window.configure(bg='lightgrey')

    # Buton Get Request
    getRequestButton = Button(window, text="GetRequest", command=GetRequest)
    getRequestButton.place(x=75, y=400)

    # Buton Set Request
    setRequestButton = Button(window, text="Set Request", command=SetRequest)
    setRequestButton.place(x=175, y=400)


    window.mainloop()
