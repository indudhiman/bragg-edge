# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/ui_mainWindow.ui'
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
        MainWindow.resize(1331, 848)
        MainWindow.setMinimumSize(QtCore.QSize(300, 0))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.splitter_2 = QtGui.QSplitter(self.tab)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setChildrenCollapsible(False)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.layoutWidget = QtGui.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.toolBox = QtGui.QToolBox(self.layoutWidget)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.sample_toolbox = QtGui.QWidget()
        self.sample_toolbox.setGeometry(QtCore.QRect(0, 0, 523, 570))
        self.sample_toolbox.setObjectName(_fromUtf8("sample_toolbox"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.sample_toolbox)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.import_sample_button = QtGui.QPushButton(self.sample_toolbox)
        self.import_sample_button.setObjectName(_fromUtf8("import_sample_button"))
        self.horizontalLayout_4.addWidget(self.import_sample_button)
        self.sample_folder = QtGui.QLabel(self.sample_toolbox)
        self.sample_folder.setText(_fromUtf8(""))
        self.sample_folder.setObjectName(_fromUtf8("sample_folder"))
        self.horizontalLayout_4.addWidget(self.sample_folder)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.list_sample = QtGui.QListWidget(self.sample_toolbox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_sample.sizePolicy().hasHeightForWidth())
        self.list_sample.setSizePolicy(sizePolicy)
        self.list_sample.setMinimumSize(QtCore.QSize(50, 0))
        self.list_sample.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.list_sample.setObjectName(_fromUtf8("list_sample"))
        self.verticalLayout_5.addWidget(self.list_sample)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.toolBox.addItem(self.sample_toolbox, _fromUtf8(""))
        self.open_beam_toolbox = QtGui.QWidget()
        self.open_beam_toolbox.setGeometry(QtCore.QRect(0, 0, 523, 570))
        self.open_beam_toolbox.setObjectName(_fromUtf8("open_beam_toolbox"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.open_beam_toolbox)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.import_open_beam_button = QtGui.QPushButton(self.open_beam_toolbox)
        self.import_open_beam_button.setObjectName(_fromUtf8("import_open_beam_button"))
        self.horizontalLayout_5.addWidget(self.import_open_beam_button)
        self.open_beam_folder = QtGui.QLabel(self.open_beam_toolbox)
        self.open_beam_folder.setText(_fromUtf8(""))
        self.open_beam_folder.setObjectName(_fromUtf8("open_beam_folder"))
        self.horizontalLayout_5.addWidget(self.open_beam_folder)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.list_open_beam = QtGui.QListWidget(self.open_beam_toolbox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_open_beam.sizePolicy().hasHeightForWidth())
        self.list_open_beam.setSizePolicy(sizePolicy)
        self.list_open_beam.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.list_open_beam.setObjectName(_fromUtf8("list_open_beam"))
        self.verticalLayout_7.addWidget(self.list_open_beam)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.toolBox.addItem(self.open_beam_toolbox, _fromUtf8(""))
        self.verticalLayout.addWidget(self.toolBox)
        self.line = QtGui.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.groupBox = QtGui.QGroupBox(self.layoutWidget)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.pushButton_4 = QtGui.QPushButton(self.groupBox)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout_6.addWidget(self.pushButton_4)
        self.time_spectra = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_spectra.sizePolicy().hasHeightForWidth())
        self.time_spectra.setSizePolicy(sizePolicy)
        self.time_spectra.setObjectName(_fromUtf8("time_spectra"))
        self.horizontalLayout_6.addWidget(self.time_spectra)
        self.verticalLayout.addWidget(self.groupBox)
        self.widget = QtGui.QWidget(self.splitter_2)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.splitter = QtGui.QSplitter(self.widget)
        self.splitter.setBaseSize(QtCore.QSize(0, 0))
        self.splitter.setFrameShadow(QtGui.QFrame.Raised)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.data_infos_box = QtGui.QGroupBox(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_infos_box.sizePolicy().hasHeightForWidth())
        self.data_infos_box.setSizePolicy(sizePolicy)
        self.data_infos_box.setMinimumSize(QtCore.QSize(100, 20))
        self.data_infos_box.setMaximumSize(QtCore.QSize(16777215, 300))
        self.data_infos_box.setBaseSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.data_infos_box.setFont(font)
        self.data_infos_box.setObjectName(_fromUtf8("data_infos_box"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.data_infos_box)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.label = QtGui.QLabel(self.data_infos_box)
        self.label.setMinimumSize(QtCore.QSize(0, 15))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_9.addWidget(self.label)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.data_infos_box)
        self.plainTextEdit.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setMinimumSize(QtCore.QSize(0, 10))
        self.plainTextEdit.setBaseSize(QtCore.QSize(0, 20))
        self.plainTextEdit.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout_9.addWidget(self.plainTextEdit)
        self.label_2 = QtGui.QLabel(self.data_infos_box)
        self.label_2.setMinimumSize(QtCore.QSize(0, 15))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_9.addWidget(self.label_2)
        self.data_general_infos = QtGui.QTextEdit(self.data_infos_box)
        self.data_general_infos.setMinimumSize(QtCore.QSize(0, 10))
        self.data_general_infos.setObjectName(_fromUtf8("data_general_infos"))
        self.verticalLayout_9.addWidget(self.data_general_infos)
        self.data_preview_box = QtGui.QGroupBox(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_preview_box.sizePolicy().hasHeightForWidth())
        self.data_preview_box.setSizePolicy(sizePolicy)
        self.data_preview_box.setMinimumSize(QtCore.QSize(0, 20))
        self.data_preview_box.setSizeIncrement(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.data_preview_box.setFont(font)
        self.data_preview_box.setObjectName(_fromUtf8("data_preview_box"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.data_preview_box)
        self.verticalLayout_10.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.widget_3 = QtGui.QWidget(self.data_preview_box)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_3.setSizeIncrement(QtCore.QSize(0, 50))
        self.widget_3.setBaseSize(QtCore.QSize(0, 300))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.verticalLayout_10.addWidget(self.widget_3)
        self.data_instrument_box = QtGui.QGroupBox(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_instrument_box.sizePolicy().hasHeightForWidth())
        self.data_instrument_box.setSizePolicy(sizePolicy)
        self.data_instrument_box.setMinimumSize(QtCore.QSize(0, 20))
        self.data_instrument_box.setMaximumSize(QtCore.QSize(16777215, 150))
        self.data_instrument_box.setBaseSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.data_instrument_box.setFont(font)
        self.data_instrument_box.setObjectName(_fromUtf8("data_instrument_box"))
        self.gridLayout_2 = QtGui.QGridLayout(self.data_instrument_box)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_3 = QtGui.QLabel(self.data_instrument_box)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(self.data_instrument_box)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.data_instrument_box)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 2, 1, 2)
        self.label_5 = QtGui.QLabel(self.data_instrument_box)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.data_instrument_box)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 1, 1, 2)
        self.label_6 = QtGui.QLabel(self.data_instrument_box)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 1, 3, 1, 1)
        self.label_7 = QtGui.QLabel(self.data_instrument_box)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.data_instrument_box)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout_2.addWidget(self.lineEdit_3, 2, 1, 1, 2)
        self.label_8 = QtGui.QLabel(self.data_instrument_box)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 2, 3, 1, 1)
        self.verticalLayout_2.addWidget(self.splitter)
        self.horizontalLayout.addWidget(self.splitter_2)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.splitter_4 = QtGui.QSplitter(self.tab_3)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName(_fromUtf8("splitter_4"))
        self.layoutWidget1 = QtGui.QWidget(self.splitter_4)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.import_normalized_data = QtGui.QPushButton(self.layoutWidget1)
        self.import_normalized_data.setObjectName(_fromUtf8("import_normalized_data"))
        self.horizontalLayout_2.addWidget(self.import_normalized_data)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.listView = QtGui.QListView(self.layoutWidget1)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.verticalLayout_4.addWidget(self.listView)
        self.widget_2 = QtGui.QWidget(self.splitter_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(300, 0))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.splitter_3 = QtGui.QSplitter(self.widget_2)
        self.splitter_3.setBaseSize(QtCore.QSize(0, 0))
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setChildrenCollapsible(False)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.groupBox_5 = QtGui.QGroupBox(self.splitter_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setMinimumSize(QtCore.QSize(100, 200))
        self.groupBox_5.setMaximumSize(QtCore.QSize(16777215, 300))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.label_9 = QtGui.QLabel(self.groupBox_5)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_11.addWidget(self.label_9)
        self.plainTextEdit_3 = QtGui.QPlainTextEdit(self.groupBox_5)
        self.plainTextEdit_3.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_3.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_3.setSizePolicy(sizePolicy)
        self.plainTextEdit_3.setMinimumSize(QtCore.QSize(0, 50))
        self.plainTextEdit_3.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.plainTextEdit_3.setObjectName(_fromUtf8("plainTextEdit_3"))
        self.verticalLayout_11.addWidget(self.plainTextEdit_3)
        self.label_10 = QtGui.QLabel(self.groupBox_5)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_11.addWidget(self.label_10)
        self.plainTextEdit_4 = QtGui.QPlainTextEdit(self.groupBox_5)
        self.plainTextEdit_4.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_4.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_4.setSizePolicy(sizePolicy)
        self.plainTextEdit_4.setMinimumSize(QtCore.QSize(0, 50))
        self.plainTextEdit_4.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.plainTextEdit_4.setObjectName(_fromUtf8("plainTextEdit_4"))
        self.verticalLayout_11.addWidget(self.plainTextEdit_4)
        self.groupBox_6 = QtGui.QGroupBox(self.splitter_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.widget_4 = QtGui.QWidget(self.groupBox_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 300))
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.verticalLayout_12.addWidget(self.widget_4)
        self.verticalLayout_3.addWidget(self.splitter_3)
        self.verticalLayout_13.addWidget(self.splitter_4)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1331, 22))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSteps = QtGui.QMenu(self.menubar)
        self.menuSteps.setObjectName(_fromUtf8("menuSteps"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action1_Data = QtGui.QAction(MainWindow)
        self.action1_Data.setObjectName(_fromUtf8("action1_Data"))
        self.action2_Normalization = QtGui.QAction(MainWindow)
        self.action2_Normalization.setEnabled(True)
        self.action2_Normalization.setObjectName(_fromUtf8("action2_Normalization"))
        self.action3_Binning = QtGui.QAction(MainWindow)
        self.action3_Binning.setObjectName(_fromUtf8("action3_Binning"))
        self.action4_Fitting = QtGui.QAction(MainWindow)
        self.action4_Fitting.setObjectName(_fromUtf8("action4_Fitting"))
        self.action5_Results = QtGui.QAction(MainWindow)
        self.action5_Results.setObjectName(_fromUtf8("action5_Results"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.action1_Raw_Data = QtGui.QAction(MainWindow)
        self.action1_Raw_Data.setObjectName(_fromUtf8("action1_Raw_Data"))
        self.action2_Normalization_2 = QtGui.QAction(MainWindow)
        self.action2_Normalization_2.setObjectName(_fromUtf8("action2_Normalization_2"))
        self.action3_Normalized_Data = QtGui.QAction(MainWindow)
        self.action3_Normalized_Data.setObjectName(_fromUtf8("action3_Normalized_Data"))
        self.menuSteps.addAction(self.action1_Raw_Data)
        self.menuSteps.addAction(self.action2_Normalization_2)
        self.menuSteps.addAction(self.action3_Normalized_Data)
        self.menuSteps.addAction(self.action3_Binning)
        self.menuSteps.addAction(self.action4_Fitting)
        self.menuSteps.addAction(self.action5_Results)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuSteps.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        QtCore.QObject.connect(self.import_sample_button, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.sample_import_button_clicked)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.time_spectra_import_button_clicked)
        QtCore.QObject.connect(self.import_open_beam_button, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.open_beam_import_button_clicked)
        QtCore.QObject.connect(self.list_sample, QtCore.SIGNAL(_fromUtf8("itemSelectionChanged()")), MainWindow.sample_list_selection_changed)
        QtCore.QObject.connect(self.list_open_beam, QtCore.SIGNAL(_fromUtf8("itemSelectionChanged()")), MainWindow.open_beam_list_selection_changed)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.import_sample_button.setText(_translate("MainWindow", "Import ...", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.sample_toolbox), _translate("MainWindow", " Sample", None))
        self.import_open_beam_button.setText(_translate("MainWindow", "Import ...", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.open_beam_toolbox), _translate("MainWindow", " Open Beam", None))
        self.groupBox.setTitle(_translate("MainWindow", "Time Spectra", None))
        self.pushButton_4.setText(_translate("MainWindow", "Import ...", None))
        self.data_infos_box.setTitle(_translate("MainWindow", "infos", None))
        self.label.setText(_translate("MainWindow", "Selection", None))
        self.label_2.setText(_translate("MainWindow", "General", None))
        self.data_preview_box.setTitle(_translate("MainWindow", "preview", None))
        self.data_instrument_box.setTitle(_translate("MainWindow", "instrument", None))
        self.label_3.setText(_translate("MainWindow", "Beam Rate", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "60", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "30", None))
        self.label_4.setText(_translate("MainWindow", "Hz", None))
        self.label_5.setText(_translate("MainWindow", "Distance source-detector", None))
        self.label_6.setText(_translate("MainWindow", "m", None))
        self.label_7.setText(_translate("MainWindow", "Detector offset", None))
        self.label_8.setText(_translate("MainWindow", "micros", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "1 - Load Data", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "2 - Normalization", None))
        self.import_normalized_data.setText(_translate("MainWindow", "Import ...", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "infos", None))
        self.label_9.setText(_translate("MainWindow", "Selection", None))
        self.label_10.setText(_translate("MainWindow", "General", None))
        self.groupBox_6.setTitle(_translate("MainWindow", "preview", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "3 - Normalized Data", None))
        self.menuSteps.setTitle(_translate("MainWindow", "Steps", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.action1_Data.setText(_translate("MainWindow", "1. Data", None))
        self.action2_Normalization.setText(_translate("MainWindow", "2. Normalization", None))
        self.action3_Binning.setText(_translate("MainWindow", "4. Binning", None))
        self.action4_Fitting.setText(_translate("MainWindow", "5. Fitting", None))
        self.action5_Results.setText(_translate("MainWindow", "6. Strain Mapping", None))
        self.actionAbout.setText(_translate("MainWindow", "About ...", None))
        self.action1_Raw_Data.setText(_translate("MainWindow", "1. Raw Data", None))
        self.action2_Normalization_2.setText(_translate("MainWindow", "2. Normalization", None))
        self.action3_Normalized_Data.setText(_translate("MainWindow", "3. Normalized Data", None))

