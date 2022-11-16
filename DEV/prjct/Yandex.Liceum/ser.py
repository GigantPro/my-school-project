import sys, ctypes
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.showMaximized()
        # self.WindowWidth = ctypes.windll.user32.GetSystemMetrics(0)
        # self.WindowHeight = ctypes.windll.user32.GetSystemMetrics(1)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_home = QtWidgets.QWidget(self.centralwidget)
        self.widget_home.setEnabled(True)
        self.widget_home.setGeometry(QtCore.QRect(0, 30, 1920, 1050))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_home.sizePolicy().hasHeightForWidth())
        self.widget_home.setSizePolicy(sizePolicy)
        self.widget_home.setStyleSheet("background: #999880")
        self.widget_home.setObjectName("widget_home")
        self.widget_tasks = QtWidgets.QWidget(self.widget_home)
        self.widget_tasks.setGeometry(QtCore.QRect(0, 0, 191, 1051))
        self.widget_tasks.setStyleSheet("background-color: #ddeff0")
        self.widget_tasks.setObjectName("widget_tasks")
        self.widget_display_tasks = QtWidgets.QWidget(self.widget_home)
        self.widget_display_tasks.setGeometry(QtCore.QRect(230, 20, 1651, 921))
        self.widget_display_tasks.setStyleSheet("background-color: #abdae0;")
        self.widget_display_tasks.setObjectName("widget_display_tasks")


        self.widget_tools = QtWidgets.QWidget(self.centralwidget)
        self.widget_tools.setGeometry(QtCore.QRect(0, -40, 1921, 71))
        self.widget_tools.setStyleSheet("background-color: #000000;")
        self.widget_tools.setObjectName("widget_tools")
        self.Button_home = QtWidgets.QPushButton(self.widget_tools)
        self.Button_home.setGeometry(QtCore.QRect(0, 40, 121, 31))
        self.Button_home.setStyleSheet("background-color: #808080;" "border: none")
        self.Button_home.setObjectName("Button_home")
        self.Button_profil = QtWidgets.QPushButton(self.widget_tools)
        self.Button_profil.setGeometry(QtCore.QRect(1771, 40, 151, 32))
        self.Button_profil.setAutoFillBackground(False)
        self.Button_profil.setStyleSheet("background-color: #808080;" "border: none")
        self.Button_profil.setIconSize(QtCore.QSize(32, 32))
        self.Button_profil.setObjectName("Button_profil")
        MainWindow.setCentralWidget(self.centralwidget)

        self.textBrowser = QtWidgets.QTextBrowser(self.widget_display_tasks)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QtCore.QRect(70, 60, 1451, 661))
        self.textBrowser.setStyleSheet("border: none")
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textBrowser.setFont(font)
        self.Button_answer = QtWidgets.QPushButton(self.widget_display_tasks)
        self.Button_answer.setObjectName('Button_answer')
        self.Button_answer.setGeometry(QtCore.QRect(70, 830, 200, 40))
        self.Button_answer.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Button_answer.setText('Ответить')
        self.textEdit_answer = QtWidgets.QTextEdit(self.widget_display_tasks)
        self.textEdit_answer.setObjectName(u"textEdit")
        self.textEdit_answer.setGeometry(QtCore.QRect(70, 700, 1200, 120))
        self.textEdit_answer.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.textEdit_answer.setFont(font)
        self.profil_pageUi(MainWindow)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Практикум"))
        self.Button_home.setText(_translate("MainWindow", "Главная"))
        self.Button_profil.setText(_translate("MainWindow", "Профиль"))
        self.Button_teacher.setText(_translate("MainWindow", "Режим учителя"))
        self.Buttonstudent.setText(_translate("MainWindow", "Режим ученика"))

    def profil_pageUi(self, MainWindow):
        self.widget_profil = QtWidgets.QWidget(self.centralwidget)
        self.widget_profil.setGeometry(QtCore.QRect(0, 30, 1920, 1080))
        self.widget_profil.setObjectName("widget_profil")
        self.Button_teacher = QtWidgets.QPushButton(self.widget_profil)
        self.Button_teacher.setGeometry(QtCore.QRect(140, 150, 100, 23))
        self.Button_teacher.setObjectName("Button_teacher")
        self.Buttonstudent = QtWidgets.QPushButton(self.widget_profil)
        self.Buttonstudent.setGeometry(QtCore.QRect(140, 190, 100, 23))
        self.Buttonstudent.setObjectName("Buttonstudent")
        self.label = QtWidgets.QLabel(self.widget_profil)
        self.label.setGeometry(QtCore.QRect(190, 250, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.widget_profil.hide()


class Ui_TeacherWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.task_text = QtWidgets.QTextEdit(self.centralwidget)
        self.task_text.setGeometry(QtCore.QRect(290, 40, 461, 241))
        self.task_text.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 10, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Button_add_theme = QtWidgets.QPushButton(self.centralwidget)
        self.Button_add_theme.setGeometry(QtCore.QRect(10, 70, 261, 23))
        self.Button_add_theme.setObjectName("Button_addtheme")
        self.Button_delete_theme = QtWidgets.QPushButton(self.centralwidget)
        self.Button_delete_theme.setGeometry(QtCore.QRect(10, 180, 101, 23))
        self.Button_delete_theme.setObjectName("Button_deletetheme")
        self.Button_save_task = QtWidgets.QPushButton(self.centralwidget)
        self.Button_save_task.setGeometry(QtCore.QRect(280, 560, 461, 23))
        self.Button_save_task.setObjectName("Button_savetask")
        self.Button_add_image = QtWidgets.QPushButton(self.centralwidget)
        self.Button_add_image.setGeometry(QtCore.QRect(290, 290, 231, 23))
        self.Button_add_image.setObjectName("Button_addimage")
        self.lineEdit_task_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_task_name.setGeometry(QtCore.QRect(280, 535, 461, 20))
        self.lineEdit_task_name.setObjectName("lineEdit_taskname")
        self.Button_delete_task = QtWidgets.QPushButton(self.centralwidget)
        self.Button_delete_task.setGeometry(QtCore.QRect(130, 180, 101, 23))
        self.Button_delete_task.setObjectName("Button_deletetask")
        self.combobox_task = QtWidgets.QComboBox(self.centralwidget)
        self.combobox_task.setGeometry(QtCore.QRect(130, 210, 101, 22))
        self.combobox_task.setObjectName("combobox_deletetask")
        self.combobox_theme = QtWidgets.QComboBox(self.centralwidget)
        self.combobox_theme.setGeometry(QtCore.QRect(10, 210, 101, 22))
        self.combobox_theme.setObjectName("combobox_deletetheme")
        self.comboBox_choosetheme = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_choosetheme.setObjectName(u"comboBox_choosetheme")
        self.comboBox_choosetheme.setGeometry(QtCore.QRect(290, 360, 461, 22))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 515, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_themename = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_themename.setGeometry(QtCore.QRect(10, 40, 261, 20))
        self.lineEdit_themename.setObjectName("lineEdit_themename")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 390, 250, 13))
        self.label_3.setObjectName("label_3")
        self.lineEdit_answers = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_answers.setGeometry(QtCore.QRect(290, 440, 221, 20))
        self.lineEdit_answers.setObjectName("lineEdit_answers")
        self.lineEdit_correct_answer = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_correct_answer.setGeometry(QtCore.QRect(540, 440, 221, 20))
        self.lineEdit_correct_answer.setObjectName("lineEdit_correctanswer")
        self.Button_add_answers = QtWidgets.QPushButton(self.centralwidget)
        self.Button_add_answers.setGeometry(QtCore.QRect(290, 410, 151, 23))
        self.Button_add_answers.setObjectName("Button_addanswers")
        self.Button_add_correct_answer = QtWidgets.QPushButton(self.centralwidget)
        self.Button_add_correct_answer.setGeometry(QtCore.QRect(540, 410, 151, 23))
        self.Button_add_correct_answer.setObjectName("Button_addcorrectanswer")
        self.Button_del_correct_answer = QtWidgets.QPushButton(self.centralwidget)
        self.Button_del_correct_answer.setGeometry(QtCore.QRect(690, 410, 71, 23))
        self.Button_del_correct_answer.setObjectName("Button_delcorrectanswer")
        self.Button_del_answers = QtWidgets.QPushButton(self.centralwidget)
        self.Button_del_answers.setGeometry(QtCore.QRect(440, 410, 71, 23))
        self.Button_del_answers.setObjectName("Button_delanswers")
        self.comboBox_answers = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_answers.setGeometry(QtCore.QRect(290, 460, 221, 22))
        self.comboBox_answers.setObjectName("comboBox_answers")
        self.comboBox_correct_answer = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_correct_answer.setGeometry(QtCore.QRect(540, 460, 221, 22))
        self.comboBox_correct_answer.setObjectName("comboBox_correctanswer")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Изменить задачи"))
        self.label.setText(_translate("MainWindow", "Введите условие задачи"))
        self.Button_add_theme.setText(_translate("MainWindow", "Добавить тему"))
        self.Button_delete_theme.setText(_translate("MainWindow", "Удалить тему"))
        self.Button_save_task.setText(_translate("MainWindow", "Добавить задачу"))
        self.Button_add_image.setText(_translate("MainWindow", "Добавить картинку"))
        self.Button_delete_task.setText(_translate("MainWindow", "Удалить задачу"))
        self.label_2.setText(_translate("MainWindow", "Название задачи"))
        self.label_3.setText(_translate("MainWindow", "Ответы к задачам"))
        self.Button_add_answers.setText(_translate("MainWindow", "Добавить вариант ответа"))
        self.Button_add_correct_answer.setText(_translate("MainWindow", "Добавить правильный овет"))
        self.Button_del_correct_answer.setText(_translate("MainWindow", "удалить"))
        self.Button_del_answers.setText(_translate("MainWindow", "удалить"))

   



