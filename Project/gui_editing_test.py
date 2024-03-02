# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designeruJQBkr.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QLabel,
    QPushButton, QSizePolicy, QTextBrowser, QTextEdit, QListWidgetItem, QListWidget,
    QWidget, QComboBox, QSpinBox, QMainWindow)
import Excercise
import typing
import os

import gui_main

class Ui_Dialog(QMainWindow):

    def __init__(self, file_path):
        self.file_path = file_path
        self.name = os.path.basename(file_path)

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(949, 580)
        self.question_list = QListWidget(Dialog)
        self.question_list.setObjectName(u"textBrowser")
        self.question_list.setGeometry(QRect(20, 60, 181, 481))
        self.label_content = QLabel(Dialog)
        self.label_content.setObjectName(u"label")
        self.label_content.setGeometry(QRect(230, 120, 81, 16))
        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(310, 100, 511, 61))
        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(250, 190, 21, 20))
        self.checkBox_2 = QCheckBox(Dialog)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(250, 250, 16, 20))
        self.checkBox_3 = QCheckBox(Dialog)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(250, 310, 21, 20))
        self.checkBox_6 = QCheckBox(Dialog)
        self.checkBox_6.setObjectName(u"checkBox_4")
        self.checkBox_6.setGeometry(QRect(250, 480, 16, 20))
        self.textEdit_1 = QTextEdit(Dialog)
        self.textEdit_1.setObjectName(u"textEdit_2")
        self.textEdit_1.setGeometry(QRect(290, 180, 511, 41))
        self.textEdit_2 = QTextEdit(Dialog)
        self.textEdit_2.setObjectName(u"textEdit_3")
        self.textEdit_2.setGeometry(QRect(290, 240, 511, 41))
        self.textEdit_3 = QTextEdit(Dialog)
        self.textEdit_3.setObjectName(u"textEdit_4")
        self.textEdit_3.setGeometry(QRect(290, 300, 511, 41))
        self.textEdit_6 = QTextEdit(Dialog)
        self.textEdit_6.setObjectName(u"textEdit_5")
        self.textEdit_6.setGeometry(QRect(290, 460, 511, 41))
        self.button_reset = QPushButton(Dialog)
        self.button_reset.setObjectName(u"pushButton")
        self.button_reset.setGeometry(QRect(230, 530, 111, 24))
        self.button_edit = QPushButton(Dialog)
        self.button_edit.setObjectName(u"pushButton_2")
        self.button_edit.setGeometry(QRect(350, 530, 101, 24))
        self.label_info_log = QLabel(Dialog)
        self.label_info_log.setObjectName(u"label_2")
        self.label_info_log.setGeometry(QRect(260, 10, 621, 21))
        self.button_back = QPushButton(Dialog)
        self.button_back.setObjectName(u"pushButton_4")
        self.button_back.setGeometry(QRect(800, 520, 111, 41))
        self.comboBox_question_type = QComboBox(Dialog)
        self.comboBox_question_type.setObjectName(u"comboBox")
        self.comboBox_question_type.setGeometry(QRect(310, 60, 221, 22))
        self.label_question_type = QLabel(Dialog)
        self.label_question_type.setObjectName(u"label_3")
        self.label_question_type.setGeometry(QRect(240, 60, 71, 16))
        self.label_number_of_points = QLabel(Dialog)
        self.label_number_of_points.setObjectName(u"label_4")
        self.label_number_of_points.setGeometry(QRect(780, 60, 91, 16))
        self.spinBox = QSpinBox(Dialog)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(880, 60, 42, 22))
        self.textEdit_open = QTextEdit(Dialog)
        self.textEdit_open.setObjectName(u"textEdit_6")
        self.textEdit_open.setGeometry(QRect(310, 180, 511, 231))
        self.label_open_anwser = QLabel(Dialog)
        self.label_open_anwser.setObjectName(u"label_5")
        self.label_open_anwser.setGeometry(QRect(240, 190, 61, 16))
        self.button_removing = QPushButton(Dialog)
        self.button_removing.setObjectName(u"pushButton_5")
        self.button_removing.setGeometry(QRect(460, 530, 101, 24))
        self.button_generate = QPushButton(Dialog)
        self.button_generate.setObjectName(u"pushButton_3")
        self.button_generate.setGeometry(QRect(50, 30, 131, 24))
        self.label_number_of_lines = QLabel(Dialog)
        self.label_number_of_lines.setObjectName(u"label_6")
        self.label_number_of_lines.setGeometry(QRect(240, 450, 161, 41))
        self.spinBox_2 = QSpinBox(Dialog)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(420, 460, 42, 22))
        self.textEdit_4 = QTextEdit(Dialog)
        self.textEdit_4.setObjectName(u"textEdit_7")
        self.textEdit_4.setGeometry(QRect(290, 350, 511, 41))
        self.checkBox_4 = QCheckBox(Dialog)
        self.checkBox_4.setObjectName(u"checkBox_5")
        self.checkBox_4.setGeometry(QRect(250, 360, 21, 20))
        self.textEdit_5 = QTextEdit(Dialog)
        self.textEdit_5.setObjectName(u"textEdit_8")
        self.textEdit_5.setGeometry(QRect(290, 400, 511, 41))
        self.checkBox_5 = QCheckBox(Dialog)
        self.checkBox_5.setObjectName(u"checkBox_6")
        self.checkBox_5.setGeometry(QRect(250, 410, 21, 20))
        self.comboBox_number_of_anwsers = QComboBox(Dialog)
        self.comboBox_number_of_anwsers.setObjectName(u"comboBox_2")
        self.comboBox_number_of_anwsers.setGeometry(QRect(697, 60, 41, 22))
        self.label_number_of_answers = QLabel(Dialog)
        self.label_number_of_answers.setObjectName(u"label_7")
        self.label_number_of_answers.setGeometry(QRect(590, 60, 101, 20))

        self.textEdit_open.hide()
        self.label_open_anwser.hide()
        self.label_number_of_lines.hide()
        self.spinBox_2.hide()
        self.spinBox.setMinimum(1)
        self.spinBox_2.setMinimum(1)

        self.dialog = Dialog

        #COMBO BOX SETUP
        self.comboBox_settings()

        #SPING BOX SETUP
        self.spinBox.setValue(1)

        self.textEditsClosed = [self.textEdit_1, self.textEdit_2, self.textEdit_3, self.textEdit_4, self.textEdit_5, self.textEdit_6]
        self.checkBoxes = [self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4, self.checkBox_5, self.checkBox_6]
        self.questions = self.read_questions_from_file()

        self.handleAnswersCount()
        self.buttons_settings()
        self.addQuestionsToList()
        self.list_widget_settings()
        self.connect_buttons()

        self.retranslateUi(Dialog)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def comboBox_settings(self):
        self.comboBox_question_type.addItem("Pytanie jednokrotnego wyboru")
        self.comboBox_question_type.addItem("Pytanie wielokrotnego wyboru")
        self.comboBox_question_type.addItem("Pytanie otwarte")

        self.comboBox_number_of_anwsers.addItem("2")
        self.comboBox_number_of_anwsers.addItem("3")
        self.comboBox_number_of_anwsers.addItem("4")
        self.comboBox_number_of_anwsers.addItem("5")
        self.comboBox_number_of_anwsers.addItem("6")

        self.comboBox_question_type.currentIndexChanged.connect(self.handleComboBoxChange)
        self.comboBox_number_of_anwsers.currentIndexChanged.connect(self.handleAnswersCount)

    def buttons_settings(self):
        if len(self.questions)==0:
            self.button_removing.setEnabled(False)
            self.button_edit.setText("Dodaj pytanie")
            self.button_edit.clicked.connect(self.add_question)
        else:
            self.button_edit.setText("Edytuj pytanie")
            self.button_edit.clicked.connect(self.edit_question)
            self.question_list.setCurrentRow(0)

        self.button_reset.clicked.connect(self.reset_all)
        self.button_back.clicked.connect(self.back)
        self.button_removing.clicked.connect(self.remove_question)
        self.button_generate.clicked.connect(self.generate_question)

        self.button_removing.setEnabled(False)

    def connect_buttons(self):
        self.checkBox.clicked.connect(lambda: self.handleCheckBoxes(0))
        self.checkBox_2.clicked.connect(lambda: self.handleCheckBoxes(1))
        self.checkBox_3.clicked.connect(lambda: self.handleCheckBoxes(2))
        self.checkBox_4.clicked.connect(lambda: self.handleCheckBoxes(3))
        self.checkBox_5.clicked.connect(lambda: self.handleCheckBoxes(4))
        self.checkBox_6.clicked.connect(lambda: self.handleCheckBoxes(5))

    def list_widget_settings(self):
        self.question_list.currentItemChanged.connect(self.detail_data)
        self.question_list.clicked.connect(self.detail_data)


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", "Generator testów - Test: " + self.name, None))
        self.label_content.setText(QCoreApplication.translate("Dialog", u"Tre\u015b\u0107 pytania", None))
        self.checkBox.setText("")
        self.checkBox_2.setText("")
        self.checkBox_3.setText("")
        self.checkBox_4.setText("")
        self.checkBox_5.setText("")
        self.checkBox_6.setText("")
        self.button_reset.setText(QCoreApplication.translate("Dialog", u"Resetuj wszystko", None))
        self.button_edit.setText(QCoreApplication.translate("Dialog", u"Dodaj pytanie", None))
        self.label_info_log.setText("")
        self.button_back.setText(QCoreApplication.translate("Dialog", u"Powr\u00f3t", None))
        self.label_question_type.setText(QCoreApplication.translate("Dialog", u"Typ pytania", None))
        self.label_number_of_points.setText(QCoreApplication.translate("Dialog", u"Liczba punkt\u00f3w", None))
        self.label_open_anwser.setText(QCoreApplication.translate("Dialog", u"Odpowied\u017a", None))
        self.button_removing.setText(QCoreApplication.translate("Dialog", u"Usu\u0144 pytanie", None))
        self.button_generate.setText(QCoreApplication.translate("Dialog", u"NOWE PYTANIE", None))
        self.label_number_of_lines.setText(QCoreApplication.translate("Dialog", u"Liczba linijek na dokumencie", None))
        self.label_number_of_answers.setText(QCoreApplication.translate("Dialog", u"Liczba odpowiedzi", None))



    def handleAnswersCount(self):
        index = self.comboBox_number_of_anwsers.currentIndex()
        count = index + 2
        for i in range(0, 6):
            if i<count:
                self.checkBoxes[i].show()
                self.textEditsClosed[i].show()
            else:
                self.checkBoxes[i].hide()
                self.textEditsClosed[i].hide()
        if self.comboBox_question_type.currentIndex() == 0:
            for i in range(self.comboBox_number_of_anwsers.currentIndex()+2, 6):
                self.checkBoxes[i].setChecked(False)

