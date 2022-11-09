from tkinter import messagebox


def SetRequest():
    conectatAgent = 0
    if conectatAgent==1:
        #implementare GetRequest
        conectatAgent=0
    else:
        messagebox.showinfo("Error", "Nu sunteti conectat la agent.")