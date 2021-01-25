from tkinter import *

rt = Tk()
rt.title("과일 선택")
selected = IntVar()

rad1 = Radiobutton(rt, text='포도', value=1, variable=selected)
rad2 = Radiobutton(rt, text='사과', value=2, variable=selected)
rad3 = Radiobutton(rt, text='딸기', value=3, variable=selected)

emptyLabel = Label(rt, text=" ")

rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)


def clicked():
printLabel = Label(rt, text=selected.get())
printLabel =grid(column=0, row=3)


btn = Button(rt, text="클릭해방", command = clicked)
btn.grid(column=1, row=2)

rt.mainloop()
