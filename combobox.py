
from tkinter import *
from tkinter.ttk import Combobox

window = Tk()
window.geometry('400x200')

combo = Combobox(window)
combo['values'] = (1, 2, 3, 4, "Hello world", 3.5)
combo.grid(row=0, column=0)
combo.current(2)

label = Label(window, font=("Courier", 16), text=f"Current selected:{combo.get()}")
label.grid(row=1, column=0)

def clicked():
    label.configure(text=f"Current selected:{combo.get()}")

button = Button(window, font=("Courier", 12), text="Update message now!", command=clicked)
button.grid(row=2, column=0)

window.mainloop()
