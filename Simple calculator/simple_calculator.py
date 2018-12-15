# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simple_calculator.ui'
#
# Created: Fri Dec 14 21:03:18 2018
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(383, 320)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout.addWidget(self.textBrowser)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_12 = QtGui.QPushButton(Form)
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.gridLayout.addWidget(self.pushButton_12, 3, 5, 1, 1)
        self.pushButton_10 = QtGui.QPushButton(Form)
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.gridLayout.addWidget(self.pushButton_10, 1, 4, 1, 1)
        self.pushButton_7 = QtGui.QPushButton(Form)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.gridLayout.addWidget(self.pushButton_7, 2, 4, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.pushButton_4, 3, 4, 1, 1)
        self.pushButton_13 = QtGui.QPushButton(Form)
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.gridLayout.addWidget(self.pushButton_13, 2, 5, 1, 1)
        self.pushButton_8 = QtGui.QPushButton(Form)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.gridLayout.addWidget(self.pushButton_8, 1, 2, 1, 1)
        self.pushButton_11 = QtGui.QPushButton(Form)
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.gridLayout.addWidget(self.pushButton_11, 4, 4, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(Form)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout.addWidget(self.pushButton_5, 2, 2, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 3, 2, 1, 1)
        self.pushButton_6 = QtGui.QPushButton(Form)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout.addWidget(self.pushButton_6, 2, 3, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 3, 3, 1, 1)
        self.pushButton_9 = QtGui.QPushButton(Form)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.gridLayout.addWidget(self.pushButton_9, 1, 3, 1, 1)
        self.pushButton_14 = QtGui.QPushButton(Form)
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.gridLayout.addWidget(self.pushButton_14, 1, 5, 1, 1)
        self.pushButton_15 = QtGui.QPushButton(Form)
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.gridLayout.addWidget(self.pushButton_15, 0, 5, 1, 1)
        self.pushButton_16 = QtGui.QPushButton(Form)
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.gridLayout.addWidget(self.pushButton_16, 4, 5, 1, 1)
        self.pushButton_17 = QtGui.QPushButton(Form)
        self.pushButton_17.setObjectName(_fromUtf8("pushButton_17"))
        self.gridLayout.addWidget(self.pushButton_17, 0, 4, 1, 1)
        self.pushButton_18 = QtGui.QPushButton(Form)
        self.pushButton_18.setObjectName(_fromUtf8("pushButton_18"))
        self.gridLayout.addWidget(self.pushButton_18, 0, 3, 1, 1)
        self.pushButton_19 = QtGui.QPushButton(Form)
        self.pushButton_19.setObjectName(_fromUtf8("pushButton_19"))
        self.gridLayout.addWidget(self.pushButton_19, 0, 2, 1, 1)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 4, 2, 1, 2)
        self.verticalLayout_2.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton_12.setText(_translate("Form", "+", None))
        self.pushButton_10.setText(_translate("Form", "9", None))
        self.pushButton_7.setText(_translate("Form", "6", None))
        self.pushButton_4.setText(_translate("Form", "3", None))
        self.pushButton_13.setText(_translate("Form", "-", None))
        self.pushButton_8.setText(_translate("Form", "7", None))
        self.pushButton_11.setText(_translate("Form", ".", None))
        self.pushButton_5.setText(_translate("Form", "4", None))
        self.pushButton_2.setText(_translate("Form", "1", None))
        self.pushButton_6.setText(_translate("Form", "5", None))
        self.pushButton_3.setText(_translate("Form", "2", None))
        self.pushButton_9.setText(_translate("Form", "8", None))
        self.pushButton_14.setText(_translate("Form", "*", None))
        self.pushButton_15.setText(_translate("Form", "/", None))
        self.pushButton_16.setText(_translate("Form", "=", None))
        self.pushButton_17.setText(_translate("Form", "%", None))
        self.pushButton_18.setText(_translate("Form", "+/-", None))
        self.pushButton_19.setText(_translate("Form", "AC", None))
        self.pushButton.setText(_translate("Form", "0", None))

