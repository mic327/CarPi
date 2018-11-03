# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'radio_play_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from resources import resources


class Ui_RadioPlayWindow(object):
    def setupUi(self, RadioPlayWindow):
        RadioPlayWindow.setObjectName("RadioPlayWindow")
        RadioPlayWindow.resize(1024, 540)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RadioPlayWindow.sizePolicy().hasHeightForWidth())
        RadioPlayWindow.setSizePolicy(sizePolicy)
        RadioPlayWindow.setMouseTracking(False)
        RadioPlayWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        RadioPlayWindow.setAnimated(True)
        RadioPlayWindow.setDocumentMode(False)
        RadioPlayWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralWidget = QtWidgets.QWidget(RadioPlayWindow)
        self.centralWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralWidget.setObjectName("centralWidget")
        self.Back = QtWidgets.QPushButton(self.centralWidget)
        self.Back.setGeometry(QtCore.QRect(860, 350, 150, 150))
        self.Back.setStyleSheet("#Back{background:#168c24 url(:/images/back.png)}")
        self.Back.setText("")
        self.Back.setObjectName("Back")
        self.label_10 = QtWidgets.QLabel(self.centralWidget)
        self.label_10.setGeometry(QtCore.QRect(860, 510, 181, 31))
        self.label_10.setObjectName("label_10")
        RadioPlayWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(RadioPlayWindow)
        self.Back.clicked.connect(RadioPlayWindow.close)
        QtCore.QMetaObject.connectSlotsByName(RadioPlayWindow)

    def retranslateUi(self, RadioPlayWindow):
        _translate = QtCore.QCoreApplication.translate
        RadioPlayWindow.setWindowTitle(_translate("RadioPlayWindow", "CarPi"))
        self.label_10.setText(_translate("RadioPlayWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Cofnij</span></p><p><br/></p></body></html>"))

