from tkinter import *
rt = Tk()
rt.geometry("500x300")
str1 = "Welcome\n Iced coffee is on sale"
msg = Message(rt, text=str1, width=500)
msg.config(bg='lightyellow', font=('times', 20, 'italic'))
msg.pack()
rt.mainloop()
