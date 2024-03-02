# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'input_namenauTNk.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QTextEdit, QWidget, QFileDialog, QMainWindow)

import os
import gui_editing_test


class Ui_Dialog(QMainWindow):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(620, 143)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(230, 10, 121, 16))
        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(20, 40, 480, 31))
        self.pushButton_ok = QPushButton(Dialog)
        self.pushButton_ok.setObjectName(u"pushButton")
        self.pushButton_ok.setGeometry(QRect(230, 100, 75, 24))
        self.pushButton_browse = QPushButton(Dialog)
        self.pushButton_browse.setObjectName(u"pushButton_2")
        self.pushButton_browse.setGeometry(QRect(520, 40, 75, 24))

        self.dialog = Dialog

        self.retranslateUi(Dialog)

        self.pushButton_ok.clicked.connect(self.editing)
        self.pushButton_browse.clicked.connect(self.open_file)

        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Generator testów", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Wyszukaj test", None))
        self.pushButton_ok.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.pushButton_browse.setText(QCoreApplication.translate("Dialog", u"Przegl\u0105daj", None))

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
                self.textEdit.setText(f"{file_path}")

    def editing(self):
        if self.validate():
            self.dialog.hide()
            dialog = QDialog()
            ui = gui_editing_test.Ui_Dialog(self.textEdit.toPlainText())
            ui.setupUi(dialog)
            dialog.exec_()
        else:
            self.label.setText("Zły plik")

    def validate(self):
        file_path = self.textEdit.toPlainText()

        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                i = 0
                while i < len(lines):
                    question_content = lines[i + 1].strip()
                    i+=6
            return True
        except Exception:
            return False




