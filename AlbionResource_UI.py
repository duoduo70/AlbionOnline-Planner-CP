# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AlbionResource_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.ButtonAdd = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonAdd.setGeometry(QtCore.QRect(350, 260, 41, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonAdd.sizePolicy().hasHeightForWidth())
        self.ButtonAdd.setSizePolicy(sizePolicy)
        self.ButtonAdd.setSizeIncrement(QtCore.QSize(0, 0))
        self.ButtonAdd.setIconSize(QtCore.QSize(36, 36))
        self.ButtonAdd.setObjectName("ButtonAdd")

        self.ButtonDel = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonDel.setGeometry(QtCore.QRect(350, 310, 41, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonDel.sizePolicy().hasHeightForWidth())
        self.ButtonDel.setSizePolicy(sizePolicy)
        self.ButtonDel.setSizeIncrement(QtCore.QSize(0, 0))
        self.ButtonDel.setIconSize(QtCore.QSize(36, 36))
        self.ButtonDel.setObjectName("ButtonDel")

        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(400, 20, 487, 551))
        self.table.setObjectName("table")
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.table.setFont(font)
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["","剩余时间","资源","地图","备注","UTC"])
        self.table.setColumnWidth(0,30)
        self.table.setColumnWidth(1,95)
        self.table.setColumnWidth(2,80)
        self.table.setColumnWidth(3,150)
        self.table.setColumnWidth(4,58)
        self.table.setColumnWidth(5,60)
        self.table.setRowHeight(0,40)
        self.table.insertRow(0)



        self.labelMap = QtWidgets.QLabel(self.centralwidget)
        self.labelMap.setGeometry(QtCore.QRect(40, 70, 54, 12))
        self.labelMap.setObjectName("labelMap")
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.labelMap.setFont(font)

        self.comboBoxRType = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxRType.setGeometry(QtCore.QRect(40, 220, 110, 22))
        self.comboBoxRType.setObjectName("comboBoxRType")
        self.comboBoxRType.addItem("")
        self.comboBoxRType.addItem("")
        self.comboBoxRType.addItem("")
        self.comboBoxRType.addItem("")
        self.comboBoxRType.addItem("")
        self.comboBoxRType.addItem("")
        self.comboBoxRType.addItem("")
        self.comboBoxRType.addItem("")
        self.comboBoxRType.addItem("")
        view = QtWidgets.QListView()
        view.setSpacing(5)
        self.comboBoxRType.setView(view)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.comboBoxRType.setFont(font)

        self.labelRType = QtWidgets.QLabel(self.centralwidget)
        self.labelRType.setGeometry(QtCore.QRect(40, 200, 54, 12))
        self.labelRType.setObjectName("labelRType")
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.labelRType.setFont(font)

        self.labelRColor = QtWidgets.QLabel(self.centralwidget)
        self.labelRColor.setGeometry(QtCore.QRect(180, 200, 91, 12))
        self.labelRColor.setObjectName("labelRColor")
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.labelRColor.setFont(font)

        self.comboBoxRColor = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxRColor.setGeometry(QtCore.QRect(180, 220, 101, 22))
        self.comboBoxRColor.setObjectName("comboBoxRColor")
        self.comboBoxRColor.addItem("-")
        view = QtWidgets.QListView()
        view.setSpacing(5)
        self.comboBoxRColor.setView(view)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.comboBoxRColor.setFont(font)

        self.labelRLvl = QtWidgets.QLabel(self.centralwidget)
        self.labelRLvl.setGeometry(QtCore.QRect(180, 260, 91, 12))
        self.labelRLvl.setObjectName("labelRLvl")
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.labelRLvl.setFont(font)

        self.tabTimeOrClock = QtWidgets.QTabWidget(self.centralwidget)
        self.tabTimeOrClock.setEnabled(True)
        self.tabTimeOrClock.setGeometry(QtCore.QRect(40, 360, 191, 151))
        self.tabTimeOrClock.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.tabTimeOrClock.setFont(font)
        self.tabTimeOrClock.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabTimeOrClock.setAutoFillBackground(False)
        self.tabTimeOrClock.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tabTimeOrClock.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabTimeOrClock.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabTimeOrClock.setIconSize(QtCore.QSize(16, 16))
        self.tabTimeOrClock.setElideMode(QtCore.Qt.ElideNone)
        self.tabTimeOrClock.setUsesScrollButtons(True)
        self.tabTimeOrClock.setDocumentMode(False)
        self.tabTimeOrClock.setMovable(False)
        self.tabTimeOrClock.setTabBarAutoHide(False)
        self.tabTimeOrClock.setObjectName("tabTimeOrClock")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.tab_1.setFont(font)
        self.tabTimeOrClock.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.tab_2.setFont(font)

        self.timeTimeRemain = QtWidgets.QTimeEdit(self.tab_1)
        self.timeTimeRemain.setGeometry(QtCore.QRect(30, 50, 131, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.timeTimeRemain.setFont(font)
        self.timeTimeRemain.setFrame(True)
        self.timeTimeRemain.setAlignment(QtCore.Qt.AlignCenter)
        self.timeTimeRemain.setTimeSpec(QtCore.Qt.LocalTime)
        self.timeTimeRemain.setTime(QtCore.QTime(0, 0, 0))
        self.timeTimeRemain.setObjectName("timeTimeRemain")

        self.tabTimeZone = QtWidgets.QTabWidget(self.tab_2)
        self.tabTimeZone.setGeometry(QtCore.QRect(10, 10, 171, 111))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setWeight(50)
        self.tabTimeZone.setFont(font)
        self.tabTimeZone.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabTimeZone.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabTimeZone.setObjectName("tabTimeZone")
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.tabTimeZone.setFont(font)

        self.tab_2_1 = QtWidgets.QWidget()
        self.tab_2_1.setObjectName("tab_2_1")
        self.timeUTC = QtWidgets.QTimeEdit(self.tab_2_1)
        self.timeUTC.setGeometry(QtCore.QRect(20, 20, 131, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setWeight(50)
        self.timeUTC.setFont(font)
        self.timeUTC.setFrame(True)
        self.timeUTC.setAlignment(QtCore.Qt.AlignCenter)
        self.timeUTC.setTimeSpec(QtCore.Qt.LocalTime)
        self.timeUTC.setTime(QtCore.QTime(0, 0, 0))
        self.timeUTC.setObjectName("timeUTC")
        self.tabTimeZone.addTab(self.tab_2_1, "")
        self.tab_2_2 = QtWidgets.QWidget()
        self.tab_2_2.setObjectName("tab_2_2")
        self.timeBeijing = QtWidgets.QTimeEdit(self.tab_2_2)
        self.timeBeijing.setGeometry(QtCore.QRect(20, 20, 131, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.timeBeijing.setFont(font)
        self.timeBeijing.setFrame(True)
        self.timeBeijing.setAlignment(QtCore.Qt.AlignCenter)
        self.timeBeijing.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.timeBeijing.setTimeSpec(QtCore.Qt.LocalTime)
        self.timeBeijing.setTime(QtCore.QTime(0, 0, 0))
        self.timeBeijing.setObjectName("timeBeijing")
        self.tabTimeZone.addTab(self.tab_2_2, "")
        self.tabTimeOrClock.addTab(self.tab_2, "")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(40, 330, 281, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.line.setFont(font)

        self.lineMap = QtWidgets.QLineEdit(self.centralwidget)
        self.lineMap.setGeometry(QtCore.QRect(40, 90, 160, 30))
        self.lineMap.setObjectName("lineMap")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        self.lineMap.setFont(font)

        self.comboBoxRLvl = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxRLvl.setGeometry(QtCore.QRect(180, 280, 101, 22))
        self.comboBoxRLvl.setObjectName("comboBoxRLvl")
        self.comboBoxRLvl.addItem("-")
        view = QtWidgets.QListView()
        view.setSpacing(5)
        self.comboBoxRLvl.setView(view)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.comboBoxRLvl.setFont(font)

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(40, 160, 281, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(323, 20, 20, 561))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabTimeOrClock.setCurrentIndex(0)
        self.tabTimeZone.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineMap, self.comboBoxRType)
        MainWindow.setTabOrder(self.comboBoxRType, self.comboBoxRColor)
        MainWindow.setTabOrder(self.comboBoxRColor, self.comboBoxRLvl)
        MainWindow.setTabOrder(self.comboBoxRLvl, self.tabTimeOrClock)
        MainWindow.setTabOrder(self.tabTimeOrClock, self.timeTimeRemain)
        MainWindow.setTabOrder(self.timeTimeRemain, self.ButtonAdd)
        MainWindow.setTabOrder(self.ButtonAdd, self.ButtonDel)
        MainWindow.setTabOrder(self.ButtonDel, self.table)
        MainWindow.setTabOrder(self.table, self.timeBeijing)
        MainWindow.setTabOrder(self.timeBeijing, self.tabTimeZone)
        MainWindow.setTabOrder(self.tabTimeZone, self.timeUTC)

    def retranslateUi(self, MainWindow): # 翻译
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AlbionResourceTimer"))
        self.ButtonAdd.setText(_translate("MainWindow", "→"))
        self.ButtonDel.setText(_translate("MainWindow", "←"))
        self.labelMap.setText(_translate("MainWindow", "地点"))

        self.comboBoxRType.setItemText(0, _translate("MainWindow", "-"))
        self.comboBoxRType.setItemText(1, _translate("MainWindow", "能量核心（球）"))
        self.comboBoxRType.setItemText(2, _translate("MainWindow", "能量水晶（风）"))
        self.comboBoxRType.setItemText(3, _translate("MainWindow", "野外宝箱"))
        self.comboBoxRType.setItemText(4, _translate("MainWindow", "采集资源(.4)"))
        self.comboBoxRType.setItemText(5, _translate("MainWindow", "猛犸象"))
        self.comboBoxRType.setItemText(6, _translate("MainWindow", "城堡"))
        self.comboBoxRType.setItemText(7, _translate("MainWindow", "哨站"))
        self.comboBoxRType.setItemText(8, _translate("MainWindow", "领地"))

        self.labelRType.setText(_translate("MainWindow", "资源类型"))
        self.labelRColor.setText(_translate("MainWindow", "资源品质（颜色）"))
        self.labelRLvl.setText(_translate("MainWindow", "资源等级"))
        self.timeTimeRemain.setDisplayFormat(_translate("MainWindow", "hh:mm:ss"))
        self.tabTimeOrClock.setTabText(self.tabTimeOrClock.indexOf(self.tab_1), _translate("MainWindow", "剩余时间"))
        self.timeUTC.setDisplayFormat(_translate("MainWindow", "hh:mm"))
        self.tabTimeZone.setTabText(self.tabTimeZone.indexOf(self.tab_2_1), _translate("MainWindow", "UTC 时间"))
        self.timeBeijing.setDisplayFormat(_translate("MainWindow", "hh:mm"))
        self.tabTimeZone.setTabText(self.tabTimeZone.indexOf(self.tab_2_2), _translate("MainWindow", "北京时间"))
        self.tabTimeOrClock.setTabText(self.tabTimeOrClock.indexOf(self.tab_2), _translate("MainWindow", "解锁时刻"))