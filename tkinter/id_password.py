from tkinter import *
root = Tk()
root.geometry("300x100")

label1 = Label(root, text='id : ')
label2 = Label(root, text='password : ')

entry1 = Entry(root)
entry2 = Entry(root)

label1.grid(row=0, column=0, sticky=E)
label2.grid(row=1, column=0, sticky=E)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

root.mainloop()
