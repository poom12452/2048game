import tkinter
from src import game2048
from src import view
from src import robot

class controller:
    def __init__(self, size):
        self.window = tkinter.Tk()
        self.window.title("2048 ParallelGame")
        self.view = view.View(self.window, size)

        self.window.bind('<Up>', self.moveupEvent)
        self.window.bind('<Down>', self.movedownEvent)
        self.window.bind('<Left>', self.moveleftEvent)
        self.window.bind('<Right>', self.moverightEvent)
        self.window.bind('<r>', self.restart)
        self.window.bind('<c>', self.calNextMoveEvent)
        self.window.bind('<p>', self.robotMode)

        self.gameboard = game2048.board(size)
        boardMatrix = self.gameboard.getBoard()
        self.view.render(boardMatrix, 0)

        self.rbt = robot.Robot()

        while 1:
            self.window.update_idletasks()
            self.window.update()

    def closeConn(self):
        self.rbt.closeConn()

    def calNextMoveEvent(self, event):
        self.calNextMove()

    def calNextMove(self):
        nextmove = self.rbt.calNextMove(self.gameboard.getBoard())
        return nextmove

    def restart(self, event):
        size = 4
        self.gameboard = game2048.board(size)
        boardMatrix = self.gameboard.getBoard()
        self.view.render(boardMatrix, 0)
        self.window.bind('<Up>', self.moveupEvent)
        self.window.bind('<Down>', self.movedownEvent)
        self.window.bind('<Left>', self.moveleftEvent)
        self.window.bind('<Right>', self.moverightEvent)

    def moveup(self):
        self.gameboard.moveUp()
        boardMatrix = self.gameboard.getBoard()
        score = self.gameboard.getScore()
        self.view.render(boardMatrix, score)
        self.testLose()

    def moveupEvent(self, event):
        self.moveup()

    def movedownEvent(self, event):
        self.movedown()

    def movedown(self):
        self.gameboard.moveDown()
        boardMatrix = self.gameboard.getBoard()
        score = self.gameboard.getScore()
        self.view.render(boardMatrix, score)
        self.testLose()

    def moveleft(self):
        self.gameboard.moveLeft()
        boardMatrix = self.gameboard.getBoard()
        score = self.gameboard.getScore()
        self.view.render(boardMatrix, score)
        self.testLose()

    def moveleftEvent(self,event):
        self.moveleft()

    def moverightEvent(self,event):
        self.moveright()

    def moveright(self):
        self.gameboard.moveRight()
        boardMatrix = self.gameboard.getBoard()
        score = self.gameboard.getScore()
        self.view.render(boardMatrix, score)
        self.testLose()

    def checkServer(self):
        return self.rbt.pingServer()

    def robotMode(self, event):
        if(self.checkServer()):
            self.view.robotAvailable()
            for i in range(10):
                if(self.gameboard.lost_status == 1):
                    break
                self.view.robotOn(i)

                print("robot is playing move" + str(i))
                nextmove = self.calNextMove()

                if(nextmove == "U"):
                    self.moveup()
                elif(nextmove == "D"):
                    self.movedown()
                elif(nextmove == "L"):
                    self.moveleft()
                else:
                    self.moveright()
                self.window.update()
            self.view.robotOff()
        else:
            self.view.robotUnavailable()

    def getBoard(self):
        self.gameboard.getBoard()

    def testLose(self):
        testleft = self.gameboard.moveLeft(test=1)
        testright = self.gameboard.moveRight(test=1)
        testup = self.gameboard.moveUp(test=1)
        testdown = self.gameboard.moveDown(test=1)

        if(testleft+testright+testup+testdown == 0 ):
            print("you lose")
            self.view.lose()
            self.gameboard.setlose()
            self.window.unbind('<Up>')
            self.window.unbind('<Down>')
            self.window.unbind('<Left>')
            self.window.unbind('<Right>')
