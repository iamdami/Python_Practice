from tkinter import *

rt = Tk()
rt.title("select fruit")
selected = IntVar()

rad1 = Radiobutton(rt, text='grape', value=1, variable=selected)
rad2 = Radiobutton(rt, text='apple', value=2, variable=selected)
rad3 = Radiobutton(rt, text='berry', value=3, variable=selected)

emptyLabel = Label(rt, text=" ")

rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)


def clicked():
printLabel = Label(rt, text=selected.get())
printLabel =grid(column=0, row=3)


btn = Button(rt, text="click", command = clicked)
btn.grid(column=1, row=2)

rt.mainloop()
