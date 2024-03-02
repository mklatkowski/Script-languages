# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designernHvDNy.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QWidget, QMainWindow)

class Ui_Dialog(QMainWindow):

    def __init__(self, questions):
        self.questions = questions

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(799, 421)
        self.listWidget = QListWidget(Dialog)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(20, 50, 351, 311))
        self.listWidget_2 = QListWidget(Dialog)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(430, 50, 331, 311))
        self.pushButton_chooseOne = QPushButton(Dialog)
        self.pushButton_chooseOne.setObjectName(u"pushButton")
        self.pushButton_chooseOne.setGeometry(QRect(380, 110, 41, 24))
        self.pushButton_chooseAll = QPushButton(Dialog)
        self.pushButton_chooseAll.setObjectName(u"pushButton_2")
        self.pushButton_chooseAll.setGeometry(QRect(380, 150, 41, 24))
        self.pushButton_removeOne = QPushButton(Dialog)
        self.pushButton_removeOne.setObjectName(u"pushButton_3")
        self.pushButton_removeOne.setGeometry(QRect(380, 260, 41, 24))
        self.pushButton_ready = QPushButton(Dialog)
        self.pushButton_ready.setObjectName(u"pushButton_4")
        self.pushButton_ready.setGeometry(QRect(370, 380, 75, 24))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 20, 131, 16))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(560, 20, 101, 16))

        self.dialog = Dialog
        self.isReady = False

        self.addToList(self.listWidget, self.questions)

        self.retranslateUi(Dialog)

        self.questionsToReturn = []

        #default conf
        self.pushButton_chooseOne.clicked.connect(self.addToReturnList)
        self.pushButton_chooseAll.clicked.connect(self.addAll)
        self.pushButton_removeOne.clicked.connect(self.removeQuestion)
        self.pushButton_ready.clicked.connect(self.ready)

        self.listWidget.itemDoubleClicked.connect(self.addToReturnList)
        self.listWidget_2.itemDoubleClicked.connect(self.removeQuestion)

        self.pushButton_removeOne.setEnabled(False)

        self.dialog.setWindowFlag(Qt.WindowCloseButtonHint, False)

        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Generator testów", None))
        self.pushButton_chooseOne.setText(QCoreApplication.translate("Dialog", u">", None))
        self.pushButton_chooseAll.setText(QCoreApplication.translate("Dialog", u">>", None))
        self.pushButton_removeOne.setText(QCoreApplication.translate("Dialog", u"X", None))
        self.pushButton_ready.setText(QCoreApplication.translate("Dialog", u"Gotowe", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Wszystkie pytania", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Wybrane pytania", None))

    def addToList(self, listWidget, questionList):
        for question in questionList:
            listWidget.addItem(question.content)

    def addToReturnList(self):
        questionToAdd = self.questions[self.listWidget.currentRow()]
        self.questions.remove(questionToAdd)
        self.questionsToReturn.append(questionToAdd)
        self.listWidget_2.addItem(questionToAdd.content)
        self.updateList(self.listWidget, self.questions)

        if len(self.questions)==0:
            self.pushButton_chooseOne.setEnabled(False)
            self.pushButton_chooseAll.setEnabled(False)
        self.pushButton_removeOne.setEnabled(True)


    def addAll(self):
        self.questionsToReturn += self.questions
        for question in self.questions:
            self.listWidget_2.addItem(question.content)
        self.questions = []
        self.listWidget.clear()
        self.pushButton_chooseOne.setEnabled(False)
        self.pushButton_chooseAll.setEnabled(False)
        self.pushButton_removeOne.setEnabled(True)


    def updateList(self, listWidget, questionList):
        listWidget.clear()
        self.addToList(listWidget, questionList)

    def ready(self):
        self.dialog.hide()
        self.isReady = True

    def removeQuestion(self):
        questionToRemove = self.questionsToReturn[self.listWidget_2.currentRow()]
        self.questions.append(questionToRemove)
        self.questionsToReturn.remove(questionToRemove)
        self.listWidget.addItem(questionToRemove.content)
        self.updateList(self.listWidget_2, self.questionsToReturn)

        if len(self.questionsToReturn)==0:
            self.pushButton_removeOne.setEnabled(False)
        self.pushButton_chooseOne.setEnabled(True)
        self.pushButton_chooseAll.setEnabled(True)
