# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/ui_initSigmaAlpha.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(224, 188)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.sigma_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.sigma_lineEdit.setObjectName("sigma_lineEdit")
        self.gridLayout.addWidget(self.sigma_lineEdit, 0, 1, 1, 1)
        self.alpha_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.alpha_lineEdit.setObjectName("alpha_lineEdit")
        self.gridLayout.addWidget(self.alpha_lineEdit, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.sigma_error = QtWidgets.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(241, 9, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 9, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 69, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.sigma_error.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.sigma_error.setFont(font)
        self.sigma_error.setObjectName("sigma_error")
        self.gridLayout.addWidget(self.sigma_error, 0, 2, 1, 1)
        self.alpha_error = QtWidgets.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(238, 11, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 11, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 69, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.alpha_error.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.alpha_error.setFont(font)
        self.alpha_error.setObjectName("alpha_error")
        self.gridLayout.addWidget(self.alpha_error, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.ok_button = QtWidgets.QPushButton(self.centralwidget)
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout.addWidget(self.ok_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 224, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.cancel_button.clicked.connect(MainWindow.cancel_button_clicked)
        self.ok_button.clicked.connect(MainWindow.ok_button_clicked)
        self.sigma_lineEdit.returnPressed.connect(MainWindow.ok_button_clicked)
        self.alpha_lineEdit.returnPressed.connect(MainWindow.ok_button_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sigma_lineEdit.setText(_translate("MainWindow", "3.5"))
        self.alpha_lineEdit.setText(_translate("MainWindow", "4.5"))
        self.label_2.setText(_translate("MainWindow", "alpha"))
        self.label.setText(_translate("MainWindow", "sigma"))
        self.sigma_error.setText(_translate("MainWindow", "*"))
        self.alpha_error.setText(_translate("MainWindow", "*"))
        self.cancel_button.setText(_translate("MainWindow", "Cancel"))
        self.ok_button.setText(_translate("MainWindow", "OK"))

