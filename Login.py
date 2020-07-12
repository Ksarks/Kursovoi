# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import hashlib

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Login")
        Dialog.resize(300, 230)
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.Login = QtWidgets.QLineEdit(self.centralwidget)
        self.Login.setObjectName("Login")
        self.Login.textChanged[str].connect(self.onChangLog)
        self.gridLayout.addWidget(self.Login, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setObjectName("Password")
        self.Password.textChanged[str].connect(self.onChangPass)
        self.gridLayout_2.addWidget(self.Password, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 42, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.Login_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Login_2.setObjectName("Login_2")
        self.Login_2.clicked.connect(self.LogClick)
        self.horizontalLayout.addWidget(self.Login_2)
        self.Registration = QtWidgets.QPushButton(self.centralwidget)
        self.Registration.setObjectName("Registration")
        self.Registration.clicked.connect(self.RegClick)
        self.horizontalLayout.addWidget(self.Registration)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(20, 41, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def onChangLog(self, text):
        self.log = text

    def onChangPass(self, text):
        self.pas = text

    def RegClick(self):
        self.Hash()

    def LogClick(self):
        self.Hash()


    def Hash(self):
        salt = 'As56$Dsfi%2jdkp2fZ21'
        mystring = self.log + salt + self.pas
        hash_object = hashlib.md5(mystring.encode())
        self.hashline = hash_object.hexdigest()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("MainWindow", "Авторизация"))
        Dialog.setWindowIcon(QtGui.QIcon('icon.png'))
        self.label.setText(_translate("MainWindow", "Введите логин и пароль"))
        self.label_2.setText(_translate("MainWindow", "Login:"))
        self.label_3.setText(_translate("MainWindow", "Password:"))
        self.Login_2.setText(_translate("MainWindow", "Вход"))
        self.Registration.setText(_translate("MainWindow", "Регистрация"))
