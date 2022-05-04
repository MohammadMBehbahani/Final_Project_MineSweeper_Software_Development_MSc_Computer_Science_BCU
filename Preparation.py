"""
Created on Wed May  4 14:18:03 2022
@author: Mohammad Moghadaszadeh Behbahani
@Student ID: 21174353
"""

import os
import tkinter
import tkinter.messagebox
import random
import tkinter.simpledialog

class preparation:
    def __init__(self, mw, game_over=False, row=10, col=10, mines=10):
        self.mw = mw
        self.mw.title("Minesweeper")
        self.game_over = game_over
        self.row = row
        self.col = col
        self.mines = mines
        self.board = []
        self.buttons = []
        self.space = 0
        self.minescount = self.mines
        self.lbl_minescount = tkinter.StringVar()
        self.lbl_spacecount = tkinter.StringVar()

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    def preparedMenu(self):
        
        menubar = tkinter.Menu(self.mw)
        menu_size = tkinter.Menu(self.mw, tearoff=0)
        menu_size.add_separator()
        menubar.add_command(label="Save", command=lambda: self.saveConfig())
        menubar.add_command(label="Load", command=lambda: self.loadConfig())
        menubar.add_command(label="Restart", command=lambda: self.restartGame())

        self.Label_Mine = tkinter.Label(self.mw, text="M:").grid(row=0, column=0)
        self.Label_Mine_Count = tkinter.Label(self.mw, textvariable=self.lbl_minescount).grid(row=0, column=1)

        self.Label_Space = tkinter.Label(self.mw, text="S:").grid(row=0, column=2)
        self.Label_Space_Count =tkinter.Label(self.mw, textvariable=self.lbl_spacecount).grid(row=0, column=3)

        self.mw.config(menu=menubar)


    def setGame_Over(self, value):
        self.game_over = value

    def getGame_Over(self):
        return self.game_over

    def restartGame(self):
        for x in self.mw.winfo_children():
            if type(x) != tkinter.Menu:
                x.destroy()

        self.game_over = False
        self.board = []
        self.buttons = []
        self.space = 0
        self.minescount = self.mines
        self.preparedMenu()
        self.prepareWindow()
        self.prepareGame()

    def saveConfig(self):
       if self.game_over == False:
            file = open("Minesweeper.txt", "w")
            file.write(f"row: {str(self.row)} \n")
            file.write(f"cols: {str(self.col)} \n")
            file.write(f"mines: {str(self.mines)} \n")
            
            for x in range(0, self.row):
                for y in range(0, self.col):
                    file.write(f"board: {x}, {y}, {self.board[x][y]} \n")
            
            for x in range(0, self.row):
                for y in range(0, self.col):
                    if self.buttons[x][y]["state"] == "disabled":
                        text = self.buttons[x][y]["text"]
                        if self.buttons[x][y]["text"] == " ":
                            text = 0
                        file.write(f"buttons: {x}, {y}, {text} \n")

            file.close()      

    def loadConfig(self):
        if os.path.exists("Minesweeper.txt"):
            file = open("Minesweeper.txt", "r")

            row = int(file.readline().split(":")[1])
            cols = int(file.readline().split(":")[1])
            mines = int(file.readline().split(":")[1])
            boards = []
            
            boardLine = file.readline()
            while boardLine !='':
                if "board:" not in boardLine:
                    break

                le = boardLine.split("board:")[1].split(",")
                contex = {
                    'x': int(le[0]),
                    'y': int(le[1]),
                    'value': int(le[2].split("\n")[0])
                }
                boards.append(contex)
                boardLine = file.readline()
                

            buttons = []

            buttonline = file.readline()
            while buttonline !='':
                le = buttonline.split("buttons:")[1].split(",")
                val = le[2].split("\n")[0]
                if "!" not in val:
                    val = int(val)

                contex = {
                    'x': int(le[0]),
                    'y': int(le[1]),
                    'value': val
                }
                buttons.append(contex)
                buttonline = file.readline()
            
            self.setSize(row, cols, mines)

            for board in boards:
                x = board['x']
                y = board['y']
                value = board['value']
                self.board[x][y] = value
            
            for button in buttons:
                x = button['x']
                y = button['y']
                value = button['value']
                if value == 0:
                    self.buttons[x][y]['state'] = 'disabled'
                    self.buttons[x][y].config(relief=tkinter.SUNKEN)
                else:
                    self.buttons[x][y]["text"] = value
                    self.buttons[x][y]['state'] = 'disabled'
                    self.buttons[x][y].config(relief=tkinter.SUNKEN)

            file.close()
        return

    def reduce_lbl_minescount(self):
        self.minescount = self.minescount - 1
        self.lbl_minescount.set(str(self.minescount))
        self.space = self.space + 1
        self.lbl_spacecount.set(str(self.space))

    def increase_lbl_minescount(self):
        self.minescount = self.minescount + 1
        self.lbl_minescount.set(str(self.minescount))
        self.space = self.space - 1
        self.lbl_spacecount.set(str(self.space))

    def increase_lbl_spacecount(self):
        self.space = self.space + 1
        self.lbl_spacecount.set(str(self.space))

    def prepareWindow(self):
        self.lbl_minescount.set(str(self.mines))
        self.lbl_spacecount.set(str(self.space))

        for x in range(0, self.row):
            self.buttons.append([])
            for y in range(0, self.col):
                b = tkinter.Button(self.mw, text=" ", width=2, command=lambda x = x, y = y: self.onPress(x, y, "You Lost"))
                b.bind("<Button-3>", lambda event, x=x, y=y:self.rightClick(x, y))
                b.grid(row=x+2, column=y, sticky=(tkinter.W, tkinter.E, tkinter.S, tkinter.N))
                self.buttons[x].append(b)

    def prepareGame(self):
        for x in range(0, self.row):
            self.board.append([])
            for y in range(0, self.col):
                 self.board[x].append(0)
        

        for _ in range(self.mines):
            x = random.randint(0, self.row - 1)
            y = random.randint(0, self.col - 1)
            while self.board[x][y] == -1:
                x = random.randint(0, self.row - 1)
                y = random.randint(0, self.col - 1)
            self.board[x][y] = -1

            if x != 0 and y != 0 and self.board[x - 1][y - 1] != -1:
                self.board[x - 1][y - 1] = int(self.board[x - 1][y - 1]) + 1

            if x != 0 and self.board[x - 1][y] != -1:
                self.board[x - 1][y] = int(self.board[x - 1][y]) + 1

            if y != 0 and self.board[x][y-1] != -1:
                self.board[x][y - 1] = int(self.board[x][y - 1]) + 1

            if x + 1< self.row and y + 1 < self.col and self.board[x + 1][y + 1] != -1:
                self.board[x + 1][y + 1] = int(self.board[x + 1][y + 1]) + 1

            if x + 1< self.row and self.board[x + 1][y] != -1:
                self.board[x + 1][y] = int(self.board[x + 1][y]) + 1

            if y + 1 < self.col and self.board[x][y + 1] != -1:
                self.board[x][y + 1] = int(self.board[x][y + 1]) + 1

            if x != 0 and y + 1 < self.col and self.board[x - 1][y + 1] != -1:
                self.board[x - 1][y + 1] = int(self.board[x - 1][y + 1]) + 1

            if y != 0 and x + 1 < self.row and self.board[x + 1][y - 1] != -1:
                self.board[x + 1][y - 1] = int(self.board[x + 1][y - 1]) + 1

    def rightClick(self,x, y):
        if self.game_over:
            return
        if self.buttons[x][y]["text"] == "!":
            self.buttons[x][y]["text"] = " "
            self.buttons[x][y]["state"] = "normal"
            self.increase_lbl_minescount()
        elif self.buttons[x][y]["text"] == " " and self.buttons[x][y]["state"] == "normal":
            self.buttons[x][y]["text"] = "!"
            self.buttons[x][y]["state"] = "disabled"
            self.buttons[x][y].config(disabledforeground='#0000FF')
            self.reduce_lbl_minescount()
       
    def onPress(self, x, y, message):
        if self.getGame_Over():
            return
        self.buttons[x][y]["text"] = str(self.board[x][y])
        if self.board[x][y] == -1:
            self.buttons[x][y]["text"] = "*"
            self.buttons[x][y].config(background='red', disabledforeground='black')
            self.setGame_Over(True)
            tkinter.messagebox.showinfo("Game Over", message)
            for _x in range(0, self.row):
                for _y in range(self.col):
                    if self.board[_x][_y] == -1:
                        self.buttons[_x][_y]["text"] = "*"
        else:
            self.buttons[x][y].config(disabledforeground='#0000FF')
        if self.board[x][y] == 0:
            self.buttons[x][y]["text"] = " "
            self.autoClick(x, y)
        self.buttons[x][y]['state'] = 'disabled'
        self.buttons[x][y].config(relief=tkinter.SUNKEN)
        self.increase_lbl_spacecount()
        self.checkWin()
        
    def checkWin(self):
        win = True
        for x in range(0, self.row):
            for y in range(0, self.col):
                if self.board[x][y] != -1 and self.buttons[x][y]["state"] == "normal":
                    win = False
        if win:
            self.setGame_Over(True)
            tkinter.messagebox.showinfo("Gave Over", "You have won.")
        
        return win

    def autoClick(self, x, y):
        if self.buttons[x][y]["state"] == "disabled":
            return
        self.increase_lbl_spacecount()
        if self.board[x][y] != 0:
            self.buttons[x][y]["text"] = str(self.board[x][y])
        else:
            self.buttons[x][y]["text"] = " "
        self.buttons[x][y].config(disabledforeground='#0000FF')
        self.buttons[x][y].config(relief=tkinter.SUNKEN)
        self.buttons[x][y]['state'] = 'disabled'
        if self.board[x][y] == 0:

            if x != 0 and y != 0:
                self.autoClick(x - 1, y - 1)

            if x != 0:
                self.autoClick(x - 1, y)

            if y != 0:
                self.autoClick(x, y - 1)

            if y + 1 < self.col and x + 1 < self.row:
                self.autoClick(x + 1, y + 1)

            if y != 0 and x + 1 < self.row:
                self.autoClick(x + 1, y - 1)

            if x != 0 and y + 1 < self.col:
                self.autoClick(x - 1, y + 1)