#READING FILE

    def read_questions_from_file(self):
        questions: List[Excercise] = []

        with open(self.file_path, 'r', encoding='UTF-8') as file:
            lines = file.readlines()
            i = 0
            while i < len(lines):
                question_content = lines[i+1].strip().replace("\\n", "\n")
                if lines[i] == "M"+ "\n":
                    answers = lines[i + 2].replace("\\n", "\n").strip().split(',')
                    correct_indices = list(map(int, lines[i + 3].strip().split(',')))
                    points = int(lines[i + 4].strip())
                    question = Excercise.MultipleChoiceExcercise(question_content, points, answers, correct_indices)
                    questions.append(question)
                elif lines[i] == "C"+ "\n":
                    answers = lines[i + 2].replace("\\n", "\n").strip().split(',')
                    correct_index = int(lines[i+3].strip())
                    points = int(lines[i + 4].strip())
                    question = Excercise.ClosedExcercise(question_content, points, answers, correct_index)
                    questions.append(question)
                else:
                    answer = lines[i+2].strip().replace("\\n", "\n")
                    points = int(lines[i + 3].strip())
                    lines_count = int(lines[i+4].strip())
                    question = Excercise.OpenExercise(question_content, points, answer, lines_count)
                    questions.append(question)
                i+=6
        return questions

