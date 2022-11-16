# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'theme_buttons.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_theory(object):
    def setupUi(self, theory):
        theory.setObjectName("theory")
        theory.resize(1000, 600)
        theory.setStyleSheet("")
        self.theme_buttons = QtWidgets.QFrame(theory)
        self.theme_buttons.setGeometry(QtCore.QRect(-1, 19, 1001, 581))
        self.theme_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.theme_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.theme_buttons.setObjectName("theme_buttons")
        self.th_first = QtWidgets.QPushButton(self.theme_buttons)
        self.th_first.setGeometry(QtCore.QRect(120, 230, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.th_first.setFont(font)
        self.th_first.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(157, 118, 90);")
        self.th_first.setObjectName("th_first")
        self.th_second = QtWidgets.QPushButton(self.theme_buttons)
        self.th_second.setGeometry(QtCore.QRect(110, 510, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.th_second.setFont(font)
        self.th_second.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(157, 118, 90);")
        self.th_second.setObjectName("th_second")
        self.th_third = QtWidgets.QPushButton(self.theme_buttons)
        self.th_third.setGeometry(QtCore.QRect(720, 230, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.th_third.setFont(font)
        self.th_third.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(157, 118, 90);")
        self.th_third.setObjectName("th_third")
        self.th_forth = QtWidgets.QPushButton(self.theme_buttons)
        self.th_forth.setGeometry(QtCore.QRect(720, 510, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.th_forth.setFont(font)
        self.th_forth.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(157, 118, 90);")
        self.th_forth.setObjectName("th_forth")
        self.th_img_1 = QtWidgets.QLabel(self.theme_buttons)
        self.th_img_1.setGeometry(QtCore.QRect(40, 20, 341, 201))
        self.th_img_1.setText("")
        self.th_img_1.setPixmap(QtGui.QPixmap("img/eniac.png"))
        self.th_img_1.setObjectName("th_img_1")
        self.th_img_2 = QtWidgets.QLabel(self.theme_buttons)
        self.th_img_2.setGeometry(QtCore.QRect(30, 300, 341, 201))
        self.th_img_2.setText("")
        self.th_img_2.setPixmap(QtGui.QPixmap("img/eniac.png"))
        self.th_img_2.setObjectName("th_img_2")
        self.th_img_3 = QtWidgets.QLabel(self.theme_buttons)
        self.th_img_3.setGeometry(QtCore.QRect(630, 20, 341, 201))
        self.th_img_3.setText("")
        self.th_img_3.setPixmap(QtGui.QPixmap("img/eniac.png"))
        self.th_img_3.setObjectName("th_img_3")
        self.th_img_4 = QtWidgets.QLabel(self.theme_buttons)
        self.th_img_4.setGeometry(QtCore.QRect(630, 300, 341, 201))
        self.th_img_4.setText("")
        self.th_img_4.setPixmap(QtGui.QPixmap("img/eniac.png"))
        self.th_img_4.setObjectName("th_img_4")

        self.retranslateUi(theory)
        QtCore.QMetaObject.connectSlotsByName(theory)

    def retranslateUi(self, theory):
        _translate = QtCore.QCoreApplication.translate
        theory.setWindowTitle(_translate("theory", "От абака до суперкомпьютера"))
        self.th_first.setText(_translate("theory", "Первое поколение"))
        self.th_second.setText(_translate("theory", "Второе поколение"))
        self.th_third.setText(_translate("theory", "Третье поколение"))
        self.th_forth.setText(_translate("theory", "Четвертое поколение"))
