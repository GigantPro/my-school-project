from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_MainWindow(QMainWindow):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(928, 600)
        Window.setMinimumSize(QtCore.QSize(0, 600))
        self.centralwidget = QtWidgets.QWidget(Window)
        self.centralwidget.setObjectName("centralwidget")
        self.main_menu = QtWidgets.QFrame(self.centralwidget)
        self.main_menu.setGeometry(QtCore.QRect(-1, -1, 931, 601))
        self.main_menu.setStyleSheet("background-color: rgb(133, 133, 99);")
        self.main_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_menu.setObjectName("main_menu")
        self.Selector_years = QtWidgets.QSlider(self.main_menu)
        self.Selector_years.setGeometry(QtCore.QRect(10, 290, 900, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Selector_years.sizePolicy().hasHeightForWidth())
        self.Selector_years.setSizePolicy(sizePolicy)
        self.Selector_years.setMinimumSize(QtCore.QSize(0, 0))
        self.Selector_years.setMouseTracking(False)
        self.Selector_years.setFocusPolicy(QtCore.Qt.TabFocus)
        self.Selector_years.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.Selector_years.setStatusTip("")
        self.Selector_years.setMaximum(1000)
        self.Selector_years.setProperty("value", 0)
        self.Selector_years.setTracking(True)
        self.Selector_years.setOrientation(QtCore.Qt.Horizontal)
        self.Selector_years.setInvertedAppearance(False)
        self.Selector_years.setInvertedControls(False)
        self.Selector_years.setObjectName("Selector_years")
        self.Project_Name = QtWidgets.QLabel(self.main_menu)
        self.Project_Name.setEnabled(True)
        self.Project_Name.setGeometry(QtCore.QRect(230, 10, 461, 91))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(24)
        font.setBold(False)
        self.Project_Name.setFont(font)
        self.Project_Name.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.Project_Name.setObjectName("Project_Name")
        self.Learn = QtWidgets.QPushButton(self.main_menu)
        self.Learn.setGeometry(QtCore.QRect(800, 350, 111, 41))
        self.Learn.setStyleSheet("background-color: rgb(72, 72, 72);\n"
"color: rgb(255, 255, 255);")
        self.Learn.setObjectName("Learn")
        self.Exit = QtWidgets.QPushButton(self.main_menu)
        self.Exit.setGeometry(QtCore.QRect(10, 570, 81, 21))
        self.Exit.setStyleSheet("background-color: rgb(72, 72, 72);\n"
"color: rgb(255, 255, 255);")
        self.Exit.setObjectName("Exit")
        Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "От абака до суперкомпьютера"))
        self.Project_Name.setText(_translate("Window", "От абака до суперкомпьютера"))
        self.Learn.setText(_translate("Window", "Изучить"))
        self.Exit.setText(_translate("Window", "Выход"))





class Example(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())