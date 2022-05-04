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
            # if game.getGame_Over() == False:
            #     if (self.check_right(x, y, game, col) 
            #         and int(self.right(x, y, game)) >= 1
                    
            #         and self.check_left(x, y, game) 
            #         and int(self.left(x, y, game)) >= 1
                    
            #         and self.check_top(x, y, game) 
            #         and int(self.top(x, y, game)) >= 1
                    
            #         and self.check_down(x, y, game, row) 
            #         and int(self.down(x, y, game)) >= 1

            #         and self.check_top_right(x, y , game, col) 
            #         and int(self.top_right(x, y, game)) >= 1

            #         and self.check_top_left(x, y , game) 
            #         and int(self.top_left(x, y, game)) >= 1

            #         and self.check_down_right(x, y , game, col, row) 
            #         and int(self.down_right(x, y, game)) >= 1

            #         and self.check_down_left(x, y , game, row) 
            #         and int(self.down_left(x, y, game)) >= 1):
            #         self.click_on_detected_mine(game, x, y, row, col)

            #     elif (self.check_right(x, y, game, col) 
            #         and int(self.right(x, y, game)) >= 1

            #         and self.check_left(x, y, game) 
            #         and int(self.left(x, y, game)) >= 1

            #         and self.check_top(x, y, game) 
            #         and int(self.top(x, y, game)) >= 1

            #         and self.check_down(x, y, game, row) 
            #         and int(self.down(x, y, game)) >= 1):
            #         self.click_on_detected_mine(game, x, y, row, col)

            #     elif (self.check_right(x, y, game, col) 
            #         and int(self.right(x, y, game)) >= 1

            #         and self.check_top(x, y, game)  
            #         and int(self.top(x, y, game)) >= 1):
            #         self.click_on_detected_mine(game, x, y, row, col)

            #     elif (self.check_left(x, y, game)
            #         and int(self.left(x, y, game)) >= 1

            #         and self.check_top(x, y, game)
            #         and int(self.top(x, y, game)) >= 1):
            #         self.click_on_detected_mine(game, x, y, row, col)
                
            #     elif (self.check_right(x, y, game, col) 
            #         and int(self.right(x, y, game)) >= 1

            #         and self.check_down(x, y, game, row) 
            #         and int(self.down(x, y, game)) >= 1):
            #         self.click_on_detected_mine(game, x, y, row, col)

            #     elif (self.check_left(x, y, game)
            #         and int(self.left(x, y, game)) >= 1

            #         and self.check_down(x, y, game, row) 
            #         and int(self.down(x, y, game)) >= 1):
            #         self.click_on_detected_mine(game, x, y, row, col)
                
            #     elif (self.check_down(x, y , game, row) 
            #         and int(self.down(x, y, game)) >= 1

            #         and self.check_top(x, y, game) 
            #         and int(self.top(x, y, game)) >= 1):
            #         self.click_on_detected_mine(game, x, y, row, col)

            #     elif (self.check_left(x, y, game) 
            #         and int(self.left(x, y, game)) >= 1

            #         and self.check_right(x, y, game, col) 
            #         and int(self.right(x, y, game)) >= 1):
            #         self.click_on_detected_mine(game, x, y, row, col)

                # else:
                #    self.play(game, x, y, row, col)

        elif self.level == 'advance':
            return
                

    def play(self, game, x, y, row, col):
        self.mw.after(self.time_delay, lambda: game.onPress(x, y, "Robot Lost"))
        self.mw.after(self.time_delay, lambda: self.robot_play(game, row , col))

    def select_on_detected_mine_around(self, game, x, y, row, col):
        # right
        if y < col - 1 and game.buttons[x][y + 1]["state"] != "disabled":
            self.click_on_detected_mine(game, x, y + 1, row, col)
        # left
        if y != 0 and game.buttons[x][y - 1]["state"] != "disabled":
            self.click_on_detected_mine(game, x, y - 1, row, col)
        # down
        if x < row - 1 and game.buttons[x + 1][y]["state"] != "disabled":
            self.click_on_detected_mine(game, x + 1, y, row, col)
        # top
        if x != 0 and game.buttons[x - 1][y]["state"] != "disabled":
            self.click_on_detected_mine(game, x - 1, y, row, col)
        # top_right
        if x != 0 and y < col - 1 and game.buttons[x - 1][y + 1]["state"] != "disabled":
            self.click_on_detected_mine(game, x - 1, y + 1, row, col)
        # top_left
        if x != 0 and y != 0 and game.buttons[x - 1][y - 1]["state"] != "disabled":
            self.click_on_detected_mine(game, x - 1, y - 1, row, col)
        # down_right
        if x < row - 1 and y < col - 1 and  game.buttons[x + 1][y + 1]["state"] != "disabled":
            self.click_on_detected_mine(game, x + 1, y + 1, row, col)
        # down_left
        if x < row - 1 and y != 0 and  game.buttons[x + 1][y - 1]["state"] != "disabled":
            self.click_on_detected_mine(game, x + 1, y - 1, row, col)

    def count_Undiseablebutton_around(self, game, x, y, row, col):
        count = 0

        # right
        if y < col - 1 and game.buttons[x][y + 1]["state"] != "disabled":
            count = count + 1

        # left
        if y != 0 and game.buttons[x][y - 1]["state"] != "disabled":
            count = count + 1

        # down
        if x < row - 1 and game.buttons[x + 1][y]["state"] != "disabled":
            count = count + 1

        # top
        if x != 0 and game.buttons[x - 1][y]["state"] != "disabled":
            count = count + 1

        # top_right
        if x != 0 and y < col - 1 and game.buttons[x - 1][y + 1]["state"] != "disabled":
            count = count + 1

        # top_left
        if x != 0 and y != 0 and game.buttons[x - 1][y - 1]["state"] != "disabled":
            count = count + 1

        # down_right
        if x < row - 1 and y < col - 1 and  game.buttons[x + 1][y + 1]["state"] != "disabled":
            count = count + 1

        # down_left
        if x < col - 1 and y != 0 and  game.buttons[x + 1][y - 1]["state"] != "disabled":
            count = count + 1
        
        return count

    def select_all_around(self, game, x, y, row, col):
        # right
        if y < col - 1 and game.buttons[x][y + 1]["state"] != "disabled":
            self.selection_list[x][y + 1] = 'selected'
            self.mw.after(self.time_delay, lambda: game.onPress(x, y + 1, "Robot Lost"))
        # left
        if y != 0 and game.buttons[x][y - 1]["state"] != "disabled":
            self.selection_list[x][y - 1] = 'selected'
            self.mw.after(self.time_delay, lambda: game.onPress(x, y - 1, "Robot Lost"))
        # down
        if x < row - 1 and game.buttons[x + 1][y]["state"] != "disabled":
            self.selection_list[x + 1][y] = 'selected'
            self.mw.after(self.time_delay, lambda: game.onPress(x + 1, y, "Robot Lost"))
        # top
        if x != 0 and  game.buttons[x - 1][y]["state"] != "disabled":
            self.selection_list[x - 1][y] = 'selected'
            self.mw.after(self.time_delay, lambda: game.onPress(x - 1, y, "Robot Lost"))
        # top_right
        if x != 0 and y < col - 1 and game.buttons[x - 1][y + 1]["state"] != "disabled":
            self.selection_list[x - 1][y + 1] = 'selected'
            self.mw.after(self.time_delay, lambda: game.onPress(x - 1, y + 1, "Robot Lost"))

        # top_left
        if x != 0 and y != 0 and game.buttons[x - 1][y - 1]["state"] != "disabled":
            self.selection_list[x - 1][y - 1] = 'selected'
            self.mw.after(self.time_delay, lambda: game.onPress(x - 1, y - 1, "Robot Lost"))
        # down_right
        if x < row - 1 and y < col - 1 and  game.buttons[x + 1][y + 1]["state"] != "disabled":
            self.selection_list[x + 1][y + 1] = 'selected'
            self.mw.after(self.time_delay, lambda: game.onPress(x + 1, y + 1, "Robot Lost"))
        # down_left
        if x < row - 1 and y != 0 and  game.buttons[x + 1][y - 1]["state"] != "disabled":
            self.selection_list[x - 1][y - 1] = 'selected'
            self.mw.after(self.time_delay, lambda: game.onPress(x + 1, y - 1, "Robot Lost"))

        self.mw.after(self.time_delay, lambda: self.robot_play(game, row , col))

    def click_on_detected_mine(self, game, x, y, row, col):
        self.selection_list[x][y] = 'selected'
        self.mw.after(self.time_delay, lambda: game.rightClick(x, y))
        self.mw.after(self.time_delay, lambda: self.robot_play(game, row , col))

    def text_button(self, game, x, y):
        return game.buttons[x][y]["text"]

    def check_button(self, game, x, y):
        return game.buttons[x][y]["text"].isdigit()

    def detected_mine_count_around(self, game, x, y, row, col):
        count = 0

        # right
        if y < col - 1 and game.buttons[x][y + 1]["state"] == "disabled" and game.buttons[x][y]["text"] == self._flag:
            count = count + 1

        # left
        if y != 0 and game.buttons[x][y - 1]["state"] == "disabled" and game.buttons[x][y - 1]["text"] == self._flag:
            count = count + 1

        # down
        if x < row - 1 and game.buttons[x + 1][y]["state"] == "disabled" and game.buttons[x + 1][y]["text"] == self._flag:
            count = count + 1

        # top
        if x != 0 and  game.buttons[x - 1][y]["state"] == "disabled" and game.buttons[x - 1][y]["text"] == self._flag:
            count = count + 1

        # top_right
        if x != 0 and y < col - 1 and game.buttons[x - 1][y + 1]["state"] == "disabled" and game.buttons[x - 1][y + 1]["text"] == self._flag:
            count = count + 1

        # top_left
        if x != 0 and y != 0 and game.buttons[x - 1][y - 1]["state"] == "disabled" and game.buttons[x - 1][y - 1]["text"] == self._flag:
            count = count + 1

        # down_right
        if x < row - 1 and y < col - 1 and  game.buttons[x + 1][y + 1]["state"] == "disabled" and game.buttons[x + 1][y + 1]["text"] == self._flag:
            count = count + 1

        # down_left
        if x < row - 1 and y != 0 and  game.buttons[x + 1][y - 1]["state"] == "disabled" and game.buttons[x + 1][y - 1]["text"] == self._flag:
            count = count + 1
        
        return count

    def check_right(self, x, y, game, col):
        return y < col - 1 and game.buttons[x][y + 1]["state"] == "disabled" and game.buttons[x][y + 1]["text"] != self.__space and game.buttons[x][y + 1]["text"] != self._flag

    def check_left(self, x, y , game):
        return y != 0 and game.buttons[x][y - 1]["state"] == "disabled" and game.buttons[x][y - 1]["text"] != self.__space and game.buttons[x][y - 1]["text"] != self._flag

    def check_down(self, x, y , game, row):
        return x < row - 1 and game.buttons[x + 1][y]["state"] == "disabled" and game.buttons[x + 1][y]["text"] != self.__space and game.buttons[x + 1][y]["text"] != self._flag

    def check_top(self, x, y , game):
        return x != 0  and  game.buttons[x - 1][y]["state"] == "disabled" and game.buttons[x - 1][y]["text"] != self.__space and game.buttons[x - 1][y]["text"]!= self._flag

    def check_top_right(self, x, y , game, col):
        return x != 0 and y < col - 1  and game.buttons[x - 1][y + 1]["state"] == "disabled" and game.buttons[x - 1][y + 1]["text"] != self.__space and game.buttons[x - 1][y + 1]["text"] != self._flag

    def check_top_left(self, x, y , game): 
        return x != 0 and y != 0  and game.buttons[x - 1][y - 1]["state"] == "disabled" and game.buttons[x - 1][y - 1]["text"] != self.__space and game.buttons[x - 1][y - 1]["text"] != self._flag

    def check_down_right(self, x, y , game, col, row):
        return x < row - 1 and y < col - 1 and  game.buttons[x + 1][y + 1]["state"] == "disabled" and game.buttons[x + 1][y + 1]["text"] != self.__space and game.buttons[x + 1][y + 1]["text"] != self._flag

    def check_down_left(self, x, y , game, row):
        return x < row - 1 and y != 0 and  game.buttons[x + 1][y - 1]["state"] == "disabled" and game.buttons[x + 1][y - 1]["text"] != self.__space and game.buttons[x + 1][y - 1]["text"] != self._flag


    def right(self, x, y , game):
        return game.buttons[x][y + 1]["text"]

    def left(self, x, y , game):
        return game.buttons[x][y - 1]["text"]

    def down(self, x, y , game):
        return game.buttons[x + 1][y]["text"]

    def top(self, x, y , game):
        return game.buttons[x - 1][y]["text"]

    def top_right(self, x, y , game):
        return game.buttons[x - 1][y + 1]["text"]

    def top_left(self, x, y , game):
        return game.buttons[x - 1][y - 1]["text"]

    def down_right(self, x, y , game):
        return game.buttons[x + 1][y + 1]["text"]

    def down_left(self, x, y , game):
        return game.buttons[x + 1][y - 1]["text"]