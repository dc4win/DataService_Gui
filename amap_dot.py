# -*- coding: utf-8 -*-
'''
PyQt中高德地图交互操作
'''
from PyQt5.QtWidgets  import QApplication , QWidget , QVBoxLayout,QPushButton,QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import *
import sys
# 创建一个 application实例
app = QApplication(sys.argv)  
win = QWidget()
win.setWindowTitle('PyQt高德地图API接入')
# 创建一个垂直布局器
layout = QVBoxLayout()
win.setLayout(layout)
# 创建一个 QWebEngineView 对象
view = QWebEngineView()
view.load(QUrl(r"file:///amap.html"))

# 创建一个按钮去调用 JavaScript代码
button = QPushButton('操作一下')
def js_callback(result):
        return result
def complete_name():
    station = view.page().runJavaScript('getValue();',js_callback)
    print(station)
# 按钮连接 'complete_name'槽，当点击按钮是会触发信号
button.clicked.connect(complete_name)
# station = complete_name()
# print(station)
# 把QWebView和button加载到layout布局中
layout.addWidget(view)
layout.addWidget(button)
# 显示窗口和运行app
win.show()
sys.exit(app.exec_())
