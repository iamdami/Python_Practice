from tkinter import *
root = Tk()


def result():
print("apple")


button1 = Button(root, text='fruit', command=result)
button1.pack()

root.mainloop()
