from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("welcome")
window.geometry('350x200')

combo = Combobox(window)
combo['values'] = ("peach","melon", "orange", "apple")
combo.current(2)
combo.grid(column=0, row=0)
window.mainloop()
