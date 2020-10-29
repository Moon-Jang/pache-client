from PyQt5.QtWidgets import *
from PyQt5.QtCore import  *
from PyQt5.QtGui import *

class WhiteButton(QPushButton) :
    def __init__(self, test):
        super(WhiteButton, self).__init__(test)
        self.setStyleSheet("background-color : rgb(255, 255, 255)")

class BlackButton(QPushButton) :
    def __init__(self, test):
        super(WhiteButton, self).__init__(test)
        self.setStyleSheet("background-color : rgb(0, 0, 0)")