from tkinter import *

with open('C:/Users/Dami/Desktop/python/3.txt', 'r') as ascending:
    arr = [int(float(i)) for i in ascending.read().split(sep=",")]

root = Tk()
root.title('Sort Ascending')
root.geometry('300x100+200+200')
root.resizable(False, False)

label1 = Label(root, text=' ')
label2 = Label(root, text='Sort Ascending')
label1.pack()
label2.pack()


def ascendingSort():
    label2.config(text='result: ' + str(sorted(arr)))


def base():
    label1.config(text='Num value read from file: ' + str(arr))


def whenClick():
    ascendingSort()
    base()


button = Button(root, text='Click to Sort', command=whenClick)
button.pack()

root.mainloop()
