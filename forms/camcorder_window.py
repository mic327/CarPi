# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camcorder_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from resources import resources

class Ui_CamcorderWindow(object):
    def setupUi(self, CamcorderWindow):
        CamcorderWindow.setObjectName("CamcorderWindow")
        CamcorderWindow.resize(1024, 540)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CamcorderWindow.sizePolicy().hasHeightForWidth())
        CamcorderWindow.setSizePolicy(sizePolicy)
        CamcorderWindow.setMouseTracking(False)
        CamcorderWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        CamcorderWindow.setAnimated(True)
        CamcorderWindow.setDocumentMode(False)
        CamcorderWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralWidget = QtWidgets.QWidget(CamcorderWindow)
        self.centralWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralWidget.setObjectName("centralWidget")
        self.Back = QtWidgets.QPushButton(self.centralWidget)
        self.Back.setGeometry(QtCore.QRect(860, 350, 150, 150))
        self.Back.setStyleSheet("#Back{background:#168c24 url(:/images/back.png)}")
        self.Back.setText("")
        self.Back.setObjectName("Back")
        self.Front_Camcorder = QtWidgets.QPushButton(self.centralWidget)
        self.Front_Camcorder.setGeometry(QtCore.QRect(333, 195, 150, 150))
        self.Front_Camcorder.setStyleSheet("#Front_Camcorder{background:#8214d0 url(:/images/camcorder.png)}")
        self.Front_Camcorder.setText("")
        self.Front_Camcorder.setObjectName("Front_Camcorder")
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setGeometry(QtCore.QRect(333, 355, 181, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralWidget)
        self.label_8.setGeometry(QtCore.QRect(540, 355, 181, 31))
        self.label_8.setObjectName("label_8")
        self.Back_Camcorder = QtWidgets.QPushButton(self.centralWidget)
        self.Back_Camcorder.setGeometry(QtCore.QRect(540, 195, 150, 150))
        self.Back_Camcorder.setStyleSheet("#Back_Camcorder{background:#26d8fc url(:/images/camera.png)}")
        self.Back_Camcorder.setText("")
        self.Back_Camcorder.setObjectName("Back_Camcorder")
        self.label_9 = QtWidgets.QLabel(self.centralWidget)
        self.label_9.setGeometry(QtCore.QRect(860, 510, 181, 31))
        self.label_9.setObjectName("label_9")
        CamcorderWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(CamcorderWindow)
        self.Back.clicked.connect(CamcorderWindow.close)
        QtCore.QMetaObject.connectSlotsByName(CamcorderWindow)
        CamcorderWindow.setTabOrder(self.Back, self.Front_Camcorder)

    def retranslateUi(self, CamcorderWindow):
        _translate = QtCore.QCoreApplication.translate
        CamcorderWindow.setWindowTitle(_translate("CamcorderWindow", "CarPi"))
        self.label_7.setText(_translate("CamcorderWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Rejestrator</span></p></body></html>"))
        self.label_8.setText(_translate("CamcorderWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Kamera cofania</span></p><p><br/></p></body></html>"))
        self.label_9.setText(_translate("CamcorderWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Cofnij</span></p><p><br/></p></body></html>"))
