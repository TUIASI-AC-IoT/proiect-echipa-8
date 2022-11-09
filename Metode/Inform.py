from tkinter import messagebox

def InformRun():
    conectatAgent = 0
    if conectatAgent==1:
        #implementare Inform
        conectatAgent=0
    else:
        messagebox.showinfo("Error", "Nu sunteti conectat la agent.")