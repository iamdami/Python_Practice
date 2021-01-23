from tkinter import *
root = Tk()
root.title("Load icon")
icon = photoImage(file="icon1.gif")
win1 = Label(root, image=icon).pack(side="right")
memo = """show icon"""
win2 = Label(root, justify=LEFT, padx=10, text=memo).pack(side="left")
root.mainloop()
