from tkinter import *
from tkinter import scrolledtext

window = Tk()
window.title("scroll")
window.geometry('350x200')
txt=scrolledtext.ScrolledText(window,width=40,height=4)
txt.grid(column=0,row=0)
txt.insert(INSERT,'write memo')
window.mainloop()
