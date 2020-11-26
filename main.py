import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen
from random import randrange


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Git и желтые окружности')
        self.pushButton.clicked.connect(self.draw_ellipse)
    
    def draw_ellipse(self):
        self.repaint()
    
    def paintEvent(self, event): 
        painter = QPainter(self)
        painter.setBrush(QBrush(QColor(255, 255, 0)))
        rand_num = randrange(20, 500)
        painter.drawEllipse(250 - rand_num / 2, 250 - rand_num / 2, rand_num, rand_num)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
