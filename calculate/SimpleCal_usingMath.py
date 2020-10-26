from tkinter import *
from math import *


def cal(event):
    label.configure(text="result: " + str(eval(entry.get())))


root = Tk()

Label(root, text="Enter the Formula:").pack()
# ex) 3*5

entry = Entry(root)
entry.bind('<Return>', cal)
entry.pack()

label = Label(root, text="result: ")
label.pack()

root.mainloop()
