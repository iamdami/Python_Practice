from tkinter import *


class MyGUI:
def __init__(self, master) :
self.master=master
master.title("A simple GUI")

self.label = Label(master, text="This is GUI")
self.label.pack()

self.greet_button = Button(master, text="Hi", command=self.greet)
self.greet_button.pack()

self.close_button = Button(master, text="Bye", command=self.quit)
self.close_button.pack()


def greet(self):
print("Greeting")


root=Tk()
my_gui = MyGUI(root)
root.mainloop()
