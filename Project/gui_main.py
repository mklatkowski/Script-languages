# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maineoJPtq.ui'
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
    QSizePolicy, QWidget, QStackedWidget, QMainWindow, QMessageBox)
import gui_name_input
import gui_pdf_options
import gui_choose_file

import os

class Ui_Dialog(QMainWindow):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(566, 328)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 20, 261, 51))
        self.dialog = Dialog
        font = QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.pushButton_newTest = QPushButton(Dialog)
        self.pushButton_newTest.setObjectName(u"pushButton")
        self.pushButton_newTest.setGeometry(QRect(120, 110, 91, 41))
        self.pushButton_editTest = QPushButton(Dialog)
        self.pushButton_editTest.setObjectName(u"pushButton_2")
        self.pushButton_editTest.setGeometry(QRect(330, 110, 91, 41))
        self.pushButton_generatePDF = QPushButton(Dialog)
        self.pushButton_generatePDF.setObjectName(u"pushButton_3")
        self.pushButton_generatePDF.setGeometry(QRect(230, 220, 91, 41))

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)
        self.pushButton_newTest.clicked.connect(self.creating_test)
        self.pushButton_editTest.clicked.connect(self.edit)
        self.pushButton_generatePDF.clicked.connect(self.generating_pdf)

        # self.stackedWidget = QStackedWidget()
        # self.stackedWidget.addWidget(gui_name_input.Ui_Dialog())
        # self.stackedWidget.addWidget(gui_choose_file.Ui_Dialog())
        # self.stackedWidget.addWidget(gui_pdf_options.Ui_Dialog())

        if len(os.listdir("./tests/")) == 0:
            self.pushButton_editTest.setEnabled(False)
            self.pushButton_generatePDF.setEnabled(False)
        else:
            self.pushButton_editTest.setEnabled(True)
            self.pushButton_generatePDF.setEnabled(True)



    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Generator testów", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"KREATOR TEST\u00d3W", None))
        self.pushButton_newTest.setText(QCoreApplication.translate("Dialog", u"Nowy Test", None))
        self.pushButton_editTest.setText(QCoreApplication.translate("Dialog", u"Edytuj test", None))
        self.pushButton_generatePDF.setText(QCoreApplication.translate("Dialog", u"Generuj PDF", None))

    def creating_test(self):
        self.dialog.hide()
        dialog = QDialog()
        ui = gui_name_input.Ui_Dialog()
        ui.setupUi(dialog)
        dialog.exec_()

    def generating_pdf(self):
        self.dialog.hide()
        dialog = QDialog()
        ui = gui_pdf_options.Ui_Dialog()
        ui.setupUi(dialog)
        dialog.exec_()

    def edit(self):
        if len(os.listdir("./tests/")) == 0:
            pass
        else:
            self.dialog.hide()
            dialog = QDialog()
            ui = gui_choose_file.Ui_Dialog()
            ui.setupUi(dialog)
            dialog.exec_()

#entery, przecinki w nazwie
