from tkinter import *
from tkinter import ttk

window = Tk()
window.title("welcome")
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='First')
tab_control.add(tab2, text='Second')

lbl1 = Label(tab1, text = 'label1', padx=15, pady=15)
lbl1.grid(column=0, row=0)
lbl2 = Label(tab1, text = 'label2')
lbl2.grid(column=0, row=0)
tab_control.pack(expand=1, fill='both')

window.mainloop()
