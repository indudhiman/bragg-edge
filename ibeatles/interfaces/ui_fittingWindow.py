# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/ui_fittingWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1222, 772)
        MainWindow.setMinimumSize(QtCore.QSize(300, 0))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter_2 = QtGui.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget = QtGui.QWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.rightFrame = QtGui.QFrame(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightFrame.sizePolicy().hasHeightForWidth())
        self.rightFrame.setSizePolicy(sizePolicy)
        self.rightFrame.setMinimumSize(QtCore.QSize(300, 400))
        self.rightFrame.setMaximumSize(QtCore.QSize(300, 16777215))
        self.rightFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.rightFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.rightFrame.setObjectName(_fromUtf8("rightFrame"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.rightFrame)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.material_groupBox = QtGui.QGroupBox(self.rightFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.material_groupBox.sizePolicy().hasHeightForWidth())
        self.material_groupBox.setSizePolicy(sizePolicy)
        self.material_groupBox.setObjectName(_fromUtf8("material_groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.material_groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.material_groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.hkl_list_ui = QtGui.QComboBox(self.material_groupBox)
        self.hkl_list_ui.setMinimumSize(QtCore.QSize(100, 0))
        self.hkl_list_ui.setMaximumSize(QtCore.QSize(100, 16777215))
        self.hkl_list_ui.setObjectName(_fromUtf8("hkl_list_ui"))
        self.horizontalLayout.addWidget(self.hkl_list_ui)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addWidget(self.material_groupBox)
        self.groupBox = QtGui.QGroupBox(self.rightFrame)
        self.groupBox.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setMinimumSize(QtCore.QSize(75, 0))
        self.label_2.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.bragg_edge_calculated = QtGui.QLabel(self.groupBox)
        self.bragg_edge_calculated.setMinimumSize(QtCore.QSize(50, 0))
        self.bragg_edge_calculated.setMaximumSize(QtCore.QSize(50, 16777215))
        self.bragg_edge_calculated.setObjectName(_fromUtf8("bragg_edge_calculated"))
        self.horizontalLayout_2.addWidget(self.bragg_edge_calculated)
        self.bragg_edge_units = QtGui.QLabel(self.groupBox)
        self.bragg_edge_units.setObjectName(_fromUtf8("bragg_edge_units"))
        self.horizontalLayout_2.addWidget(self.bragg_edge_units)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lambda_min_label = QtGui.QLabel(self.groupBox_3)
        self.lambda_min_label.setObjectName(_fromUtf8("lambda_min_label"))
        self.gridLayout.addWidget(self.lambda_min_label, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lambda_min_units = QtGui.QLabel(self.groupBox_3)
        self.lambda_min_units.setObjectName(_fromUtf8("lambda_min_units"))
        self.gridLayout.addWidget(self.lambda_min_units, 0, 2, 1, 1)
        self.lambda_max_label = QtGui.QLabel(self.groupBox_3)
        self.lambda_max_label.setObjectName(_fromUtf8("lambda_max_label"))
        self.gridLayout.addWidget(self.lambda_max_label, 1, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lambda_max_units = QtGui.QLabel(self.groupBox_3)
        self.lambda_max_units.setObjectName(_fromUtf8("lambda_max_units"))
        self.gridLayout.addWidget(self.lambda_max_units, 1, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.bottomFrame = QtGui.QFrame(self.splitter_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottomFrame.sizePolicy().hasHeightForWidth())
        self.bottomFrame.setSizePolicy(sizePolicy)
        self.bottomFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.bottomFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.bottomFrame.setObjectName(_fromUtf8("bottomFrame"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.bottomFrame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.advanced_table_checkBox = QtGui.QCheckBox(self.bottomFrame)
        self.advanced_table_checkBox.setChecked(True)
        self.advanced_table_checkBox.setObjectName(_fromUtf8("advanced_table_checkBox"))
        self.verticalLayout_5.addWidget(self.advanced_table_checkBox)
        self.label_3 = QtGui.QLabel(self.bottomFrame)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_5.addWidget(self.label_3)
        self.header_table = QtGui.QTableWidget(self.bottomFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header_table.sizePolicy().hasHeightForWidth())
        self.header_table.setSizePolicy(sizePolicy)
        self.header_table.setMinimumSize(QtCore.QSize(1180, 0))
        self.header_table.setMaximumSize(QtCore.QSize(1180, 22))
        self.header_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.header_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.header_table.setAutoScroll(True)
        self.header_table.setCornerButtonEnabled(True)
        self.header_table.setObjectName(_fromUtf8("header_table"))
        self.header_table.setColumnCount(11)
        self.header_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.header_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.header_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.header_table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.header_table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.header_table.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.header_table.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.header_table.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.header_table.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.header_table.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.header_table.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.header_table.setHorizontalHeaderItem(10, item)
        self.header_table.horizontalHeader().setVisible(True)
        self.header_table.horizontalHeader().setHighlightSections(True)
        self.header_table.horizontalHeader().setStretchLastSection(False)
        self.header_table.verticalHeader().setVisible(False)
        self.header_table.verticalHeader().setHighlightSections(False)
        self.header_table.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_5.addWidget(self.header_table)
        self.value_table = QtGui.QTableWidget(self.bottomFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.value_table.sizePolicy().hasHeightForWidth())
        self.value_table.setSizePolicy(sizePolicy)
        self.value_table.setMinimumSize(QtCore.QSize(1180, 0))
        self.value_table.setMaximumSize(QtCore.QSize(1180, 16777215))
        self.value_table.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.value_table.setFrameShadow(QtGui.QFrame.Sunken)
        self.value_table.setLineWidth(1)
        self.value_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.value_table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.value_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.value_table.setObjectName(_fromUtf8("value_table"))
        self.value_table.setColumnCount(19)
        self.value_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(14, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(15, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(16, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(17, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(18, item)
        self.value_table.verticalHeader().setVisible(False)
        self.verticalLayout_5.addWidget(self.value_table)
        self.verticalLayout.addWidget(self.splitter_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.hkl_list_ui, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), MainWindow.hkl_list_changed)
        QtCore.QObject.connect(self.value_table, QtCore.SIGNAL(_fromUtf8("customContextMenuRequested(QPoint)")), MainWindow.value_table_right_click)
        QtCore.QObject.connect(self.value_table, QtCore.SIGNAL(_fromUtf8("cellClicked(int,int)")), MainWindow.selection_in_value_table_of_rows_cell_clicked)
        QtCore.QObject.connect(self.value_table, QtCore.SIGNAL(_fromUtf8("itemSelectionChanged()")), MainWindow.selection_in_value_table_changed)
        QtCore.QObject.connect(self.advanced_table_checkBox, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), MainWindow.advanced_table_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.material_groupBox.setTitle(_translate("MainWindow", "Material", None))
        self.label.setText(_translate("MainWindow", "h,k,l", None))
        self.groupBox.setTitle(_translate("MainWindow", "Bragg Edge", None))
        self.label_2.setText(_translate("MainWindow", "calculated", None))
        self.bragg_edge_calculated.setText(_translate("MainWindow", "N/A", None))
        self.bragg_edge_units.setText(_translate("MainWindow", "A", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Range Selected", None))
        self.lambda_min_label.setText(_translate("MainWindow", "Lambda min", None))
        self.lambda_min_units.setText(_translate("MainWindow", "A", None))
        self.lambda_max_label.setText(_translate("MainWindow", "Lambda min", None))
        self.lambda_max_units.setText(_translate("MainWindow", "A", None))
        self.advanced_table_checkBox.setText(_translate("MainWindow", "Advanced Fitting", None))
        item = self.header_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Lock", None))
        item = self.header_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Active", None))
        item = self.header_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Fitting Confidence", None))
        item = self.header_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "D-spacing", None))
        item = self.header_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Sigma", None))
        item = self.header_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Alpha", None))
        item = self.header_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "A1", None))
        item = self.header_table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "A2", None))
        item = self.header_table.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "A5", None))
        item = self.header_table.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "A6", None))
        item = self.header_table.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Intensity", None))
        item = self.value_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Val.", None))
        item = self.value_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Err.", None))
        item = self.value_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Val.", None))
        item = self.value_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Err.", None))
        item = self.value_table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Val.", None))
        item = self.value_table.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Err.", None))
        item = self.value_table.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Val.", None))
        item = self.value_table.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Err.", None))
        item = self.value_table.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Val.", None))
        item = self.value_table.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Err.", None))
        item = self.value_table.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Val.", None))
        item = self.value_table.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "Err.", None))
        item = self.value_table.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "Val.", None))
        item = self.value_table.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "Err.", None))
        item = self.value_table.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "Val.", None))
        item = self.value_table.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "Err.", None))

import icons_rc
