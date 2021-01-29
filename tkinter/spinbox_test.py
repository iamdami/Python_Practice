from tkinter import *

window = Tk()
window.title("hello")
window.geometry('350x200')
var=IntVar()
var.set(5)
spin=Spinbox(window, from=0, to=10, width=20, textvalueable=var)
spin.grid(column=0, row=0)
window.mainloop()
