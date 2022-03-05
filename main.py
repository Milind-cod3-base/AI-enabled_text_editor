
#Using Tkinter libraries of Python, this project creates a notepad. Tkinter will help with GUI.

# Functions / Menus like 'file, edit, saving, opening, cut/paste etc' will be available in the GUI.

import os
import tkinter   #python's GUI package installed
from tkinter import *

from tkinter.messagebox import *    #its to write text / message in the notepad

from tkinter.filedialog import *   #used for the dialog box to appear when you are opening file from anywhere in your system / saving your file in a particular position of place

#creating a class

class editorNotepad:

    __root = Tk()   #class's name mangling done. Can be called only by ._classname__namemangle

    #setting window height and width of the editor
    __ofHeight = 400
    __ofWidth = 400
    __ofTextArea = Text(__root)
    __ofMenuBar = Menu(__root)
    
    #creating three panels in the menu bar
    __ofFileMenu = Menu(__ofMenuBar, tearoff=0)  #here tearoff is set to 0 to avoid the dotted lines at the top of the drop down menu.
    __ofEditMenu = Menu(__ofMenuBar, tearoff=0)
    __ofHelpMenu = Menu(__ofMenuBar, tearoff=0)
    __ofAiMenu = Menu(__ofMenuBar, tearoff=0)    #object created to store the ai call details. Its on the menubar and tearoff is set to 0 and is place at the end in menubar

    #A scrollbar to scroll up and down in the window
    __ofScrollBar = Scrollbar(__ofTextArea)   #setting up a scrollbar in the entire text area
    __file =   None

    def __init__(self, **kwargs):  
        
        #init initialises objects state (constructor) - it sets the characteristics of the class.
        #**kwargs will let the function to accept multiple number of keyboard arguments

        #icon setup
        try:
            self.__root.wm_iconbitmap("Editor.ico")

        except: 
            pass

        #window size setup - where default is marked as 400x400
        try:
            self.__ofWidth = kwargs['width']

        except KeyError:
            pass

        try:
            self.__ofHeight = kwargs['height']

        except KeyError:
            pass

        #window text must be set

        self.__root.title("Untitled - Editor pad")

        #Center the window
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()  #bug fixed


        #left aligning the window

        left = (screenWidth / 2) - (self.__ofWidth /2)

        #right aligning
        top = (screenHeight /2) - (self.__ofHeight /2)

        #Top and bottom alignment
        self.__root.geometry('%dx%d+%d+%d' %(self.__ofWidth, self.__ofHeight, left, top))

        #making text area resizable(auto)

        self.__root.grid_rowconfigure(0,weight=1)  #minisize(minimum size of the row), weight(how much does  the additional space propagate to this row)
        self.__root.grid_columnconfigure(0,weight=1)

        #Adding widget controls
        self.__ofTextArea.grid(sticky= N + E + S +W )

        #opening a new file code
        self.__ofFileMenu.add_command(label="New", command = self.__newFile)

        #opening existing file
        self.__ofFileMenu.add_command(label = "Open", command= self.__openFile)

        #saving a file
        self.__ofFileMenu.add_command(label="Save", command = self.__saveFile)  #bug fixed

        #creating a new line in the dialoge

        self.__ofFileMenu.add_separator()
        self.__ofFileMenu.add_command(label= "Exit", command= self.__quitApplication)
        self.__ofMenuBar.add_cascade(label="File", menu = self.__ofFileMenu) #add heirarichal menu item


        #Cutting a text feature
        self.__ofEditMenu.add_command(label = "Cut", command = self.__cut)

        #copy a text feature
        self.__ofEditMenu.add_command(label="Copy", command =self.__copy)

        #paste feature
        self.__ofEditMenu.add_command(label="Paste", command=self.__paste)

        #To give a feature of editing
        self.__ofMenuBar.add_cascade(label="Edit",menu= self.__ofEditMenu)   #bug fixed, assigning attribute menu instead of command.

        #CASCADE creates a new hierarchical menu by associating a given menu to a parent menu

        #to create a feature of description of the Notepad/editor
        self.__ofHelpMenu.add_command(label="About Editor", command=self.__showAbout)

        self.__ofMenuBar.add_cascade(label="Help", menu=self.__ofHelpMenu)

        self.__root.config(menu=self.__ofMenuBar)

        self.__ofScrollBar.pack(side=RIGHT,fill=Y)
        #fill packs a widget inside a container, filling the entire container. 

        # Scrollbar will adjust automatically according to the content
        self.__ofScrollBar.config(command=self.__ofTextArea.yview)
        self.__ofTextArea.config(yscrollcommand=self.__ofScrollBar.set)

    def __quitApplication(self):

        self.__root.destroy()  #this will exit the application

    def __showAbout(self):
        showinfo("Editor", "Milind")

    def __openFile(self):

        self.__file = askopenfilename(defaultextension=".txt",filetypes=[("All files", "*.*"),("Text Documents", "*.txt")])

        if self.__file =="":
            self.__file= None  #there is no file to open

        else:
                #try to open the file and set the window title / name
            self.__root.title(os.path.basename(self.__file) + " - Editor")
            self.__ofTextArea.delete(1.0,END)

            file = open(self.__file,"r")

            self.__ofTextArea.insert(1.0,file.read())

            file.close()

    def __newFile(self):
        self.__root.title("Untitled - Editor")
        self.__file= None
        self.__ofTextArea.delete(1.0, END) #deletes the characters between index 1 and index 2 (not including them)

    
    def __saveFile(self):

        if self.__file == None:    #saving a newly built file

            self.__file = asksaveasfilename(initialfile = "Untitled.txt", defaultextension=".txt", filetypes=[("All files", "*.*"),("Text Documents", "*.txt")])
            #unamed file will be untitled and default extension would be txt

            if self.__file=="":
                self.__file= None

            else:
                #try to save the file

                file = open(self.__file,"w")
                file.write(self.__ofTextArea.get(1.0,END))
                file.close()

                #changing the window title
                self.__root.title(os.path.basename(self.__file) + " - Editor")

        else:
                #saving pre existing file
            file = open(self.__file,"w")     #'w' flags help to write into the file after opening it
            file.write(self.__ofTextArea.get(1.0, END))
            file.close()

    def __cut(self):
        self.__ofTextArea.event_generate("<<Cut>>")  #cut function built

    def __copy(self):
        self.__ofTextArea.event_generate("<<Copy>>")  #copy function ready to be called

    
    def __paste(self):
        self.__ofTextArea.event_generate("<<Paste>>")

    
    def run(self): #function to run the application

        self.__root.mainloop()



#Driver's code

editor = editorNotepad(width=600, height=400)  
editor.run()
