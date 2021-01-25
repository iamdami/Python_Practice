from tkinter import *

root = Tk()
root.geometry("400x300")

topFrame = Frame(root)
bottomFrame = Frame(root)
leftFrame = Frame(root)
rightFrame = Frame(root)

topFrame.pack(side=TOP)
bottomFrame.pack(side=BOTTOM)
leftFrame.pack(side=LEFT)
rightFrame.pack(side=RIGHT)

b1= Button(topFrame, text="button1", fg="red")
b2= Button(leftFrame, text="button2", fg="green")
b3= Button(rightFrame, text="button3", fg="black")
b4= Button(bottomFrame, text="button4", fg="purple")

b1.pack()
b2.pack()
b3.pack()
b4.pack()

root.mainloop()
