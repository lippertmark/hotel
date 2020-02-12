# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manager.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_manager(object):
    def setupUi(self, MainWindow_manager):
        MainWindow_manager.setObjectName("MainWindow_manager")
        MainWindow_manager.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow_manager)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 541, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_admin_hotel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_admin_hotel.setGeometry(QtCore.QRect(240, 190, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_admin_hotel.setFont(font)
        self.pushButton_admin_hotel.setObjectName("pushButton_admin_hotel")
        self.pushButton_hotel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_hotel.setGeometry(QtCore.QRect(240, 250, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_hotel.setFont(font)
        self.pushButton_hotel.setObjectName("pushButton_hotel")
        MainWindow_manager.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_manager)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_manager)

    def retranslateUi(self, MainWindow_manager):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_manager.setWindowTitle(_translate("MainWindow_manager", "MainWindow"))
        self.label.setText(_translate("MainWindow_manager", "Управляющий сетью гостиниц"))
        self.pushButton_admin_hotel.setText(_translate("MainWindow_manager", "Администратор гостиницы"))
        self.pushButton_hotel.setText(_translate("MainWindow_manager", "Гостиница"))
