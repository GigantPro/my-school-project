import json
import math
import sys
import sqlite3
from PyQt5.QtGui import QFontDatabase, QFont
import hashlib
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

   
ch_flag = False
app = None

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        
        #theory_wigit
        self.main_wiget_theory = QtWidgets.QFrame(MainWindow)
        self.main_wiget_theory.setGeometry(QtCore.QRect(0, 20, 1000, 580))
        self.main_wiget_theory.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_wiget_theory.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_wiget_theory.setObjectName("main_wiget_theory")
        
        self.m_text_theory = QtWidgets.QLabel(self.main_wiget_theory)
        self.m_text_theory.setGeometry(QtCore.QRect(120, 270, 820, 140))
        self.m_text_theory.setObjectName("m_text_theory")
        
        self.m_img = QtWidgets.QLabel(self.main_wiget_theory)
        self.m_img.setGeometry(QtCore.QRect(15, 9, 970, 240))
        self.m_img.setObjectName("m_img")
        
        self.m_split_slider = QtWidgets.QSlider(self.main_wiget_theory)
        self.m_split_slider.setGeometry(QtCore.QRect(90, 500, 830, 20))
        self.m_split_slider.setOrientation(QtCore.Qt.Horizontal)
        self.m_split_slider.setObjectName("m_split_slider")

        #m
        self.m_page = QtWidgets.QLineEdit(self.main_wiget_theory)
        self.m_page.setGeometry(QtCore.QRect(477, 523, 25, 15))
        self.m_page.setObjectName("m_page")
        self.m_l_change = QtWidgets.QPushButton(self.main_wiget_theory)
        self.m_l_change.setGeometry(QtCore.QRect(40, 495, 31, 23))
        self.m_l_change.setObjectName("m_right_change")
        self.m_r_change = QtWidgets.QPushButton(self.main_wiget_theory)
        self.m_r_change.setGeometry(QtCore.QRect(930, 495, 31, 23))
        self.m_r_change.setObjectName("m_left_change")
        self.m_all_page = QtWidgets.QLabel(self.main_wiget_theory)
        self.m_all_page.setGeometry(QtCore.QRect(500, 523, 47, 16))
        self.m_all_page.setObjectName("m_all_page")
        

        #theme_buttons 
        self.theme_buttons = QtWidgets.QFrame(MainWindow)
        self.theme_buttons.setGeometry(QtCore.QRect(0, 27, 1000, 600))
        self.theme_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.theme_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.theme_buttons.setObjectName("theme_buttons")
        
        self.th_zero = QtWidgets.QPushButton(self.theme_buttons)
        self.th_zero.setGeometry(QtCore.QRect(60, 250, 160 , 50))
        self.th_zero.setObjectName("th_zero")
        
        self.th_first = QtWidgets.QPushButton(self.theme_buttons)
        self.th_first.setGeometry(QtCore.QRect(230, 250, 160 , 50))
        self.th_first.setObjectName("th_first")
        
        self.th_second = QtWidgets.QPushButton(self.theme_buttons)
        self.th_second.setGeometry(QtCore.QRect(410, 250, 161, 50))
        self.th_second.setObjectName("th_second")
        
        self.th_third = QtWidgets.QPushButton(self.theme_buttons)
        self.th_third.setGeometry(QtCore.QRect(590, 250, 160, 50))
        self.th_third.setObjectName("th_third")
        
        self.th_forth = QtWidgets.QPushButton(self.theme_buttons)
        self.th_forth.setGeometry(QtCore.QRect(770, 250, 160, 50))
        self.th_forth.setObjectName("th_forth")
        
        self.th_name = QtWidgets.QLabel(self.theme_buttons)
        self.th_name.setGeometry(QtCore.QRect(420, 40, 150, 50))
        self.th_name.setObjectName("th_name")
        
        MainWindow.setCentralWidget(self.theme_buttons)

        #blind
        self.blind = QtWidgets.QWidget(MainWindow)
        self.blind.setGeometry(QtCore.QRect(0, 0, 1000, 27))
        self.blind.setObjectName("blind")
        
        self.b_theory_button = QtWidgets.QPushButton(self.blind)
        self.b_theory_button.setGeometry(QtCore.QRect(5, 1, 75, 25))
        self.b_theory_button.setObjectName("b_theory_button")
        
        self.b_accaunt_button = QtWidgets.QPushButton(self.blind)
        self.b_accaunt_button.setGeometry(QtCore.QRect(920, 1, 75, 25))
        self.b_accaunt_button.setObjectName("b_accaunt_button")
        
        self.b_test_button = QtWidgets.QPushButton(self.blind)
        self.b_test_button.setGeometry(QtCore.QRect(90, 1, 75, 25))
        self.b_test_button.setObjectName("b_test_button")
        
        self.b_change_color = QtWidgets.QPushButton(self.blind)
        self.b_change_color.setGeometry(QtCore.QRect(750, 1, 150, 25))
        self.b_change_color.setObjectName("b_change_color")

        #accaunt_wigit
        self.accaunt_wigit = QtWidgets.QFrame(MainWindow)
        self.accaunt_wigit.setGeometry(QtCore.QRect(0, 27, 1000, 600))
        self.accaunt_wigit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.accaunt_wigit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.accaunt_wigit.setObjectName("accaunt_wigit")
        
        self.ac_accaunt_name = QtWidgets.QLabel(self.accaunt_wigit)
        self.ac_accaunt_name.setGeometry(QtCore.QRect(10, 17, 991, 31))
        self.ac_accaunt_name.setObjectName("ac_accaunt_name")
        self.ac_history_label = QtWidgets.QLabel(self.accaunt_wigit)
        self.ac_history_label.setGeometry(QtCore.QRect(475, 17, 440, 40))
        self.ac_history_label.setObjectName("ac_history_label")
        
        self.ac_login = QtWidgets.QPushButton(self.accaunt_wigit)
        self.ac_login.setGeometry(QtCore.QRect(10, 55, 120, 23))
        self.ac_login.setObjectName("ac_login")
        
        self.ac_registr = QtWidgets.QPushButton(self.accaunt_wigit)
        self.ac_registr.setGeometry(QtCore.QRect(10, 85, 120, 23))
        self.ac_registr.setObjectName("ac_registr")
        
        self.ac_view_balls = QtWidgets.QLabel(self.accaunt_wigit)
        self.ac_view_balls.setGeometry(QtCore.QRect(6, 502, 601, 61))
        self.ac_view_balls.setObjectName("ac_view_balls")
        
        self.ac_histiry_results = QtWidgets.QListWidget(self.accaunt_wigit)
        self.ac_histiry_results.setGeometry(QtCore.QRect(475, 70, 451, 461))
        self.ac_histiry_results.setObjectName("ac_histiry_results")
        
        #test_wigit_theme
        self.test_theme_get = QtWidgets.QFrame(MainWindow)
        self.test_theme_get.setGeometry(QtCore.QRect(0, 27, 1000, 600))
        self.test_theme_get.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.test_theme_get.setFrameShadow(QtWidgets.QFrame.Raised)
        self.test_theme_get.setObjectName("test_theme_get")
        
        self.te_zero = QtWidgets.QPushButton(self.test_theme_get)
        self.te_zero.setGeometry(QtCore.QRect(60, 250, 160 , 50))
        self.te_zero.setObjectName("te_zero")
        
        self.te_first = QtWidgets.QPushButton(self.test_theme_get)
        self.te_first.setGeometry(QtCore.QRect(230, 250, 160, 50))
        self.te_first.setObjectName("te_first")
        
        self.te_second = QtWidgets.QPushButton(self.test_theme_get)
        self.te_second.setGeometry(QtCore.QRect(410, 250, 160, 50))
        self.te_second.setObjectName("te_second")
        
        self.te_third = QtWidgets.QPushButton(self.test_theme_get)
        self.te_third.setGeometry(QtCore.QRect(590, 250, 160, 50))
        self.te_third.setObjectName("te_third")
        
        self.te_forth = QtWidgets.QPushButton(self.test_theme_get)
        self.te_forth.setGeometry(QtCore.QRect(770, 250, 160, 50))
        self.te_forth.setObjectName("te_forth")
        
        self.te_name = QtWidgets.QLabel(self.test_theme_get)
        self.te_name.setGeometry(QtCore.QRect(420, 40, 150, 50))
        self.te_name.setObjectName('te_name')
        
        #test_wigit_answers
        self.test_wigit_answers = QtWidgets.QFrame(MainWindow)
        self.test_wigit_answers.setGeometry(QtCore.QRect(0, 27, 1000, 600))
        self.test_wigit_answers.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.test_wigit_answers.setFrameShadow(QtWidgets.QFrame.Raised)
        self.test_wigit_answers.setObjectName("test_wigit_answers")
        self.ta_question = QtWidgets.QLabel(self.test_wigit_answers)
        self.ta_question.setGeometry(QtCore.QRect(150, 30, 730, 220))
        self.ta_question.setObjectName("ta_answer")
        self.ta_progress = QtWidgets.QProgressBar(self.test_wigit_answers)
        self.ta_progress.setGeometry(QtCore.QRect(50, 530, 920, 25))
        self.ta_progress.setProperty("value", 0)
        self.ta_progress.setObjectName("ta_progress")
        self.ta_fst_answ = QtWidgets.QCheckBox(self.test_wigit_answers)
        self.ta_fst_answ.setGeometry(QtCore.QRect(200, 310, 360, 20))
        self.ta_fst_answ.setObjectName("ta_fst_answ")
        self.ta_sec_answ = QtWidgets.QCheckBox(self.test_wigit_answers)
        self.ta_sec_answ.setGeometry(QtCore.QRect(200, 370, 360, 20))
        self.ta_sec_answ.setObjectName("ta_sec_answ")
        self.ta_third_answ = QtWidgets.QCheckBox(self.test_wigit_answers)
        self.ta_third_answ.setGeometry(QtCore.QRect(560, 310, 400, 20))
        self.ta_third_answ.setObjectName("ta_third_answ")
        self.ta_forth_answ = QtWidgets.QCheckBox(self.test_wigit_answers)
        self.ta_forth_answ.setGeometry(QtCore.QRect(560, 370, 400, 20))
        self.ta_forth_answ.setObjectName("ta_forth_answ")
        self.ta_answ = QtWidgets.QPushButton(self.test_wigit_answers)
        self.ta_answ.setGeometry(QtCore.QRect(350, 430, 75, 30))
        self.ta_answ.setObjectName("ta_answ")

        #-----------------------------------------------------------------------------------
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "От абака до суперкомпьютера"))


        #theme_buttons
        self.th_zero.setText(_translate("MainWindow", "Механическое поколение"))
        self.th_first.setText(_translate("MainWindow", "Первое поколение"))
        self.th_second.setText(_translate("MainWindow", "Второе поколение"))
        self.th_third.setText(_translate("MainWindow", "Третье поколение"))
        self.th_forth.setText(_translate("MainWindow", "Четвертое поколение"))
        
        self.th_name.setText(_translate("MainWindow", "<b>Теория</b>"))
        self.m_all_page.setText(_translate("MainWindow", "TextLabel"))
        self.m_l_change.setText(_translate("MainWindow", "<--"))
        self.m_r_change.setText(_translate("MainWindow", "-->"))

        #blind
        self.b_theory_button.setText(_translate("MainWindow", "Теория"))
        self.b_accaunt_button.setText(_translate("MainWindow", "Аккаунт"))
        self.b_test_button.setText(_translate("MainWindow", "Тесты"))
        self.b_change_color.setText(_translate("MainWindow", "Сменить расцветку"))

        #theory_wigit
        self.m_text_theory.setText(_translate("MainWindow", "Теория"))

        #accaunt_wigit
        self.ac_accaunt_name.setText(_translate("MainWindow", "Не зарегистрирован"))
        self.ac_login.setText(_translate("MainWindow", "Войти"))
        self.ac_registr.setText(_translate("MainWindow", "Зарегистрироваться"))
        self.ac_view_balls.setText(_translate("MainWindow", "Полученно баллов 10/1000"))
        self.ac_history_label.setText(_translate("MainWindow", "Последние результаты (только с аккаунтом)"))
        
        #test_wigit_theme
        self.te_zero.setText(_translate("MainWindow", "Механическое поколение"))
        self.te_first.setText(_translate("MainWindow", "Первое поколение"))
        self.te_second.setText(_translate("MainWindow", "Второе поколение"))
        self.te_third.setText(_translate("MainWindow", "Третье поколение"))
        self.te_forth.setText(_translate("MainWindow", "Четвертое поколение"))
        self.te_name.setText(_translate("MainWindow", "<b>Тест</b>"))
        
        #test_wigit_answers
        self.ta_question.setText(_translate("MainWindow", "TextLabel"))
        self.ta_fst_answ.setText(_translate("MainWindow", "CheckBox"))
        self.ta_sec_answ.setText(_translate("MainWindow", "CheckBox"))
        self.ta_third_answ.setText(_translate("MainWindow", "CheckBox"))
        self.ta_forth_answ.setText(_translate("MainWindow", "CheckBox"))
        self.ta_answ.setText(_translate("MainWindow", "Ответить"))


