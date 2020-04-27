
from tkinter import *
from tkinter.ttk import Checkbutton

window = Tk()
window.geometry('200x200')

state = BooleanVar()
state.set(True)
check_button = Checkbutton(window, text='Choose', var=state)
check_button.grid(row=0, column=0)

window.mainloop()
