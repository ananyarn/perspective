from tkinter import *
from tkinter.ttk import *
from time import strftime
r = Tk()
r.title('CLOCK')

def time():
    s = strftime('%H:%M:%S %p')
    label.config(text=s)
    label.after(1000,time)
    
label = Label(r,font=("ds-digital",50), background="black", foreground="cyan")
label.pack(anchor="center")
time()
mainloop()
