# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'front_camcorder_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from resources import resources


class Ui_FrontCamcorderWindow(object):
    def setupUi(self, FrontCamcorderWindow):
        FrontCamcorderWindow.setObjectName("FrontCamcorderWindow")
        FrontCamcorderWindow.resize(1024, 540)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FrontCamcorderWindow.sizePolicy().hasHeightForWidth())
        FrontCamcorderWindow.setSizePolicy(sizePolicy)
        FrontCamcorderWindow.setMouseTracking(False)
        FrontCamcorderWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        FrontCamcorderWindow.setAnimated(True)
        FrontCamcorderWindow.setDocumentMode(False)
        FrontCamcorderWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralWidget = QtWidgets.QWidget(FrontCamcorderWindow)
        self.centralWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralWidget.setObjectName("centralWidget")
        self.Start_Record = QtWidgets.QPushButton(self.centralWidget)
        self.Start_Record.setGeometry(QtCore.QRect(644, 195, 150, 150))
        self.Start_Record.setStyleSheet("#Start_Record{background:#13de00 url(:/images/record.png)}")
        self.Start_Record.setText("")
        self.Start_Record.setObjectName("Start_Record")
        self.Preview_Front_Camcorder = QtWidgets.QPushButton(self.centralWidget)
        self.Preview_Front_Camcorder.setGeometry(QtCore.QRect(230, 195, 150, 150))
        self.Preview_Front_Camcorder.setStyleSheet("#Preview_Front_Camcorder{background:#26d8fc url(:/images/camera.png)}")
        self.Preview_Front_Camcorder.setText("")
        self.Preview_Front_Camcorder.setObjectName("Preview_Front_Camcorder")
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setGeometry(QtCore.QRect(230, 355, 181, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralWidget)
        self.label_8.setGeometry(QtCore.QRect(437, 355, 181, 31))
        self.label_8.setObjectName("label_8")
        self.Stop_Record = QtWidgets.QPushButton(self.centralWidget)
        self.Stop_Record.setGeometry(QtCore.QRect(437, 195, 150, 150))
        self.Stop_Record.setStyleSheet("#Stop_Record{background:#fe022c url(:/images/stop.png)}")
        self.Stop_Record.setText("")
        self.Stop_Record.setObjectName("Stop_Record")
        self.label_9 = QtWidgets.QLabel(self.centralWidget)
        self.label_9.setGeometry(QtCore.QRect(644, 355, 181, 31))
        self.label_9.setObjectName("label_9")
        self.Back = QtWidgets.QPushButton(self.centralWidget)
        self.Back.setGeometry(QtCore.QRect(860, 350, 150, 150))
        self.Back.setStyleSheet("#Back{background:#168c24 url(:/images/back.png)}")
        self.Back.setText("")
        self.Back.setObjectName("Back")
        self.label_10 = QtWidgets.QLabel(self.centralWidget)
        self.label_10.setGeometry(QtCore.QRect(860, 510, 181, 31))
        self.label_10.setObjectName("label_10")
        FrontCamcorderWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(FrontCamcorderWindow)
        self.Back.clicked.connect(FrontCamcorderWindow.close)
        QtCore.QMetaObject.connectSlotsByName(FrontCamcorderWindow)
        FrontCamcorderWindow.setTabOrder(self.Start_Record, self.Preview_Front_Camcorder)

    def retranslateUi(self, FrontCamcorderWindow):
        _translate = QtCore.QCoreApplication.translate
        FrontCamcorderWindow.setWindowTitle(_translate("FrontCamcorderWindow", "CarPi"))
        self.label_7.setText(_translate("FrontCamcorderWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Podgląd</span></p></body></html>"))
        self.label_8.setText(_translate("FrontCamcorderWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Wyłącz nagrywanie</span></p></body></html>"))
        self.label_9.setText(_translate("FrontCamcorderWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Włącz nagrywanie</span></p></body></html>"))
        self.label_10.setText(_translate("FrontCamcorderWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Cofnij</span></p><p><br/></p></body></html>"))

