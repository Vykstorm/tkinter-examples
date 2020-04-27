from tkinter import *

window = Tk()
window.title('Tkinter example')
window.geometry('350x200')

label = Label(window, text='Hello world', font=("Arial Bold", 50))
label.grid(column=0, row=0)

def clicked():
    label.configure(text="Bye world")

button = Button(window, text="Click me", font=("Arial Bold", 25), bg="orange", fg="red", command=clicked)
button.grid(column=0, row=1)

window.mainloop()
