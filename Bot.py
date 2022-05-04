"""
Created on Wed May  4 14:18:03 2022
@author: Mohammad Moghadaszadeh Behbahani
@Student ID: 21174353
"""

import random

class robot:
    def __init__(self, mw, name='robot', level='beginner', time_delay = 2000):
        self.mw= mw
        self.name = name
        self.level = level
        self.selection_list = []
        self.time_delay = time_delay
        self.__space = ' '
        self._flag = "!"
    
    def define_selected_list(self, row, col):
        if not self.selection_list:
            for x in range(0, row):
                self.selection_list.append([])
                for y in range(0, col):
                    self.selection_list[x].append(0)
    
    def select_random_coordinator(self, row, col, game):
            x = random.randint(0, row - 1)
            y = random.randint(0, col - 1)
            while (self.selection_list[x][y] != 0 
                    or game.buttons[x][y]['state'] == 'disabled'):
                    x = random.randint(0, row - 1)
                    y = random.randint(0, col - 1)

            self.selection_list[x][y] = 'selected'

            return x, y

    def robot_play(self, game, row , col):
        self.define_selected_list(row, col)

        if self.level == 'beginner':
            
            x, y = self.select_random_coordinator(row, col, game)

            if game.getGame_Over() == False:
                self.play(game, x, y, row, col)
                    
                    
        elif self.level == 'medium':
            x, y = self.select_random_coordinator(row, col, game)
            return
            
        elif self.level == 'advance':
            return      

    def play(self, game, x, y, row, col):
        self.mw.after(self.time_delay, lambda: game.onPress(x, y, "Robot Lost"))
        self.mw.after(self.time_delay, lambda: self.robot_play(game, row , col))