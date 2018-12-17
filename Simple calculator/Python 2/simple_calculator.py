# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simple_calculator.ui'
#
# Created: Sat Dec 15 16:28:46 2018
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        self.Plus_Button = QtGui.QPushButton(Form)
        self.Plus_Button.setObjectName(_fromUtf8("Plus_Button"))
        self.gridLayout.addWidget(self.Plus_Button, 3, 5, 1, 1)
        self.Nine_Button = QtGui.QPushButton(Form)
        self.Nine_Button.setObjectName(_fromUtf8("Nine_Button"))
        self.gridLayout.addWidget(self.Nine_Button, 1, 4, 1, 1)
        self.Six_Button = QtGui.QPushButton(Form)
        self.Six_Button.setObjectName(_fromUtf8("Six_Button"))
        self.gridLayout.addWidget(self.Six_Button, 2, 4, 1, 1)
        self.Three_Button = QtGui.QPushButton(Form)
        self.Three_Button.setObjectName(_fromUtf8("Three_Button"))
        self.gridLayout.addWidget(self.Three_Button, 3, 4, 1, 1)
        self.Minus_Button = QtGui.QPushButton(Form)
        self.Minus_Button.setObjectName(_fromUtf8("Minus_Button"))
        self.gridLayout.addWidget(self.Minus_Button, 2, 5, 1, 1)
        self.Seven_Button = QtGui.QPushButton(Form)
        self.Seven_Button.setObjectName(_fromUtf8("Seven_Button"))
        self.gridLayout.addWidget(self.Seven_Button, 1, 2, 1, 1)
        self.Point_Button = QtGui.QPushButton(Form)
        self.Point_Button.setObjectName(_fromUtf8("Point_Button"))
        self.gridLayout.addWidget(self.Point_Button, 4, 4, 1, 1)
        self.Four_Button = QtGui.QPushButton(Form)
        self.Four_Button.setObjectName(_fromUtf8("Four_Button"))
        self.gridLayout.addWidget(self.Four_Button, 2, 2, 1, 1)
        self.One_Button = QtGui.QPushButton(Form)
        self.One_Button.setObjectName(_fromUtf8("One_Button"))
        self.gridLayout.addWidget(self.One_Button, 3, 2, 1, 1)
        self.Five_Button = QtGui.QPushButton(Form)
        self.Five_Button.setObjectName(_fromUtf8("Five_Button"))
        self.gridLayout.addWidget(self.Five_Button, 2, 3, 1, 1)
        self.Two_Button = QtGui.QPushButton(Form)
        self.Two_Button.setObjectName(_fromUtf8("Two_Button"))
        self.gridLayout.addWidget(self.Two_Button, 3, 3, 1, 1)
        self.Eight_Button = QtGui.QPushButton(Form)
        self.Eight_Button.setObjectName(_fromUtf8("Eight_Button"))
        self.gridLayout.addWidget(self.Eight_Button, 1, 3, 1, 1)
        self.Times_Button = QtGui.QPushButton(Form)
        self.Times_Button.setObjectName(_fromUtf8("Times_Button"))
        self.gridLayout.addWidget(self.Times_Button, 1, 5, 1, 1)
        self.Divide_Button = QtGui.QPushButton(Form)
        self.Divide_Button.setObjectName(_fromUtf8("Divide_Button"))
        self.gridLayout.addWidget(self.Divide_Button, 0, 5, 1, 1)
        self.Result_Button = QtGui.QPushButton(Form)
        self.Result_Button.setObjectName(_fromUtf8("Result_Button"))
        self.gridLayout.addWidget(self.Result_Button, 4, 5, 1, 1)
        self.Percentage_Button = QtGui.QPushButton(Form)
        self.Percentage_Button.setObjectName(_fromUtf8("Percentage_Button"))
        self.gridLayout.addWidget(self.Percentage_Button, 0, 4, 1, 1)
        self.P_or_N_Button = QtGui.QPushButton(Form)
        self.P_or_N_Button.setObjectName(_fromUtf8("P_or_N_Button"))
        self.gridLayout.addWidget(self.P_or_N_Button, 0, 3, 1, 1)
        self.AC_Button = QtGui.QPushButton(Form)
        self.AC_Button.setObjectName(_fromUtf8("AC_Button"))
        self.gridLayout.addWidget(self.AC_Button, 0, 2, 1, 1)
        self.Zero_Button = QtGui.QPushButton(Form)
        self.Zero_Button.setObjectName(_fromUtf8("Zero_Button"))
        self.gridLayout.addWidget(self.Zero_Button, 4, 2, 1, 2)
        self.verticalLayout_2.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Simple Calculator", None))
        self.Plus_Button.setText(_translate("Form", "+", None))
        self.Plus_Button.clicked.connect(self.pressplus)

        self.Nine_Button.setText(_translate("Form", "9", None))
        self.Nine_Button.clicked.connect(self.pressnine)

        self.Six_Button.setText(_translate("Form", "6", None))
        self.Six_Button.clicked.connect(self.presssix)

        self.Three_Button.setText(_translate("Form", "3", None))
        self.Three_Button.clicked.connect(self.pressthree)

        self.Minus_Button.setText(_translate("Form", "-", None))
        self.Minus_Button.clicked.connect(self.pressminus)

        self.Seven_Button.setText(_translate("Form", "7", None))
        self.Seven_Button.clicked.connect(self.pressseven)

        self.Point_Button.setText(_translate("Form", ".", None))
        self.Point_Button.clicked.connect(self.presspoint)

        self.Four_Button.setText(_translate("Form", "4", None))
        self.Four_Button.clicked.connect(self.pressfour)

        self.One_Button.setText(_translate("Form", "1", None))
        self.One_Button.clicked.connect(self.pressone)

        self.Five_Button.setText(_translate("Form", "5", None))
        self.Five_Button.clicked.connect(self.pressfive)

        self.Two_Button.setText(_translate("Form", "2", None))
        self.Two_Button.clicked.connect(self.presstwo)

        self.Eight_Button.setText(_translate("Form", "8", None))
        self.Eight_Button.clicked.connect(self.presseight)

        self.Times_Button.setText(_translate("Form", "*", None))
        self.Times_Button.clicked.connect(self.presstimes)

        self.Divide_Button.setText(_translate("Form", "/", None))
        self.Divide_Button.clicked.connect(self.pressdivide)

        self.Result_Button.setText(_translate("Form", "=", None))
        self.Result_Button.clicked.connect(self.pressresult)

        self.Percentage_Button.setText(_translate("Form", "%", None))
        self.Percentage_Button.clicked.connect(self.presspercentage)

        self.P_or_N_Button.setText(_translate("Form", "+/-", None))
        self.P_or_N_Button.clicked.connect(self.pressPN)

        self.AC_Button.setText(_translate("Form", "AC", None))
        self.AC_Button.clicked.connect(self.pressAC)

        self.Zero_Button.setText(_translate("Form", "0", None))
        self.Zero_Button.clicked.connect(self.presszero)

    display_number = ''
    f_number = ''
    s_number = ''
    sign = ''
    result = ''

    def pressone(self):
        if self.result != '':
            self.display_number = '1'
            self.result = ''
        else:
            self.display_number += '1'
            self.textBrowser.setText(self.display_number)

    def presstwo(self):
        if self.result != '':
            self.display_number = '2'
            self.result = ''
        else:
            self.display_number += '2'
            self.textBrowser.setText(self.display_number)

    def pressthree(self):
        if self.result != '':
            self.display_number = '3'
            self.result = ''
        else:
            self.display_number += '3'
            self.textBrowser.setText(self.display_number)

    def pressfour(self):
        if self.result != '':
            self.display_number = '4'
            self.result = ''
        else:
            self.display_number += '4'
            self.textBrowser.setText(self.display_number)

    def pressfive(self):
        if self.result != '':
            self.display_number = '5'
            self.result = ''
        else:
            self.display_number += '5'
            self.textBrowser.setText(self.display_number)

    def presssix(self):
        if self.result != '':
            self.display_number = '6'
            self.result = ''
        else:
            self.display_number += '6'
            self.textBrowser.setText(self.display_number)

    def pressseven(self):
        if self.result != '':
            self.display_number = '7'
            self.result = ''
        else:
            self.display_number += '7'
            self.textBrowser.setText(self.display_number)

    def presseight(self):
        if self.result != '':
            self.display_number = '8'
            self.result = ''
        else:
            self.display_number += '8'
            self.textBrowser.setText(self.display_number)
    def pressnine(self):
        if self.result != '':
            self.display_number = '9'
            self.result = ''
        else:
            self.display_number += '9'
            self.textBrowser.setText(self.display_number)

    def presszero(self):
        if self.result != '':
            self.display_number = '0'
            self.result = ''
        else:
            self.display_number += '0'
            self.textBrowser.setText(self.display_number)

    def presspoint(self):
        if self.result != '':
            self.display_number = '0.'
            self.result = ''
        else:
            self.display_number += '.'
            self.textBrowser.setText(self.display_number)

    def presspercentage(self):
        self.display_number = self.intflo(float(self.display_number)/100)
        self.textBrowser.setText(self.display_number)

    def pressPN(self):
        self.display_number = self.intflo(float(self.display_number)* -1)
        self.textBrowser.setText(self.display_number)

    def pressAC(self):
        self.display_number = ''
        self.result = ''
        self.sign = ''
        self.f_number = ''
        self.s_number = ''
        self.textBrowser.setText(self.display_number)

    def pressplus(self):
        if self.result == '':
            if self.f_number != '' and self.sign != '':
                self.pressresult()
                self.f_number = self.display_number
                self.sign = '+'
                self.s_number = ''
                self.result = ''
                self.display_number = ''
            elif self.s_number == '':
                self.sign = '+'
                self.f_number = self.display_number
                self.display_number = ''
        else:
            if self.f_number != '' and self.s_number != '' and self.sign != '':
                self.f_number = self.display_number
                self.sign = '+'
                self.s_number = ''
                self.result = ''
                self.display_number = ''


    def pressminus(self):
        if self.result == '':
            if self.f_number != '' and self.sign != '':
                self.pressresult()
                self.f_number = self.display_number
                self.sign = '-'
                self.s_number = ''
                self.result = ''
                self.display_number = ''
            elif self.s_number == '':
                self.sign = '-'
                self.f_number = self.display_number
                self.display_number = ''
        else:
            if self.f_number != '' and self.s_number != '' and self.sign != '':
                self.f_number = self.display_number
                self.sign = '-'
                self.s_number = ''
                self.result = ''
                self.display_number = ''

    def presstimes(self):
        if self.result == '':
            if self.f_number != '' and self.sign != '':
                self.pressresult()
                self.f_number = self.display_number
                self.sign = '*'
                self.s_number = ''
                self.result = ''
                self.display_number = ''
            elif self.s_number == '':
                self.sign = '*'
                self.f_number = self.display_number
                self.display_number = ''
        else:
            if self.f_number != '' and self.s_number != '' and self.sign != '':
                self.f_number = self.display_number
                self.sign = '*'
                self.s_number = ''
                self.result = ''
                self.display_number = ''

    def pressdivide(self):
        if self.result == '':
            if self.f_number != '' and self.sign != '':
                self.pressresult()
                self.f_number = self.display_number
                self.sign = '/'
                self.s_number = ''
                self.result = ''
                self.display_number = ''
            elif self.s_number == '':
                self.sign = '/'
                self.f_number = self.display_number
                self.display_number = ''
        else:
            if self.f_number != '' and self.s_number != '' and self.sign != '':
                self.f_number = self.display_number
                self.sign = '/'
                self.s_number = ''
                self.result = ''
                self.display_number = ''

    def pressresult(self):
        res = self.calculate()
        self.result = self.intflo(res)
        self.display_number = self.result
        self.textBrowser.setText(self.display_number)


    def calculate(self):
        if self.s_number == '':
            self.s_number = self.display_number
            result = eval(str(float(self.f_number)) + self.sign + self.s_number)
            self.f_number = result
        else:
            result = eval(str(float(self.f_number)) + self.sign + self.s_number)
            self.f_number = result
        return result

    def intflo(self,check):
        if check.is_integer():
            result = str(int(check))
        elif check.is_integer() == False:
            result = str(check)
        else:
            result = 'ERROR'
        return result

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

