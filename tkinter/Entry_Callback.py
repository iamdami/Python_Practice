from tkinter import *

master = Tk()  # creating master window

# Entry widget
e = Entry(master)
e.pack()

# set the focus
e.focus_set()


def callback():
    print(e.get())  # text you may want to use later


# Button widget
b = Button(master, text="OK", width=10, command=callback)
b.pack()

mainloop()

