# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MP3_player_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from resources import resources


class Ui_MP3PlayerWindow(object):
    def setupUi(self, MP3PlayerWindow):
        MP3PlayerWindow.setObjectName("MP3PlayerWindow")
        MP3PlayerWindow.resize(1024, 540)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MP3PlayerWindow.sizePolicy().hasHeightForWidth())
        MP3PlayerWindow.setSizePolicy(sizePolicy)
        MP3PlayerWindow.setMouseTracking(False)
        MP3PlayerWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MP3PlayerWindow.setAnimated(True)
        MP3PlayerWindow.setDocumentMode(False)
        MP3PlayerWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralWidget = QtWidgets.QWidget(MP3PlayerWindow)
        self.centralWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralWidget.setObjectName("centralWidget")
        self.Playlist = QtWidgets.QPushButton(self.centralWidget)
        self.Playlist.setGeometry(QtCore.QRect(644, 195, 150, 150))
        self.Playlist.setStyleSheet("#Playlist{background:#016285 url(:/images/playlist.png)}")
        self.Playlist.setText("")
        self.Playlist.setObjectName("Playlist")
        self.Pendrive = QtWidgets.QPushButton(self.centralWidget)
        self.Pendrive.setGeometry(QtCore.QRect(230, 195, 150, 150))
        self.Pendrive.setStyleSheet("#Pendrive{background:#26d8fc url(:/images/pendrive.png)}")
        self.Pendrive.setText("")
        self.Pendrive.setObjectName("Pendrive")
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setGeometry(QtCore.QRect(230, 355, 181, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralWidget)
        self.label_8.setGeometry(QtCore.QRect(437, 355, 181, 31))
        self.label_8.setObjectName("label_8")
        self.Memory_Card = QtWidgets.QPushButton(self.centralWidget)
        self.Memory_Card.setGeometry(QtCore.QRect(437, 195, 150, 150))
        self.Memory_Card.setStyleSheet("#Memory_Card{background:#8214d0 url(:/images/memory_card.png)}")
        self.Memory_Card.setText("")
        self.Memory_Card.setObjectName("Memory_Card")
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
        self.label_11 = QtWidgets.QLabel(self.centralWidget)
        self.label_11.setGeometry(QtCore.QRect(110, 150, 201, 31))
        self.label_11.setObjectName("label_11")
        MP3PlayerWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MP3PlayerWindow)
        self.Back.clicked.connect(MP3PlayerWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MP3PlayerWindow)
        MP3PlayerWindow.setTabOrder(self.Playlist, self.Pendrive)

    def retranslateUi(self, MP3PlayerWindow):
        _translate = QtCore.QCoreApplication.translate
        MP3PlayerWindow.setWindowTitle(_translate("MP3PlayerWindow", "CarPi"))
        self.label_7.setText(_translate("MP3PlayerWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Pendrive</span></p></body></html>"))
        self.label_8.setText(_translate("MP3PlayerWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Karta pamięci</span></p></body></html>"))
        self.label_9.setText(_translate("MP3PlayerWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Playlista</span></p></body></html>"))
        self.label_10.setText(_translate("MP3PlayerWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Cofnij</span></p><p><br/></p></body></html>"))
        self.label_11.setText(_translate("MP3PlayerWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Odtwarzaj muzykę z...</span></p></body></html>"))

