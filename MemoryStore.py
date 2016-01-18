from Tkinter import *

elements = {}


class ModifiedMixin:
    def _init(self):
        self.clearModifiedFlag()
        self.bind_all('<<Modified>>', self._beenModified)

    def _beenModified(self, event=None):
        if self._resetting_modified_flag: return
        self.clearModifiedFlag()
        self.beenModified(event)

    def beenModified(self, event=None):
        pass

    def clearModifiedFlag(self):
        self._resetting_modified_flag = True
        try:
            self.tk.call(self._w, 'edit', 'modified', 0)
        finally:
            self._resetting_modified_flag = False


class TextWithModifyListener(ModifiedMixin, Text):
    def __init__(self, *a, **b):
        Text.__init__(self, *a, **b)
        self._init()

    def setTextChangedListener(self, listener):
        self.listener = listener

    def beenModified(self, event=None):
        self.listener()

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

        self.addButton = Button(self.frame, text="Add", fg="#0066FF")

        self.searchTitleTopLabel.grid(row=0, column=0,sticky=W)

        self.searchTitleLabel.grid(row=1, column=0)
        self.titleSearchEntry.grid(row=1, column=1)
        self.searchTagLabel.grid(row=1, column=2)
        self.tagSearchEntry.grid(row=1, column=3)
        self.searchButton.grid(row=1, column=4,sticky=W)

        self.elementTitleTopLabel.grid(row=2, column=0,sticky=W)

        self.elementTitleLabel.grid(row=3, column=0)
        self.titleElementEntry.grid(row=3, column=1)
        self.elementTagLabel.grid(row=3, column=2)
        self.tagElementEntry.grid(row=3, column=3)
        self.addButton.grid(row=3, column=4,sticky=W)

def addButtonPushed():
    title = topSection.titleSearchEntry.get()
    tags = topSection.tagSearchEntry.get()

    elementList.insert(ACTIVE, "title")
    elements[title] = ""

def searchButtonPushed():
    pass


def synchronizeElements():
    pass


def textAreaTextChanged():
    print("Yes")

root = Tk()

topSection = TopSideSection(root)

elementList = Listbox(root, bg="#8b0000", fg="white")
elementList.pack(side=LEFT,expand=True,fill=BOTH)

textArea = TextWithModifyListener(root, bg="#ffc966")
textArea.setTextChangedListener(textAreaTextChanged)
textArea.pack(side=LEFT,expand=True, fill=BOTH)

topSection.addButton.config(command=addButtonPushed)
topSection.searchButton.config(command=searchButtonPushed)

mainloop()
