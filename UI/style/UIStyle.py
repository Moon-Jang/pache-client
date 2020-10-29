from PyQt5.QtWidgets import *
from PyQt5.QtCore import  *
from PyQt5.QtGui import *

class WhiteButton(QPushButton) :
    def __init__(self, test):
        super(WhiteButton, self).__init__(test)
        self.setStyleSheet("background-color : rgb(255, 255, 255)")

class BlackButton(QPushButton) :
    def __init__(self, test):
        super(BlackButton, self).__init__(test)
        self.setStyleSheet("background-color : rgb(0, 0, 0)")

class GrayButton(QPushButton) :
    def __init__(self, test):
        super(GrayButton, self).__init__(test)
        self.setStyleSheet(
            "color : white;"
            "border : 0px solid;"
            "background-color : rgb(153, 153, 153)")

class Alpha0Button(QPushButton) :
    def __init__(self, test):
        super(Alpha0Button, self).__init__(test)
        self.setStyleSheet(
            "background-color : rgba(255, 255, 255, 0);")