# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'p2design.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(682, 462)
        self.horizontalLayout_4 = QHBoxLayout(Form)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonLT = QPushButton(Form)
        self.pushButtonLT.setObjectName(u"pushButtonLT")
        self.pushButtonLT.setMinimumSize(QSize(0, 50))
        self.pushButtonLT.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout.addWidget(self.pushButtonLT)

        self.pushButtonRT = QPushButton(Form)
        self.pushButtonRT.setObjectName(u"pushButtonRT")
        self.pushButtonRT.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.pushButtonRT)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pushButtonCenter = QPushButton(Form)
        self.pushButtonCenter.setObjectName(u"pushButtonCenter")
        self.pushButtonCenter.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.pushButtonCenter)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButtonLD = QPushButton(Form)
        self.pushButtonLD.setObjectName(u"pushButtonLD")
        self.pushButtonLD.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_2.addWidget(self.pushButtonLD)

        self.pushButtonRD = QPushButton(Form)
        self.pushButtonRD.setObjectName(u"pushButtonRD")
        self.pushButtonRD.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_2.addWidget(self.pushButtonRD)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.pushButtonGET = QPushButton(Form)
        self.pushButtonGET.setObjectName(u"pushButtonGET")

        self.verticalLayout.addWidget(self.pushButtonGET)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.dial = QDial(Form)
        self.dial.setObjectName(u"dial")

        self.horizontalLayout_3.addWidget(self.dial)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_2.addWidget(self.comboBox)

        self.lcdNumber = QLCDNumber(Form)
        self.lcdNumber.setObjectName(u"lcdNumber")

        self.verticalLayout_2.addWidget(self.lcdNumber)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalSlider = QSlider(Form)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.horizontalSlider)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.plainTextEdit = QPlainTextEdit(Form)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_4.addWidget(self.plainTextEdit)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButtonLT.setText(QCoreApplication.translate("Form", u"\u041b\u0435\u0432\u043e/\u0412\u0435\u0440\u0445", None))
        self.pushButtonRT.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0430\u0432\u043e/\u0412\u0435\u0440\u0445", None))
        self.pushButtonCenter.setText(QCoreApplication.translate("Form", u"\u0426\u0435\u043d\u0442\u0440", None))
        self.pushButtonLD.setText(QCoreApplication.translate("Form", u"\u041b\u0435\u0432\u043e/\u041d\u0438\u0437", None))
        self.pushButtonRD.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0430\u0432\u043e/\u041d\u0438\u0437", None))
        self.pushButtonGET.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u043e\u043a\u043d\u0430", None))
    # retranslateUi

