from Tkinter import *


root = Tk()

one = Label(root,text="one",bg="grey",fg="cyan")
one.pack()

two = Label(root,text="two",bg="#0066FF",fg="green")
two.pack(fill=X)

three = Label(root,text="three",bg="grey",fg="white")
three.pack(side=LEFT,fill=Y)

root.mainloop()