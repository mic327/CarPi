# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FM_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from resources import resources


class Ui_FMWindow(object):
    def setupUi(self, FMWindow):
        FMWindow.setObjectName("FMWindow")
        FMWindow.resize(1024, 540)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FMWindow.sizePolicy().hasHeightForWidth())
        FMWindow.setSizePolicy(sizePolicy)
        FMWindow.setMouseTracking(False)
        FMWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        FMWindow.setAnimated(True)
        FMWindow.setDocumentMode(False)
        FMWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralWidget = QtWidgets.QWidget(FMWindow)
        self.centralWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralWidget.setObjectName("centralWidget")
        self.Search_Stations = QtWidgets.QPushButton(self.centralWidget)
        self.Search_Stations.setGeometry(QtCore.QRect(644, 195, 150, 150))
        self.Search_Stations.setStyleSheet("#Search_Stations{background:#016285 url(:/images/search.png)}")
        self.Search_Stations.setText("")
        self.Search_Stations.setObjectName("Search_Stations")
        self.Select_Station = QtWidgets.QPushButton(self.centralWidget)
        self.Select_Station.setGeometry(QtCore.QRect(230, 195, 150, 150))
        self.Select_Station.setStyleSheet("#Select_Station{background:#26d8fc url(:/images/radio.png)}")
        self.Select_Station.setText("")
        self.Select_Station.setObjectName("Select_Station")
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setGeometry(QtCore.QRect(230, 355, 181, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralWidget)
        self.label_8.setGeometry(QtCore.QRect(437, 355, 181, 31))
        self.label_8.setObjectName("label_8")
        self.Favourited_Stations = QtWidgets.QPushButton(self.centralWidget)
        self.Favourited_Stations.setGeometry(QtCore.QRect(437, 195, 150, 150))
        self.Favourited_Stations.setStyleSheet("#Favourited_Stations{background:#8214d0 url(:/images/favourited.png)}")
        self.Favourited_Stations.setText("")
        self.Favourited_Stations.setObjectName("Favourited_Stations")
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
        FMWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(FMWindow)
        self.Back.clicked.connect(FMWindow.close)
        QtCore.QMetaObject.connectSlotsByName(FMWindow)
        FMWindow.setTabOrder(self.Search_Stations, self.Select_Station)

    def retranslateUi(self, FMWindow):
        _translate = QtCore.QCoreApplication.translate
        FMWindow.setWindowTitle(_translate("FMWindow", "CarPi"))
        self.label_7.setText(_translate("FMWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Wszystkie stacje</span></p><p><br/></p></body></html>"))
        self.label_8.setText(_translate("FMWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Ulubione</span></p><p><br/></p></body></html>"))
        self.label_9.setText(_translate("FMWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Wyszukaj stację</span></p><p><br/></p></body></html>"))
        self.label_10.setText(_translate("FMWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Cofnij</span></p><p><br/></p></body></html>"))

