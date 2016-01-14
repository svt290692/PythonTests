from Tkinter import *

root = Tk()


#def print_name():
#    print("My name is vovko")


#print_name_button = Button(root, text="print name", command=print_name)
#print_name_button.pack()

def print_name(event):
    print("My name is vovko")


print_name_button = Button(root, text="print name")
print_name_button.bind("<Button-1>",print_name)
print_name_button.pack()


root.mainloop()
