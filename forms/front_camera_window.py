# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'front_camera_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from resources import resources


class Ui_FrontCameraWindow(object):
    def setupUi(self, FrontCameraWindow):
        FrontCameraWindow.setObjectName("FrontCameraWindow")
        FrontCameraWindow.resize(1024, 540)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FrontCameraWindow.sizePolicy().hasHeightForWidth())
        FrontCameraWindow.setSizePolicy(sizePolicy)
        FrontCameraWindow.setMouseTracking(False)
        FrontCameraWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        FrontCameraWindow.setAnimated(True)
        FrontCameraWindow.setDocumentMode(False)
        FrontCameraWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralWidget = QtWidgets.QWidget(FrontCameraWindow)
        self.centralWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralWidget.setObjectName("centralWidget")
        self.Sequence_Photos = QtWidgets.QPushButton(self.centralWidget)
        self.Sequence_Photos.setGeometry(QtCore.QRect(540, 195, 150, 150))
        self.Sequence_Photos.setStyleSheet("#Sequence_Photos{background:#fe022c url(:/images/desktop.png)}")
        self.Sequence_Photos.setText("")
        self.Sequence_Photos.setObjectName("Sequence_Photos")
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
        self.Take_Photo = QtWidgets.QPushButton(self.centralWidget)
        self.Take_Photo.setGeometry(QtCore.QRect(333, 195, 150, 150))
        self.Take_Photo.setStyleSheet("#Take_Photo{background:#26d8fc url(:/images/camera.png)}")
        self.Take_Photo.setText("")
        self.Take_Photo.setObjectName("Take_Photo")
        self.label_9 = QtWidgets.QLabel(self.centralWidget)
        self.label_9.setGeometry(QtCore.QRect(540, 355, 181, 31))
        self.label_9.setObjectName("label_9")
        FrontCameraWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(FrontCameraWindow)
        self.Back.clicked.connect(FrontCameraWindow.close)
        QtCore.QMetaObject.connectSlotsByName(FrontCameraWindow)
        FrontCameraWindow.setTabOrder(self.Sequence_Photos, self.Back)

    def retranslateUi(self, FrontCameraWindow):
        _translate = QtCore.QCoreApplication.translate
        FrontCameraWindow.setWindowTitle(_translate("FrontCameraWindow", "CarPi"))
        self.label_7.setText(_translate("FrontCameraWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Cofnij</span></p><p><br/></p></body></html>"))
        self.label_8.setText(_translate("FrontCameraWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Zrób zdjęcie</span></p><p><br/></p></body></html>"))
        self.label_9.setText(_translate("FrontCameraWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Seria zdjęć (20)</span></p><p><br/></p></body></html>"))
