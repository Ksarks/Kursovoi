# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(352, 158)
        self.formLayout = QtWidgets.QFormLayout(Dialog)
        self.formLayout.setObjectName("formLayout")
        self.Timer = QtWidgets.QSpinBox(Dialog)
        self.Timer.setMinimum(15)
        self.Timer.setMaximum(50)
        self.Timer.setSingleStep(5)
        self.Timer.setProperty("value", 25)
        self.Timer.setObjectName("Timer")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Timer)
        self.Priority = QtWidgets.QPushButton(Dialog)
        self.Priority.setObjectName("Priority")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.Priority)
        self.NewWork = QtWidgets.QPushButton(Dialog)
        self.NewWork.setObjectName("NewWork")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.NewWork)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Настройки"))
        Dialog.setWindowIcon(QtGui.QIcon('icon.png'))
        self.Priority.setText(_translate("Dialog", "Изменить преоритеты"))
        self.NewWork.setText(_translate("Dialog", "Добавить новую работу"))
        self.label.setText(_translate("Dialog", "Таймер на 1 помидор"))
