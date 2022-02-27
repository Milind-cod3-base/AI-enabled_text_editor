
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

    