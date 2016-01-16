from Tkinter import *


def doNothing():
    print("nothing")


root = Tk()
# menu
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

# toolbar

toolbar = Frame(root, bg="#0066FF")
insertButt = Button(toolbar, text="insertButton", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)  # pad(x|y)=padding
printButt = Button(toolbar, text="printtButton", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)  # pad(x|y)=padding

toolbar.pack(side=TOP, fill=X)

# Status Bar

status = Label(root, text="Preparing to text", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()
