import os
import sys
import json

from PyQt5.QtWidgets import *
from PyQt5.QtCore import  *
from PyQt5.QtGui import *

class signUp(QWidget) :
    def __init__(self, parent, server):
        super().__init__(parent)
        self.setWindowTitle("회원가입")
        self.initUI()
        #서버
        self.server = server
        # 체크 값
        self.id_check = False
        self.checked_id = ""
        self.pw_check = False

    def initUI(self):

        # 레이아웃
        self.hLayout = QHBoxLayout()
        self.vLayout = QVBoxLayout()
        self.photoLayout = QVBoxLayout()
        self.idLayout = QHBoxLayout()

        # 위젯
        self.photo_select_image_label = QLabel()
        self.photo_select_button = QPushButton("사진 선택")
        self.id_lineEdit = QLineEdit()
        self.id_overlap_check_button = QPushButton("중복 확인")
        self.pw_lineEdit = QLineEdit()
        self.pw_same_check_lineEdit = QLineEdit()
        self.nickname_lineEdit = QLineEdit()
        self.email_lineEdit = QLineEdit()
        self.submit_button = QPushButton("확인")



        # 위젯 설정
        self.pw_lineEdit.setEchoMode(QLineEdit.Password)
        self.pw_same_check_lineEdit.setEchoMode(QLineEdit.Password)

        # 위젯 스타일
        self.photo_select_button.setStyleSheet("background-color : rgba(255, 255, 255, 0)")

        # 크기설정
        self.SIGNUP_WIDTH = 360
        self.SIGNUP_HEIGHT = 540
        self.PHOTO_SIZE = 60
        self.WIDGET_DEFAULT_HEIGHT = 30
        self.SUBMIT_HEIGHT = 45
        self.LAYOUT_SPACING = 10

        self.setMinimumSize(self.SIGNUP_WIDTH, self.SIGNUP_HEIGHT)

        self.photo_select_image_label.setFixedSize(self.PHOTO_SIZE, self.PHOTO_SIZE)
        self.photo_select_button.setFixedHeight(self.WIDGET_DEFAULT_HEIGHT)
        self.id_lineEdit.setFixedHeight(self.WIDGET_DEFAULT_HEIGHT)
        self.id_overlap_check_button.setFixedHeight(self.WIDGET_DEFAULT_HEIGHT)
        self.pw_lineEdit.setFixedHeight(self.WIDGET_DEFAULT_HEIGHT)
        self.pw_same_check_lineEdit.setFixedHeight(self.WIDGET_DEFAULT_HEIGHT)
        self.nickname_lineEdit.setFixedHeight(self.WIDGET_DEFAULT_HEIGHT)
        self.email_lineEdit.setFixedHeight(self.WIDGET_DEFAULT_HEIGHT)
        self.submit_button.setFixedHeight(self.SUBMIT_HEIGHT)

        self.vLayout.setSpacing(self.LAYOUT_SPACING)

        # 필드 힌트
        self.id_lineEdit.setPlaceholderText("아이디")
        self.pw_lineEdit.setPlaceholderText("비밀번호")
        self.pw_same_check_lineEdit.setPlaceholderText("비밀번호 확인")
        self.nickname_lineEdit.setPlaceholderText("이름 / 닉네임")
        self.email_lineEdit.setPlaceholderText("이메일")

        # 이벤트
        self.photo_select_button.clicked.connect(self.photo_upload_event)
        self.id_overlap_check_button.clicked.connect(self.id_overlap_check_event)
        self.submit_button.clicked.connect(self.submit_event)
        self.id_lineEdit.textChanged.connect(self.id_input_change_event)
        self.pw_lineEdit.textChanged.connect(self.pw_same_check_event)
        self.pw_same_check_lineEdit.textChanged.connect(self.pw_same_check_event)

        # 배치
        self.photoLayout.addWidget(self.photo_select_image_label)
        self.photoLayout.addWidget(self.photo_select_button)

        self.idLayout.addWidget(self.id_lineEdit)
        self.idLayout.addWidget(self.id_overlap_check_button)

        self.hLayout.addStretch(1)
        self.hLayout.addLayout(self.vLayout)
        self.hLayout.addStretch(1)

        self.vLayout.addStretch(1)
        self.vLayout.addLayout(self.photoLayout)
        self.vLayout.addLayout(self.idLayout)
        self.vLayout.addWidget(self.pw_lineEdit)
        self.vLayout.addWidget(self.pw_same_check_lineEdit)
        self.vLayout.addWidget(self.nickname_lineEdit)
        self.vLayout.addWidget(self.email_lineEdit)
        self.vLayout.addWidget(self.submit_button)
        self.vLayout.addStretch(2)

        # 정렬
        self.photoLayout.setAlignment(self.photo_select_image_label, Qt.AlignCenter)
        self.photoLayout.setAlignment(self.photo_select_button, Qt.AlignCenter)

        self.vLayout.setAlignment(self.photoLayout, Qt.AlignCenter)

        # 화면 설정
        self.setLayout(self.hLayout)

    def photo_upload_event(self):
        FPath = QFileDialog.getOpenFileName(self, "Open File", "", "Image files (*.jpg *.gif *.png)")

        if len(FPath[0]) > 0 :
            image = QPixmap(FPath[0])
            #.photo_select_image_label.setPixmap(QSize(self.PHOTO_SIZE, self.PHOTO_SIZE))
            image.scaledToWidth(self.PHOTO_SIZE)
            self.photo_select_image_label.setPixmap(image)

            self.photo_select_image_label.setStyleSheet("background-color : rgba(255, 255, 255, 0)")

    def id_overlap_check_event(self):
        message = dict()
        params = dict()
        message["request"] = "id_overlap_check"
        message["params"] = params
        if (self.id_lineEdit.text() != "") :
            params["id"] = self.id_lineEdit.text()
            print(json.dumps(message))
            self.server.send(json.dumps(message))
            # 임시
            self.id_check = True
            self.checked_id = self.id_lineEdit.text()
        else :
            reply = QMessageBox.about(self, "", "아이디를 입력해주세요.")

    def id_input_change_event(self):
        if (self.checked_id != self.id_lineEdit.text()) :
            self.id_check = False
        else :
            self.id_check = True

    def pw_same_check_event(self):
        if (self.pw_lineEdit.text() == self.pw_same_check_lineEdit.text()) :
            self.pw_same_check_lineEdit.setStyleSheet(
                "border-style: solid;"
                "border-width: 2px;"
                "border-color: #4caf50;"
                "border-radius: 3px")
            self.pw_check = True
        else :
            self.pw_same_check_lineEdit.setStyleSheet(
                "border-style: solid;"
                "border-width: 2px;"
                "border-color: #FA8072;"
                "border-radius: 3px")
            self.pw_check = False

    def submit_event(self):
        if (self.id_check and self.pw_check) :
            message = dict()
            params = dict()
            message["request"] = "sign_up_submit"
            message["params"] = params
            params["id"] = self.id_lineEdit.text()
            params["password"] = self.pw_lineEdit.text()
            params["nickname"] = self.nickname_lineEdit.text()
            params["email"] = self.email_lineEdit.text()
            print(json.dumps(message))
            self.server.send(json.dumps(message))
        else :
            if (not self.id_check) :
                QMessageBox.about(self, "", "아이디 중복 확인을 해주세요.")
                self.id_lineEdit.setFocus()
            else :
                if (not self.pw_check) :
                    QMessageBox.about(self, "", "비밀번호가 일치하지 않습니다.")
                    self.pw_same_check_lineEdit.setFocus()




## 테스트 용
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = signUp()
    form.show()
    exit(app.exec_())
