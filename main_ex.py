# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ex.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 80, 301, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.v_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.v_layout.setContentsMargins(0, 0, 0, 0)
        self.v_layout.setObjectName("v_layout")
        self.line_edit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_edit1.setGeometry(QtCore.QRect(350, 80, 181, 31))
        self.line_edit1.setObjectName("line_edit1")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(350, 130, 311, 281))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.v_layout2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.v_layout2.setContentsMargins(0, 0, 0, 0)
        self.v_layout2.setObjectName("v_layout2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "main"))

