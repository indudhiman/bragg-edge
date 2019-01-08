# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/ui_advancedFittingSelection.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(946, 766)
        MainWindow.setMinimumSize(QtCore.QSize(300, 0))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.selection_table = QtWidgets.QTableWidget(self.tab)
        self.selection_table.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.selection_table.setObjectName("selection_table")
        self.selection_table.setColumnCount(0)
        self.selection_table.setRowCount(0)
        self.verticalLayout.addWidget(self.selection_table)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.lock_table = QtWidgets.QTableWidget(self.tab_2)
        self.lock_table.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.lock_table.setObjectName("lock_table")
        self.lock_table.setColumnCount(0)
        self.lock_table.setRowCount(0)
        self.verticalLayout_3.addWidget(self.lock_table)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.advanced_selection_cell_size_slider = QtWidgets.QSlider(self.centralwidget)
        self.advanced_selection_cell_size_slider.setMinimum(10)
        self.advanced_selection_cell_size_slider.setMaximum(50)
        self.advanced_selection_cell_size_slider.setProperty("value", 20)
        self.advanced_selection_cell_size_slider.setOrientation(QtCore.Qt.Horizontal)
        self.advanced_selection_cell_size_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.advanced_selection_cell_size_slider.setObjectName("advanced_selection_cell_size_slider")
        self.horizontalLayout_4.addWidget(self.advanced_selection_cell_size_slider)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.apply_button = QtWidgets.QPushButton(self.centralwidget)
        self.apply_button.setObjectName("apply_button")
        self.horizontalLayout_4.addWidget(self.apply_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.advanced_selection_cell_size_slider.sliderMoved['int'].connect(MainWindow.selection_cell_size_changed)
        self.apply_button.clicked.connect(MainWindow.apply_button_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "All Bins selected in this table will be used to display the Counts vs Lambda plot"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Active"))
        self.label_3.setText(_translate("MainWindow", "All Bins selected in this table will be locked (their fitting parameters can not be modified)."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Lock"))
        self.label.setText(_translate("MainWindow", "Cells Size"))
        self.apply_button.setText(_translate("MainWindow", "Apply"))

