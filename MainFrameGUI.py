"""
Created on Wed May  4 14:18:03 2022
@author: Mohammad Moghadaszadeh Behbahani
@Student ID: 21174353
"""

import tkinter  

class Main_Frame_Gui:
    def __init__(self):
        self.mw = tkinter.Tk()
        self.mw.title("Minesweeper, Welcom!")
        self.mw.geometry("480x220")
        self.mw.resizable(width=False, height=False)
        self.selected_opt = "Normal"

        self.frame1 = tkinter.Frame(self.mw, bg='yellow', width=300, height=600)
        self.frame1.pack(side="right", fill=tkinter.BOTH, expand=1)
        btn1 = tkinter.Button(self.frame1, text = "Robot Play", command= lambda: self.set_select_opt("Robot"))
        btn1.pack(side="left",expand=1)


        self.frame2 = tkinter.Frame(self.mw, bg='blue', width=300, height=600)
        self.frame2.pack(side="left", fill=tkinter.BOTH, expand=1)
        btn2 = tkinter.Button(self.frame2, text = "Normal Game", command= lambda: self.set_select_opt("Normal"))
        btn2.pack(side="left",expand=1)

        tkinter.mainloop()

    def set_select_opt(self, value):
        self.selected_opt = value
        self.mw.destroy()

    def get_selected_opt(self):
        return self.selected_opt