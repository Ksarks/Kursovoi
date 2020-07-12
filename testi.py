# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Test")
        Dialog.resize(487, 213)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)
        self.LeftButton = QtWidgets.QPushButton(Dialog)
        self.LeftButton.setObjectName("LeftButton")
        self.gridLayout.addWidget(self.LeftButton, 3, 0, 1, 1)
        self.RightButton = QtWidgets.QPushButton(Dialog)
        self.RightButton.setObjectName("RightButton")
        self.gridLayout.addWidget(self.RightButton, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 4, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Тестирование"))
        Dialog.setWindowIcon(QtGui.QIcon('icon.png'))
        self.label.setText(_translate("Dialog", "Для определения ваших предпочтений, требуется провести небольшой тест.\n"
                                                "Выберите что важнее для вас из двух вариантов,\n"
                                                "нажав на соответствующую кнопку."))
        self.LeftButton.setText(_translate("Dialog", "PushButton"))
        self.RightButton.setText(_translate("Dialog", "PushButton"))
