import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_theory(object):
    def setupUi(self, theory):
        theory.setObjectName("theory")
        theory.resize(1000, 600)
        theory.setStyleSheet("background-color: rgb(255, 240, 230);")
        self.theme_buttons = QtWidgets.QFrame(theory)
        self.theme_buttons.setGeometry(QtCore.QRect(-1, 19, 1001, 581))
        self.theme_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.theme_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.theme_buttons.setObjectName("theme_buttons")
        self.first = QtWidgets.QPushButton(self.theme_buttons)
        self.first.setGeometry(QtCore.QRect(180, 250, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.first.setFont(font)
        self.first.setStyleSheet("background-color: rgb(189, 171, 130);\n"
"selection-color: rgb(255, 244, 221);")
        self.first.setObjectName("first")
        self.second = QtWidgets.QPushButton(self.theme_buttons)
        self.second.setGeometry(QtCore.QRect(340, 250, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.second.setFont(font)
        self.second.setStyleSheet("background-color: rgb(189, 171, 130);\n"
"selection-color: rgb(255, 244, 221);")
        self.second.setObjectName("second")
        self.third = QtWidgets.QPushButton(self.theme_buttons)
        self.third.setGeometry(QtCore.QRect(500, 250, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.third.setFont(font)
        self.third.setStyleSheet("background-color: rgb(189, 171, 130);\n"
"selection-color: rgb(255, 244, 221);")
        self.third.setObjectName("third")
        self.forth = QtWidgets.QPushButton(self.theme_buttons)
        self.forth.setGeometry(QtCore.QRect(660, 250, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.forth.setFont(font)
        self.forth.setStyleSheet("background-color: rgb(189, 171, 130);\n"
"selection-color: rgb(255, 244, 221);")
        self.forth.setObjectName("forth")

        self.retranslateUi(theory)
        QtCore.QMetaObject.connectSlotsByName(theory)

    def retranslateUi(self, theory):
        _translate = QtCore.QCoreApplication.translate
        theory.setWindowTitle(_translate("theory", "От абака до суперкомпьютера"))
        self.first.setText(_translate("theory", "Первое поколение"))
        self.second.setText(_translate("theory", "Второе поколение"))
        self.third.setText(_translate("theory", "Третье поколение"))
        self.forth.setText(_translate("theory", "Четвертое поколение"))




class Example(Ui_theory, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.first.clicked.connect(self.a)

    
    def a(self):
        self.theme_buttons.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())