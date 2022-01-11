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
        self.setStyleSheet('#loginwindow{background-color:black}')
        self.setFixedSize(650,400)
        self.setWindowTitle("登录界面")
        self.setWindowIcon(QIcon('blue-sky-with-windy-clouds.jpg'))
        self.text = "镇江气象数据服务平台"

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = LoginForm()
    sys.exit(app.exec_())
