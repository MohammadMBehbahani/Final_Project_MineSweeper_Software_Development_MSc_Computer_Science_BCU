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
        self.mw.geometry("480x320")
        self.mw.resizable(width=False, height=False)
        
        self.entry_row = tkinter.StringVar(self.mw, value='')
        self.entry_col = tkinter.StringVar(self.mw, value='')
        self.entry_mine = tkinter.StringVar(self.mw, value='')

        self.Label_title_Btn = tkinter.Label(self.mw, text="Select level or configure size")

        self.btn_normal = tkinter.Button(self.mw, text="normal", command=lambda: self.selected_button(1))
        self.btn_medium = tkinter.Button(self.mw, text="medium", command=lambda: self.selected_button(2))
        self.btn_advance = tkinter.Button(self.mw, text="advance", command=lambda: self.selected_button(3))

        self.Label_title = tkinter.Label(self.mw, text="Enter values or leave empty for default")

        self.Label_row = tkinter.Label(self.mw, text="Enter Row")
        self.num_row = tkinter.Entry(self.mw, textvariable=self.entry_row, width=15)
        
        self.Label_col = tkinter.Label(self.mw, text="Enter Col")
        self.num_col = tkinter.Entry(self.mw, textvariable=self.entry_col, width=15)

        self.Label_mine = tkinter.Label(self.mw, text="Enter Mine")
        self.num_mine = tkinter.Entry(self.mw, textvariable=self.entry_mine, width=15)

        self.confirm_btn = tkinter.Button(self.mw, text="Confirm", command= self.confirm)

        self.Label_title_Btn.pack(side="top")

        self.btn_normal.pack(side="top")
        self.btn_medium.pack(side="top")
        self.btn_advance.pack(side="top")

        self.Label_title.pack(side="top")

        self.Label_row.pack(side="top")
        self.num_row.pack(side="top")

        self.Label_col.pack(side="top")
        self.num_col.pack(side="top")

        self.Label_mine.pack(side="top")
        self.num_mine.pack(side="top")

        self.confirm_btn.pack(side="top")

        tkinter.mainloop()

    def selected_button(self, level):
        if level == 1:
            self.entry_row.set(10)
            self.entry_col.set(10)
            self.entry_mine.set(10)
            self.mw.destroy()

        elif level == 2:
            self.entry_row.set(20)
            self.entry_col.set(20)
            self.entry_mine.set(40)
            self.mw.destroy()

        elif level == 3:
            self.entry_row.set(25)
            self.entry_col.set(35)
            self.entry_mine.set(120)
            self.mw.destroy()

    def confirm(self):
        row, col, mine = self.get_sizes()

        try:
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

            else:
                self.entry_row.set(row)
                self.entry_col.set(col)
                self.entry_mine.set(mine)
                self.mw.destroy()
        except:
            tkinter.messagebox.showwarning("Value Error", "Invalid value hase been enter, Please enter a valid number")

    def get_sizes(self):
        row = self.entry_row.get()
        col = self.entry_col.get()
        mine = self.entry_mine.get()
        return row, col, mine