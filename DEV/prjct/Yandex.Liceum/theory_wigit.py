# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'theory_wigit.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 600)
        self.main_wiget_theory = QtWidgets.QFrame(Form)
        self.main_wiget_theory.setGeometry(QtCore.QRect(0, 20, 1001, 581))
        self.main_wiget_theory.setStyleSheet("background-color: rgb(194, 168, 150);\n"
"")
        self.main_wiget_theory.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_wiget_theory.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_wiget_theory.setObjectName("main_wiget_theory")
        self.m_text_theory = QtWidgets.QLabel(self.main_wiget_theory)
        self.m_text_theory.setGeometry(QtCore.QRect(120, 270, 771, 141))
        self.m_text_theory.setStyleSheet("")
        self.m_text_theory.setObjectName("m_text_theory")
        self.m_img = QtWidgets.QLabel(self.main_wiget_theory)
        self.m_img.setGeometry(QtCore.QRect(276, 49, 431, 211))
        self.m_img.setText("")
        self.m_img.setObjectName("m_img")
        self.m_split_slider = QtWidgets.QSlider(self.main_wiget_theory)
        self.m_split_slider.setGeometry(QtCore.QRect(89, 500, 831, 22))
        self.m_split_slider.setStyleSheet("")
        self.m_split_slider.setOrientation(QtCore.Qt.Horizontal)
        self.m_split_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.m_split_slider.setTickInterval(1)
        self.m_split_slider.setObjectName("m_split_slider")
        self.m_all_page = QtWidgets.QLabel(self.main_wiget_theory)
        self.m_all_page.setGeometry(QtCore.QRect(500, 520, 47, 16))
        self.m_all_page.setObjectName("m_all_page")
        self.pushButton = QtWidgets.QPushButton(self.main_wiget_theory)
        self.pushButton.setGeometry(QtCore.QRect(40, 495, 31, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.main_wiget_theory)
        self.pushButton_2.setGeometry(QtCore.QRect(930, 495, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.m_page = QtWidgets.QLineEdit(self.main_wiget_theory)
        self.m_page.setGeometry(QtCore.QRect(470, 520, 21, 20))
        self.m_page.setObjectName("m_page")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.m_text_theory.setText(_translate("Form", "Теория"))
        self.m_all_page.setText(_translate("Form", "TextLabel"))
        self.pushButton.setText(_translate("Form", "<-"))
        self.pushButton_2.setText(_translate("Form", "->"))
