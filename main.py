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
        print(grid)

        for width in range(10):
            for height in range(10):
                type = grid[width][height]
                btn = Button('',parent=self,state=type)

                btn.setGeometry(200,150,20,20)
                btn.move(width*20+40,height*20+40)


        self.setGeometry(300,300,300,300)
        self.setWindowTitle('MineSweeper')
        self.show()

    def pressed(self):
        self.sender().setIcon(QIcon('mine.png'))

    def generate_grid(self):
        totalgrid = []
        for w in range(10):
            row = []
            for h in range(10):
                r = random.random()
                if r < 0.1:
                    row.append('m')
                else:
                    row.append('nm')
            totalgrid.append(row)
        return totalgrid

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
            self.sender().setText('3')


def main():
    app = QApplication(sys.argv)
    MW = MineSweeper()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


