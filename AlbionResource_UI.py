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
        MainWindow.resize(920, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)

        font = QtGui.QFont()
        font.setFamily("微软雅黑")

        # ButtonAdd
        self.ButtonAdd = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonAdd.setGeometry(QtCore.QRect(347, 160, 41, 41)) # x,y,dx,dy
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonAdd.sizePolicy().hasHeightForWidth())
        self.ButtonAdd.setSizePolicy(sizePolicy)
        self.ButtonAdd.setSizeIncrement(QtCore.QSize(0, 0))
        self.ButtonAdd.setIconSize(QtCore.QSize(36, 36))
        self.ButtonAdd.setFont(font)

        # ButtonDel
        self.ButtonDel = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonDel.setGeometry(QtCore.QRect(347, 210, 41, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonDel.sizePolicy().hasHeightForWidth())
        self.ButtonDel.setSizePolicy(sizePolicy)
        self.ButtonDel.setSizeIncrement(QtCore.QSize(0, 0))
        self.ButtonDel.setIconSize(QtCore.QSize(36, 36))
        self.ButtonDel.setFont(font)

        # ButtonClip
        self.ButtonClip = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonClip.setGeometry(QtCore.QRect(347, 260, 41, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonClip.sizePolicy().hasHeightForWidth())
        self.ButtonClip.setSizePolicy(sizePolicy)
        self.ButtonClip.setSizeIncrement(QtCore.QSize(0, 0))
        #self.ButtonClip.setIcon() # 图标
        self.ButtonClip.setIconSize(QtCore.QSize(36, 36))
        self.ButtonClip.setFont(font)

        # ButtonClear
        self.ButtonClear = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonClear.setGeometry(QtCore.QRect(347, 310, 41, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonClear.sizePolicy().hasHeightForWidth())
        self.ButtonClear.setSizePolicy(sizePolicy)
        self.ButtonClear.setSizeIncrement(QtCore.QSize(0, 0))
        self.ButtonClear.setIconSize(QtCore.QSize(36, 36))
        self.ButtonClear.setFont(font)


        # labelMap
        self.labelMap = QtWidgets.QLabel(self.centralwidget)
        self.labelMap.setGeometry(QtCore.QRect(40, 70, 54, 12))
        self.labelMap.setFont(font)

        # lineMap
        self.lineMap = QtWidgets.QLineEdit(self.centralwidget)
        self.lineMap.setGeometry(QtCore.QRect(40, 90, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        self.lineMap.setFont(font)

        # mapCompleter
        # with open('Map.txt','r') as file: # 打开地图库文件
        #     self.maps = file.readlines()
        #     self.mapTable = []
        #     self.mapLvl = []
        #     self.mapName = []
        #     self.mapAbbr = []
        #     for mapLine in self.maps:
        #         mapLine = mapLine.replace('\n','') # 每行地图信息去掉行尾回车
        #         mapList = mapLine.split('\t') # 分割进各列
        #         self.mapTable.append(mapList) # 形成地图信息表
        #         self.mapLvl.append(mapList[0])
        #         self.mapName.append(mapList[1])
        #         self.mapAbbr.append(mapList[2])
        # self.completions = self.mapName
        # model = QtGui.QStringListModel(self.completions)
        # self.mapCompleter = QtWidgets.QCompleter(model)
        # self.mapCompleter.setWidget(self.lineMap)
        # self.mapCompleter.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)


        self.checkAbbr = QtWidgets.QCheckBox(self.centralwidget)
        self.checkAbbr.setGeometry(QtCore.QRect(220, 80, 100, 24))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.checkAbbr.setFont(font)
        self.checkAbbr.setText("地图名缩写")
        self.checkAbbr.setChecked(True)

        self.checkAbbr = QtWidgets.QCheckBox(self.centralwidget)
        self.checkAbbr.setGeometry(QtCore.QRect(220, 100, 100, 24))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.checkAbbr.setFont(font)
        self.checkAbbr.setText("地图全名")
        self.checkAbbr.setChecked(False)

        self.comboBoxRType = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxRType.setGeometry(QtCore.QRect(40, 220, 110, 22))
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

        self.comboBoxRLvl = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxRLvl.setGeometry(QtCore.QRect(180, 280, 101, 22))
        self.comboBoxRLvl.addItem("-")
        view = QtWidgets.QListView()
        view.setSpacing(5)
        self.comboBoxRLvl.setView(view)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.comboBoxRLvl.setFont(font)

        self.comboBoxRColor = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxRColor.setGeometry(QtCore.QRect(180, 220, 101, 22))
        self.comboBoxRColor.addItem("-")
        view = QtWidgets.QListView()
        view.setSpacing(5)
        self.comboBoxRColor.setView(view)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.comboBoxRColor.setFont(font)

        self.labelRLvl = QtWidgets.QLabel(self.centralwidget)
        self.labelRLvl.setGeometry(QtCore.QRect(180, 260, 91, 12))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.labelRLvl.setFont(font)

        self.labelRType = QtWidgets.QLabel(self.centralwidget)
        self.labelRType.setGeometry(QtCore.QRect(40, 200, 54, 12))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.labelRType.setFont(font)

        self.labelRColor = QtWidgets.QLabel(self.centralwidget)
        self.labelRColor.setGeometry(QtCore.QRect(180, 200, 91, 12))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.labelRColor.setFont(font)

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
        self.tab_1 = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.tab_1.setFont(font)
        self.tabTimeOrClock.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
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

        self.tabTimeZone = QtWidgets.QTabWidget(self.tab_2)
        self.tabTimeZone.setGeometry(QtCore.QRect(10, 10, 171, 111))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setWeight(50)
        self.tabTimeZone.setFont(font)
        self.tabTimeZone.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabTimeZone.setTabShape(QtWidgets.QTabWidget.Rounded)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.tabTimeZone.setFont(font)

        self.tab_2_1 = QtWidgets.QWidget()
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
        self.tabTimeZone.addTab(self.tab_2_1, "")
        self.tab_2_2 = QtWidgets.QWidget()
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
        self.tabTimeZone.addTab(self.tab_2_2, "")
        self.tabTimeOrClock.addTab(self.tab_2, "")

        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(400, 20, 510, 551))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.table.setFont(font)
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["图标","剩余时间","资源","地图","备注","UTC"])
        self.table.setColumnWidth(0,30)
        self.table.setColumnWidth(1,95)
        self.table.setColumnWidth(2,80)
        self.table.setColumnWidth(3,150)
        self.table.setColumnWidth(4,58)
        self.table.setColumnWidth(5,50)
        self.table.setRowHeight(0,40)
        self.table.insertRow(0)

        self.frameline_1 = QtWidgets.QFrame(self.centralwidget)
        self.frameline_1.setGeometry(QtCore.QRect(40, 330, 281, 16))
        self.frameline_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.frameline_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frameline_2 = QtWidgets.QFrame(self.centralwidget)
        self.frameline_2.setGeometry(QtCore.QRect(40, 160, 281, 16))
        self.frameline_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.frameline_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frameline_3 = QtWidgets.QFrame(self.centralwidget)
        self.frameline_3.setGeometry(QtCore.QRect(323, 20, 20, 561))
        self.frameline_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.frameline_3.setFrameShadow(QtWidgets.QFrame.Sunken)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
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
        MainWindow.setTabOrder(self.ButtonDel, self.ButtonClip)
        MainWindow.setTabOrder(self.ButtonClip, self.ButtonClear)

    def retranslateUi(self, MainWindow): # 翻译
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AlbionResourceTimer"))
        self.ButtonAdd.setText(_translate("MainWindow", "→"))
        self.ButtonDel.setText(_translate("MainWindow", "←"))
        self.ButtonClip.setText(_translate("MainWindow", "复制"))
        self.ButtonClear.setText(_translate("MainWindow", "清空"))
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
