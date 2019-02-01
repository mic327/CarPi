import os 
import sys
from PyQt5.QtCore import *
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


#importuje pliki klas
from classes.SlotsAndSignals import MainWindow

def main():
	CarPi = QApplication(sys.argv)
	CarPi.setStyleSheet(open("/home/pi/Desktop/CarPi/resources/style.qss", "r").read())

	
	SplashPixmap=QPixmap("/home/pi/Desktop/CarPi/splash.png")
	Splash=QSplashScreen(SplashPixmap)
	Splash.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
	Splash.show()

	MainWindowForm = MainWindow()
	MainWindowForm.setWindowFlags(QtCore.Qt.FramelessWindowHint)	#usuwam pasek okna (minimalzacja, zamykanie etc) 
	MainWindowForm.show()	#wyświetlam formularz
			

					

	sys.exit(CarPi.exec_())
	

main()