class DB:
    def __init__(self, base_name: str) -> None:
        self.base = sqlite3.connect(base_name, check_same_thread=False)
        self.cur = self.base.cursor()
        if not self.base:
            raise ConnectionError('Error to connection DB')

    def add_value(self, tabl_n: str, *args) -> None:
        self.cur.execute('INSERT INTO {} VALUES({})'.format(tabl_n, ', '.join(['?' for _ in range(len(args))])), tuple(args))
        self.base.commit()
    
    def create_table(self, name: str, *arg) -> None:
        self.base.execute('CREATE TABLE IF NOT EXISTS {}({})'.format(name, ', '.join(arg)))
        self.base.commit()

    def read_all_from_table(self, tabl_n: str) -> list:
        return self.base.execute(f"SELECT * FROM {tabl_n}").fetchall()

    def get_lines(self, tabl_n: str, colum_name: str, value: str):
        return self.base.execute("SELECT * FROM {} WHERE {} == ?".format(tabl_n, colum_name), (value,)).fetchall()

    def get_line(self, tabl_n: str, colum_name: str, value: str):
        return self.base.execute("SELECT * FROM {} WHERE {} == ?".format(tabl_n, colum_name), (value,)).fetchone()
    
    def delete_line(self, tabl_n: str, fl_colum_name: str, fl_value: str) -> None:
        self.cur.execute('DELETE FROM {} WHERE {} == ?'.format(tabl_n, fl_colum_name), (fl_value,))
        self.base.commit()
    
    def change_value(self, tabl_n: str, fl_value: str, colum_fl_name: str, new_value: str, colum_new_name: str) -> None:
        self.cur.execute('UPDATE {} SET {} == ? WHERE {} == ?'.format(tabl_n, colum_new_name, colum_fl_name), (new_value, fl_value))
        self.base.commit()


