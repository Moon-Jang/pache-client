from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from UI.sign_up_UI import signUp
from UI.login import Ui_LoginPage
import sys, os
from client_socket import ClientSocket
import json
from config import config_socket


class UI_PACHE(object):
    def __init__(self):
        self.client_socket = ClientSocket(self)
        server_ip = config_socket["serverIP"]
        port = config_socket["PORT"]
        self.client_socket.connectServer(server_ip, port)

    
    def setupUi(self, PACHE):
        self.main_widget = QWidget()
        # LoginPage = QtWidgets.QWidget()
        # ui = Ui_LoginPage()
        # ui.setupUi(LoginPage)
        # login = Ui_LoginPage()
        # login.setupUi(self.login_widget)
        self.layers = QStackedLayout()
        
        self.sign_up_widget = signUp()
        self.login_widget = Ui_LoginPage(self.layers, self.client_socket)
        self.layers.addWidget(self.login_widget)
        self.layers.addWidget(self.sign_up_widget)
        self.layers.setCurrentIndex(0)
        
        self.back_button = QPushButton("<")
        self.back_button.setFixedSize(30, 30)
        
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.back_button)
        self.mainLayout.addLayout(self.layers)
        
        if (self.layers.currentIndex() == 0):
            self.back_button.setHidden(True)
        PACHE.setLayout(self.mainLayout)
        PACHE.setStyleSheet("background-color : rgb(255, 255, 255)")
        
        PACHE.setObjectName("PACHE")
        PACHE.resize(390, 542)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_widget.sizePolicy().hasHeightForWidth())
        
        self.retranslateUi(PACHE)
        QMetaObject.connectSlotsByName(PACHE)
    
    def retranslateUi(self, PACHE):
        _translate = QCoreApplication.translate
        PACHE.setWindowTitle(_translate("PACHE", "PACHE"))

    def updateMsg(self, msg):
        print("updateMsg: ", msg)

    def updateDisconnect(self):
        print("disconnect")


if __name__ == "__main__":
    import sys
    
    app = QApplication(sys.argv)
    PACHE = QWidget()
    ui = UI_PACHE()
    ui.setupUi(PACHE)
    PACHE.show()
    sys.exit(app.exec_())