#ADDING QUESTION

    def generate_question(self):
        self.button_removing.setEnabled(False)
        self.label_info_log.setText("Pod spodem swtórz swoje pytanie")
        self.question_list.clearSelection()
        self.reset_all()
        self.button_removing.setEnabled(False)
        self.button_edit.setText("Dodaj pytanie")
        self.button_edit.clicked.disconnect()
        self.button_edit.clicked.connect(self.add_question)



    def addQuestionsToList(self):
        i = 1
        for question in self.questions:
            self.question_list.addItem(f'{i}. {question.content}')
            i+=1

#SHOWING QUESTION DATA
    def detail_data(self):

        self.button_edit.setText("Edytuj pytanie")
        self.button_edit.clicked.disconnect()
        self.button_edit.clicked.connect(self.edit_question)

        self.button_removing.setEnabled(True)
        index = self.question_list.currentRow()
        if len(self.questions) > 0:
            question = self.questions[index]
            self.spinBox.setValue(question.points)
            self.textEdit.setText(question.content)
            if isinstance(question, Excercise.OpenExercise):
                self.comboBox_question_type.setCurrentIndex(2)
                self.show_open_fields()
                self.textEdit_open.setText(question.correct_anwser)
                self.spinBox_2.setValue(question.lines_count)
            else:
                self.show_closed_fields()
                self.clear_other_fileds()

                i = 0
                self.comboBox_number_of_anwsers.setCurrentIndex(len(question.anwsers_list) - 2)
                for anwser in question.anwsers_list:
                    self.textEditsClosed[i].setText(anwser)
                    i+=1

                for box in self.checkBoxes:
                    box.setChecked(False)

                if isinstance(question, Excercise.ClosedExcercise):
                    self.comboBox_question_type.setCurrentIndex(0)
                    self.checkBoxes[question.correct_index].setChecked(True)
                else:
                    self.comboBox_question_type.setCurrentIndex(1)
                    for index in question.correct_index_list:
                        self.checkBoxes[index].setChecked(True)
        else:
            self.reset_all()


    def clear_other_fileds(self):
        for i in range(self.comboBox_number_of_anwsers.currentIndex() + 2, 6):
            self.textEditsClosed[i].setText("")
            self.checkBoxes[i].setChecked(False)

