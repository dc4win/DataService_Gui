import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter, QColor, QFont, QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication, QLabel, QDesktopWidget, QHBoxLayout, QFormLayout, \
    QPushButton, QLineEdit

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """初始化UI"""
        self.setObjectName("loginwindow")
        self.setStyleSheet('#loginwindow{background-color:white}')
        self.setFixedSize(650,400)
        self.setWindowTitle("登录界面")
        self.setWindowIcon(QIcon('logo.ico'))
        self.text = "镇江气象数据服务平台"
        ###顶部设置
        #背景图片设置
        pixmap = QPixmap("blue-sky-with-windy-clouds.jpg")
        scaredPixmap = pixmap.scaled(650,140)
        label = QLabel(self)
        label.setPixmap(scaredPixmap)
        #文字设置
        label_logo= QLabel(self)
        label_logo.setText(self.text)
        label_logo.setStyleSheet("QWidget{color:white;font-weight:600;background:transparent;font-size:30px;}")
        label_logo.setFont(QFont("Microsoft YaHei"))
        label_logo.move(160, 50)
        # label_logo.setAlignment(Qt.AlignCenter)
        label_logo.raise_()#设置在最上方

        #登陆表单内容
        login_widget = QWidget(self)
        login_widget.setGeometry(0,140,650,260)

        #设置为水平布局
        hbox = QHBoxLayout()
        #左侧logo
        logo = QLabel(self)
        logopix = QPixmap('logo.ico')
        logopix_scared = logopix.scaled(200,200)
        logo.setPixmap(logopix_scared)
        logo.setAlignment(Qt.AlignCenter)
        hbox.addWidget(logo,1)
        #右侧表单
        fmlayout = QFormLayout()
        userid = QLabel("用户名")
        userid.setFont(QFont("Microsoft YaHei"))
        userid_input = QLineEdit()
        userid_input.setFixedWidth(270)
        userid_input.setFixedHeight(38)

        password = QLabel("密码")
        password.setFont(QFont("Microsoft YaHei"))
        pwd_input  = QLineEdit()
        pwd_input.setEchoMode(QLineEdit.Password)
        pwd_input.setFixedWidth(270)
        pwd_input.setFixedHeight(38)

        btn_login = QPushButton("登录")
        btn_login.setFixedWidth(270)
        btn_login.setFixedHeight(40)
        btn_login.setFont(QFont("Microsoft YaHei"))
        btn_login.setObjectName("login_btn")
        btn_login.setStyleSheet("#login_btn{background-color:#2c7adf;color:#fff;border:none;border-radius:4px;}")

        fmlayout.addRow(userid,userid_input)
        fmlayout.addRow(password,pwd_input)
        fmlayout.addWidget(btn_login)
        hbox.setAlignment(Qt.AlignCenter)
        #调整间距
        fmlayout.setHorizontalSpacing(20)
        fmlayout.setVerticalSpacing(12)
        hbox.addLayout(fmlayout,20)
        login_widget.setLayout(hbox)
        self.show()
if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = LoginForm()
    sys.exit(app.exec_())

