"""
Created on Wed May  4 14:18:03 2022
@author: Mohammad Moghadaszadeh Behbahani
@Student ID: 21174353
"""

import tkinter
import MainFrameGUI
import SelectLevelGUI
import Preparation
import Bot
import SetSizeGUI


def prepare(row_s, col_s, mine_s):
        initTikinter = tkinter.Tk()
        pr= Preparation.preparation(initTikinter, row = row_s, col= col_s, mines=mine_s)
        pr.preparedMenu()
        pr.prepareWindow()
        pr.prepareGame()
        return initTikinter, pr

def set_size():
    s = SetSizeGUI.Select_Level_GUI()
    row_s, col_s, mine_s = s.get_sizes()

    if row_s == '':
        row_s = 10
    if col_s == '':
        col_s = 10
    if mine_s == '':
        mine_s = 10

    try:
        row_s = int(row_s)
        col_s = int(col_s)
        mine_s = int(mine_s)
    except:
        tkinter.messagebox.showwarning("Value Error", "Invalid value hase been enter, Please enter a valid number")
        
    
    return row_s, col_s, mine_s

def Robot(row_s, col_s, mine_s):
        r = SelectLevelGUI.Select_Level_GUI()
        level = r.get_level()
        initTikinter, pr = prepare(row_s, col_s, mine_s)

        row = pr.get_row()
        col = pr.get_col()

        bot = Bot.robot(initTikinter, level=level)
        bot.robot_play(pr, row, col)
        tkinter.mainloop()

def main():
    f = MainFrameGUI.Main_Frame_Gui()
    row_s, col_s, mine_s = set_size()

    selected = f.get_selected_opt()
    
    if selected == 'Robot':
        Robot(row_s, col_s, mine_s)

    else:
        prepare(row_s, col_s, mine_s)
        tkinter.mainloop()


main()
    