#SHOWING FIELDS
    def show_open_fields(self):
        self.textEdit_1.hide()
        self.textEdit_2.hide()
        self.textEdit_3.hide()
        self.textEdit_4.hide()
        self.textEdit_5.hide()
        self.textEdit_6.hide()

        self.label_number_of_answers.hide()
        self.comboBox_number_of_anwsers.hide()

        self.checkBox.hide()
        self.checkBox_2.hide()
        self.checkBox_3.hide()
        self.checkBox_4.hide()
        self.checkBox_5.hide()
        self.checkBox_6.hide()

        self.textEdit_open.show()
        self.label_open_anwser.show()
        self.label_number_of_lines.show()
        self.spinBox_2.show()

    def show_closed_fields(self):

        for i in range(0,6):
            self.checkBoxes[i].hide()
            self.textEditsClosed[i].hide()
        for i in range(0, self.comboBox_number_of_anwsers.currentIndex() + 2):
            self.checkBoxes[i].show()
            self.textEditsClosed[i].show()

        self.label_number_of_answers.show()
        self.comboBox_number_of_anwsers.show()
        self.textEdit_open.hide()
        self.label_open_anwser.hide()
        self.label_number_of_lines.hide()
        self.spinBox_2.hide()


    def remove_question(self):
        index = self.question_list.currentRow()
        self.questions.remove(self.questions[index])
        self.question_list.clear()
        self.addQuestionsToList()
        self.save()
        self.set_list_index()
        self.label_info_log.setText(f'Pytanie zostało usunięte.')


    def save(self):
            sciezka = os.path.join("tests", self.name)
            with open(sciezka, 'w', encoding='UTF-8') as plik:
                for pytanie in self.questions:

                    if isinstance(pytanie, Excercise.MultipleChoiceExcercise):
                        plik.write("M"+ "\n")
                        plik.write(pytanie.content.replace("\n", "\\n") + "\n")
                        plik.write(','.join(pytanie.anwsers_list).replace("\n", "\\n") + "\n")
                        correct_strings = [str(element) for element in pytanie.correct_index_list]
                        plik.write(','.join(correct_strings) + "\n")
                        plik.write(str(pytanie.points) + "\n")
                        plik.write("\n")
                    elif isinstance(pytanie, Excercise.ClosedExcercise):
                        plik.write("C"+ "\n")
                        plik.write(pytanie.content.replace("\n", "\\n") + "\n")
                        plik.write(','.join(pytanie.anwsers_list).replace("\n", "\\n") + "\n")
                        plik.write(str(pytanie.correct_index)+ "\n")
                        plik.write(str(pytanie.points) + "\n")
                        plik.write("\n")
                    else:
                        plik.write("O"+ "\n")
                        plik.write(pytanie.content.replace("\n", "\\n") + "\n")
                        plik.write(pytanie.correct_anwser.replace("\n", "\\n") + "\n")
                        plik.write(str(pytanie.points) + "\n")
                        plik.write(str(pytanie.lines_count) + "\n")
                        plik.write("\n")

    def set_list_index(self):
        if len(self.questions)!=0:
            self.question_list.setCurrentRow(0)
        else:
            self.button_removing.setEnabled(False)
            self.button_edit.setText("Dodaj pytanie")
            self.button_edit.clicked.disconnect()
            self.button_edit.clicked.connect(self.add_question)


