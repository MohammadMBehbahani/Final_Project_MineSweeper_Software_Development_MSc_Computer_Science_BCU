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
            if game.getGame_Over() == False:
                x, y = self.select_random_coordinator(row, col, game)
                self.play(game, x, y, row, col)
                                   
        elif self.level == 'medium':
             if game.getGame_Over() == False:
                isBreak = False
                inFore = False

                for x in range(0, row):
                    for y in range(0, col):
                        if self.current_button_text(game, x, y).isdigit():
                            num_current_btn = int(self.current_button_text(game, x, y))

                            
                            count_undisable_btn_around = self.count_undisable_btn_around(game, x, y, row, col)
                            if num_current_btn == count_undisable_btn_around:
                                # select all mine around the current button if not selected already or not disable
                                has_click_on_mine = self.selecte_mine_around(game, x, y, row, col)

                                if has_click_on_mine:
                                    isBreak = True
                                    inFore = True
                                    break

                    if isBreak:
                        break
                   
                if inFore == False:
                    x, y = self.select_random_coordinator(row, col, game)
                    self.play(game, x, y, row, col)
            
        elif self.level == 'advance':
            if game.getGame_Over() == False:
                isBreak = False
                inFore = False

                for x in range(0, row):
                    for y in range(0, col):
                        if self.current_button_text(game, x, y).isdigit():
                            num_current_btn = int(self.current_button_text(game, x, y))

                            count_mine_around =  self.count_mine_around(game, x, y, row, col)

                            if num_current_btn == count_mine_around:
                                # select all around the current button if not disable
                                hase_click = self.select_all_around(game, x, y, row, col)
                                if hase_click:
                                    isBreak = True
                                    inFore = True
                                    break

                            else:
                                count_undisable_btn_around = self.count_undisable_btn_around(game, x, y, row, col)
                                if num_current_btn == count_undisable_btn_around:
                                    # select all mine around the current button if not selected already or not disable
                                    has_click_on_mine = self.selecte_mine_around(game, x, y, row, col)

                                    if has_click_on_mine:
                                        isBreak = True
                                        inFore = True
                                        break

                    if isBreak:
                        break
                   
                if inFore == False:
                    x, y = self.select_random_coordinator(row, col, game)
                    self.play(game, x, y, row, col)

    def selecte_mine_around(self, game, x, y, row, col):
        hase_click = False

        if self.has_right(y, col) and self.state_right(game, x, y) != 'disabled' and self._flag not in self.txt_right(game, x, y):
            hase_click = True
            self.mw.after(self.time_delay, lambda: game.rightClick(x, y + 1))

        if self.has_left(y) and self.state_left(game, x, y) != 'disabled' and self._flag not in self.txt_left(game, x, y):
            hase_click = True
            self.mw.after(self.time_delay, lambda: game.rightClick(x, y - 1))

        if self.has_top(x) and self.state_top(game, x, y) != 'disabled' and self._flag not in self.txt_top(game, x, y):
            hase_click = True
            self.mw.after(self.time_delay, lambda: game.rightClick(x - 1, y))
        
        if self.has_down(x, row) and self.state_down(game, x, y) != 'disabled' and self._flag not in self.txt_down(game, x, y):
            hase_click = True
            self.mw.after(self.time_delay, lambda: game.rightClick(x + 1, y))

        if self.has_top_right(x, y, col) and self.state_top_right(game, x, y) != 'disabled' and self._flag not in self.txt_top_right(game, x, y):
            hase_click = True
            self.mw.after(self.time_delay, lambda: game.rightClick(x - 1, y + 1))

        if self.has_top_left(x, y) and self.state_top_left(game, x, y) != 'disabled' and self._flag not in self.txt_top_left(game, x, y):
            hase_click = True
            self.mw.after(self.time_delay, lambda: game.rightClick(x - 1, y - 1))
        
        if self.has_down_right(x, y, col, row) and self.state_down_right(game, x, y) != 'disabled' and self._flag not in self.txt_down_right(game, x, y):
            hase_click = True
            self.mw.after(self.time_delay, lambda: game.rightClick(x + 1, y + 1))

        if self.has_down_left(x, y, row) and self.state_down_left(game, x, y) != 'disabled' and self._flag not in self.txt_down_left(game, x, y):
            hase_click = True
            self.mw.after(self.time_delay, lambda: game.rightClick(x + 1, y - 1))
        
        if hase_click:
            self.mw.after(self.time_delay, lambda: self.robot_play(game, row , col))

        return hase_click

    def select_all_around(self, game, x, y, row, col):
        hase_click = False

        if self.has_right(y, col) and self.state_right(game, x, y) != 'disabled':
            hase_click = True
            self.mw.after(self.time_delay, lambda: game.onPress(x, y + 1, "Robot Lost"))
        
        if self.has_left(y) and self.state_left(game, x, y) != 'disabled':
            hase_click = True
            self.mw.after(self.time_delay, lambda: game.onPress(x, y - 1, "Robot Lost"))
        
        if self.has_top(x) and self.state_top(game, x, y) != 'disabled':
            hase_click = True
            self.mw.after(self.time_delay, lambda: game.onPress(x - 1, y, "Robot Lost"))
        
        if self.has_down(x, row) and self.state_down(game, x, y) != 'disabled':
            hase_click = True
            self.mw.after(self.time_delay, lambda: game.onPress(x + 1, y, "Robot Lost"))
        
        if self.has_top_right(x, y, col) and self.state_top_right(game, x, y) != 'disabled':
            hase_click = True
            self.mw.after(self.time_delay, lambda: game.onPress(x - 1, y + 1, "Robot Lost"))
        
        if self.has_top_left(x, y) and self.state_top_left(game, x, y) != 'disabled':
            hase_click = True
            self.mw.after(self.time_delay, lambda: game.onPress(x - 1, y - 1, "Robot Lost"))
        
        if self.has_down_right(x, y, col, row) and self.state_down_right(game, x, y) != 'disabled':
            hase_click = True
            self.mw.after(self.time_delay, lambda: game.onPress(x + 1, y + 1, "Robot Lost"))
        
        if self.has_down_left(x, y, row) and self.state_down_left(game, x, y) != 'disabled':
            hase_click = True
            self.mw.after(self.time_delay, lambda: game.onPress(x + 1, y - 1, "Robot Lost"))
        
        if hase_click:
            self.mw.after(self.time_delay, lambda: self.robot_play(game, row , col))
        
        return hase_click

    def count_undisable_btn_around(self, game, x, y, row, col):
        count = 0
        # rigth
        if self.has_right(y, col) and self.state_right(game, x, y) != 'disabled':
            count = count + 1
         # left
        if self.has_left(y) and self.state_left(game, x, y) != 'disabled':
            count = count + 1

        # top
        if self.has_top(x) and self.state_top(game, x, y) != 'disabled':
            count = count + 1
        
        # down
        if self.has_down(x, row) and self.state_down(game, x, y) != 'disabled':
            count = count + 1

        # top_right
        if self.has_top_right(x, y, col) and self.state_top_right(game, x, y) != 'disabled':
            count = count + 1

        # top_left
        if self.has_top_left(x, y) and self.state_top_left(game, x, y) != 'disabled':
            count = count + 1

        # down_right
        if self.has_down_right(x, y, col, row) and self.state_down_right(game, x, y) != 'disabled':
            count = count + 1

        # down_left
        if self.has_down_left(x, y, row) and self.state_down_left(game, x, y) != 'disabled':
            count = count + 1
        
        return count

    def current_button_text(self, game, x, y):
        return game.buttons[x][y]["text"]

    def right_is_disable(self,game, x, y):
       return self.state_right(game, x, y) == 'disabled'
    
    def left_is_disable(self,game, x, y):
       return  self.state_left(game, x, y) == 'disabled'
    
    def top_is_disable(self,game, x, y):
       return  self.state_top(game, x, y) == 'disabled'
    
    def down_is_disable(self,game, x, y):
       return  self.state_down(game, x, y) == 'disabled'
    
    def top_right_is_disable(self,game, x, y):
       return  self.state_top_right(game, x, y) == 'disabled'
    
    def top_left_is_disable(self,game, x, y):
       return  self.state_top_left(game, x, y) == 'disabled'
    
    def down_right_is_disable(self,game, x, y):
       return  self.state_down_right(game, x, y) == 'disabled'

    def down_left_is_disable(self,game, x, y):
       return self.state_down_left(game, x, y) == 'disabled'

    def count_mine_around(self, game, x, y, row, col):
        count = 0
        # rigth
        if self.has_right(y, col) and  self.right_is_disable(game, x, y) and self._flag in self.txt_right(game, x, y):
            count = count + 1
        
        # left
        if self.has_left(y) and self.left_is_disable(game, x, y) and self._flag in self.txt_left(game, x, y):
            count = count + 1

        # top
        if self.has_top(x) and self.top_is_disable(game, x, y) and self._flag in self.txt_top(game, x, y):
            count = count + 1
        
        # down
        if self.has_down(x, row) and self.down_is_disable(game, x, y) and self._flag in self.txt_down(game, x, y):
            count = count + 1
        
        # top_right
        if self.has_top_right(x, y, col) and self.top_right_is_disable(game, x, y) and self._flag in self.txt_top_right(game, x, y):
            count = count + 1
        
        # top_left
        if self.has_top_left(x, y) and self.top_left_is_disable(game, x, y) and self._flag in self.txt_top_left(game, x, y):
            count = count + 1
        
        # down_right
        if self.has_down_right(x, y, col, row) and self.down_right_is_disable(game, x, y) and self._flag in self.txt_down_right(game, x, y):
            count = count + 1
        
        # down_left
        if self.has_down_left(x, y, row) and self.down_left_is_disable(game, x, y) and self._flag in self.txt_down_left(game, x, y):
            count = count + 1
        
        return count

    def play(self, game, x, y, row, col):
        self.mw.after(self.time_delay, lambda: game.onPress(x, y, "Robot Lost"))
        self.mw.after(self.time_delay, lambda: self.robot_play(game, row , col))
    
    def has_right(self, y, col):
        return y < col - 1

    def has_left(self, y):
        return y != 0

    def has_down(self, x, row):
        return x < row - 1
    
    def has_top(self, x):
        return x != 0

    def has_top_right(self, x, y, col):
        return x != 0 and y < col - 1
    
    def has_top_left(self, x, y):
        return x != 0 and y != 0
    
    def has_down_right(self, x, y, col, row):
        return x < row - 1 and y < col - 1
    
    def has_down_left(self, x, y, row):
        return x < row - 1 and y != 0

    def state_right(self, game, x, y):
        return game.buttons[x][y + 1]["state"]

    def state_left(self, game, x, y):
        return game.buttons[x][y - 1]["state"]
    
    def state_down(self, game, x, y):
        return game.buttons[x + 1][y]["state"]
    
    def state_top(self, game, x, y):
        return game.buttons[x - 1][y]["state"]
    
    def state_top_right(self, game, x, y):
        return game.buttons[x - 1][y + 1]["state"]
    
    def state_top_left(self, game, x, y):
        return game.buttons[x - 1][y - 1]["state"]
    
    def state_down_right(self, game, x, y):
        return game.buttons[x + 1][y + 1]["state"]
    
    def state_down_left(self, game, x, y):
        return game.buttons[x + 1][y - 1]["state"]

    def txt_right(self, game, x, y):
        return game.buttons[x][y + 1]["text"]

    def txt_left(self, game, x, y):
        return game.buttons[x][y - 1]["text"]
    
    def txt_down(self, game, x, y):
        return game.buttons[x + 1][y]["text"]
    
    def txt_top(self, game, x, y):
        return game.buttons[x - 1][y]["text"]
    
    def txt_top_right(self, game, x, y):
        return game.buttons[x - 1][y + 1]["text"]
    
    def txt_top_left(self, game, x, y):
        return game.buttons[x - 1][y - 1]["text"]
    
    def txt_down_right(self, game, x, y):
        return game.buttons[x + 1][y + 1]["text"]
    
    def txt_down_left(self, game, x, y):
        return game.buttons[x + 1][y - 1]["text"]
        
