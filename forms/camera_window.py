# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camera_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from resources import resources


class Ui_CameraWindow(object):
    def setupUi(self, CameraWindow):
        CameraWindow.setObjectName("CameraWindow")
        CameraWindow.resize(1024, 540)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CameraWindow.sizePolicy().hasHeightForWidth())
        CameraWindow.setSizePolicy(sizePolicy)
        CameraWindow.setMouseTracking(False)
        CameraWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        CameraWindow.setAnimated(True)
        CameraWindow.setDocumentMode(False)
        CameraWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralWidget = QtWidgets.QWidget(CameraWindow)
        self.centralWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralWidget.setObjectName("centralWidget")
        self.Back = QtWidgets.QPushButton(self.centralWidget)
        self.Back.setGeometry(QtCore.QRect(860, 350, 150, 150))
        self.Back.setStyleSheet("#Back{background:#168c24 url(:/images/back.png)}")
        self.Back.setText("")
        self.Back.setObjectName("Back")
        self.Front_Camera = QtWidgets.QPushButton(self.centralWidget)
        self.Front_Camera.setGeometry(QtCore.QRect(333, 195, 150, 150))
        self.Front_Camera.setStyleSheet("#Front_Camera{background:#8214d0 url(:/images/camcorder.png)}")
        self.Front_Camera.setText("")
        self.Front_Camera.setObjectName("Front_Camera")
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setGeometry(QtCore.QRect(333, 355, 181, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralWidget)
        self.label_8.setGeometry(QtCore.QRect(540, 355, 181, 31))
        self.label_8.setObjectName("label_8")
        self.Back_Camera = QtWidgets.QPushButton(self.centralWidget)
        self.Back_Camera.setGeometry(QtCore.QRect(540, 195, 150, 150))
        self.Back_Camera.setStyleSheet("#Back_Camera{background:#26d8fc url(:/images/camera.png)}")
        self.Back_Camera.setText("")
        self.Back_Camera.setObjectName("Back_Camera")
        self.label_9 = QtWidgets.QLabel(self.centralWidget)
        self.label_9.setGeometry(QtCore.QRect(860, 510, 181, 31))
        self.label_9.setObjectName("label_9")
        CameraWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(CameraWindow)
        self.Back.clicked.connect(CameraWindow.close)
        QtCore.QMetaObject.connectSlotsByName(CameraWindow)
        CameraWindow.setTabOrder(self.Back, self.Front_Camera)

    def retranslateUi(self, CameraWindow):
        _translate = QtCore.QCoreApplication.translate
        CameraWindow.setWindowTitle(_translate("CameraWindow", "CarPi"))
        self.label_7.setText(_translate("CameraWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Aparat przedni</span></p></body></html>"))
        self.label_8.setText(_translate("CameraWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Aparat tylny</span></p><p><br/></p></body></html>"))
        self.label_9.setText(_translate("CameraWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Cofnij</span></p><p><br/></p></body></html>"))

