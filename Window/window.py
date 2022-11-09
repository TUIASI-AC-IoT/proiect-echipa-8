from tkinter import *
from Metode.GetRequest import GetRequest
from Metode.SetRequest import SetRequest
from tkinter import messagebox

window = Tk()

def startWindow():
    window.title("SNMP interface")
    window.configure(width=500, height=500)
    window.configure(bg='lightgrey')

    #Buton Get Request
    GetRequestButton = Button(window, text="GetRequest", command=GetRequest)
    GetRequestButton.place(x=100, y=400)

    #Buton Set Request
    SetRequestButton = Button(window, text="Set Request", command=SetRequest)
    SetRequestButton.place(x=200, y=400)
    window.mainloop()


def test():
    conectatAgent = 0
    if conectatAgent==1:
        #implementare GetRequest
        conectatAgent=0
    else:
        messagebox.showinfo("Error", "Nu sunteti conectat la agent.")