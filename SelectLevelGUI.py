"""
Created on Wed May  4 14:18:03 2022
@author: Mohammad Moghadaszadeh Behbahani
@Student ID: 21174353
"""

import tkinter

class Select_Level_GUI:
    def __init__(self):
        self.mw = tkinter.Tk()
        self.mw.title("Level")
        self.mw.geometry("480x220")
        self.mw.resizable(width=False, height=False)

        self.radio_val = tkinter.StringVar()
        self.radio_val.set('beginner')

        self.Label_title = tkinter.Label(self.mw, text="Please select the level of robot")

        self.rb1 = tkinter.Radiobutton(self.mw, text="beginner", variable=self.radio_val, value='beginner', command=self.radio_change)
        self.rb2 = tkinter.Radiobutton(self.mw, text="medium", variable=self.radio_val, value='medium', command=self.radio_change)
        self.rb3 = tkinter.Radiobutton(self.mw, text="advance", variable=self.radio_val, value='advance', command=self.radio_change)
        self.confirm_btn = tkinter.Button(self.mw, text="Confirm", command= self.confirm)

        self.Label_title.pack(side="top")
        self.rb1.pack(side="top")
        self.rb2.pack(side="top")
        self.rb3.pack(side="top")
        self.confirm_btn.pack(side="top")

        tkinter.mainloop()

    def confirm(self):
        self.mw.destroy()

    def radio_change(self, *args):
        self.radio_val.set(self.radio_val.get())

    def get_level(self):
        return self.radio_val.get()