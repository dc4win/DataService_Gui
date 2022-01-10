'''
此脚本用于编写登陆界面
'''
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter, QColor, QFont, QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication, QLabel, QDesktopWidget, QHBoxLayout, QFormLayout, \
    QPushButton, QLineEdit

class LoginWindow(QWidget):
    def __init__(self):
        super.__init__()
        self.initUI()
    def initUI(self):

