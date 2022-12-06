# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ASL-SPELLER.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ASLSPELLER(object):
    def setupUi(self, ASLSPELLER):
        ASLSPELLER.setObjectName("ASLSPELLER")
        ASLSPELLER.resize(751, 557)
        self.camera_label = QtWidgets.QLabel(ASLSPELLER)
        self.camera_label.setGeometry(QtCore.QRect(140, 50, 461, 301))
        self.camera_label.setText("")
        self.camera_label.setPixmap(QtGui.QPixmap("webcam.jpg"))
        self.camera_label.setObjectName("camera_label")
        self.startbutton = QtWidgets.QPushButton(ASLSPELLER)
        self.startbutton.setGeometry(QtCore.QRect(240, 440, 112, 34))
        self.startbutton.setObjectName("startbutton")
        self.finishbutton = QtWidgets.QPushButton(ASLSPELLER)
        self.finishbutton.setGeometry(QtCore.QRect(410, 440, 112, 34))
        self.finishbutton.setObjectName("finishbutton")
        self.text_result = QtWidgets.QLineEdit(ASLSPELLER)
        self.text_result.setEnabled(False)
        self.text_result.setGeometry(QtCore.QRect(140, 370, 461, 25))
        self.text_result.setText("")
        self.text_result.setObjectName("text_result")

        self.retranslateUi(ASLSPELLER)
        QtCore.QMetaObject.connectSlotsByName(ASLSPELLER)

    def retranslateUi(self, ASLSPELLER):
        _translate = QtCore.QCoreApplication.translate
        ASLSPELLER.setWindowTitle(_translate("ASLSPELLER", "ASL-SPELLER"))
        self.startbutton.setText(_translate("ASLSPELLER", "Start"))
        self.finishbutton.setText(_translate("ASLSPELLER", "Finish"))

