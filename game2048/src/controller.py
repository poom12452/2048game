import tkinter
from src import game2048
from src import view
from src import robot

class controller:
    def __init__(self, size):
        self.window = tkinter.Tk()
        self.view = view.View(self.window, size)

        self.window.bind('<Up>', self.moveup)
        self.window.bind('<Down>', self.movedown)
        self.window.bind('<Left>', self.moveleft)
        self.window.bind('<Right>', self.moveright)
        self.window.bind('<r>', self.restart)
        self.window.bind('<c>', self.calNextMove)

        self.gameboard = game2048.board(size)
        boardMatrix = self.gameboard.getBoard()
        self.view.render(boardMatrix, 0)

        self.rbt = robot.Robot()

        while 1:
            self.window.update_idletasks()
            self.window.update()


    def calNextMove(self, event):
        self.rbt.calNextMove(self.gameboard.getBoard())

    def restart(self, event):
        size = 4
        self.gameboard = game2048.board(size)
        boardMatrix = self.gameboard.getBoard()
        self.view.render(boardMatrix, 0)

    def moveup(self, event):
        self.gameboard.moveUp()
        boardMatrix = self.gameboard.getBoard()
        score = self.gameboard.getScore()
        self.view.render(boardMatrix, score)

    def movedown(self, event):
        self.gameboard.moveDown()
        boardMatrix = self.gameboard.getBoard()
        score = self.gameboard.getScore()
        self.view.render(boardMatrix, score)

    def moveleft(self, event):
        self.gameboard.moveLeft()
        boardMatrix = self.gameboard.getBoard()
        score = self.gameboard.getScore()
        self.view.render(boardMatrix, score)

    def moveright(self, event):
        self.gameboard.moveRight()
        boardMatrix = self.gameboard.getBoard()
        score = self.gameboard.getScore()
        self.view.render(boardMatrix, score)

    def getBoard(self):
        self.gameboard.getBoard()


