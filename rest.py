# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rest.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(411, 126)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 3)
        self.Less = QtWidgets.QPushButton(Dialog)
        self.Less.setObjectName("Less")
        self.gridLayout.addWidget(self.Less, 2, 0, 1, 1)
        self.Midlle = QtWidgets.QPushButton(Dialog)
        self.Midlle.setObjectName("Midlle")
        self.gridLayout.addWidget(self.Midlle, 2, 1, 1, 1)
        self.More = QtWidgets.QPushButton(Dialog)
        self.More.setObjectName("More")
        self.gridLayout.addWidget(self.More, 2, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Перерыв"))
        self.label.setText(_translate("Dialog", "Перерыв!"))
        self.label_2.setText(_translate("Dialog", "Выберите, увеличить время работы, уменьшить,\n"
"либо оставить прежним"))
        self.Less.setText(_translate("Dialog", "Уменьшить"))
        self.Midlle.setText(_translate("Dialog", "Не изменять"))
        self.More.setText(_translate("Dialog", "Увеличить"))
