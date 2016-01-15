from Tkinter import *

root = Tk()


def leftButtonClieck(event):
    print("Left Button Has been clicked")


def rightButtonClieck(event):
    print("Right Button Has been clicked")


def middleButtonClieck(event):
    print("Middle Button Has been clicked")


frame = Frame(root, width=300, height=250)
frame.bind("<Button-1>", leftButtonClieck)
frame.bind("<Button-2>", middleButtonClieck)
frame.bind("<Button-3>", rightButtonClieck)

frame.pack()
root.mainloop()
