# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sun.ui'
#
# Created: Thu Oct 10 19:30:10 2013
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_CSRH(object):
    def setupUi(self, Sun):
        Sun.setObjectName(_fromUtf8("Sun"))
        Sun.resize(433, 374)
        Sun.setStyleSheet(_fromUtf8("#Sun{background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));}\n"
"#Sun *{background-color:url();}"))
        self.centralwidget = QtGui.QWidget(Sun)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_4 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        spacerItem = QtGui.QSpacerItem(58, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 2, 1, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setStyleSheet(_fromUtf8("background-color: rgb(176, 176, 176);"))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.layoutWidget = QtGui.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 191, 95))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.layoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.yBox = QtGui.QComboBox(self.layoutWidget)
        self.yBox.setObjectName(_fromUtf8("yBox"))
        self.yBox.addItem(_fromUtf8(""))
        self.yBox.addItem(_fromUtf8(""))
        self.yBox.addItem(_fromUtf8(""))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.yBox)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.mBox = QtGui.QComboBox(self.layoutWidget)
        self.mBox.setObjectName(_fromUtf8("mBox"))
        self.mBox.addItem(_fromUtf8(""))
        self.mBox.addItem(_fromUtf8(""))
        self.mBox.addItem(_fromUtf8(""))
        self.mBox.addItem(_fromUtf8(""))
        self.mBox.addItem(_fromUtf8(""))
        self.mBox.addItem(_fromUtf8(""))
        self.mBox.addItem(_fromUtf8(""))
        self.mBox.addItem(_fromUtf8(""))
        self.mBox.addItem(_fromUtf8(""))
        self.mBox.addItem(_fromUtf8(""))
        self.mBox.addItem(_fromUtf8(""))
        self.mBox.addItem(_fromUtf8(""))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.mBox)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.dBox = QtGui.QComboBox(self.layoutWidget)
        self.dBox.setObjectName(_fromUtf8("dBox"))
        self.dBox.addItem(_fromUtf8(""))
        self.dBox.addItem(_fromUtf8(""))
        self.dBox.addItem(_fromUtf8(""))
        self.dBox.addItem(_fromUtf8(""))
        self.dBox.addItem(_fromUtf8(""))
        self.dBox.addItem(_fromUtf8(""))
        self.dBox.addItem(_fromUtf8(""))
        self.dBox.addItem(_fromUtf8(""))
        self.dBox.addItem(_fromUtf8(""))
        self.dBox.addItem(_fromUtf8(""))
        self.dBox.addItem(_fromUtf8(""))
        self.dBox.addItem(_fromUtf8(""))
        self.dBox.addItem(_fromUtf8(""))
        self.dBox.addItem(_fromUtf8(""))
        self.dBox.addItem(_fromUtf8(""))
        self.dBox.addItem(_fromUtf8(""))
        self.dBox.addItem(_fromUtf8(""))
        self.dBox.addItem(_fromUtf8(""))
        self.dBox.addItem(_fromUtf8(""))
        self.dBox.addItem(_fromUtf8(""))
        self.dBox.addItem(_fromUtf8(""))
        self.dBox.addItem(_fromUtf8(""))
        self.dBox.addItem(_fromUtf8(""))
        self.dBox.addItem(_fromUtf8(""))
        self.dBox.addItem(_fromUtf8(""))
        self.dBox.addItem(_fromUtf8(""))
        self.dBox.addItem(_fromUtf8(""))
        self.dBox.addItem(_fromUtf8(""))
        self.dBox.addItem(_fromUtf8(""))
        self.dBox.addItem(_fromUtf8(""))
        self.dBox.addItem(_fromUtf8(""))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.dBox)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.cButton = QtGui.QPushButton(self.centralwidget)
        self.cButton.setObjectName(_fromUtf8("cButton"))
        self.verticalLayout.addWidget(self.cButton)
        self.rButton = QtGui.QPushButton(self.centralwidget)
        self.rButton.setObjectName(_fromUtf8("rButton"))
        self.verticalLayout.addWidget(self.rButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem3 = QtGui.QSpacerItem(20, 58, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setStyleSheet(_fromUtf8("background-color: rgb(176, 176, 176);"))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.hEdit = QtGui.QLineEdit(self.groupBox_2)
        self.hEdit.setObjectName(_fromUtf8("hEdit"))
        self.horizontalLayout.addWidget(self.hEdit)
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_5)
        self.mEdit = QtGui.QLineEdit(self.groupBox_2)
        self.mEdit.setObjectName(_fromUtf8("mEdit"))
        self.horizontalLayout.addWidget(self.mEdit)
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout.addWidget(self.label_6)
        self.sEdit = QtGui.QLineEdit(self.groupBox_2)
        self.sEdit.setObjectName(_fromUtf8("sEdit"))
        self.horizontalLayout.addWidget(self.sEdit)
        self.gridLayout.addWidget(self.groupBox_2, 2, 0, 1, 2)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 198, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_2.addWidget(self.label_7)
        spacerItem6 = QtGui.QSpacerItem(208, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 2)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 1, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem7, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        Sun.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Sun)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 433, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        Sun.setMenuBar(self.menubar)
        self.menubar.addAction(self.menu_File.menuAction())

        self.retranslateUi(Sun)
        QtCore.QObject.connect(self.rButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.hEdit.clear)
        QtCore.QObject.connect(self.rButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.mEdit.clear)
        QtCore.QObject.connect(self.rButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sEdit.clear)
        QtCore.QObject.connect(self.cButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Sun.caculate)
        QtCore.QMetaObject.connectSlotsByName(Sun)

    def retranslateUi(self, Sun):
        Sun.setWindowTitle(_translate("Sun", "Sun Caculate", None))
        self.groupBox.setTitle(_translate("Sun", "Date", None))
        self.label.setText(_translate("Sun", "Year", None))
        self.yBox.setItemText(0, _translate("Sun", "1990", None))
        self.yBox.setItemText(1, _translate("Sun", "1991", None))
        self.yBox.setItemText(2, _translate("Sun", "1992", None))
        self.label_2.setText(_translate("Sun", "Month", None))
        self.mBox.setItemText(0, _translate("Sun", "1", None))
        self.mBox.setItemText(1, _translate("Sun", "2", None))
        self.mBox.setItemText(2, _translate("Sun", "3", None))
        self.mBox.setItemText(3, _translate("Sun", "4", None))
        self.mBox.setItemText(4, _translate("Sun", "5", None))
        self.mBox.setItemText(5, _translate("Sun", "6", None))
        self.mBox.setItemText(6, _translate("Sun", "7", None))
        self.mBox.setItemText(7, _translate("Sun", "8", None))
        self.mBox.setItemText(8, _translate("Sun", "9", None))
        self.mBox.setItemText(9, _translate("Sun", "10", None))
        self.mBox.setItemText(10, _translate("Sun", "11", None))
        self.mBox.setItemText(11, _translate("Sun", "12", None))
        self.label_3.setText(_translate("Sun", "Day", None))
        self.dBox.setItemText(0, _translate("Sun", "1", None))
        self.dBox.setItemText(1, _translate("Sun", "2", None))
        self.dBox.setItemText(2, _translate("Sun", "3", None))
        self.dBox.setItemText(3, _translate("Sun", "4", None))
        self.dBox.setItemText(4, _translate("Sun", "5", None))
        self.dBox.setItemText(5, _translate("Sun", "6", None))
        self.dBox.setItemText(6, _translate("Sun", "7", None))
        self.dBox.setItemText(7, _translate("Sun", "8", None))
        self.dBox.setItemText(8, _translate("Sun", "9", None))
        self.dBox.setItemText(9, _translate("Sun", "10", None))
        self.dBox.setItemText(10, _translate("Sun", "11", None))
        self.dBox.setItemText(11, _translate("Sun", "12", None))
        self.dBox.setItemText(12, _translate("Sun", "13", None))
        self.dBox.setItemText(13, _translate("Sun", "14", None))
        self.dBox.setItemText(14, _translate("Sun", "15", None))
        self.dBox.setItemText(15, _translate("Sun", "16", None))
        self.dBox.setItemText(16, _translate("Sun", "17", None))
        self.dBox.setItemText(17, _translate("Sun", "18", None))
        self.dBox.setItemText(18, _translate("Sun", "19", None))
        self.dBox.setItemText(19, _translate("Sun", "20", None))
        self.dBox.setItemText(20, _translate("Sun", "21", None))
        self.dBox.setItemText(21, _translate("Sun", "22", None))
        self.dBox.setItemText(22, _translate("Sun", "23", None))
        self.dBox.setItemText(23, _translate("Sun", "24", None))
        self.dBox.setItemText(24, _translate("Sun", "25", None))
        self.dBox.setItemText(25, _translate("Sun", "26", None))
        self.dBox.setItemText(26, _translate("Sun", "27", None))
        self.dBox.setItemText(27, _translate("Sun", "28", None))
        self.dBox.setItemText(28, _translate("Sun", "29", None))
        self.dBox.setItemText(29, _translate("Sun", "30", None))
        self.dBox.setItemText(30, _translate("Sun", "New Item", None))
        self.cButton.setText(_translate("Sun", "Caculate", None))
        self.rButton.setText(_translate("Sun", "Reset", None))
        self.groupBox_2.setTitle(_translate("Sun", "Time", None))
        self.label_4.setText(_translate("Sun", "Hour", None))
        self.label_5.setText(_translate("Sun", "Minute", None))
        self.label_6.setText(_translate("Sun", "Second", None))
        self.label_7.setText(_translate("Sun", "The Position of the Sun:", None))
        self.menu_File.setTitle(_translate("Sun", "&File", None))

