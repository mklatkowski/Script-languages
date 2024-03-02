# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerSndqmu.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QTextEdit, QWidget, QMainWindow)
import gui_editing_test

import re

class Ui_Dialog(QMainWindow):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(280, 143)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 10, 121, 16))
        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(30, 30, 221, 31))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 100, 75, 24))

        self.pushButton.clicked.connect(self.creating)

        self.retranslateUi(Dialog)
        self.dialog = Dialog

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Generator testów", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Podaj nazw\u0119 testu", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"OK", None))
    # retranslateUi

    def creating(self):
        nazwa_testu = self.textEdit.toPlainText()
        sciezka = os.path.join("tests", nazwa_testu)
        if self.validate(nazwa_testu):
            with open(sciezka, 'w', encoding='UTF-8') as plik:
                plik.write("")
            self.dialog.hide()
            dialog = QDialog()
            ui = gui_editing_test.Ui_Dialog(sciezka)
            ui.setupUi(dialog)
            dialog.exec_()
        else:
            self.label.setText("Zła nazwa")

    def validate(self, nazwa):
        regex = '^[^\\/]*$'
        match = re.match(regex, nazwa)
        search = re.search("\n", nazwa)
        if match and not search:
            return True
        return False



