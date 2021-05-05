import time
import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):

    def __init__(self, x, y, w, h):
        super().__init__()
        self.setWindowTitle("Help ")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setGeometry(x, y, w, h)
        self.UiComponents()
        self.show()

    def UiComponents(self):
        button = QPushButton("help", self)
        button.setGeometry(85, 80, 120, 80)
        # button.setStyleSheet("background-image : url(./img.png);")
        button.clicked.connect(self.action)

    def action(self):
        print('action')
        help_img = cv2.imread('help.jpeg')
        cv2.imshow('Help', help_img)
        cv2.moveWindow('help', 100, 100)
        cv2.setWindowProperty('help', cv2.WND_PROP_TOPMOST, 1)


def open_help(screen_width, screen_height):
    window_width = int(screen_width / 4)
    window_height = int(screen_height / 3)
    x_pos = 3 * window_width
    y_pos = screen_height - window_height
    app = QApplication(sys.argv)
    window = Window(x_pos, y_pos, window_width, window_height)
    app.exec_()


# open_help()
