#
# Author: Andy Schultheiss
#
# Description: Python course p. 124, .txt file copier program wth GUI and database recording
#
# Python version: 3.8.2
#
# Date: 20 April 2020
#
# Tested to work on Windows 10


import os
from pathlib import Path
import shutil
import sqlite3
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import tkinter.messagebox

import txtCopier_func

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.minsize(620,540)
        self.master.maxsize(620,540)
        self.sourceDir = StringVar()   # source directory string
        self.destDir = StringVar()     # destination directory string

        self.master.title('File mover for .txt')
        self.master.config(bg='#F0F0F0')

        # Catch if user clicks upper corner 'x' using built-in tkinter method
        self.master.protocol("WM_DELETE_WINDOW", lambda: txtCopier_func.ask_quit(self))
        
        # Instantiate the Tkinter menu dropdown object 
        # This is the menu that will appear at the top of our window
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1, accelerator="Ctrl+Q",command = lambda: txtCopier_func.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        self.master.config(menu=menubar, borderwidth='1')
        
        # instructions label
        self.instrLabel = Label(self.master, text='Press buttons below to browse. Selected directories will appear in entry boxes below. \nPress Execute to move all .txt files to destination. \nFile operations will be logged in a database in destination directory.')
        self.instrLabel.grid(row=0,column=0,rowspan=1,columnspan=6,padx=(15,15),pady=(25,5),sticky=N+W)

        self.btnBrowseSrc = Button(self.master, text="Browse for\n source directory", width=20, height=2, command = lambda: txtCopier_func.browse_source(self))
        self.btnBrowseSrc.grid(row=1,column=0,padx=(15,15),pady=(15,5),sticky=N+W)

        self.btnBrowseDest = Button(self.master, text="Browse for\n destination directory", width=20, height=2, command = lambda: txtCopier_func.browse_dest(self))
        self.btnBrowseDest.grid(row=2,column=0,padx=(15,15),pady=(15,5),sticky=N+W)

        # button to execute file copy
        self.btnExec = Button(self.master, text="Execute", width=20, height=2, command = lambda: txtCopier_func.execute_txtfile_move(self))
        self.btnExec.grid(row=3,column=0,padx=(15,15),pady=(15,5),sticky=N+W)

        # source directory display
        self.txt_browse_src = tk.Entry(self.master,text='')
        self.txt_browse_src.grid(row=1,column=1,rowspan=1,columnspan=5,ipadx=(120),padx=(10,10),pady=(15,5),sticky=N+E+W)

        # destination directory display
        self.txt_browse_dest= tk.Entry(self.master,text='')
        self.txt_browse_dest.grid(row=2,column=1,rowspan=1,columnspan=5,ipadx=(120),padx=(10,10),pady=(15,5),sticky=N+E+W)

        # Define listbox with scrollbar and grid them in
        self.listLabel = Label(self.master, text='Files moved:')
        self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
        self.lstList1 = Listbox(self.master, exportselection=0, yscrollcommand=self.scrollbar1.set)
        self.lstList1.bind('<<ListboxSelect>>')
        self.scrollbar1.config(command=self.lstList1.yview)
        self.listLabel.grid(row=3,column=1,padx=(5,15),pady=(15,5),sticky=N+W)
        self.scrollbar1.grid(row=4,column=5,rowspan=6,columnspan=1,padx=(0,0),pady=(0,0),sticky=N+S+W)
        self.lstList1.grid(row=4,column=1,rowspan=6,columnspan=4,padx=(10,0),pady=(0,0),sticky=N+E+S+W)

        self.statusLabel = Label(self.master, text='')
        self.statusLabel.grid(row=10,column=1,padx=(5,15),pady=(15,5),sticky=N+W)

        self.btnClose = Button(self.master, text="Close Program", width=20, height=2, command = lambda: txtCopier_func.ask_quit(self))
        self.btnClose.grid(row=4,column=0,padx=(15,15),pady=(15,5),sticky=N+W)

    
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
