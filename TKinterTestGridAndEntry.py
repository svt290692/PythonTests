from Tkinter import *


root = Tk()

name_label = Label(root,text="Name: ")
pass_label = Label(root,text="Password: ")

name_entry = Entry(root)
pass_entry = Entry(root)

name_label.grid(row=0,sticky=E)
pass_label.grid(row=1,sticky=E)

name_entry.grid(row=0,column=1)
pass_entry.grid(row=1,column=1)

check_box = Checkbutton(root,text="keep me logged in")
check_box.grid(columnspan=2,row=2)

root.mainloop()