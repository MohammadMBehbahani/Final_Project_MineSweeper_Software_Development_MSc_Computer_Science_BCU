"""
Created on Wed May  4 14:18:03 2022
@author: Mohammad Moghadaszadeh Behbahani
@Student ID: 21174353
"""

import tkinter

class Select_Level_GUI:
    def __init__(self):
        self.mw = tkinter.Tk()
        self.mw.title("Set Size")
        self.mw.geometry("480x220")
        self.mw.resizable(width=False, height=False)
        
        self.entry_row = tkinter.StringVar(self.mw, value='')
        self.entry_col = tkinter.StringVar(self.mw, value='')
        self.entry_mine = tkinter.StringVar(self.mw, value='')

        self.Label_title = tkinter.Label(self.mw, text="Enter values or leave empty for default")

        self.Label_row = tkinter.Label(self.mw, text="Enter Row")
        self.num_row = tkinter.Entry(self.mw, textvariable=self.entry_row, width=15)
        
        self.Label_col = tkinter.Label(self.mw, text="Enter Col")
        self.num_col = tkinter.Entry(self.mw, textvariable=self.entry_col, width=15)

        self.Label_mine = tkinter.Label(self.mw, text="Enter Mine")
        self.num_mine = tkinter.Entry(self.mw, textvariable=self.entry_mine, width=15)

        self.confirm_btn = tkinter.Button(self.mw, text="Confirm", command= self.confirm)

        self.Label_title.pack(side="top")

        self.Label_row.pack(side="top")
        self.num_row.pack(side="top")

        self.Label_col.pack(side="top")
        self.num_col.pack(side="top")

        self.Label_mine.pack(side="top")
        self.num_mine.pack(side="top")

        self.confirm_btn.pack(side="top")

        tkinter.mainloop()

    def confirm(self):
        row, col, mine = self.get_sizes()

        if row == '':
            row = 10
        else:
            row = int(row)

        if col == '':
            col = 10
        else:
            col = int(col)

        if mine == '':
            mine = 10
        else:
            mine = int(mine)

        if mine > row*col:
            tkinter.messagebox.showwarning("Custom size", "Maximum mines for this dimension is: " + str((row*col) - 1) + "\nEnter amount of mines")
            self.entry_row.set(10)
            self.entry_col.set(10)
            self.entry_mine.set(10)

        else:
            self.entry_row.set(row)
            self.entry_col.set(col)
            self.entry_mine.set(mine)
            self.mw.destroy()
    
    def get_sizes(self):
        row = self.entry_row.get()
        col = self.entry_col.get()
        mine = self.entry_mine.get()
        return row, col, mine