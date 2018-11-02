#jeśli dodaję się lub usuwa stację z ulubionych nie powinno być uruchamiane polecenie rtl_fm | aplay kolejny raz!!
#kombinacja plus/minus z ulubionych stacji coś nie działa w połączeniu z nagrywaniem stacji, do sprawdzenia!
import os 
import sys
from PyQt5.QtCore import *
from PyQt5 import *
from PyQt5.QtWidgets import *

#importuje pliki klas
from classes.SlotsAndSignals import MainWindow

def main():
	CarPi = QApplication(sys.argv)
	MainWindowForm = MainWindow()

	MainWindowForm.setWindowFlags(QtCore.Qt.FramelessWindowHint)   #usuwam pasek okna (minimalzacja, zamykanie etc) 
	MainWindowForm.show()      #wyświetlam formularz
 
	#bez tego skrypt odrazu się zamknie
	sys.exit(CarPi.exec_())
	

# python bit to figure how who started This
if __name__ == "__main__":
	main()
