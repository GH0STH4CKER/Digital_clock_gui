from tkinter import *
from tkinter.ttk import *
import time

root = Tk()
root.title('Digital Clock')
root.configure(bg='black')

p1 = PhotoImage(file = 'C:\\Users\\Dimuth De Zoysa\\Pictures\\768px-Python-logo-notext.svg.png')
root.iconphoto(False, p1)

lable = Label(root, font=("ds-digital",70), background="black", foreground="lime")
lable.pack(anchor="center")

def current_time() :

    string = time.strftime("%H:%M:%S")
    lable.config(text=string)
    lable.after(1000,current_time)

current_time() 

mainloop()