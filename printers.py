# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'printers.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(307, 209)
        Dialog.setMinimumSize(QtCore.QSize(307, 209))
        Dialog.setMaximumSize(QtCore.QSize(307, 209))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.button_pantum = QtWidgets.QPushButton(Dialog)
        self.button_pantum.setGeometry(QtCore.QRect(10, 100, 88, 34))
        self.button_pantum.setObjectName("button_pantum")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 10, 91, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 91, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(210, 80, 91, 20))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.button_brother = QtWidgets.QPushButton(Dialog)
        self.button_brother.setGeometry(QtCore.QRect(110, 100, 88, 34))
        self.button_brother.setObjectName("button_brother")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(110, 80, 91, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.button_simple_scan = QtWidgets.QPushButton(Dialog)
        self.button_simple_scan.setGeometry(QtCore.QRect(210, 100, 88, 34))
        self.button_simple_scan.setObjectName("button_simple_scan")
        self.button_kyosera = QtWidgets.QPushButton(Dialog)
        self.button_kyosera.setGeometry(QtCore.QRect(110, 30, 88, 34))
        self.button_kyosera.setObjectName("button_kyosera")
        self.button_oki = QtWidgets.QPushButton(Dialog)
        self.button_oki.setGeometry(QtCore.QRect(10, 30, 88, 34))
        self.button_oki.setObjectName("button_oki")
        self.button_pdf = QtWidgets.QPushButton(Dialog)
        self.button_pdf.setGeometry(QtCore.QRect(210, 30, 88, 34))
        self.button_pdf.setObjectName("button_pdf")
        self.button_other = QtWidgets.QPushButton(Dialog)
        self.button_other.setGeometry(QtCore.QRect(110, 170, 88, 34))
        self.button_other.setObjectName("button_other")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(210, 10, 91, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(110, 150, 91, 20))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Принтера"))
        self.label.setText(_translate("Dialog", "OKI"))
        self.button_pantum.setText(_translate("Dialog", "Установить"))
        self.label_2.setText(_translate("Dialog", "Kyosera"))
        self.label_4.setText(_translate("Dialog", "Pantum"))
        self.label_6.setText(_translate("Dialog", "Simple-scan"))
        self.button_brother.setText(_translate("Dialog", "Установить"))
        self.label_5.setText(_translate("Dialog", "Brother"))
        self.button_simple_scan.setText(_translate("Dialog", "Установить"))
        self.button_kyosera.setText(_translate("Dialog", "Установить"))
        self.button_oki.setText(_translate("Dialog", "Установить"))
        self.button_pdf.setText(_translate("Dialog", "Установить"))
        self.button_other.setText(_translate("Dialog", "Установить"))
        self.label_3.setText(_translate("Dialog", "PDF"))
        self.label_7.setText(_translate("Dialog", "Другие"))