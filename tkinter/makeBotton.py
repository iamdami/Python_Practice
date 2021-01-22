from tkinter import *
rt = Tk()
rt.geometry("500x300")
rt.title("title")
lbl = Label(rt, text="zip ga go si per", font=("Arial Bold", 20))
lbl.grid(column=0, row=0)
btn = Button(rt, text="Click me")
btn.grid(column=1, row=0)
