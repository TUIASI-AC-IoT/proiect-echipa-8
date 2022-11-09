from tkinter import *
from Metode.GetRequest import GetRequestRun
from Metode.SetRequest import SetRequestRun
from Metode.Trap import TrapRun
from Metode.Inform import InformRun


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

    # Trap
    trap = Button(window, text="Set Trap", command=TrapRun)
    trap.place(x=275, y=400)

    # Inform
    trap = Button(window, text="Set Inform", command=InformRun)
    trap.place(x=355, y=400)


    window.mainloop()
