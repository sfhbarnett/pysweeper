import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
import random

class MineSweeper(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        grid,self.buttongrid = self.generate_grid()

        for width in range(10):
            for height in range(10):
                type = grid[width][height]
                if type == 'nm':
                    nMines = self.calculateNumber(grid,width,height)
                    type = nMines
                btn = Button('',parent=self,state=type,w=width,h=height)
                btn.setGeometry(200,150,20,20)
                btn.move(width*20+40,height*20+40)
                self.buttongrid[width][height] = btn

        self.Flagbtn = QPushButton('',self)
        self.Flagbtn.setIcon(QIcon('flag.png'))
        self.Flagbtn.setGeometry(80, 10, 20, 20)
        self.Flagbtn.move(80, 10)
        self.Flagbtn.clicked.connect(self.setFlagMode)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle('MineSweeper')
        self.show()

        self.flagstate = -1


    def generate_grid(self):
        ##Randomly assign where mines are generated, 10 percent chance
        totalgrid = []
        buttongrid = []
        for w in range(10):
            row = []
            buttonrow = []
            for h in range(10):
                r = random.random()
                buttonrow.append(0)
                if r < 0.1:
                    row.append('m')
                else:
                    row.append('nm')
            totalgrid.append(row)
            buttongrid.append(buttonrow)
        return totalgrid, buttongrid

    def calculateNumber(self,grid,w,h):
        number = 0
        for x in range(-1,2,1):
            for y in range(-1,2,1):
                middle = 0
                xcoord = w+x
                ycoord = h+y
                if -1 < xcoord < len(grid[0]) and -1 < ycoord < len(grid[0]): #only works for square grids
                    location = grid[w+x][h+y]
                    if x == 0 and y == 0:
                        middle = 1
                    if location == 'm' and middle == 0:
                        number += 1
        return number

    def collapse(self,button,w,h):
        #Performs the floodfill to fill in all zero squares and reveal edge numbers
        #Need to change so it's 4 connectivity instead of 8
        currentW = button.width
        currentH = button.height
        for x in range(-1,2,1):
            for y in range(-1,2,1):
                xcoord = currentW+x
                ycoord = currentH+y
                if -1 < xcoord < len(self.buttongrid[0]) and -1 < ycoord < len(self.buttongrid[0]):
                    btn = self.buttongrid[xcoord][ycoord]
                    if btn.checked == False:
                        btn.click()

    def setFlagMode(self):
        self.flagstate *= -1
        if self.flagstate == -1:
            self.Flagbtn.setStyleSheet("background-color: light gray")
        else:
            self.Flagbtn.setStyleSheet("background-color: #6a6461")


class Button(QPushButton):
    def __init__(self,Text,parent=None,state=None,w=None,h=None):
        super(Button,self).__init__(parent)
        self.parent = parent
        self.setupbutton()
        self.state = state
        self.width = w
        self.height = h
        self.checked = False
        self.flag = False

    def setupbutton(self):
        self.clicked.connect(self.pressed)

    def pressed(self):
        if self.parent.flagstate != 1 and self.flag == False:
            self.checked = True
            if self.state == 'm':
                self.sender().setIcon(QIcon('mine.png'))
            elif self.state == 0:
                self.parent.collapse(self, self.width,self.height)
                self.setStyleSheet("background-color: #6a6461")
            else:
                self.sender().setText(str(self.state))
        else:
            self.sender().setIcon(QIcon('flag.png'))
            self.checked = True
            self.flag = True


def main():
    app = QApplication(sys.argv)
    MW = MineSweeper()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


