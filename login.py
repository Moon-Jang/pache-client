from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PACHE(object):
    def setupUi(self, PACHE):
        PACHE.setObjectName("PACHE")
        PACHE.resize(390, 542)
        self.main_widget = QtWidgets.QWidget(PACHE)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_widget.sizePolicy().hasHeightForWidth())
        self.main_widget.setSizePolicy(sizePolicy)
        self.main_widget.setAutoFillBackground(False)
        self.main_widget.setStyleSheet("background: rgb(255, 255, 255)")
        self.main_widget.setObjectName("main_widget")
        self.input_id = QtWidgets.QLineEdit(self.main_widget)
        self.input_id.setGeometry(QtCore.QRect(60, 190, 271, 41))
        self.input_id.setStyleSheet("border: 1px solid black;")
        self.input_id.setObjectName("input_id")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.main_widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 230, 271, 41))
        self.lineEdit_2.setStyleSheet("border: 1px solid black;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.button_siginup = QtWidgets.QPushButton(self.main_widget)
        self.button_siginup.setGeometry(QtCore.QRect(60, 280, 131, 41))
        self.button_siginup.setStyleSheet("border: 1px solid black;\n"
                                          "background: rgba(0,0,0,0.0);\n"
                                          "font-size: 16px;\n"
                                          "font-weight: 600;")
        self.button_siginup.setObjectName("button_siginup")
        self.button_login = QtWidgets.QPushButton(self.main_widget)
        self.button_login.setGeometry(QtCore.QRect(200, 280, 131, 41))
        self.button_login.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.button_login.setTabletTracking(False)
        self.button_login.setStyleSheet("border: 0px solid black;\n"
                                        "background: rgba(0,0,0,0.6);\n"
                                        "color: white;\n"
                                        "font-size: 16px;\n"
                                        "font-weight: 600;")
        self.button_login.setObjectName("button_login")
        self.button_login.clicked.connect(self.btn_clicked)
        PACHE.setCentralWidget(self.main_widget)
        self.statusbar = QtWidgets.QStatusBar(PACHE)
        self.statusbar.setObjectName("statusbar")
        PACHE.setStatusBar(self.statusbar)
        
        self.retranslateUi(PACHE)
        QtCore.QMetaObject.connectSlotsByName(PACHE)
    
    def retranslateUi(self, PACHE):
        _translate = QtCore.QCoreApplication.translate
        PACHE.setWindowTitle(_translate("PACHE", "PACHE"))
        self.button_siginup.setText(_translate("PACHE", "회원가입"))
        self.button_login.setText(_translate("PACHE", "로그인"))
    
    def btn_clicked(self):
        print("버튼 클릭")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PACHE = QtWidgets.QMainWindow()
    ui = Ui_PACHE()
    ui.setupUi(PACHE)
    PACHE.show()
    sys.exit(app.exec_())
