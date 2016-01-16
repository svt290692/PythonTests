from Tkinter import *


def doNothing():
    print("nothing")


root = Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)

subMenu.add_command(label="firstCommand", command=doNothing)
subMenu.add_command(label="secondCommand", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="exit", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

root.mainloop()
