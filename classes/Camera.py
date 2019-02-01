from PyQt5.QtCore import QThread, QObject, pyqtSignal
import cv2
from PyQt5 import *
from PyQt5.QtGui import QPixmap
import os
from pathlib import Path
import datetime


#klasa Camera dziedziczy po QObject, aby była możliwość wykorzystania slotów i sygnałów
#nagrywanie, będzie dostepne później
class Camera(QObject):
	def __init__(self,CameraDevice):
		super(self.__class__, self).__init__()
		self.CameraDevice=CameraDevice
	
	#sygnały przesyłane z wątku kamery do wątku głównego
	FinishedSignal = pyqtSignal()
	StreamSignal = pyqtSignal(QPixmap)	

	def startCamcorderStream(self): 
		#tworze tymczasowy plik, który rozpoczyna lub kończy stream z kamerki
		os.system('touch /home/pi/Desktop/CarPi/temp/stream')

		#inicjuję odpowiednią kamere
		Webcam = cv2.VideoCapture(self.CameraDevice)

		#ustalam rozdzielczość kamery
		Width = Webcam.set(3,640)
		Height = Webcam.set(4,480)

		while(True):
			#ReturnValue otrzyma True jeśli, ramka została poprawnie odczytana
			#jeśli otrzyma False
			#może to służyć do weryfikacji końca streamu?
			#Frame zawiera "ramkę" odczytaną z kamery
			ReturnValue, Frame = Webcam.read()
			
			#konwertuję ramkę z modelu kolorów BGR na model kolorów RGB
			rgbImage = cv2.cvtColor(Frame, cv2.COLOR_BGR2RGB)
			
			#tworzenie overlay
			#generuję datę i godzinę
			i = datetime.datetime.now()
			Date=("%s-%s-%s" % (i.day, i.month, i.year))
			Time=("%s:%s:%s" % (i.hour, i.minute, i.second))
			
			#wybor jednego z fontów przeznaczonych dla OpenCV
			Font = cv2.FONT_HERSHEY_SIMPLEX
			#obrazek, (x,y), Font, rozmiar(skalowanie względem rozmiaru fontu),
			#kolor w RGB (R,G,B), grubość linii, typ linii
			cv2.putText(rgbImage,Date,(490,445), Font, 0.6,(255,255,255),1,cv2.LINE_AA)
			cv2.putText(rgbImage,Time,(490,470), Font, 0.6,(255,255,255),1,cv2.LINE_AA)

			#wywołuje poniżej konstruktor klasy QImage
			#QImage(uchar *data, int width, int height, QImage::Format format,
			#QImageCleanupFunction cleanupFunction = nullptr, void *cleanupInfo = nullptr)
			QImageFrame = QtGui.QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0],
                                         QtGui.QImage.Format_RGB888)
			
			#konwertuję obiekt QImage na obiekt QPixmap?
			QPixmapFrame = QtGui.QPixmap.fromImage(QImageFrame)
			
			#wykorzystuję konstruktor QPixmap(const QPixmap &pixmap)
			Pixmap = QPixmap(QPixmapFrame)
			
			#skaluję obraz width, height
			ResizedPixmap = Pixmap.scaled(840, 540)
						
			#sprawdzam czy istnieje tymczasowy plik stream
			StreamFile = Path("/home/pi/Desktop/CarPi/temp/stream")
			if StreamFile.is_file():
				isStreaming=True
			else:
				isStreaming=False	
				
			#sprawdzam czy istnieje tymczasowy plik photo
			PhotoFile = Path("/home/pi/Desktop/CarPi/temp/photo")
			if PhotoFile.is_file():
				#jeśli plik istnieje to robię zdjęcie i usuwam plik temp/photo
				#generuję nazwę pliku zdjęcia
				i = datetime.datetime.now()
				PhotoTime=("%s-%s-%s-%s:%s:%s" % (i.day, i.month, i.year, i.hour, i.minute, i.second))
				#sprawdzam, z której kamery zrobione zdjęcie
				if(self.CameraDevice=="/dev/FrontCamcorder"):
					PhotoLocation="/home/pi/Pictures/FrontCamcorder/"+str(PhotoTime)+".png"
					#PhotoLocation="/home/pi/Pictures/"+str(PhotoTime)+".png"
				elif(self.CameraDevice=="/dev/BackCamcorder"):
					PhotoLocation="/home/pi/Pictures/BackCamcorder/"+str(PhotoTime)+".png"
					#PhotoLocation="/home/pi/Pictures/"+str(PhotoTime)+".png"
				cv2.imwrite(PhotoLocation,rgbImage)
				os.system("rm /home/pi/Desktop/CarPi/temp/photo")
			
			#emituję sygnał "StreamSignal", który zawiera w sobie 
			#gotową do wyświetlania ramkę w postaci obiektu QPixmap
			#ramka zostanie odebrana przez funkcję streamFromFrontWebcam() z klasy FrontCamcorderWindow
			#z pomocą tej funkcji zostanie "wklejona" do etykiety VideoLabel
			#a potem ta etykieta zostanie wyświetlona
			self.StreamSignal.emit(ResizedPixmap)
			
			#jeśli nie ma tymczasowego pliku stream
			#to zamykam proces streamowania
			if(isStreaming==False):
				#uwalniam zasoby kamery i zamykam wszystkie okna OpenCV
				Webcam.release()
				cv2.destroyAllWindows()	
				#wysyłam sygnał "FinishedSignal" do głównego wątku
				#w wyniku tego zamknie się wątek odpowiedzialny za streamowanie z kamery
				#ponieważ ten sygnał jest połączony z slotem QThread.quit()
				self.FinishedSignal.emit()
				#zamykam nieskończoną pętlę
				break


