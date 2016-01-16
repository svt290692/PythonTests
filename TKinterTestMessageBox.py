import tkMessageBox
from Tkinter import *

root = Tk()

# tkMessageBox.showinfo('window Title',"you are here")

answer = tkMessageBox.askquestion("Question 1 ", 'are you sure?')

if answer == 'yes':
    print("good!")

root.mainloop()
