# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guiYXdihw.ui'
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
    QSizePolicy, QTextBrowser, QTextEdit, QWidget, QListWidget, QListWidgetItem)

import itertools
import re
import pytz
import logging

from datetime import datetime


class Ui_Dialog(object):
    def __init__(self):
        self.count = 2000
        self.logs = []
        logging.basicConfig(level=logging.INFO)

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(839, 501)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(690, 30, 91, 41))
        self.pushButton.clicked.connect(self.open_logs)

        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 450, 75, 24))
        self.pushButton_2.clicked.connect(self.previous_log)

        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(740, 460, 75, 24))
        self.pushButton_3.clicked.connect(self.next_log)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(470, 110, 101, 16))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(480, 170, 49, 16))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(480, 220, 49, 16))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(470, 290, 71, 16))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(450, 350, 49, 16))
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(470, 410, 49, 16))
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(670, 220, 61, 16))
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(680, 290, 61, 16))
        self.textBrowser_2 = QTextBrowser(Dialog)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(560, 100, 256, 31))
        self.textBrowser_3 = QTextBrowser(Dialog)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(540, 160, 256, 31))
        self.textBrowser_4 = QTextBrowser(Dialog)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setGeometry(QRect(530, 210, 131, 31))
        self.textBrowser_5 = QTextBrowser(Dialog)
        self.textBrowser_5.setObjectName(u"textBrowser_5")
        self.textBrowser_5.setGeometry(QRect(730, 210, 101, 31))
        self.textBrowser_6 = QTextBrowser(Dialog)
        self.textBrowser_6.setObjectName(u"textBrowser_6")
        self.textBrowser_6.setGeometry(QRect(540, 280, 101, 31))
        self.textBrowser_7 = QTextBrowser(Dialog)
        self.textBrowser_7.setObjectName(u"textBrowser_7")
        self.textBrowser_7.setGeometry(QRect(740, 280, 91, 31))
        self.textBrowser_8 = QTextBrowser(Dialog)
        self.textBrowser_8.setObjectName(u"textBrowser_8")
        self.textBrowser_8.setGeometry(QRect(510, 340, 320, 31))
        self.textBrowser_9 = QTextBrowser(Dialog)
        self.textBrowser_9.setObjectName(u"textBrowser_9")
        self.textBrowser_9.setGeometry(QRect(530, 400, 256, 31))
        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 100, 49, 16))
        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(60, 90, 141, 41))
        font = QFont()
        font.setPointSize(11)

        self.textEdit.setFont(font)
        self.textEdit_2 = QTextEdit(Dialog)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(250, 90, 161, 41))
        self.textEdit_2.setFont(font)
        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(220, 100, 49, 16))
        self.textEdit_3 = QTextEdit(Dialog)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(20, 20, 641, 51))
        font1 = QFont()
        font1.setPointSize(14)
        self.textEdit_3.setFont(font1)

        self.listWidget = QListWidget(Dialog)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(30, 150, 401, 281))
        self.listWidget.currentItemChanged.connect(self.detail_data)

        self.retranslateUi(Dialog)

        self.pushButton_2.setDisabled(True)
        self.pushButton_3.setDisabled(True)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Open", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Previous", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Next", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Remote host", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Date", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Time", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Status code", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Resource", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Size", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Timezone", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Method", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"From", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"To", None))
    # retranslateUi



    def open_logs(self):
        file_path = self.textEdit_3.toPlainText()
        self.listWidget.clear()
        self.pushButton_2.setDisabled(True)
        self.pushButton_3.setDisabled(False)
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.logs = self.filter_by_dates(file.readlines()[:self.count])
                for log in itertools.islice(self.logs, self.count):
                    self.listWidget.addItem(log[:60]+'...')

                if self.logs != []:
                    self.listWidget.setCurrentRow(0)
                    self.detail_data()
                    self.pushButton_2.setDisabled(True)
                else:
                    self.clear_data()
                if 0<=len(self.logs)<=1:
                    self.pushButton_3.setDisabled(True)
                # else:
                    # item = QListWidgetItem()
                    # item.setText("Brak danych")
                    # self.listWidget.addItem(item)
        except (FileNotFoundError, NameError):
            logging.log(logging.INFO, "Błąd w ścieżce")
            pass
            # item = QListWidgetItem()
            # item.setText("Plik nie istieje")
            # self.listWidget.addItem(item)


    def next_log(self):
        current_index = self.listWidget.currentRow()
        self.listWidget.setCurrentRow(current_index+1)
        self.detail_data()
        if current_index == self.count-1:
            self.pushButton_3.setDisabled(True)
        self.pushButton_2.setDisabled(False)

    def previous_log(self):
        current_index = self.listWidget.currentRow()
        self.listWidget.setCurrentRow(current_index - 1)
        self.detail_data()
        if current_index==1:
            self.pushButton_2.setDisabled(True)
        self.pushButton_3.setDisabled(False)

    def detail_data(self):
        if self.listWidget.currentRow() == 0:
            self.pushButton_2.setDisabled(True)
        else:
            self.pushButton_2.setDisabled(False)

        if self.listWidget.currentRow() == len(self.logs)-1:
            self.pushButton_3.setDisabled(True)
        else:
            self.pushButton_3.setDisabled(False)

        log = self.logs[self.listWidget.currentRow()]
        pattern = r'^(\S+) - - \[(\d{2}/\w+/\d{4}):(\d{2}:\d{2}:\d{2}) ([+-]\d{4})\] "(\w+) ([^"]+) HTTP/1.0" (\d+) (\d+)$'
        regex = re.compile(pattern)

        match = regex.search(log)
        if match:
            ip = match.group(1)
            date = match.group(2)
            time = match.group(3)
            timezone = match.group(4)
            method = match.group(5)
            resource = match.group(6)
            status = match.group(7)
            size = match.group(8)

            self.textBrowser_2.setText(ip)
            self.textBrowser_3.setText(date)
            self.textBrowser_4.setText(time)
            self.textBrowser_5.setText(self.parse_timezone(int(timezone[:-2])))
            self.textBrowser_6.setText(status)
            self.textBrowser_7.setText(method)
            self.textBrowser_8.setText(resource)
            self.textBrowser_9.setText(size +" Bytes")

            if 200<=int(status)<300:
                self.textBrowser_6.setStyleSheet("color: green;")
            else:
                self.textBrowser_6.setStyleSheet("color: red;")

    def filter_by_dates(self, logs):
        date_format = "%d/%b/%Y"
        return_list = []

        pattern = r'^(\S+) - - \[(\d{2}/\w+/\d{4}):(\d{2}:\d{2}:\d{2}) ([+-]\d{4})\] "(\w+) ([^"]+) HTTP/1.0" (\d+) (\d+)$'
        regex = re.compile(pattern)

        try:
            start_date = datetime.strptime(self.textEdit.toPlainText(), date_format)
            end_date = datetime.strptime(self.textEdit_2.toPlainText(), date_format)

        except ValueError:
            return logs

        for log in logs:
            match = regex.search(log)
            if match:
                if start_date <= datetime.strptime(match.group(2), date_format) <= end_date:
                    return_list.append(log)
        return return_list

    def parse_timezone(self, timezone_int):
        try:
            timezone = pytz.timezone('ETC/GMT' + str(timezone_int))
            return timezone.zone
        except pytz.UnknownTimeZoneError:
            return None

    def clear_data(self):
        self.textBrowser_2.clear()
        self.textBrowser_3.clear()
        self.textBrowser_4.clear()
        self.textBrowser_5.clear()
        self.textBrowser_6.clear()
        self.textBrowser_7.clear()
        self.textBrowser_8.clear()
        self.textBrowser_9.clear()
