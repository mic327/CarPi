# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from resources import resources


class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.resize(1024, 540)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingsWindow.sizePolicy().hasHeightForWidth())
        SettingsWindow.setSizePolicy(sizePolicy)
        SettingsWindow.setMouseTracking(False)
        SettingsWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        SettingsWindow.setAnimated(True)
        SettingsWindow.setDocumentMode(False)
        SettingsWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralWidget = QtWidgets.QWidget(SettingsWindow)
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
        self.Save = QtWidgets.QPushButton(self.centralWidget)
        self.Save.setGeometry(QtCore.QRect(860, 160, 150, 150))
        self.Save.setStyleSheet("#Save{background:#016285 url(:/images/save.png)}")
        self.Save.setText("")
        self.Save.setObjectName("Save")
        self.label_12 = QtWidgets.QLabel(self.centralWidget)
        self.label_12.setGeometry(QtCore.QRect(860, 320, 181, 31))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralWidget)
        self.label_13.setGeometry(QtCore.QRect(100, 90, 271, 31))
        self.label_13.setObjectName("label_13")
        self.SortOrder = QtWidgets.QComboBox(self.centralWidget)
        self.SortOrder.setGeometry(QtCore.QRect(140, 115, 241, 25))
        self.SortOrder.setObjectName("SortOrder")
        self.SliderVolume = QtWidgets.QSlider(self.centralWidget)
        self.SliderVolume.setGeometry(QtCore.QRect(140, 220, 160, 16))
        self.SliderVolume.setOrientation(QtCore.Qt.Horizontal)
        self.SliderVolume.setObjectName("SliderVolume")
        self.label_14 = QtWidgets.QLabel(self.centralWidget)
        self.label_14.setGeometry(QtCore.QRect(100, 170, 271, 31))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralWidget)
        self.label_15.setGeometry(QtCore.QRect(140, 200, 160, 31))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralWidget)
        self.label_16.setGeometry(QtCore.QRect(140, 240, 160, 31))
        self.label_16.setObjectName("label_16")
        self.SliderBrightness = QtWidgets.QSlider(self.centralWidget)
        self.SliderBrightness.setGeometry(QtCore.QRect(140, 260, 160, 16))
        self.SliderBrightness.setOrientation(QtCore.Qt.Horizontal)
        self.SliderBrightness.setObjectName("SliderBrightness")
        SettingsWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(SettingsWindow)
        self.Back.clicked.connect(SettingsWindow.close)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

    def retranslateUi(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "CarPi"))
        self.label_10.setText(_translate("SettingsWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Cofnij</span></p><p><br/></p></body></html>"))
        self.label_12.setText(_translate("SettingsWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Zapisz</span></p><p><br/></p></body></html>"))
        self.label_13.setText(_translate("SettingsWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Sortowanie stacji radiowych wg:</span></p><p><br/></p></body></html>"))
        self.label_14.setText(_translate("SettingsWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Parametry startowe:</span></p><p><br/></p></body></html>"))
        self.label_15.setText(_translate("SettingsWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Domyślna głośność:</span></p><p><br/></p></body></html>"))
        self.label_16.setText(_translate("SettingsWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Domyślna jasność:</span></p><p><br/></p></body></html>"))

