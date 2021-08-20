from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('Digital Clock')
#root.geometry("50 x 100")
root.configure(bg='green')
root.wm_attributes('-transparentcolor','green')

p1 = PhotoImage(file = '768px-Python-logo-notext.svg (1).png')
root.iconphoto(False, p1)

def current_time():
    string = strftime("%H:%M:%S") 
    lable.config(text=string)
    lable.after(1000,current_time) 

lable = Label(root, font=("ds-digital",80), background="green", foreground="lime")
lable.pack(anchor="center")

current_time()

mainloop()
