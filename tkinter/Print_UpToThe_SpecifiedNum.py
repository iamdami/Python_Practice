from tkinter import *
from tkinter import scrolledtext

window = Tk()
window.title("scroll")
window.geometry('350x200')
txt=scrolledtext.ScrolledText(window,width=40,height=4)
txt.grid(column=0, row=0)
txt.insert(INSERT, 'write memo')
txt.insert(INSERT, '\nSecond memo entered')
txt.delete(1.0, 1.5)  # Print up to the 5th letter of the first line memo
window.mainloop()
