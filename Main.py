# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 700)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.CalendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.CalendarWidget.setObjectName("CalendarWidget")
        self.verticalLayout.addWidget(self.CalendarWidget)

        self.gridLayout.addLayout(self.verticalLayout, 2, 1, 2, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.GoalB = QtWidgets.QPushButton(self.centralwidget)
        self.GoalB.setObjectName("GoalB")
        self.horizontalLayout.addWidget(self.GoalB)

        self.RecordB = QtWidgets.QPushButton(self.centralwidget)
        self.RecordB.setObjectName("RecordB")
        self.horizontalLayout.addWidget(self.RecordB)

        self.gridLayout.addLayout(self.horizontalLayout, 5, 5, 1, 1)

        self.ShedulWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.ShedulWidget.setObjectName("ShedulWidget")
        self.gridLayout.addWidget(self.ShedulWidget, 2, 5, 3, 1)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)

        self.SettingB = QtWidgets.QPushButton(self.centralwidget)
        self.SettingB.setObjectName("SettingB")
        self.horizontalLayout_4.addWidget(self.SettingB)

        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 5, 1, 1)

        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setObjectName("deleteButton")
        self.gridLayout.addWidget(self.deleteButton, 6, 5, 1, 1)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        #self.SrokB = QtWidgets.QPushButton(self.centralwidget)
        #self.SrokB.setObjectName("SrokB")

        #self.horizontalLayout_2.addWidget(self.SrokB)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)

        self.gridLayout.addLayout(self.horizontalLayout_2, 6, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Личное расписание"))
        MainWindow.setWindowIcon(QtGui.QIcon('icon.png'))
        self.GoalB.setText(_translate("MainWindow", "Создать новую цель"))
        self.RecordB.setText(_translate("MainWindow", "Создать запись"))
        self.SettingB.setText(_translate("MainWindow", "Настройка"))
        self.deleteButton.setText(_translate("MainWindow", "Удалить запись"))
        #self.SrokB.setText(_translate("MainWindow", "Срочное"))
