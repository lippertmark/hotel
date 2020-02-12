# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_admin(object):
    def setupUi(self, MainWindow_admin):
        MainWindow_admin.setObjectName("MainWindow_admin")
        MainWindow_admin.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow_admin)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(64, 19, 511, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self._numbers_hotel = QtWidgets.QPushButton(self.centralwidget)
        self._numbers_hotel.setGeometry(QtCore.QRect(170, 150, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self._numbers_hotel.setFont(font)
        self._numbers_hotel.setObjectName("_numbers_hotel")
        self.pushButton_in = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_in.setGeometry(QtCore.QRect(170, 200, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_in.setFont(font)
        self.pushButton_in.setObjectName("pushButton_in")
        self.pushButton_out = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_out.setGeometry(QtCore.QRect(170, 250, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_out.setFont(font)
        self.pushButton_out.setObjectName("pushButton_out")
        self.pushButton_guest = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_guest.setGeometry(QtCore.QRect(170, 100, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_guest.setFont(font)
        self.pushButton_guest.setObjectName("pushButton_guest")
        MainWindow_admin.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_admin)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_admin)

    def retranslateUi(self, MainWindow_admin):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_admin.setWindowTitle(_translate("MainWindow_admin", "MainWindow"))
        self.label.setText(_translate("MainWindow_admin", "Администратор гостиницы"))
        self._numbers_hotel.setText(_translate("MainWindow_admin", "Номера гостиницы"))
        self.pushButton_in.setText(_translate("MainWindow_admin", "Заселение"))
        self.pushButton_out.setText(_translate("MainWindow_admin", "Выселение"))
        self.pushButton_guest.setText(_translate("MainWindow_admin", "Постоялец"))
