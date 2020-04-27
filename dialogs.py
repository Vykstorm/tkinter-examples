
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title()
window.geometry('350x200')

def clicked():
    messagebox.showwarning('Important message', 'Hello world!')

btn = Button(window,text='Click here', command=clicked)
btn.grid(column=0,row=0)

window.mainloop()
