# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ASL-SPELLER.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ASLSPELLER(object):
    def setupUi(self, ASLSPELLER):
        ASLSPELLER.setObjectName("ASLSPELLER")
        ASLSPELLER.resize(1099, 782)
        self.camera_label = QtWidgets.QLabel(ASLSPELLER)
        self.camera_label.setGeometry(QtCore.QRect(10, 10, 1081, 631))
        self.camera_label.setText("")
        self.camera_label.setPixmap(QtGui.QPixmap(".\\webcam.jpg"))
        self.camera_label.setAlignment(QtCore.Qt.AlignCenter)
        self.camera_label.setObjectName("camera_label")
        self.startbutton = QtWidgets.QPushButton(ASLSPELLER)
        self.startbutton.setGeometry(QtCore.QRect(380, 730, 112, 34))
        self.startbutton.setObjectName("startbutton")
        self.finishbutton = QtWidgets.QPushButton(ASLSPELLER)
        self.finishbutton.setGeometry(QtCore.QRect(600, 730, 112, 34))
        self.finishbutton.setObjectName("finishbutton")
        self.text_result = QtWidgets.QLineEdit(ASLSPELLER)
        self.text_result.setEnabled(False)
        self.text_result.setGeometry(QtCore.QRect(70, 670, 961, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.text_result.setFont(font)
        self.text_result.setObjectName("text_result")

        self.retranslateUi(ASLSPELLER)
        QtCore.QMetaObject.connectSlotsByName(ASLSPELLER)

    def retranslateUi(self, ASLSPELLER):
        _translate = QtCore.QCoreApplication.translate
        ASLSPELLER.setWindowTitle(_translate("ASLSPELLER", "ASL-SPELLER"))
        self.startbutton.setText(_translate("ASLSPELLER", "Start"))
        self.finishbutton.setText(_translate("ASLSPELLER", "Finish"))
