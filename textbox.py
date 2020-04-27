
from tkinter import *
from threading import Thread
from time import sleep

window = Tk()
window.geometry('500x200')

label = Label(window, font=("Courier", 20), text="")
label.grid(row=0, column=0)

text = Entry(window, width=10, font=("Courier", 20), state='disabled')
text.grid(row=1, column=0)

def clicked():
    label.configure(text=text.get())

button = Button(window, font=("Courier", 12), text="Update message now!", command=clicked)
button.grid(row=2, column=0)

def wait():
    for i in range(0, 4):
        label.configure(text=f"wait {3-i} seconds")
        sleep(1)
    label.configure(text="You can now change the message!")
    text.configure(state='normal')


th = Thread(target=wait)
th.daemon = False
th.start()

text.focus()

window.mainloop()
