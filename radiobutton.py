
from tkinter import *
from tkinter.ttk import Radiobutton

window = Tk()
window.geometry('200x200')

selected = IntVar()
rad1 = Radiobutton(window,text='First', value=1, variable=selected)
rad2 = Radiobutton(window,text='Second', value=2, variable=selected)
rad3 = Radiobutton(window,text='Third', value=3, variable=selected)

rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)

button = Button(window, text="Click me!", command=lambda: print(selected.get()))
button.grid(row=1, column=0)

window.mainloop()
