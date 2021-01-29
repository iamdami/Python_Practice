from tkinter import *


def position(event):
print("mouse position: (%s %s)" % (event.x, event.y))
return

master = Tk()
str= "move mouse"
msg = Message(master, text = str)
msg.config(bg = 'lightgreen', font=('times', 24, 'italic'))
msg.bind('<Motion>', position)
msg.pack()
mainloop()
