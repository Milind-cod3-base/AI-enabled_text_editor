
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
    