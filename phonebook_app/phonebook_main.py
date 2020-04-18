#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: Andy Schultheiss
#
# Description: Phonebook demonstrating OOP practices and Tkinter GUI module usage
#
# Python Version: 3.8.2
#
# Date: last updated 17 April 2020
#
# Tested to work on Windows 10

from tkinter import *
import tkinter as tk
import tkinter.messagebox


# Import other modules 
import phonebook_gui
import phonebook_func

class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__ (self, master, *args, **kwargs)

        # Define master frame config
        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)
        
        # Center window on user's screen
        phonebook_func.center_window(self,500,300)
        
        self.master.title('Tkinter Phonebook Demo')
        self.master.config(bg='#F0F0F0')
        
        # Catch if user clicks upper corner 'x' using built-in tkinter method
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # load GUI widgets from separate module
        phonebook_gui.load_gui(self)

        # Instantiate the Tkinter menu dropdown object 
        # This is the menu that will appear at the top of our window
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1, accelerator="Ctrl+Q",command = lambda: phonebook_func.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0) # defines the particular drop down column and tearoff=0 means do not separate from menubar
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label="About This Phonebook Demo") # add_command is a child menubar item of the add_cascde parent item
        menubar.add_cascade(label="Help", menu=helpmenu) # add_cascade is a parent menubar item (visible heading)
        self.master.config(menu=menubar, borderwidth='1')




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    





        
