from Tkinter import *


root = Tk()

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

bottom1 = Button(topFrame,text="Very usual button",bg="red")
bottom2 = Button(topFrame,text="second usual button",bg="green")

bottom3 = Button(bottomFrame,text="strange button",bg="yellow")
bottom4 = Button(bottomFrame,text="have no time button",bg="blue")
bottom5 = Button(bottomFrame,text="hurry button",bg="purple")

bottom1.pack(side=LEFT)
bottom2.pack(side=LEFT)
bottom3.pack(side=BOTTOM)
bottom4.pack(side=LEFT)
bottom5.pack(side=LEFT)

root.mainloop()