class DB:
    def __init__(self, base_name: str='practicum.db') -> None:
        self.base = sqlite3.connect(base_name, check_same_thread=False)
        self.cur = self.base.cursor()
        if not self.base:
            raise ConnectionError('Error to connection DB')

    def create_table(self, name: str, *arg) -> None:
        self.base.execute('CREATE TABLE IF NOT EXISTS {}({})'.format(name, ', '.join(arg)))
        self.base.commit()
    
    def add_value(self, tabel_name: str, *values) -> None:  #!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.cur.execute('INSERT INTO {} VALUES({})'.format(tabel_name, ', '.join(['?' for _ in range(len(values))])), tuple(values))
        self.base.commit()

    def read_all_from_table(self, tabel_name: str) -> list:
        return self.base.execute(f"SELECT * FROM {tabel_name}").fetchall()

    def read_line(self, tabel_name: str, colum_name: str, value: str):
        return self.base.execute("SELECT * FROM {} WHERE {} == ?".format(tabel_name, colum_name), (value,)).fetchone()

    def read_lines(self, tabel_name: str, colum_name: str, value: str):
        return self.base.execute("SELECT * FROM {} WHERE {} == ?".format(tabel_name, colum_name), (value,)).fetchall()
    
    def update_value(self, tabel_name: str, flag_value: str, colum_flag_name: str, new_value: str, colum_new_name: str) -> None:
        self.cur.execute('UPDATE {} SET {} == ? WHERE {} == ?'.format(tabel_name, colum_new_name, colum_flag_name), (new_value, flag_value))
        self.base.commit()

    def delete_line(self, table_name: str, flag_colum_name: str, flag_value: str) -> None:
        self.cur.execute('DELETE FROM {} WHERE {} == ?'.format(table_name, flag_colum_name), (flag_value,))
        self.base.commit()


class Edit_Window(Ui_TeacherWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    

class Main_Window(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        DB().create_table('practicum', *('idtask INTEGER PRIMARY KEY', 'theme_name', 'task_name', 'text', 'answers', 'correct_answer'))
        self.Button_home.clicked.connect(self.show_home)
        self.Button_profil.clicked.connect(self.show_profil)
        self.Button_teacher.clicked.connect(self.edit_window)
    
    def show_home(self):
        self.widget_profil.hide()
        self.widget_home.show()
    
    def show_profil(self):
        self.widget_home.hide()
        self.widget_profil.show()
    
    def edit_window(self):
        global edit_window
        edit_window = Edit_Window()
        edit_window.show()
    
       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main_window = Main_Window()
    Main_window.show()
    sys.exit(app.exec())