#BACK BUTTON HANDLE
    def back(self):
        self.dialog.hide()
        dialog = QDialog()
        ui = gui_main.Ui_Dialog()
        ui.setupUi(dialog)
        dialog.exec_()

#CHECKBOX HANDLE
    def handleCheckBoxes(self, index):
        if self.comboBox_question_type.currentIndex() == 0:
            for i in range(0, self.comboBox_number_of_anwsers.currentIndex() + 2):
                if i!=index:
                    self.checkBoxes[i].setChecked(False)
                else:
                    self.checkBoxes[i].setChecked(True)

#COMBOBOX HANDLE
    def handleComboBoxChange(self, index):
        if index == 2:
            self.show_open_fields()
            self.reset()

        else:
            self.show_closed_fields()
        self.resetCheckBoxes()

    #RESET
    def reset_all(self):
        self.textEdit.clear()
        self.reset()

    def reset(self):
        self.textEdit_1.clear()
        self.textEdit_2.clear()
        self.textEdit_3.clear()
        self.textEdit_4.clear()
        self.textEdit_5.clear()
        self.textEdit_6.clear()

        self.textEdit_open.clear()

        self.resetCheckBoxes()
        self.spinBox.setValue(1)
        self.spinBox_2.setValue(1)

    def resetCheckBoxes(self):
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        self.checkBox_4.setChecked(False)
        self.checkBox_5.setChecked(False)
        self.checkBox_6.setChecked(False)

    #QUESTION VALIDATION
    def validate_question(self):
        if self.textEdit.toPlainText() == "":
            self.label_info_log.setText("Pytanie musi zawierać treść")
            return False
        elif self.spinBox.value() == 0:
            self.label_info_log.setText("Pytanie musi być punktowane za więcej niż 0 punktów")
            return False
        else:
            if self.comboBox_question_type.currentIndex() == 2:
                return self.validate_open_questions()
            else:
                return self.validate_closed_questions()

    def validate_closed_questions(self):
        for i in range(0, self.comboBox_number_of_anwsers.currentIndex() + 2):
            if self.textEditsClosed[i].toPlainText() == "":
                self.label_info_log.setText("Pytanie musi zawierać odpowiedzi")
                return False

        for i in range(0, self.comboBox_number_of_anwsers.currentIndex() + 2):
            if self.checkBoxes[i].isChecked():
                return True
        self.label_info_log.setText("Musi zostać wybrana przynajmniej jedna odpowiedź")
        return False


    def validate_open_questions(self):
        if self.textEdit_open.toPlainText() =="":
            self.label_info_log.setText("Pytanie musi zawierać odpowiedź")
            return False
        if self.spinBox_2.value() == 0:
            self.label_info_log.setText("Pytanie otwarte na PDF musi mieć minimum 1 linijkę")
        return True


    #QUESTION ADDING
    def add_question(self):
        if self.validate_question():
            tresc_pytania = self.textEdit.toPlainText()
            anwsers = []

            for i in range(0, self.comboBox_number_of_anwsers.currentIndex() + 2):
                anwsers.append(self.textEditsClosed[i].toPlainText())

            open_anwser = self.textEdit_open.toPlainText()

            points = self.spinBox.value()

            zaznaczone = []

            for i in range(0, self.comboBox_number_of_anwsers.currentIndex() + 2):
                if self.checkBoxes[i].isChecked():
                    zaznaczone.append(i)

            if self.comboBox_question_type.currentIndex() == 1:
                self.questions.append(Excercise.MultipleChoiceExcercise(tresc_pytania, points, anwsers, zaznaczone))
            elif self.comboBox_question_type.currentIndex() ==0:
                self.questions.append(Excercise.ClosedExcercise(tresc_pytania, points, anwsers, zaznaczone[0]))
            else:
                lines_count = self.spinBox_2.value()
                self.questions.append(Excercise.OpenExercise(tresc_pytania, points, open_anwser, lines_count))
            self.reset_all()
            self.question_list.addItem(f'{len(self.questions)}. {tresc_pytania}')
            self.button_removing.setEnabled(True)
            self.save()
            self.label_info_log.setText(f'Pytanie zostało dodane.')
            self.question_list.clearSelection()
            self.button_removing.setEnabled(False)

    def edit_question(self):
        if self.validate_question():
            self.clear_other_fileds()
            tresc_pytania = self.textEdit.toPlainText()
            anwsers = []

            for i in range(0, self.comboBox_number_of_anwsers.currentIndex() + 2):
                anwsers.append(self.textEditsClosed[i].toPlainText())

            open_anwser = self.textEdit_open.toPlainText()


            points = self.spinBox.value()

            zaznaczone = []

            for i in range(0, self.comboBox_number_of_anwsers.currentIndex() + 2):
                if self.checkBoxes[i].isChecked():
                    zaznaczone.append(i)

            index = self.question_list.currentRow()

            if self.comboBox_question_type.currentIndex() == 1:
                self.questions[self.question_list.currentRow()] = Excercise.MultipleChoiceExcercise(tresc_pytania, points, anwsers, zaznaczone)
            elif self.comboBox_question_type.currentIndex() ==0:
                self.questions[self.question_list.currentRow()] = Excercise.ClosedExcercise(tresc_pytania, points, anwsers, zaznaczone[0])
            else:
                lines_count = self.spinBox_2.value()
                self.questions[self.question_list.currentRow()] = Excercise.OpenExercise(tresc_pytania, points, open_anwser, lines_count)

            self.question_list.item(index).setText(f'{index + 1}. {tresc_pytania}')
            self.save()
            self.label_info_log.setText(f'Pytanie zostało zedytowane.')