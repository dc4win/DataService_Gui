# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Shikuangchaxun.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1109, 589)
        mainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        mainWindow.setStatusTip("")
        mainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        mainWindow.setAnimated(False)
        mainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        mainWindow.setDockNestingEnabled(False)
        mainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(560, 10, 547, 491))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setIconSize(QtCore.QSize(12, 2))
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 210, 521, 181))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.clientInfo_lineedit = QtWidgets.QLineEdit(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.clientInfo_lineedit.setFont(font)
        self.clientInfo_lineedit.setAutoFillBackground(True)
        self.clientInfo_lineedit.setInputMask("")
        self.clientInfo_lineedit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.clientInfo_lineedit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.clientInfo_lineedit.setObjectName("clientInfo_lineedit")
        self.horizontalLayout_5.addWidget(self.clientInfo_lineedit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.starttime = QtWidgets.QDateTimeEdit(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.starttime.setFont(font)
        self.starttime.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(12, 0, 0)))
        self.starttime.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1930, 1, 1), QtCore.QTime(0, 0, 0)))
        self.starttime.setCalendarPopup(True)
        self.starttime.setObjectName("starttime")
        self.horizontalLayout_3.addWidget(self.starttime)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.endtime = QtWidgets.QDateTimeEdit(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.endtime.setFont(font)
        self.endtime.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(12, 0, 0)))
        self.endtime.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1930, 1, 1), QtCore.QTime(0, 0, 0)))
        self.endtime.setCalendarPopup(True)
        self.endtime.setObjectName("endtime")
        self.horizontalLayout_2.addWidget(self.endtime)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.station_lineEdit = QtWidgets.QLineEdit(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.station_lineEdit.setFont(font)
        self.station_lineEdit.setObjectName("station_lineEdit")
        self.horizontalLayout.addWidget(self.station_lineEdit)
        self.horizontalLayout_11.addLayout(self.horizontalLayout)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.line_2 = QtWidgets.QFrame(self.layoutWidget_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_9.addWidget(self.line_2)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_9.addWidget(self.label_2)
        self.username = QtWidgets.QComboBox(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.username.setFont(font)
        self.username.setEditable(True)
        self.username.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.username.setDuplicatesEnabled(True)
        self.username.setObjectName("username")
        self.username.addItem("")
        self.username.addItem("")
        self.username.addItem("")
        self.username.addItem("")
        self.username.addItem("")
        self.username.addItem("")
        self.username.addItem("")
        self.username.setItemText(6, "")
        self.horizontalLayout_9.addWidget(self.username)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.line_3 = QtWidgets.QFrame(self.layoutWidget_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_10.addWidget(self.line_3)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_10.addWidget(self.label_6)
        self.makedate = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.makedate.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.makedate.setFont(font)
        self.makedate.setObjectName("makedate")
        self.horizontalLayout_10.addWidget(self.makedate)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(10, 410, 521, 51))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem3)
        self.runpage_PB = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.runpage_PB.setFont(font)
        self.runpage_PB.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.runpage_PB.setAutoFillBackground(True)
        self.runpage_PB.setObjectName("runpage_PB")
        self.horizontalLayout_12.addWidget(self.runpage_PB)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem4)
        self.generate_PB = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.generate_PB.setFont(font)
        self.generate_PB.setObjectName("generate_PB")
        self.horizontalLayout_12.addWidget(self.generate_PB)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem5)
        self.preview_PB = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.preview_PB.setFont(font)
        self.preview_PB.setObjectName("preview_PB")
        self.horizontalLayout_12.addWidget(self.preview_PB)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem8)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(11, 11, 551, 491))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.view = QWebEngineView(self.widget)
        self.view.load(QUrl(r"file:///amap.html"))
        self.view.setObjectName("view")
        self.verticalLayout.addWidget(self.view)
        self.mapbutton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.mapbutton.setFont(font)
        self.mapbutton.setAutoDefault(True)
        self.mapbutton.setDefault(False)
        self.mapbutton.setFlat(False)
        self.mapbutton.setObjectName("mapbutton")
        self.verticalLayout.addWidget(self.mapbutton)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.mapbutton.clicked.connect(self.complete_name)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def complete_name(self):
        self.view.page().runJavaScript('getValue();', self.stationFill)
    def stationFill(self,station):
        self.station_lineEdit.setText(str(station))
        self.station =station
        print(station)
    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.label_4.setText(_translate("mainWindow", "法人信息"))
        self.clientInfo_lineedit.setText(_translate("mainWindow", ""))
        self.label_5.setText(_translate("mainWindow", "起始时间："))
        self.label_3.setText(_translate("mainWindow", "终止时间："))
        self.label.setText(_translate("mainWindow", "站点名称"))
        self.label_2.setText(_translate("mainWindow", "操作人员"))
        self.username.setItemText(0, _translate("mainWindow", "孙翠梅"))
        self.username.setItemText(1, _translate("mainWindow", "张孝龙"))
        self.username.setItemText(2, _translate("mainWindow", "王燕"))
        self.username.setItemText(3, _translate("mainWindow", "尹君"))
        self.username.setItemText(4, _translate("mainWindow", "戴晨"))
        self.username.setItemText(5, _translate("mainWindow", "吴昕悦"))
        self.label_6.setText(_translate("mainWindow", "制作日期"))
        self.runpage_PB.setText(_translate("mainWindow", "启动网页"))
        self.generate_PB.setText(_translate("mainWindow", "生成文件"))
        self.preview_PB.setText(_translate("mainWindow", "预览文件"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("mainWindow", "保险理赔"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("mainWindow", "资料证明"))
        self.mapbutton.setText(_translate("mainWindow", "点击确认当前站点"))

if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QMainWindow()  # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = Ui_mainWindow()  # ui是你创建的ui类的实例化对象
    ui.setupUi(MainWindow)  # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
    MainWindow.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())
