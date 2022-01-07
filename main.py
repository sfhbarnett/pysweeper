import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
import random

class MineSweeper(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        grid = self.generate_grid()
        grid[0][0] = 'nm'
        for line in grid:
            print(line)

        for width in range(10):
            for height in range(10):
                type = grid[width][height]
                if type == 'nm':
                    nMines = self.calculateNumber(grid,width,height)
                    type = nMines
                btn = Button('',parent=self,state=type)

                btn.setGeometry(200,150,20,20)
                btn.move(width*20+40,height*20+40)


        self.setGeometry(300,300,300,300)
        self.setWindowTitle('MineSweeper')
        self.show()


    def generate_grid(self):
        ##Randomly assign where mines are generated, 10 percent chance
        totalgrid = []
        for w in range(10):
            row = []
            for h in range(10):
                r = random.random()
                if r < 0.3:
                    row.append('m')
                else:
                    row.append('nm')
            totalgrid.append(row)
        return totalgrid

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



class Button(QPushButton):
    def __init__(self,Text,parent=None,state=None):
        super(Button,self).__init__(parent)
        self.setupbutton()
        self.state = state

    def setupbutton(self):
        self.clicked.connect(self.pressed)


    def pressed(self):
        if self.state == 'm':
            self.sender().setIcon(QIcon('mine.png'))
        else:
            self.sender().setText(str(self.state))


def main():
    app = QApplication(sys.argv)
    MW = MineSweeper()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