class Main_Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.accaunt = None 

        self.db = DB('db.db')
        self.db.create_table('accaunts', 'id INTENGER PRIMARY KEY', 'name', 'pass', 'balls', 'all_balls')
        self.db.create_table('results', 'id INTENGER PRIMARY KEY', 'name', 'type', 'balls', 'max_balls')

        #perem
        self.c_page_chage_code = False

        self.theme_button()

        #Коннект кнопок
        #m
        self.m_r_change.clicked.connect(self.m_change)
        self.m_l_change.clicked.connect(self.m_change)
        self.m_page.setText('1')
        self.m_page.textChanged.connect(self.m_page_change)

        #theme_buttons
        self.th_zero.clicked.connect(self.theme_change)
        self.th_first.clicked.connect(self.theme_change)
        self.th_second.clicked.connect(self.theme_change)
        self.th_third.clicked.connect(self.theme_change)
        self.th_forth.clicked.connect(self.theme_change)

        #blind
        self.b_theory_button.clicked.connect(self.theme_button)
        self.b_test_button.clicked.connect(self.test_wigit_controller)
        self.b_accaunt_button.clicked.connect(self.accaunt_button)
        self.b_change_color.clicked.connect(self.change_color)

        #test_select_theme
        self.te_zero.clicked.connect(self.test_buttons)
        self.te_first.clicked.connect(self.test_buttons)
        self.te_second.clicked.connect(self.test_buttons)
        self.te_third.clicked.connect(self.test_buttons)
        self.te_forth.clicked.connect(self.test_buttons)

        #accaunts
        self.ac_login.clicked.connect(self.login)
        self.ac_registr.clicked.connect(self.registred)
        # self.ac_export_csv.clicked.connect(self.export_results)
        
        #Fonts init
        fontId = QFontDatabase.addApplicationFont("fonts\RedOctober-Fat.ttf")

        if fontId == 0:
            fontName = QFontDatabase.applicationFontFamilies(fontId)[0]
            self.font = QFont(fontName, 30)
        else:
            self.font = QFont()


    def m_change(self):
        self.c_page_chage_code = True
        if self.sender() == self.m_r_change:
            self.m_split_slider.setValue(self.m_split_slider.value() + 1)
            self.m_page.setText(str(self.m_split_slider.value() + 1))
        elif self.sender() == self.m_l_change:
            self.m_split_slider.setValue(self.m_split_slider.value() - 1)
            self.m_page.setText(str(self.m_split_slider.value() + 1))
      
    def m_page_change(self):
        if self.c_page_chage_code:
            self.c_page_chage_code = False
            return
        if self.m_page.text() == '':
            return
        if len([i for i in self.m_page.text() if i not in '0123456789']) != 0:
            self.m_page.setText(''.join([i for i in self.m_page.text() if i in '0123456789']))
            return
        elif int(self.m_page.text()) > self.m_split_slider.maximum() + 1:
            self.m_page.setText(str(self.m_split_slider.maximum() + 1))
        elif int(self.m_page.text()) <= 0:
            self.m_page.setText('1')

        self.m_split_slider.setValue(int(self.m_page.text()) - 1)

    def theme_button(self):
        self.main_wiget_theory.hide()
        self.accaunt_wigit.hide()
        self.test_wigit_answers.hide()
        self.test_theme_get.hide()

        self.theme_buttons.show()
        self.blind.show()

    def view_theory(self):
        # self._dashes_under_slider()
        self.m_img.setGeometry(QtCore.QRect(15, 10, 970, 240))
        self.m_img.setPixmap(QPixmap())
        self.m_text_theory.setGeometry(QtCore.QRect(120, 270, 820, 140))

        a = str(self.m_split_slider.value() + 1)
        json_ = None
        with open(f"json/theme{self.theme}.json", "r", encoding='utf-8') as file:
            json_ = json.loads(file.read())
        try:
            pixmap = QPixmap(json_[a]['img'])
            if pixmap.width() > self.m_img.width() and pixmap.height() <= self.m_img.height():  # Подгон размеров картинки под label
                otn = pixmap.width() / pixmap.height()
                pixmap = pixmap.scaled(self.m_img.width(),  math.ceil(self.m_img.width() / otn))
            elif pixmap.width() <= self.m_img.width() and pixmap.height() > self.m_img.height():
                otn = pixmap.width() / pixmap.height()
                pixmap = pixmap.scaled(int(self.m_img.height() * otn), self.m_img.height())
            elif pixmap.width() > self.m_img.width() and pixmap.height() > self.m_img.height():
                otn = pixmap.width() / pixmap.height()
                pixmap = pixmap.scaled(self.m_img.width(),  math.ceil(self.m_img.width() / otn))
                if pixmap.width() <= self.m_img.width() and pixmap.height() > self.m_img.height():
                    otn = pixmap.width() / pixmap.height()
                    pixmap = pixmap.scaled( math.ceil(self.m_img.height() * otn), self.m_img.height())
            if pixmap.width() < self.m_img.width() and pixmap.height() < self.m_img.height():
                otn = pixmap.width() / pixmap.height()
                pixmap = pixmap.scaled(int(self.m_img.height() * otn), self.m_img.height())
                if pixmap.width() > self.m_img.width() and pixmap.height() <= self.m_img.height():
                    otn = pixmap.width() / pixmap.height()
                    pixmap = pixmap.scaled(self.m_img.width(),  math.ceil(self.m_img.width() / otn))
            # Задавание пиксмапа
            self.m_img.setPixmap(pixmap)
            x = int((970 / 2) - (pixmap.width()  / 2))  # Чтобы картинка была посередине
            y = int((240 / 2) - (pixmap.height() / 2))
            self.m_img.setGeometry(QtCore.QRect(15 + x, 10 + y, pixmap.width(), pixmap.height()))
        except (TypeError, ZeroDivisionError):
            self.m_text_theory.setGeometry(QtCore.QRect(30, 20, 930, 410))
            self.m_img.setGeometry(QtCore.QRect(0, 0, 0, 0))
    
        self.m_split_slider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.m_split_slider.setTickInterval(1)
        
        # self.c_page_chage_code = True
        self.m_page.setText(str(self.m_split_slider.value() + 1))
        self.m_all_page.setText('/' + str(self.m_split_slider.maximum() + 1))

        self.m_text_theory.setText(str(json_[a]['text']))
        self.m_text_theory.setFont(QtGui.QFont('Times New Roman', 15))
        self.m_text_theory.setWordWrap(True)  # Чтобы текст был с переносами

    def theme_change(self):
        self.theme_buttons.hide()
        self.accaunt_wigit.hide()
        self.test_wigit_answers.hide()
        self.test_theme_get.hide()

        self.main_wiget_theory.show()
        self.blind.show()

        if self.sender() == self.th_zero:
            self.theme = '0'
        elif self.sender() == self.th_first:
            self.theme = '1'
        elif self.sender() == self.th_second:
            self.theme = '2'
        elif self.sender() == self.th_third:
            self.theme = '3'
        elif self.sender() == self.th_forth:
            self.theme = '4'
        
        json_ = None
        with open(f"json/theme{self.theme}.json", "r") as file:
            json_ = json.loads(file.read())

        self.m_split_slider.setValue(0)
        self.m_split_slider.setMaximum(len(json_) - 1)
        self.m_split_slider.setSingleStep(1)
        self.m_split_slider.valueChanged.connect(self.view_theory)
        self.view_theory()

    def test_wigit_controller(self):
        if not self.accaunt:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Упс...")
            dlg.setText(f"Вам нужно войти в свой аккаунт, чтобы решать тесты!")
            dlg.exec()
            return
        self.main_wiget_theory.hide()
        self.accaunt_wigit.hide()
        self.test_wigit_answers.hide()

        self.test_theme_get.show()
        self.blind.show()

    def accaunt_button(self):
        self.theme_buttons.hide()
        self.main_wiget_theory.hide()
        self.test_theme_get.hide()
        
        self.accaunt_wigit.show()
        self.blind.show()

        self.ac_view_balls.clear()
        self.ac_histiry_results.clear()

        if self.accaunt:
            self.ac_accaunt_name.setText(self.accaunt[1])
            results = self.db.get_lines('results', 'name', self.accaunt[1])
            all_balls, your_balls = 0, 0
            for i in results:
                self.ac_histiry_results.addItem(f"{i[2]}: {i[3]}/{i[4]} ({i[3] / i[4] * 100}%)")
                all_balls += i[4]
                your_balls += i[3]
            self.ac_view_balls.setText(f"Полученно баллов {your_balls}/{all_balls} ({int(your_balls / all_balls * 100) if all_balls != 0 else 0}%)")
            self.db.change_value('accaunts', self.accaunt[1], 'name', your_balls, 'balls')
            self.db.change_value('accaunts', self.accaunt[1], 'name', all_balls, 'all_balls')
            # self.ac_export_csv.setEnabled(True)
        else:
            # self.ac_export_csv.setEnabled(False)
            self.ac_accaunt_name.setText("Не зарегистрирован")
            self.ac_view_balls.setText(f"Полученно баллов 0/0")
          
    def display_questions(self):
        self.ta_answ.setText('Ответить')
        questions = None
        with open(f"json/test{self.test_theme}.json", 'r', encoding='utf-8') as file:
            questions = json.loads(file.read())
        self.max_balls = len(questions)
        if int(self.question_now) > len(questions):
            self.end_test()
            return
        self.ta_question.setWordWrap(True)

        self.ta_question.setText(questions[self.question_now]['text'])
        self.ta_fst_answ.setText(questions[self.question_now]['var'].split('\r')[0])
        self.ta_sec_answ.setText(questions[self.question_now]['var'].split('\r')[1])
        self.ta_third_answ.setText(questions[self.question_now]['var'].split('\r')[2])
        self.ta_forth_answ.setText(questions[self.question_now]['var'].split('\r')[3])

        self.ta_fst_answ.setStyleSheet('')
        self.ta_sec_answ.setStyleSheet('')
        self.ta_third_answ.setStyleSheet('')
        self.ta_forth_answ.setStyleSheet('')

        self.ta_fst_answ.setChecked(False)
        self.ta_sec_answ.setChecked(False)
        self.ta_third_answ.setChecked(False)
        self.ta_forth_answ.setChecked(False)

        self.theme_buttons.hide()
        self.main_wiget_theory.hide()
        self.accaunt_wigit.hide()
        self.test_theme_get.hide()

        self.test_wigit_answers.show()
        self.blind.show()

        try:
            self.ta_answ.clicked.disconnect()
        except TypeError:
            pass
        self.ta_answ.clicked.connect(self.check_answer)

    def check_answer(self):
        question = None
        with open(f"json/test{self.test_theme}.json", 'r', encoding='utf-8') as file:
            question = json.loads(file.read())[self.question_now]
        check_boxes = (self.ta_fst_answ, self.ta_sec_answ, 
                        self.ta_third_answ, self.ta_forth_answ)
        answers = (self.ta_fst_answ.isChecked(), self.ta_sec_answ.isChecked(), 
                    self.ta_third_answ.isChecked(), self.ta_forth_answ.isChecked())
        corr_num = None
        for i in range(len(check_boxes)):
            if check_boxes[i].text() == question["corr"]:
                corr_num = i
                break
        if answers[corr_num] == True and answers.count(True) == 1:
            self.balls += 1
            check_boxes[corr_num].setStyleSheet("background-color: rgba(0, 255, 0, 100);")
        else:
            for i, j in [(answers[x], check_boxes[x]) for x in range(4)]:
                if i == True and j != check_boxes[corr_num]:
                    j.setStyleSheet("background-color: rgba(255, 0, 0, 100);")
            check_boxes[corr_num].setStyleSheet("background-color: rgba(0, 255, 0, 100);")
        self.ta_answ.setText('Продолжить')
        self.ta_answ.clicked.disconnect()
        self.ta_answ.clicked.connect(self.display_questions)
        self.ta_progress.setProperty("value", int(self.balls) * 100 / self.max_balls)
        self.question_now = str(int(self.question_now) + 1)

    def end_test(self):
        self.b_accaunt_button.setEnabled(True)
        self.b_theory_button.setEnabled(True)
        self.b_test_button.setEnabled(True)

        dlg = QMessageBox(self)
        dlg.setWindowTitle("Тест пройден!")
        dlg.setText(f"Вы прошли тест! Баллов набрано: {self.balls}/{self.max_balls} ({self.balls / self.max_balls * 100}%)")
        dlg.exec()

        thems = {
            '0': 'Механическое поколение',
            '1': 'Первое поколение',
            '2': 'Второе поколение',
            '3': 'Третье поколение',
            '4': 'Четвертое поколение'
        }
        self.db.add_value('results', None, self.accaunt[1], thems[self.test_theme], self.balls, self.max_balls)

        self.test_wigit_answers.hide()
        self.main_wiget_theory.hide()
        self.test_theme_get.hide()
        self.theme_buttons.hide()

        self.accaunt_wigit.show()
        self.blind.show()

        self.accaunt_button()

    def test_buttons(self):
        self.balls = 0
        self.ta_progress.setProperty("value", 0)

        self.test_theme = ''
        if self.sender() == self.te_zero:
            self.test_theme = '0'
        elif self.sender() == self.te_first:
            self.test_theme = '1'
        elif self.sender() == self.te_second:
            self.test_theme = '2'
        elif self.sender() == self.te_third:
            self.test_theme = '3'
        elif self.sender() == self.te_forth:
            self.test_theme = '4'
        self.question_now = '1'
        self.ta_question
        self.display_questions()
        self.b_accaunt_button.setEnabled(False)
        self.b_test_button.setEnabled(False)
        self.b_theory_button.setEnabled(False)
        
    def login(self):
        a = QInputDialog()
        b = a.getText(self.accaunt_wigit, 'Login', 'Введите имя вашего аккаунта:')
        if b[1] is False:
            return
        
        accaunt = self.db.get_line('accaunts', 'name', b[0])
        if accaunt:
            a = QInputDialog()
            b = a.getText(self.accaunt_wigit, 'Login', 'Введите пароль от вашего аккаунта:')
            if b[1]:
                hash_object = hashlib.sha256(b[0].encode('UTF-8'))
                hex_dig = hash_object.hexdigest()
                if accaunt[2] == hex_dig:
                    self.accaunt = accaunt
                    self.accaunt_button()
                    dlg = QMessageBox(self)
                    dlg.setWindowTitle("Успех!")
                    dlg.setText(f"Вы зашли в аккаунт {accaunt[1]}")
                    dlg.exec()
            else:
                return
        else: # "Упс...", "Аккаунта с таким именем нет в базе."
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Упс...")
            dlg.setText("Аккаунта с таким именем нет в базе...")
            dlg.exec()

    def registred(self):
        a = QInputDialog()
        name = a.getText(self.accaunt_wigit, 'Registr', 'Введите имя вашего аккаунта:')
        accaunt = self.db.get_line('accaunts', 'name', name[0])
        if accaunt:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Упс...")
            dlg.setText("В базе уже есть такой аккаунт...")
            dlg.exec()
            self.registred()
            return
        a = QInputDialog()
        passwd = a.getText(self.accaunt_wigit, 'Registr', 'Введите пароль от вашего аккаунта:')
        if passwd[1]:
            hash_object = hashlib.sha256(passwd[0].encode('UTF-8'))
            hex_dig = hash_object.hexdigest()
            self.db.add_value('accaunts', None, name[0], hex_dig, 0, 0)
            accaunt = self.db.get_line('accaunts', 'name', name[0])
            self.accaunt = accaunt
            self.accaunt_button()
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Успех!")
            dlg.setText(f"Вы создали аккаунт {accaunt[1]}")
            dlg.exec()
        else:
            return

    # def export_results(self):
    #     writer = None
    #     with open('results.csv', 'w', encoding='utf-8') as file:
    #         writer = csv.DictWriter(file, ['theme_name', 'your_balls', 'max_balls'])
    #         results = self.db.get_lines('results', 'name', self.accaunt[1])
    #         results_csv = []
    #         for i in results:
    #             results_csv.append({'theme_name': i[2], 'your_balls': i[3], 'max_balls': i[4]})
    #         writer.writerows(results_csv)
    #     dlg = QMessageBox(self)
    #     dlg.setWindowTitle("Успех!")
    #     dlg.setText("Файл экспортирован! Он лежит рядом с исполняемым файлом под названием results.csv")
    #     dlg.exec()

    def img_to_label(self, img_road, label):
        pixmap = QPixmap(img_road)
        if pixmap.width() > label.width() and pixmap.height() <= label.height():  # Подгон размеров картинки под label
            otn = pixmap.width() / pixmap.height()
            pixmap = pixmap.scaled(label.width(),  math.ceil(label.width() / otn))
        elif pixmap.width() <= label.width() and pixmap.height() > label.height():
            otn = pixmap.width() / pixmap.height()
            pixmap = pixmap.scaled(int(label.height() * otn), label.height())
        elif pixmap.width() > label.width() and pixmap.height() > label.height():
            otn = pixmap.width() / pixmap.height()
            pixmap = pixmap.scaled(label.width(),  math.ceil(label.width() / otn))
            if pixmap.width() <= label.width() and pixmap.height() > label.height():
                otn = pixmap.width() / pixmap.height()
                pixmap = pixmap.scaled( math.ceil(label.height() * otn), label.height())
        if pixmap.width() < label.width() and pixmap.height() < label.height():
            otn = pixmap.width() / pixmap.height()
            pixmap = pixmap.scaled(int(label.height() * otn), label.height())
            if pixmap.width() > label.width() and pixmap.height() <= label.height():
                otn = pixmap.width() / pixmap.height()
                pixmap = pixmap.scaled(label.width(),  math.ceil(label.width() / otn))
        # Задавание пиксмапа
        label.setPixmap(pixmap)
        
    def change_color(self):
        global ch_flag, color_now
        
        color_now += 1
        col = init_style_sheet()
        if color_now >= len(col):
            color_now = 0
        app.setStyleSheet(col[color_now][0].strip())
        

def init_style_sheet() -> tuple[tuple[str, tuple], ...]:
    file = None
    with open('json/styles.txt') as f:
        file = f.readlines()
    all_styles = []
    
    temp = []
    colors = False
    for i in file:
        if i.strip() == '=123' and colors is False:
            colors = temp
            temp = ''
        elif i.strip() == '#---------------------------------------------------------------------------------------------------------------------------------':
            temp = temp.replace('{a}', colors[4]).replace('{b}', colors[3]).replace('{c}', colors[2]).replace('{d}', colors[1]).replace('{e}', colors[0]).replace('{font}', colors[-1]).replace('{blind}', colors[5])     
            all_styles.append((temp, colors))
            colors = False
            temp = []
        elif bool(colors) == False:
            if i:
                temp += [i.strip()]
        else:
            temp += i
    return tuple(all_styles)


def main():
    global ch_flag, app, color_now
    color_now = 0
    app = QApplication(sys.argv)
    app.setStyleSheet(init_style_sheet()[color_now][0])
    Main_window = Main_Window()
    Main_window.show()
    sys.exit(app.exec())
if __name__ == '__main__':
    main()
