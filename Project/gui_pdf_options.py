# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerFjsQgt.ui'
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
    QPushButton, QSizePolicy, QSpinBox, QTextEdit,
    QWidget, QButtonGroup, QRadioButton, QMainWindow)

from PySide6.QtWidgets import QApplication, QDialog, QFileDialog
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from typing import List

import Excercise

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import utils
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase.pdfmetrics import stringWidth

import os
import shutil
import webbrowser

import gui_main
import gui_choosing_questions

from random import shuffle


def create_directory():
    nazwa_folderu = "pdf"
    if not os.path.exists(nazwa_folderu):
        os.makedirs(nazwa_folderu)


class Ui_Dialog(QMainWindow):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(602, 418)
        self.textEdit_browse_file = QTextEdit(Dialog)
        self.textEdit_browse_file.setObjectName(u"textEdit")
        self.textEdit_browse_file.setGeometry(QRect(20, 40, 451, 31))
        self.pushButton_browse_file = QPushButton(Dialog)
        self.pushButton_browse_file.setObjectName(u"pushButton")
        self.pushButton_browse_file.setGeometry(QRect(490, 40, 91, 24))
        self.radioButton_allQuestions = QRadioButton(Dialog)
        self.radioButton_allQuestions.setObjectName(u"radioButton")
        self.radioButton_allQuestions.setGeometry(QRect(80, 180, 171, 20))
        self.radioButton_random = QRadioButton(Dialog)
        self.radioButton_random.setObjectName(u"radioButton_2")
        self.radioButton_random.setGeometry(QRect(80, 200, 181, 20))
        self.radioButton_browse = QRadioButton(Dialog)
        self.radioButton_browse.setObjectName(u"radioButton_3")
        self.radioButton_browse.setGeometry(QRect(80, 260, 91, 20))
        self.checkBox_generate_with_answers = QCheckBox(Dialog)
        self.checkBox_generate_with_answers.setObjectName(u"checkBox")
        self.checkBox_generate_with_answers.setGeometry(QRect(50, 330, 211, 20))
        self.checkBox_random = QCheckBox(Dialog)
        self.checkBox_random.setObjectName(u"checkBox_2")
        self.checkBox_random.setGeometry(QRect(60, 125, 171, 20))
        self.pushButton_generate = QPushButton(Dialog)
        self.pushButton_generate.setObjectName(u"pushButton_3")
        self.pushButton_generate.setGeometry(QRect(340, 370, 111, 41))
        self.pushButton_return = QPushButton(Dialog)
        self.pushButton_return.setObjectName(u"pushButton_4")
        self.pushButton_return.setGeometry(QRect(180, 370, 111, 41))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 230, 161, 16))
        self.spinBox = QSpinBox(Dialog)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(260, 230, 42, 22))
        self.textEdit_browse_questions = QTextEdit(Dialog)
        self.textEdit_browse_questions.setObjectName(u"textEdit_2")
        self.textEdit_browse_questions.setGeometry(QRect(120, 290, 261, 31))
        self.pushButton_browse = QPushButton(Dialog)
        self.pushButton_browse.setObjectName(u"pushButton_2")
        self.pushButton_browse.setGeometry(QRect(400, 290, 121, 24))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(200,10,111,20))

        self.pushButton_browse_file.clicked.connect(self.open_file)
        self.pushButton_return.clicked.connect(self.back)
        self.pushButton_generate.clicked.connect(self.generate_pdf)


        self.dialog = Dialog

        self.retranslateUi(Dialog)

        #default conf
        self.buttonGroup = QButtonGroup()
        self.buttonGroup.addButton(self.radioButton_allQuestions)
        self.buttonGroup.addButton(self.radioButton_random)
        self.buttonGroup.addButton(self.radioButton_browse)

        self.radioButton_allQuestions.setChecked(True)
        self.spinBox.setEnabled(False)
        self.pushButton_browse.setEnabled(False)

        self.radioButton_allQuestions.clicked.connect(lambda: self.handleRadioButton(0))
        self.radioButton_random.clicked.connect(lambda: self.handleRadioButton(1))
        self.radioButton_browse.clicked.connect(lambda: self.handleRadioButton(2))

        self.pushButton_browse.clicked.connect(self.getExactQuestions)
        #default conf

        self.questions = []
        self.questionsToGenerate = []

        self.textEdit_browse_questions.setText("Wybierz pytania spośród listy pytań")
        self.textEdit_browse_questions.setEnabled(False)
        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Generator testów", None))
        self.pushButton_browse_file.setText(QCoreApplication.translate("Dialog", u"Przeglądaj", None))
        self.radioButton_allQuestions.setText(QCoreApplication.translate("Dialog", u"Wszystkie pytania", None))
        self.radioButton_random.setText(QCoreApplication.translate("Dialog", u"Losowe pytania ", None))
        self.radioButton_browse.setText(QCoreApplication.translate("Dialog", u"Pytania z puli", None))
        self.checkBox_generate_with_answers.setText(QCoreApplication.translate("Dialog", u"Generuj z odpowiedziami", None))
        self.checkBox_random.setText(QCoreApplication.translate("Dialog", u"Losowa kolejno\u015b\u0107 pyta\u0144", None))
        self.pushButton_generate.setText(QCoreApplication.translate("Dialog", u"Generuj", None))
        self.pushButton_return.setText(QCoreApplication.translate("Dialog", u"Powr\u00f3t", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Liczba losowych pyta\u0144:", None))
        self.pushButton_browse.setText(QCoreApplication.translate("Dialog", u"Przegl\u0105daj pytania", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"", None))

    def open_file(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)

        initial_dir = "/tests/"
        file_dialog.setDirectory(initial_dir)

        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            if len(selected_files) > 0:
                file_path = selected_files[0]
                file_name = os.path.basename(file_path).split('.')[0]
                file_name = os.path.splitext(file_name)[0]
                self.textEdit_browse_file.setText(f"{file_path}")
                self.questions = self.read_questions_from_file()
                self.spinBox.setMaximum(len(self.questions))

    def read_questions_from_file(self):
        questions: List[Excercise] = []
        file_path = self.textEdit_browse_file.toPlainText()

        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                i = 0
                while i < len(lines):
                    question_content = lines[i+1].strip()
                    if lines[i] == "M"+ "\n":
                        answers = lines[i + 2].strip().split(',')
                        correct_indices = list(map(int, lines[i + 3].strip().split(',')))
                        points = int(lines[i + 4].strip())
                        question = Excercise.MultipleChoiceExcercise(question_content, points, answers, correct_indices)
                        questions.append(question)
                    elif lines[i] == "C"+ "\n":
                        answers = lines[i + 2].strip().split(',')
                        correct_index = int(lines[i+3].strip())
                        points = int(lines[i + 4].strip())
                        question = Excercise.ClosedExcercise(question_content, points, answers, correct_index)
                        questions.append(question)
                    else:
                        answer = lines[i+2].strip()
                        points = int(lines[i + 3].strip())
                        lines_count = int(lines[i+4].strip())
                        question = Excercise.OpenExercise(question_content, points, answer, lines_count)
                        questions.append(question)
                    i+=6
            return questions
        except Exception:
            self.label_2.setText("Zły plik")

    def back(self):
        self.dialog.hide()
        dialog = QDialog()
        ui = gui_main.Ui_Dialog()
        ui.setupUi(dialog)
        dialog.exec_()


    def handleRadioButton(self, index):
        self.questionsToGenerate = []
        if index == 0:
            self.spinBox.setEnabled(False)
            self.pushButton_browse.setEnabled(False)
            self.textEdit_browse_questions.clear()
        elif index == 1:
            self.spinBox.setEnabled(True)
            self.pushButton_browse.setEnabled(False)
            self.textEdit_browse_questions.clear()
        else:
            self.spinBox.setEnabled(False)
            self.pushButton_browse.setEnabled(True)

    def getRandomQuestions(self):
        questionsFromFile = self.read_questions_from_file()
        if self.spinBox.value()>= len(questionsFromFile):
            return questionsFromFile
        shuffle(questionsFromFile)
        returnList = []
        for i in range(0, self.spinBox.value()):
            returnList.append(questionsFromFile[0])
            questionsFromFile.remove(questionsFromFile[0])
        return returnList

    def getExactQuestions(self):
        dialog = QDialog()
        ui = gui_choosing_questions.Ui_Dialog(self.read_questions_from_file())
        ui.setupUi(dialog)
        dialog.exec_()
        questions = []

        while True:
            if ui.isReady:
                self.questionsToGenerate = ui.questionsToReturn
                break

        match len(self.questionsToGenerate):
            case 1:
                self.textEdit_browse_questions.setText(f"Dodano 1 pytanie do testu.")
            case 2 | 3 | 4:
                self.textEdit_browse_questions.setText(f"Dodano {len(self.questionsToGenerate)} pytania do testu.")
            case _:
                self.textEdit_browse_questions.setText(f"Dodano {len(self.questionsToGenerate)} pytań do testu.")

    def generate_pdf(self):
        style_sheet = getSampleStyleSheet()
        style = style_sheet["Normal"]
        style.fontName = "Arial"
        style.fontSize = 12
        style.leading = 15

        create_directory()
        
        test_name = self.get_name()

        pdfmetrics.registerFont(TTFont("Arial", "Arial.ttf"))
        pdfmetrics.registerFont(TTFont("Arial-Bold", "Arial-Bold.ttf"))
        file_directory = os.path.join("pdf", test_name + ".pdf")
        document = canvas.Canvas(file_directory, pagesize=letter)

        if self.checkBox_generate_with_answers.isChecked():
            document.setTitle("Odpowiedzi")
        else:
            document.setTitle("Test")

        if self.radioButton_allQuestions.isChecked():
            self.questionsToGenerate = self.read_questions_from_file()
        elif self.radioButton_random.isChecked() and len(self.questionsToGenerate)==0:
            self.questionsToGenerate = self.getRandomQuestions()
        else:
            pass

        points = 0
        for question in self.questionsToGenerate:
            points+= question.points

        x = 10
        y = 750
        max_y = 50

        document.setFont("Arial", 12)
        if not self.checkBox_generate_with_answers.isChecked():
            self.draw_header(document, y, max_y, points)
        x = 50
        y -= 100

        document.setFont("Arial-Bold", 16)
        document.drawCentredString(0.5 * letter[0], y, os.path.basename(self.textEdit_browse_file.toPlainText()))
        y -= 50

        document.setFont("Arial", 12)

        i = 1


        if self.checkBox_random.isChecked():
            shuffle(self.questionsToGenerate)

        for question in self.questionsToGenerate:
            document.setFont("Arial", 12)

            if not isinstance(question, Excercise.OpenExercise):
                if isinstance(question, Excercise.MultipleChoiceExcercise):
                    x, y = self.draw_multiple_choice_question(document, i, x, y, max_y, question, style)
                else:
                    x, y = self.draw_single_choice_question(document, i, x, y, max_y, question, style)
            else:
                x, y = self.draw_open_question(document, i, x, y, max_y, question, style)

            i += 1

        document.save()
        webbrowser.open(file_directory)

    def draw_header(self, document, y, max_y, points):
        x = 0.5 * letter[0]

        document.drawString(x - 250, y, '.'*60)
        document.drawString(x + 150, y, '.'*30)

        text = "Imię, Nazwisko, Indeks"
        document.drawString(x - 250, y - 20, text)

        text = "Data"
        text_width = stringWidth(text, "Arial", 12)
        document.drawString(x + 180, y - 20, text)

        document.drawString(x + 180, y - 60, f'...../{points} p.')

    def draw_multiple_choice_question(self, document, i, x, y, max_y, question, style):
        y = self.check_page(y, max_y, document)
        style.fontName = "Arial"

        count = question.content.count(r'\n')
        y -= 30 * count

        question.content = question.content.replace(r'\n', '<br />\n')

        paragraph = Paragraph(f'{i}. {question.content}. Podaj wszystkie prawidłowe odpowiedzi. ({question.points} p.)',
                              style)
        paragraph.wrapOn(document, 500, 0)
        paragraph.drawOn(document, x, y)

        y -= 25
        for idx, answer in enumerate(question.anwsers_list):
            y = self.check_page(y, max_y, document)
            style.fontName = "Arial-Bold" if idx in question.correct_index_list and self.checkBox_generate_with_answers.isChecked() else "Arial"
            paragraph = Paragraph(f"{chr(ord('a') + idx)}) {answer}", style)
            paragraph.wrapOn(document, 500, 0)
            paragraph.drawOn(document, x + 20, y)

            y -= 25

        y -= 10
        return x, y

    def draw_single_choice_question(self, document, i, x, y, max_y, question, style):
        y = self.check_page(y, max_y, document)
        style.fontName = "Arial"

        count = question.content.count(r'\n')
        y -= 12*count

        question.content = question.content.replace(r'\n', '<br />\n')

        paragraph = Paragraph(f'{i}. {question.content}. Podaj prawidłową odpowiedź. ({question.points} p.)', style)
        paragraph.wrapOn(document, 500, 0)
        paragraph.drawOn(document, x, y)

        y -= 25

        for idx, answer in enumerate(question.anwsers_list):
            y = self.check_page(y, max_y, document)
            style.fontName = "Arial-Bold" if idx == question.correct_index and self.checkBox_generate_with_answers.isChecked() else "Arial"
            paragraph = Paragraph(f"{chr(ord('a') + idx)}) {answer}", style)
            paragraph.wrapOn(document, 500, 0)
            paragraph.drawOn(document, x + 20, y)

            y -= 25

        y -= 10
        return x, y

    def draw_open_question(self, document, i, x, y, max_y, question, style):
        y = self.check_page(y, max_y, document)
        style.fontName = "Arial"

        count = question.content.count(r'\n')
        y-=10*count

        question.content = question.content.replace(r'\n', '<br />\n')
        paragraph = Paragraph(f'{i}. {question.content}. Podaj pełną odpowiedź. ({question.points} p.)', style)
        paragraph.wrapOn(document, 500, 0)
        paragraph.drawOn(document, x, y)

        y -= 55

        if not self.checkBox_generate_with_answers.isChecked():
            for i in range(question.lines_count):
                y = self.check_page(y, max_y, document)
                document.setFont("Arial", 12)
                document.drawString(x + 20, y,
                                    ".......................................................................................................................................")

                y -= 30
        else:
            anwser = question.correct_anwser.replace(r'\n', '<br />\n')
            style.alignment = 4
            document.setFont("Arial-Bold", 12)
            paragraph = Paragraph(anwser, style)
            paragraph.wrapOn(document, 500, 0)
            paragraph.drawOn(document, x + 20, y - paragraph.height + 30)
            y -= 25

        y -= 10
        return x, y

    def get_name(self):
        if not self.checkBox_generate_with_answers.isChecked():
            return self.get_name_test()
        else:
            return self.get_name_anwsers()

    def get_name_test(self):
        basename = os.path.basename(self.textEdit_browse_file.toPlainText())
        if not os.path.isfile(os.path.join("pdf", basename+".pdf")):
            return basename
        else:
            flag = False
            i = 1
            while(not flag):
                if not os.path.isfile(os.path.join("pdf", basename+f'({i}).pdf')):
                    return basename+f'({i})'
                else:
                    i+=1

    def get_name_anwsers(self):
        basename = os.path.basename(self.textEdit_browse_file.toPlainText() + "-odpowiedzi")
        if not os.path.isfile(os.path.join("pdf", basename+".pdf")):
            return basename
        else:
            flag = False
            i = 1
            while(not flag):
                if not os.path.isfile(os.path.join("pdf", basename+f'({i}).pdf')):
                    return basename+f'({i})'
                else:
                    i+=1

    def check_page(self, y, max_y, document):
        if y <= max_y:
            document.showPage()
            y = 750
        return y