from Tkinter import *


class GoodButtons:
    def __init__(self, master):  # maseter - root or main window

        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="print message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="QUIT", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("GREAT MESSAGE!")


root = Tk()

goodButtonClass = GoodButtons(root)

root.mainloop()
