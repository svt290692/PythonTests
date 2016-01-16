from Tkinter import *


class TopSideSection:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack(side=TOP, fill=X)

        self.searchTitleTopLabel = Label(self.frame, text="Search:", fg="#0066FF")
        self.searchTitleLabel = Label(self.frame, text="Title:", fg="#0066FF")
        self.titleSearchEntry = Entry(self.frame, bg="#ccffff", width=50)
        self.searchTagLabel = Label(self.frame, text="Tag:", fg="#0066FF")
        self.tagSearchEntry = Entry(self.frame, bg="#ccffff")

        self.searchButton = Button(self.frame, text="Search", fg="#0066FF")

        self.elementTitleTopLabel = Label(self.frame, text="Element:", fg="#0066FF")
        self.elementTitleLabel = Label(self.frame, text="Title::", fg="#0066FF")
        self.titleElementEntry = Entry(self.frame, bg="#ccffff", width=50)
        self.elementTagLabel = Label(self.frame, text="Tags:", fg="#0066FF")
        self.tagElementEntry = Entry(self.frame, bg="#ccffff")

        self.searchTitleTopLabel.grid(row=0, column=0)

        self.searchTitleLabel.grid(row=1, column=0)
        self.titleSearchEntry.grid(row=1, column=1)
        self.searchTagLabel.grid(row=1, column=2)
        self.tagSearchEntry.grid(row=1, column=3)
        self.searchButton.grid(row=1, column=4)

        self.elementTitleTopLabel.grid(row=2, column=0)

        self.elementTitleLabel.grid(row=3, column=0)
        self.titleElementEntry.grid(row=3, column=1)
        self.elementTagLabel.grid(row=3, column=2)
        self.tagElementEntry.grid(row=3, column=3)


root = Tk()

topSection = TopSideSection(root)

elementList = Listbox(root, bg="#8b0000")
elementList.pack(side=LEFT, fill=Y)

textArea = Text(root, bg="#ffc966")
textArea.pack(side=RIGHT, fill=Y)

mainloop()
