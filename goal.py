# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'goal.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(525, 369)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)
        self.year = QtWidgets.QComboBox(Dialog)
        self.year.setObjectName("year")
        self.gridLayout.addWidget(self.year, 5, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Discard|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 9, 1, 1, 4)
        self.WorkLoad = QtWidgets.QDoubleSpinBox(Dialog)
        self.WorkLoad.setMinimum(0.5)
        self.WorkLoad.setMaximum(720.0)
        self.WorkLoad.setSingleStep(0.5)
        self.WorkLoad.setObjectName("WorkLoad")
        self.gridLayout.addWidget(self.WorkLoad, 7, 3, 1, 1)
        self.WorkName = QtWidgets.QTextEdit(Dialog)
        self.WorkName.setObjectName("WorkName")
        self.gridLayout.addWidget(self.WorkName, 3, 2, 1, 3)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.WorkTipe = QtWidgets.QComboBox(Dialog)
        self.WorkTipe.setObjectName("WorkTipe")
        self.gridLayout.addWidget(self.WorkTipe, 0, 2, 1, 3)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 4, 1, 1)
        self.mounth = QtWidgets.QComboBox(Dialog)
        self.mounth.setObjectName("mounth")
        self.gridLayout.addWidget(self.mounth, 5, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 1, 1, 2)
        self.data = QtWidgets.QComboBox(Dialog)
        self.data.setObjectName("data")
        self.gridLayout.addWidget(self.data, 5, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 4, 1, 1)
        self.Concentrate = QtWidgets.QCheckBox(Dialog)
        self.Concentrate.setObjectName("Concentrate")
        self.gridLayout.addWidget(self.Concentrate, 8, 2, 1, 3)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Новая цель"))
        Dialog.setWindowIcon(QtGui.QIcon('icon.png'))
        self.label_2.setText(_translate("Dialog", "Короткое название"))
        self.label_3.setText(_translate("Dialog", "Год"))
        self.label_7.setText(_translate("Dialog", "Срок окончания"))
        self.label.setText(_translate("Dialog", "Тип работы"))
        self.label_4.setText(_translate("Dialog", "Месяц"))
        self.label_5.setText(_translate("Dialog", "Число"))
        self.label_8.setText(_translate("Dialog", "Приблизительное время выполнения работы"))
        self.label_6.setText(_translate("Dialog", "Часов"))
        self.Concentrate.setText(_translate("Dialog", "Требуется концентрация на работе"))