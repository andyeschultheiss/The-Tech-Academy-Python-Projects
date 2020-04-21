#
# Author: Andy Schultheiss
#
# Description: txtCopier app function library
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

import txtCopier_main

# verify if user wants to exit program
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Are you sure you want to exit the application?"):
        self.master.destroy()
        os._exit(0)

# source browsing
def browse_source(self):
    # wipe text boxes first
    self.txt_browse_src.delete(0,END)
    self.statusLabel.config(text='')
    self.lstList1.delete(0,END)
    
    self.sourceDir = browse_dir(self)
    self.txt_browse_src.insert(0,self.sourceDir)

# destination browsing
def browse_dest(self):
    # wipe text boxes first
    self.txt_browse_dest.delete(0,END)
    self.statusLabel.config(text='')
    self.lstList1.delete(0,END)
    
    self.destDir = browse_dir(self)
    self.txt_browse_dest.insert(0,self.destDir)
    
## browse function
def browse_dir(self):
    chosenDirectory = filedialog.askdirectory()
    print(chosenDirectory) # command line display as well to verify
    return chosenDirectory

# execute button function
def execute_txtfile_move(self):
    if (self.sourceDir == self.destDir):
        # Message for matching source and destination
        self.statusLabel.config(text='Identical source and destination directories.\nPlease select a different directory and try again.')

    else:
        # clear listbox and status label
        self.lstList1.delete(0,END)
        self.statusLabel.config(text='')
        # scan and move, returning a count of files moved
        count = txt_scan(self, self.sourceDir, self.destDir)
        # display status text
        if (count > 0):
            self.statusLabel.config(text='{} files moved successfully! \nList recorded in ''txtList.db'''.format(count))
        elif (count == 0):
            self.statusLabel.config(text='No .txt files found in source directory. \nNo files were moved.')
    

# text file scan and move function with database recording
def txt_scan(self, sourcepath, destinationpath):
    # initialize file counter
    filecount = 0
    # place database in destination folder
    database_name = 'txtList.db'
    conn = sqlite3.connect(os.path.join(destinationpath,database_name))
    with conn:
        cur = conn.cursor()
        # command line description of actions taken
        print("txt files copied and corresponding mtimes: ")
        with os.scandir(sourcepath) as f:
            for entry in f:
                if entry.name.endswith('.txt') and entry.is_file():
                    # only create database if there are txt files to log
                    cur.execute("CREATE TABLE if not exists tbl_txtList( \
                                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                                col_filename TEXT, \
                                col_mtime TEXT \
                                );")
                    filecount = filecount + 1
                    entry_stats = os.stat(os.path.join(sourcepath, entry.name))
                    # pull modified timestamp
                    entry_mtime = entry_stats.st_mtime
                    # print to command line
                    print(entry.name + " - modified timestamp: " + str(entry_mtime))
                    # move file to destination
                    shutil.move(os.path.join(sourcepath, entry.name),os.path.join(destinationpath, entry.name))
                    # add to database
                    cur.execute("""INSERT INTO tbl_txtList(col_filename, col_mtime) VALUES (?, ?)""", (entry.name, str(entry_mtime)))
                    self.lstList1.insert(0,str(entry.name))
            f.close()
        # commit() to save changes & close the database connection
    conn.commit()
    conn.close()

    return filecount
    
