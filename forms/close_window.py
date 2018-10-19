# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'close_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from resources import resources


class Ui_CloseWindow(object):
    def setupUi(self, CloseWindow):
        CloseWindow.setObjectName("CloseWindow")
        CloseWindow.resize(1024, 540)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CloseWindow.sizePolicy().hasHeightForWidth())
        CloseWindow.setSizePolicy(sizePolicy)
        CloseWindow.setMouseTracking(False)
        CloseWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        CloseWindow.setAnimated(True)
        CloseWindow.setDocumentMode(False)
        CloseWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralWidget = QtWidgets.QWidget(CloseWindow)
        self.centralWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralWidget.setObjectName("centralWidget")
        self.Restart = QtWidgets.QPushButton(self.centralWidget)
        self.Restart.setGeometry(QtCore.QRect(540, 195, 150, 150))
        self.Restart.setStyleSheet("#Restart{background:#fe022c url(:/images/close.png)}")
        self.Restart.setText("")
        self.Restart.setObjectName("Restart")
        self.Back = QtWidgets.QPushButton(self.centralWidget)
        self.Back.setGeometry(QtCore.QRect(860, 350, 150, 150))
        self.Back.setStyleSheet("#Back{background:#168c24 url(:/images/back.png)}")
        self.Back.setText("")
        self.Back.setObjectName("Back")
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setGeometry(QtCore.QRect(860, 510, 181, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralWidget)
        self.label_8.setGeometry(QtCore.QRect(333, 355, 181, 31))
        self.label_8.setObjectName("label_8")
        self.Desktop = QtWidgets.QPushButton(self.centralWidget)
        self.Desktop.setGeometry(QtCore.QRect(333, 195, 150, 150))
        self.Desktop.setStyleSheet("#Desktop{background:#bd74f2 url(:/images/desktop.png)}")
        self.Desktop.setText("")
        self.Desktop.setObjectName("Desktop")
        self.label_9 = QtWidgets.QLabel(self.centralWidget)
        self.label_9.setGeometry(QtCore.QRect(540, 355, 181, 31))
        self.label_9.setObjectName("label_9")
        CloseWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(CloseWindow)
        self.Back.clicked.connect(CloseWindow.close)
        QtCore.QMetaObject.connectSlotsByName(CloseWindow)
        CloseWindow.setTabOrder(self.Restart, self.Back)

    def retranslateUi(self, CloseWindow):
        _translate = QtCore.QCoreApplication.translate
        CloseWindow.setWindowTitle(_translate("CloseWindow", "CarPi"))
        self.label_7.setText(_translate("CloseWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Cofnij</span></p><p><br/></p></body></html>"))
        self.label_8.setText(_translate("CloseWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Pulpit</span></p><p><br/></p></body></html>"))
        self.label_9.setText(_translate("CloseWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Uruchom ponownie</span></p><p><br/></p></body></html>"))

