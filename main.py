
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

    #A scrollbar to scroll up and down in the window
    __ofScrollBar = Scrollbar(__ofTextArea)   #setting up a scrollbar in the entire text area
    

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
        screenHeight = self._root.winfo_screenheight()


        #left aligning the window

        left = (screenWidth / 2) - (self.__ofWidth /2)

        #right aligning
        top = (screenHeight /2) - (self.__ofHeight /2)

        #Top and bottom alignment
        self.__root.geometry('%dx%d+%d+%d' %(self.__ofWidth, self.__ofHeight, left, top))

        #making text area resizable(auto)

        self.__root.grid_rowconfigure(0,weight=1)  #minisize(minimum size of the row), weight(how much does  the additional space propagate to this row)
        self.__root.grid_columnconfigure(0,weight=1)