# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'answer_login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_answer_login(object):
    def setupUi(self, Form_answer_login):
        Form_answer_login.setObjectName("Form_answer_login")
        Form_answer_login.resize(482, 160)
        font = QtGui.QFont()
        font.setPointSize(16)
        Form_answer_login.setFont(font)
        self.label_user_type = QtWidgets.QLabel(Form_answer_login)
        self.label_user_type.setGeometry(QtCore.QRect(20, 20, 441, 41))
        self.label_user_type.setAlignment(QtCore.Qt.AlignCenter)
        self.label_user_type.setObjectName("label_user_type")
        self.pushButton = QtWidgets.QPushButton(Form_answer_login)
        self.pushButton.setGeometry(QtCore.QRect(130, 90, 211, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form_answer_login)
        QtCore.QMetaObject.connectSlotsByName(Form_answer_login)

    def retranslateUi(self, Form_answer_login):
        _translate = QtCore.QCoreApplication.translate
        Form_answer_login.setWindowTitle(_translate("Form_answer_login", "Form"))
        self.label_user_type.setText(_translate("Form_answer_login", "TextLabel"))
        self.pushButton.setText(_translate("Form_answer_login", "PushButton"))
