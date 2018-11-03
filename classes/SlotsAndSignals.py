#Klasa przechwouje wszystkie sloty i sygnały w aplikacji

#Moduły wbudowane
import os
from PyQt5.QtWidgets import *
from PyQt5 import *
import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QThread

#Moduły aplikacji
from forms import blank_window


#klasa odpowiadająca za główny ekran, czyli za forms/main_window.py
#pierwszy ekran po uruchomieniu aplikacji!
from forms import main_window
class MainWindow(QMainWindow, main_window.Ui_MainWindow):
#ten konstruktor nadpisuje konstruktor z klasy bazowej
#dlatego wywołujemy konstruktor z klasy bazowej z poziomu konstruktora klasy dziedziczącej
	def __init__(self):
		super().__init__()
		#wywołuję główną metodę piku formularza
		self.setupUi(self) # metoda zdefiniowana w pliku *.UI zamienionym na *.py, czyli w formularzu
		#przypisuje konkretną funkcję(slot) do przycisku i sygnał
		self.MP3_Player.clicked.connect(lambda: self.showMP3PlayerForm())
		self.FM_Radio.clicked.connect(lambda: self.showFMForm())
		self.Navigation.clicked.connect(lambda: self.startNavigation())
		self.Camcorder.clicked.connect(lambda: self.showCamcorderForm())
		self.Camera.clicked.connect(lambda: self.showCameraForm())
		self.Multimedia.clicked.connect(lambda: self.showMultimediaForm())
		self.Close.clicked.connect(lambda: self.showCloseForm())
		self.setStyleSheet(open("resources/style.qss", "r").read())
	
	#funkcję(sloty) do obsługi przycisków
	def showMP3PlayerForm(self):
		#tworzę obiekt klasy MusicWindow
		self.dialog = MusicWindow()
		#wyświetlam formualrz (pierwszy!) odtwarzacza muzyki
		#analogicznie działają funkcję niżej
		self.dialog.show()
	def showFMForm(self):
		self.dialog = FMWindow()
		self.dialog.show()
	def startNavigation(self):
		#uruchamiam nawigację navit
		os.system('navit') 
	def showCamcorderForm(self):
		self.dialog = CamcorderWindow()
		self.dialog.show()
	def showCameraForm(self):
		self.dialog = CameraWindow()
		self.dialog.show()
	def showMultimediaForm(self):
		self.dialog = MultimediaWindow()
		self.dialog.show()
	def showCloseForm(self):
		self.dialog = CloseWindow()
		self.dialog.show()


#Klasa odpowiadająca za MP3PlayerWindow czyli za forms/MP3_player_window.py
from forms import MP3_player_window
class MusicWindow(QMainWindow, MP3_player_window.Ui_MP3PlayerWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self) 
		
		#przypisuje konkretną funkcję do przycisku i sygnał
		self.Pendrive.clicked.connect(lambda: self.playPendrive())
		self.Memory_Card.clicked.connect(lambda: self.playMemoryCard())
		self.Playlist.clicked.connect(lambda: self.showPlaylist())
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setStyleSheet(open("resources/style.qss", "r").read()) 
	
	#funkcję(sloty) do obsługi przycisków
	def playPendrive(self):
		os.system('sudo pkill -9 aplay;sudo pkill -9 rtl_fm;vlc /media/pi/307E-6572 --fullscreen')
	def playMemoryCard(self):
		os.system('sudo pkill -9 aplay;sudo pkill -9 rtl_fm;vlc --no-media-library /home/pi/Music')
	def showPlaylist(self):
		self.dialog = PlaylistsWindow()
		self.dialog.show()


#Klasa odpowiadająca za FMWindow, czyli za forms/FM_window.py
#Wybranie przycisku "Wybierz stację" wywołuje klasę SelectFMWindow
#która najpierw rysuje pusty formularz
#potem rysuje na nim przyciski do uruchamiania stacji radiowych
#przyciski za pomocą klasy ListStations
from forms import FM_window
FMWindowList = 0
class FMWindow(QMainWindow, FM_window.Ui_FMWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self) # gets defined in the UI file
		
		#przypisuje konkretną funkcję do przycisku i sygnał
		self.Select_Station.clicked.connect(lambda: self.showSelectStationForm())
		self.Favourited_Stations.clicked.connect(lambda: self.showSelectFavouritedStationForm())
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		#otwieram plik ze stylami CSS
		#które ustalają wygląd elementów, analogicznie jak dla HTML
		self.setStyleSheet(open("resources/style.qss", "r").read()) 
	
	#funkcję(sloty) do obsługi przycisków
	def showSelectStationForm(self):
		global FMWindowList
		FMWindowList = SelectFMWindow('normal')
		FMWindowList.show()
	def showSelectFavouritedStationForm(self):
		#zmienna o zagięgu globalnym
		global FMWindowList
		FMWindowList = SelectFMWindow('favourited')
		FMWindowList.show()

#Klasa odpowiadająca za SelectFMWindow
#która najpierw rysuje pusty formularz
#potem rysuje na nim przyciski do uruchamiania stacji radiowych
#za pomocą klasy ListStations
#kind argument przekazany do rozróżnienia widoku na normalny i na widok ulubionych
#później ten argument będzie przekazany do klasy ListStations
#i na tej podstawie zostanie skonstruowane odpowiednie zapytanie do bazy
#zrobić najlepiej bez globalnej zmiennej offset!
from classes.ListStations import ListStations
#globalna zmienna
#offset dla rekordów z bazy
offset=0
#zmienna globala przechowuje nazwę aktualnie odtwarzanej stacji
StationPlayed=0
class SelectFMWindow(QMainWindow, blank_window.Ui_BlankWindow):
#w tym konstruktorze trzeba wywołać instancję klasy ListStations
#i przekazać do niej argument kind, aby wiedziała
#czy ma generować widok normalny czy widok ulubionych
	def __init__(self,kind):
		super(self.__class__, self).__init__()
		self.setupUi(self) 
		#tworzę obiekt, który zgodnie z argumentem kind stworzy odpowiedni widok
		self.setStyleSheet(open("resources/style.qss", "r").read()) 
		
		#dodaję napis Wszystkie stacje lub Ulubione stację
		if(kind=='normal'):
			self.test=QtWidgets.QLabel("sd",self)
			#parametry: x, y, width, height
			self.test.setGeometry(QtCore.QRect(80, 100, 181, 31))
			_translate = QtCore.QCoreApplication.translate
			self.test.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Wszystkie stacje:</span></p><p><br/></p></body></html>"))
			#wyświetlam etykietę
			self.test.show()
		else:
			self.test=QtWidgets.QLabel("sd",self)
			self.test.setGeometry(QtCore.QRect(80, 100, 181, 31))
			_translate = QtCore.QCoreApplication.translate
			self.test.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Ulubione stacje:</span></p><p><br/></p></body></html>"))
			self.test.show()
		
		self.ListStationsObject=ListStations(kind)

		#standardowe rysowanie przycisków
		#rysuje albo normalny widok albo widok ulubionych
		self.drawStationsButtons(kind,offset)
		
		#przypisuje konkretną funkcję do przycisku i sygnał
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
	
	#funkcję(sloty) do obsługi przycisków
	def playStation(self,sender,kind):
		global StationPlayed
		#pobieram z bazy częstotliwość stacja o danej nazwie (nazwa zawiera się w sender)
		Frequency=self.ListStationsObject.getStationFrequency(sender)
		FMPlayString="sudo pkill arecord;sudo pkill -9 aplay;sudo pkill -9 rtl_fm;sudo rtl_fm -f "+str(Frequency)+"e6 -s 200000 -r 48000 | aplay -r 48000 -f S16_LE &"
		#jeśli będzie otwierana ta sama stacja to nie zostanie ona ponownie uruchomiona
		#oraz nie zostanie zatrzmane nagrywanie
		#będzie działać w tle
		
		#drugi warunek wyklucza sytuację, gdy VLC zamknął aplay i rtl_fm
		#a mamy zamiar ponownie otworzyć tę samą stację
		#co przed uruchomieniem VLC
		#gdy get_pid() nie zwróci PID procesu aplay to self.isAplayRun=False
		self.AplayPID=RadioPlayWindow.get_pid(self,"aplay")
		self.isAplayRun=isinstance(self.AplayPID,int)
		if(StationPlayed!=sender or self.isAplayRun==False):
			os.system(FMPlayString)
			#zwiększam liczbę odtworzeń
			#stację wyświetlane są od najczęściej używanych
			CounterPlayed=self.ListStationsObject.increaseStationPlayed(sender)
		#obiekt klasy, która wyświetla końcowy formularz odtwarzania stacji
		#tj. ten z przyciskami: Dodaj do ulubionych/usuń z ulubionych
		#normalne/ulubione
		#nagrywaj/zatrzymaj nagrywanie
		self.dialog = RadioPlayWindow(sender,kind)
		#wyświetlam ten formularz
		self.dialog.show()
		#przypisuje aktualnie odtwarzaną stację do zmiennej globalnej
		StationPlayed=sender

	def showPreviousStations(self,kind,offset):
		#czyszczę poprzednie przyciski do stacji
		#czyszczę przyciski nawigacji (dalej, wstecz)
		self.cleanStationsButtons(kind)
		#rysuję przyciski do poprzednich stacji
		#rysuję przyciski nawigacji
		self.drawStationsButtons(kind,offset=offset-4)
	def showNextStations(self,kind,offset):
		#analogicznie jak w funkcji wyżej
		self.cleanStationsButtons(kind)
		self.drawStationsButtons(kind,offset=offset+4)
		#funkcja, która rysuję przyciski do stacji
		#oraz rysuję przyciski nawigacji
	def drawStationsButtons(self,kind,offset):
		#tworzę listę ze stacjami
		StationsList=self.ListStationsObject.getStationName(kind,offset)
		#rysuje przyciski ze stacjami
		offset_x=84
		self.i=0
		self.StationsListLength=len(StationsList)
		self.StationsListButtons=[]
		self.StationsListLabels=[]

		#tworzę przyciski dopóki są rekordy z bazy
		while self.StationsListLength>0:
			self.StationsListButtons.append(QPushButton(self))
			#parametry: x, y, width, height
			self.StationsListButtons[self.i].setGeometry(QtCore.QRect(offset_x, 150, 150, 150))
			#wygląd przycisku uruchamiającego daną stację
			self.StationsListButtons[self.i].setStyleSheet("QPushButton{background:#26d8fc url(:/images/radio.png)}")
			#ustalam nazwę obiektu (czyli nazwę konkretnego przycisku)
			#ta nazwa będzie później wykorzystana w celu jednoznacznej identyfikacji
			#który konkretny przycisk wcisnął użytkownik
			#ta informacją posłuży do uruchomienia właściwej stacji
			self.StationsListButtons[self.i].setObjectName(StationsList[self.i])

			#dodaje rysowanie etykiet
			#analogicznie jak etykiety wyżej
			self.StationsListLabels.append(QtWidgets.QLabel("sd",self))
			self.StationsListLabels[self.i].setGeometry(QtCore.QRect(offset_x, 310, 181, 31))
			self.StationsListLabels[self.i].setObjectName(StationsList[self.i])
			_translate = QtCore.QCoreApplication.translate
			self.StationsListLabels[self.i].setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">"+StationsList[self.i]+"</span></p><p><br/></p></body></html>"))
			self.StationsListLabels[self.i].show()

			self.StationsListButtons[self.i].show()
			offset_x=offset_x+234
			self.StationsListLength=self.StationsListLength-1
			#połączenie sygnału, czyli wciśnięcia przycisku uruchamiającego daną stację
			#ze slotem, czyli funkcją, który zostanie wykonana po wciśnięciu tego przycisku
			#do funkcji playStation() z obecnej klasy zostanie przekazana nazwa obiektu (opisałem wyżej) oraz kind czyli rodzaj stacji
			#normalna lub ulubiona
			#za nazwę obiektu odpowiada: self.sender().objectName()
			self.StationsListButtons[self.i].clicked.connect(lambda: self.playStation(self.sender().objectName(),kind))
			self.i=self.i+1
			
			
		#sprawdzam ile jest wszystkich rekordów
		self.StationsCount=self.ListStationsObject.getCountStations(kind)
		#rysuję przycisk do przodu jeśli jest więcej wyników
		
		if(self.StationsCount>(offset+4)):
			self.ButtonNext=QPushButton(self)
			self.ButtonNext.setGeometry(QtCore.QRect(600, 350, 150, 150))
			self.ButtonNext.setStyleSheet("QPushButton{background:#168c24 url(:/images/forward.png)}")
			#dodaje rysowanie etykiet
			self.LabelForward=QtWidgets.QLabel("sd",self)
			self.LabelForward.setGeometry(QtCore.QRect(600, 510, 181, 31))
			_translate = QtCore.QCoreApplication.translate
			self.LabelForward.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Następne</span></p><p><br/></p></body></html>"))
			self.LabelForward.show()
			
			self.ButtonNext.show()
			self.ButtonNext.clicked.connect(lambda: self.showNextStations(kind,offset))
		else:
			#wykorzystanie exceptions (wyjątków)
			try:
				self.ButtonNext #sprawdza czy istnieje przycisk "Dalej"
			except:
				pass #jeśli nie ma to zostanie wykonana ta linijka, który właściwie nic nie robi
			else:
				#jeśli istnieję to ukryję przycisk do przodu oraz jego etykietę
				self.ButtonNext.hide()
				self.LabelForward.hide()
				

		#rysuję przycisk wstecz jeśli jest inna strona niż pierwsza
		#czyli w praktycę jeśli offset jest rózny od zera
		if(offset!=0):
			self.ButtonPrev=QPushButton(self)
			self.ButtonPrev.setGeometry(QtCore.QRect(400, 350, 150, 150))
			self.ButtonPrev.setStyleSheet("QPushButton{background:#168c24 url(:/images/backward.png)}")
			self.ButtonPrev.show()
			self.ButtonPrev.clicked.connect(lambda: self.showPreviousStations(kind,offset))
			
			#dodaje rysowanie etykiet
			self.LabelBackward=QtWidgets.QLabel("sd",self)
			self.LabelBackward.setGeometry(QtCore.QRect(400, 510, 181, 31))
			_translate = QtCore.QCoreApplication.translate
			self.LabelBackward.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Poprzednie</span></p><p><br/></p></body></html>"))
			self.LabelBackward.show()
		else:
			try:
				self.ButtonPrev
			except:
				pass
			else:
				self.ButtonPrev.hide()
				self.LabelBackward.hide()

	#metoda czyszcząca wcześniej wyświetlone stacje
	def cleanStationsButtons(self,kind):
		#czyszczę obecną listę przycisków
		for i in range(len(self.StationsListButtons)):
			self.StationsListButtons[i].hide()
		#czyszczę obecną listę etykiet
		for i in range(len(self.StationsListLabels)):
			self.StationsListLabels[i].hide()
		#czyszczę przyciski nawigacji:
		try:
			self.ButtonPrev
		except:
			pass
		else:
			self.ButtonPrev.hide()
			self.LabelBackward.hide()
		try:
			self.ButtonNext
		except:
			pass
		else:
			self.ButtonNext.hide()
			self.LabelForward.hide()	
	#funkcja zamyka okno z listą stacji (z przyciskami do danych stacji)
	def closeFMListForm():
			global FMWindowList
			FMWindowList.close()

#Klasa odpowiadająca za RadioPlayWindow, czyli za forms/radio_play_window.py
#Wyświetla widok odtwarzania konkretnej stacji radiowej
#nagrywanie stacji działa póki co tylko na PC
#nie działa na raspberry
from forms import radio_play_window
#moduł do obsługi czasu
import datetime
from PyQt5.QtGui import QPixmap

from subprocess import check_output
FMName=0
class RadioPlayWindow(QMainWindow, radio_play_window.Ui_RadioPlayWindow):
	def __init__(self,sender,kind):
		super(self.__class__, self).__init__()
		self.setupUi(self) 
		#globalna zmienna nazwa stacji, która jest odtwarzana
		global FMName
		FMName=sender
		#wypisuję nazwę stacji		
		self.RadioName=QtWidgets.QLabel("sd",self)
		self.RadioName.setGeometry(QtCore.QRect(387, 280, 181, 31))
		_translate = QtCore.QCoreApplication.translate
		self.RadioName.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">"+sender+"</span></p><p><br/></p></body></html>"))
		self.RadioName.show()
		
		#obiekt do operacji na bazie danych
		self.ListStationsObject=ListStations(kind)

		#wyświetlam logo stacji
		#tworze etykiete, w której wyświetlą się obiekt QPixmap, czyli logo
		self.LogoLabel = QLabel(self)
		#ustalam pozycję i wymiary: x, y, szerokość, wysokość
		self.LogoLabel.setGeometry(QtCore.QRect(387, 20, 250, 250))
		
		#tworzę dynamiczną nazwę pliku, który zawiera logo stacji radiowej
		FileLogo=FMName+".png"
		
		#uruchamiam konstruktor taki?
		#QImage(const QString &fileName, const char *format = nullptr)
		self.QImageLogo = QtGui.QImage("resources/FMLogo/"+FileLogo)
			
		#konwertuję obiekt QImage na obiekt QPixmap
		self.QPixmapLogo = QtGui.QPixmap.fromImage(self.QImageLogo)
			
		#tworzę instancję obiektu QPixmao
		self.PixmapLogo = QPixmap(self.QPixmapLogo)
		
		#"wklejam: obiekt QPixmap do obiektu QLabel, czyli do etykiety
		self.LogoLabel.setPixmap(self.PixmapLogo)
		
		#wyświetlam etykietę, czyli logo
		self.LogoLabel.show()
			


		#sprawdzam czy nagrywanie jest już aktywne
		#nagrywanie dla konkretnej stacji
		self.PIDarecord=self.get_pid("arecord")
		if(isinstance(self.PIDarecord, int) and FMName==StationPlayed):
			#Rysuję przycisk stop nagrywania
			self.StopButton=self.drawControlFMButton("Stop nagrywania",627,350,"#fe022c","stop.png")
			self.StopButton.show()
			#dodanie slotu
			self.StopButton.clicked.connect(lambda: self.useControlFMButton(self.sender().objectName()))
			#dodaje rysowanie etykiety
			self.StopLabel=self.drawControlButtonLabel(627,510,"Zatrzymaj nagrywanie")
			self.StopLabel.show()
		else:
			#Rysuję przycisk start nagrywania
			self.RecordButton=self.drawControlFMButton("Nagrywaj",627,350,"#016285","record.png")
			self.RecordButton.show()
			#dodanie slotu
			self.RecordButton.clicked.connect(lambda: self.useControlFMButton(self.sender().objectName()))
			#dodaje rysowanie etykiety
			self.RecordLabel=self.drawControlButtonLabel(627,510,"Nagrywaj")
			self.RecordLabel.show()

		#najpierw muszę sprawdzić stacja jest w ulubionych
		#trzeba wysłać zapytanie do bazy i sprawdzić, czy jest w ulubionych
		self.isFavourited=self.ListStationsObject.isStationFavourited(FMName)
		if(self.isFavourited==0):
			#Rysuję przycisk Ulubione
			self.FavouritedButton=self.drawControlFMButton("Ulubione",247,350,"#8214d0","favourited.png")
			self.FavouritedButton.show()
			#Dodanie slotu
			self.FavouritedButton.clicked.connect(lambda: self.useControlFMButton(self.sender().objectName()))
			#Etykieta
			self.FavouritedLabel=self.drawControlButtonLabel(247,510,"Ulubione")
			self.FavouritedLabel.show()
			#Rysuję przycisk dodaj do ulubionych
			self.AddtoFavouritedButton=self.drawControlFMButton("Dodaj",437,350,"#13de00","add.png")
			self.AddtoFavouritedButton.show()
			#Dodanie slotu
			self.AddtoFavouritedButton.clicked.connect(lambda: self.useControlFMButton(self.sender().objectName()))
			#dodaje rysowanie etykiety
			self.AddtoFavouritedLabel=self.drawControlButtonLabel(437,510,"Dodaj do ulubionych")
			self.AddtoFavouritedLabel.show()
		else:
			#Rysuję przycisk Normalne
			self.NormalButton=self.drawControlFMButton("Normalne",247,350,"#26d8fc","radio.png")
			#Dodanie slotu 
			self.NormalButton.clicked.connect(lambda: self.useControlFMButton(self.sender().objectName()))
			#dodaje rysowanie etykiety
			self.NormalLabel=self.drawControlButtonLabel(247,510,"Normalne")	
			self.NormalLabel.show()	
			#usuń z ulubionych
			self.DeleteFromFavouritedButton=self.drawControlFMButton("Usun",437,350,"#fe022c","delete.png")
			self.DeleteFromFavouritedButton.show()
			#Dodanie slotu
			self.DeleteFromFavouritedButton.clicked.connect(lambda: self.useControlFMButton(self.sender().objectName()))
			#dodaje rysowanie etykiety
			self.DeleteFromFavouritedLabel=self.drawControlButtonLabel(437,510,"Usuń z ulubionych")
			self.DeleteFromFavouritedLabel.show()
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setStyleSheet(open("resources/style.qss", "r").read()) 
		
	
	#definicja własnego sygnału
	#wcześniej korzystałem z wbudowanych sygnałów
	#np. z kliknięcia przycisku
	trigger = pyqtSignal()
	#trigger został specjalnie stworzony do zamknęcia okna listy stacji
	
	#funkcję(sloty) do obsługi przycisków
	#obsługa przycisków do przechodzenia z widoku odtwarzania konkretnej np. ulubionej stacji
	#do widoku listy stacji normalnych (czyli wszystkich stacji)	
	def useControlFMButton(self,sender):
		global FMWindowList
		#ta linijka łączy sygnał ze slotem closeFMListForm() z klasy SelectFMWindow
		self.trigger.connect(lambda: SelectFMWindow.closeFMListForm())
		if(sender=="Ulubione"):
				#emituje sygnał z obecnej klasy do klasy SelectFMWindow (opisane wyżej)
				#powyższy slot ma zadanie zamknąć okno z listą stacji
				#w tym przypasku zamknie listę wszystkich stacji
				self.trigger.emit()
				#zamykam okno odtwarzania danej stacji normalnej
				self.close()	
				#otwieram okno z listą stacji ulubionych
				FMWindowList = SelectFMWindow('favourited')
				#wyświetlam to okno
				FMWindowList.show()
		if(sender=="Normalne"):
				#analogicznie jak wyżej
				self.trigger.emit()
				self.close()
				FMWindowList = SelectFMWindow('normal')
				FMWindowList.show()
		#dodawanie danej stacji do ulubionych
		if(sender=="Dodaj"): #jeśli wciśnięto przycisk "Dodaj do ulubionych"
				#dodaję stację do ulubionych
				#zmieniam parametr Favourited w bazie z "0" na "1"
				self.ListStationsObject.addFMStationToFavourited(FMName)
				#emituje sygnał do zamknięcia listy wszystkich stacji 
				self.trigger.emit()
				#zamykam okno odtwarzania konkretnej stacji 
				#w tym przpadku stacji należącej do wszystkich stacji (nie należy do ulubionych)
				self.close()
				#otwieram listę stacji ulubionych
				FMWindowList = SelectFMWindow('favourited')
				#wyświetlam okno z listą stacji ulubionych
				FMWindowList.show()
				#wyświetla widok odtwarzania stacji, j/w
				self.dialog = RadioPlayWindow(FMName,"favourited")
				self.dialog.show()
		#usuwanie z ulubionych
		#analogicznie jak wyżej
		if(sender=="Usun"): #jeśli wciśnięto przycisk "Usuń z ulubionych"
				self.ListStationsObject.deleteFMStationFromFavourited(FMName)
				self.trigger.emit()
				self.close()
				FMWindowList = SelectFMWindow('normal')
				FMWindowList.show()
				self.dialog = RadioPlayWindow(FMName,"normal")
				self.dialog.show()
		#nagrywanie dźwięku z radia
		#działa póki co tylko na PC
		#nie działa jeszcze na raspberry
		#w nazwie pliku jest nazwa stacji
		#oraz data i godzina nagrywania
		if(sender=="Nagrywaj"):
			#zmieniam wygląd przycisku
			#nagrywam
			i = datetime.datetime.now()
			time=("%s-%s-%s-%s:%s:%s" % (i.day, i.month, i.year, i.hour, i.minute, i.second))
			RecordString="sudo pkill arecord;arecord "+'"'+FMName+"-"+str(time)+".wav\" &"
			os.system(RecordString)
			self.close()
			self.dialog = RadioPlayWindow(FMName,"normal")
			self.dialog.show()
		if(sender=="Stop nagrywania"):
			#zmieniam wygląd przycisku
			#zatrzymuje nagrywanie
			os.system('sudo pkill -9 arecord')
			self.close()
			self.dialog = RadioPlayWindow(FMName,"normal")
			self.dialog.show()

	#rysuję przycisk w widoku stacji
	#Ulubione/Normalne
	#dodaj/usuń z ulubionych
	#nagrywaj/zatrzymaj nagrywanie
	def drawControlFMButton(self,objectname,offset_x,offset_y,background,image):
		self.ControlFMButton=QPushButton(self)
		self.ControlFMButton.setGeometry(QtCore.QRect(offset_x, offset_y, 150, 150))
		self.ControlFMButton.setStyleSheet("QPushButton{background:"+str(background)+" url(:/images/"+str(image)+")}")
		self.ControlFMButton.setObjectName(objectname)
		return self.ControlFMButton

	#to samo tylko, że dla etykiet tych przycisków
	def drawControlButtonLabel(self,offset_x,offset_y,label):
		self.ControlFMButtonLabel=QtWidgets.QLabel("sd",self)
		self.ControlFMButtonLabel.setGeometry(QtCore.QRect(offset_x, offset_y, 181, 31))
		_translate = QtCore.QCoreApplication.translate
		self.ControlFMButtonLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">"+str(label)+"</span></p><p><br/></p></body></html>"))
		return self.ControlFMButtonLabel
	#funkcję zwraca pid procesu, np pid procesu arecord
	#służy do sprawdzenia czy jakaś stacja jest już nagrywana
	def get_pid(self,name):
		try:
			return int(check_output(["pidof","-s",name]))
		except:
			pass
		else:
			pass


#Klasa odpowiadająca za ListsPlaylistWindow, czyli za forms/playlists_window.py
#tworzy pusty formularz z przyciskiem wstecz, na którym będzie wylistowana lista playlist
#oraz tworzy obiekt klasy ListPlaylist (z pliku ListPlaylists.py), która odpowiada za właściwą obsługę listowania playlist

#importuję kod klasy ListPlaylists
from classes.ListPlaylists import ListPlaylists
class PlaylistsWindow(QMainWindow, blank_window.Ui_BlankWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self) 
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setStyleSheet(open("resources/style.qss", "r").read()) 
		self.PlaylistsWindowForm=ListPlaylists()
		self.PlaylistsWindowForm.show()
		self.Back.clicked.connect(lambda: self.backToMP3PlayerWindow())
	
	#przypisanie slotów
	#funkcja, która wraca do widoku odtwarzacza (3 przyciski: pendrive, kara pamięci, playlista)
	def backToMP3PlayerWindow(self):
		self.close()
		self.PlaylistsWindowForm.close()


#Klasa odpowiadająca za CamcorderWindow, czyli za forms/camcorder_window
#wyświetla pierwszy formularz po wciśnieciu przycisku Kamera z głównego ekranu
from forms import camcorder_window
class CamcorderWindow(QMainWindow, camcorder_window.Ui_CamcorderWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self) 

		#przypisuje konkretną funkcję do przycisku i sygnał
		self.Front_Camcorder.clicked.connect(lambda: self.showFrontCamcorderForm())		
		self.Back_Camcorder.clicked.connect(lambda: self.showBackCamcorderForm())
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setStyleSheet(open("resources/style.qss", "r").read())
	
	#funkcję(sloty) do obsługi przycisków
	#tworzy obiekt klasy FrontCamcorderWindow
	#która wyświetla formularz przedniej kamery (rejestrator)
	def showFrontCamcorderForm(self):
		self.dialog = FrontCamcorderWindow()
	#analogicznie formularz kamery cofania
	def showBackCamcorderForm(self):
		self.dialog = BackCamcorderWindow()


#Klasa odpowiadająca za FrontCamcorderWindow, czyli za forms/front_camcorder_window.py
#widok formularza przedniej kamery (rejestratora)
from classes.Camera import Camera
class FrontCamcorderWindow(QMainWindow, blank_window.Ui_BlankWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self) 
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setStyleSheet(open("resources/style.qss", "r").read())
		#wyświetlam pusty formularz, na którym się wyświetli stream z kamery
		self.show()
		
		self.Back.clicked.connect(lambda: self.closeFrontCamcorderStream())

		#tworze etykiete, w której wyświetlą się ramki QPixmap "pobrane" z kamerki
		self.VideoLabel = QLabel(self)
		#ustalam pozycję i wymiary: x, y, szerokość, wysokość
		self.VideoLabel.setGeometry(QtCore.QRect(0, 0, 840, 540))

		#tworze nowy wątek
		self.ThreadStream = QThread()
		#tworzę obiekt, który dziedziczy po QObject
		#dzięki niemu będzie możliwość obsługi slotów i sygnałów
		self.WorkerStream = Camera("/dev/FrontCamcorder")
		
		#jeśli obiekt klasy Camera wyślę sygnał "StreamSignal", który zawiera w sobie obiekt QPixmap
		#to funkcja streamFromFrontWebcam() go obsłuży
		#czyli "wklei" go do etykiety VideoLabel, a potem tę etykietę wyświetli
		self.WorkerStream.StreamSignal.connect(self.streamFromFrontWebcam)
		
		#przenoszę obiekt WorkerStream do nowego wątku
		self.WorkerStream.moveToThread(self.ThreadStream)
		
		#jeśli obiekt klasy Camera, wyślę sygnał FinishedSignal, to wątek, który obsługiwał streamowanie się zakończy
		self.WorkerStream.FinishedSignal.connect(self.ThreadStream.quit)
		
		#jeśli nowy wątek zostanie uruchomiony to
		#zostanie wykonana funkcja startFrontCamcorderStream() z klasy Camera 
		self.ThreadStream.started.connect(self.WorkerStream.startCamcorderStream)
		
		#uruchamiam nowy wątek
		self.ThreadStream.start()
	
	#funkcja zamykająca stream z kamerki
	def closeFrontCamcorderStream(self):
		os.system("rm temp/stream")
		self.close()
	#slot, który wyświetla w etykiecie VideoLabel obiekt QPixmap otrzymany od obiektu klasy Camera
	def streamFromFrontWebcam(self,ResizedFrame):
		self.VideoLabel.setPixmap(ResizedFrame)
		self.VideoLabel.show()


#Klasa odpowiadająca za BackCamcorderWindow, czyli za forms/back_camcorder_window.py
#analogicznie dla kamery cofania
class BackCamcorderWindow(QMainWindow, blank_window.Ui_BlankWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self) 
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setStyleSheet(open("resources/style.qss", "r").read()) 
		self.show()
		
		self.Back.clicked.connect(lambda: self.closeBackCamcorderStream())
		
		#tworze etykiete, w której wyświetlą się ramki QPixmap "pobrane" z kamerki
		self.VideoLabel = QLabel(self)
		#ustalam pozycję i wymiary: x, y, szerokość, wysokość
		self.VideoLabel.setGeometry(QtCore.QRect(0, 0, 840, 540))
		
		#tworze nowy wątek
		self.ThreadStream = QThread()
		#tworzę obiekt, który dziedziczy po QObject
		#dzięki niemu będzie możliwość obsługi slotów i sygnałów
		self.WorkerStream = Camera("/dev/BackCamcorder")
		
		#jeśli obiekt klasy Camera wyślę sygnał "StreamSignal", który zawiera w sobie obiekt QPixmap
		#to funkcja streamFromBackWebcam() go obsłuży
		#czyli "wklei" go do etykiety VideoLabel, a potem tę etykietę wyświetli
		self.WorkerStream.StreamSignal.connect(self.streamFromBackWebcam)
		
		#przenoszę obiekt WorkerStream do nowego wątku
		self.WorkerStream.moveToThread(self.ThreadStream)
		
		#jeśli obiekt klasy Camera, wyślę sygnał FinishedSignal, to wątek, który obsługiwał streamowanie się zakończy
		self.WorkerStream.FinishedSignal.connect(self.ThreadStream.quit)
		
		#jeśli nowy wątek zostanie uruchomiony to
		#zostanie wykonana funkcja startCamcorderStream() z klasy Camera 
		self.ThreadStream.started.connect(self.WorkerStream.startCamcorderStream)
		
		#uruchamiam nowy wątek
		self.ThreadStream.start()

	
	#funkcja zamykająca stream z kamerki
	def closeBackCamcorderStream(self):
		os.system("rm temp/stream")
		self.close()
	#slot, który wyświetla w etykiecie VideoLabel obiekt QPixmap otrzymany od obiektu klasy Camera
	def streamFromBackWebcam(self,ResizedFrame):
		self.VideoLabel.setPixmap(ResizedFrame)
		self.VideoLabel.show()


#Klasa odpowiadająca za CameraWindow, czyli za forms/camera_window
#analogicznie jak wyżej, tylko klasa do obługi zdjęć
#wszystkie 3 następne klasy do obsługi robienia zdjęć
from forms import camera_window
class CameraWindow(QMainWindow, camera_window.Ui_CameraWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self) 

		#przypisuje konkretną funkcję do przycisku i sygnał
		self.Front_Camera.clicked.connect(lambda: self.showFrontCameraForm())		
		self.Back_Camera.clicked.connect(lambda: self.showBackCameraForm())
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setStyleSheet(open("resources/style.qss", "r").read())
	
	#funkcję(sloty) do obsługi przycisków
	def showFrontCameraForm(self):
		self.dialog = FrontCameraWindow()
	def showBackCameraForm(self):
		self.dialog = BackCameraWindow()

#Klasa odpowiadająca za FrontCameraWindow, czyli za forms/front_camera_window.py
class FrontCameraWindow(QMainWindow, blank_window.Ui_BlankWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self) 

		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setStyleSheet(open("resources/style.qss", "r").read())
		self.show()

		self.Back.clicked.connect(lambda: self.closeFrontCamcorderStream())
		
		#tworze etykiete, w której wyświetlą się ramki QPixmap "pobrane" z kamerki
		self.VideoLabel = QLabel(self)
		#ustalam pozycję i wymiary: x, y, szerokość, wysokość
		self.VideoLabel.setGeometry(QtCore.QRect(0, 0, 840, 540))
		
		#Rysuję przycisk zrób zdjęcie
		self.TakePhoto=RadioPlayWindow.drawControlFMButton(self,"TakePhoto",860,160,"#26d8fc","camera.png")
		self.TakePhoto.clicked.connect(lambda: self.takePhoto())
		self.TakePhoto.show()
		#dodaje rysowanie etykiety
		self.TakePhotoLabel=RadioPlayWindow.drawControlButtonLabel(self,860,320,"Zrób zdjęcie")
		self.TakePhotoLabel.show()
		
		#tworze nowy wątek
		self.ThreadStream = QThread()
		#tworzę obiekt, który dziedziczy po QObject
		#dzięki niemu będzie możliwość obsługi slotów i sygnałów
		self.WorkerStream = Camera("/dev/FrontCamcorder")
		
		#jeśli obiekt klasy Camera wyślę sygnał "StreamSignal", który zawiera w sobie obiekt QPixmap
		#to funkcja streamFromWebcam() go obsłuży
		#czyli "wklei" go do etykiety VideoLabel, a potem tę etykietę wyświetli
		self.WorkerStream.StreamSignal.connect(self.streamFromFrontWebcam)
		
		#przenoszę obiekt WorkerStream do nowego wątku
		self.WorkerStream.moveToThread(self.ThreadStream)
		
		#jeśli obiekt klasy Camera, wyślę sygnał FinishedSignal, to wątek, który obsługiwał streamowanie się zakończy
		self.WorkerStream.FinishedSignal.connect(self.ThreadStream.quit)
		
		#jeśli nowy wątek zostanie uruchomiony to
		#zostanie wykonana funkcja startCamcorderStream() z klasy Camera 
		self.ThreadStream.started.connect(self.WorkerStream.startCamcorderStream)
		
		#uruchamiam nowy wątek
		self.ThreadStream.start()

	#funkcja zamykająca stream z kamerki
	def closeFrontCamcorderStream(self):
		os.system("rm temp/stream")
		self.close()
	#slot, który wyświetla w etykiecie VideoLabel obiekt QPixmap otrzymany od obiektu klasy Camera
	def streamFromFrontWebcam(self,ResizedFrame):
		self.VideoLabel.setPixmap(ResizedFrame)
		self.VideoLabel.show()
	def takePhoto(self):
		os.system("touch temp/photo")

#Klasa odpowiadająca za BackCameraWindow, czyli za forms/back_camera_window.py
class BackCameraWindow(QMainWindow, blank_window.Ui_BlankWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self) 

		#przypisuje konkretną funkcję do przycisku i sygnał
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setStyleSheet(open("resources/style.qss", "r").read())
		self.show()

		self.Back.clicked.connect(lambda: self.closeBackCamcorderStream())
		
		#tworze etykiete, w której wyświetlą się ramki QPixmap "pobrane" z kamerki
		self.VideoLabel = QLabel(self)
		#ustalam pozycję i wymiary: x, y, szerokość, wysokość
		self.VideoLabel.setGeometry(QtCore.QRect(0, 0, 840, 540))
		
		#Rysuję przycisk zrób zdjęcie
		self.TakePhoto=RadioPlayWindow.drawControlFMButton(self,"TakePhoto",860,160,"#26d8fc","camera.png")
		self.TakePhoto.clicked.connect(lambda: self.takePhoto())
		self.TakePhoto.show()
		#dodaje rysowanie etykiety
		self.TakePhotoLabel=RadioPlayWindow.drawControlButtonLabel(self,860,320,"Zrób zdjęcie")
		self.TakePhotoLabel.show()
		
		#tworze nowy wątek
		self.ThreadStream = QThread()
		#tworzę obiekt, który dziedziczy po QObject
		#dzięki niemu będzie możliwość obsługi slotów i sygnałów
		self.WorkerStream = Camera("/dev/BackCamcorder")
		
		#jeśli obiekt klasy Camera wyślę sygnał "StreamSignal", który zawiera w sobie obiekt QPixmap
		#to funkcja streamFromBackWebcam() go obsłuży
		#czyli "wklei" go do etykiety VideoLabel, a potem tę etykietę wyświetli
		self.WorkerStream.StreamSignal.connect(self.streamFromBackWebcam)
		
		#przenoszę obiekt WorkerStream do nowego wątku
		self.WorkerStream.moveToThread(self.ThreadStream)
		
		#jeśli obiekt klasy Camera, wyślę sygnał FinishedSignal, to wątek, który obsługiwał streamowanie się zakończy
		self.WorkerStream.FinishedSignal.connect(self.ThreadStream.quit)
		
		#jeśli nowy wątek zostanie uruchomiony to
		#zostanie wykonana funkcja startCamcorderStream() z klasy Camera 
		self.ThreadStream.started.connect(self.WorkerStream.startCamcorderStream)
		
		#uruchamiam nowy wątek
		self.ThreadStream.start()

	
	#funkcja zamykająca stream z kamerki
	def closeBackCamcorderStream(self):
		os.system("rm temp/stream")
		self.close()
	#slot, który wyświetla w etykiecie VideoLabel obiekt QPixmap otrzymany od obiektu klasy Camera
	def streamFromBackWebcam(self,ResizedFrame):
		self.VideoLabel.setPixmap(ResizedFrame)
		self.VideoLabel.show()
	def takePhoto(self):
		os.system("touch temp/photo")

#Klasa odpowiadająca za MultimediaWindow czyli za forms/multimedia_window.py
#wyświetla listę multimedialnych przycisków (netflix, spotify itd.)
#oraz odpowiada za ich obsługę
from forms import multimedia_window
class MultimediaWindow(QMainWindow, multimedia_window.Ui_MultimediaWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self) # gets defined in the UI file
		
		#przypisuje konkretną funkcję do przycisku i sygnał
		self.Spotify.clicked.connect(lambda: self.playSpotify())
		self.Youtube.clicked.connect(lambda: self.playYoutube())
		self.Internet.clicked.connect(lambda: self.startChromium())
		self.Netflix.clicked.connect(lambda: self.startNetflix())
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setStyleSheet(open("resources/style.qss", "r").read()) 

	#funkcję(sloty) do obsługi przycisków
	def playSpotify(self):
		spotifyPath="chromium-browser https://open.spotify.com/browse/featured"
		#spotifyPath="firefox https://open.spotify.com/browse/featured"
		os.system(spotifyPath)
	def playYoutube(self):
		youtubePath="chromium-browser https://www.youtube.com"
		os.system(youtubePath)
	def startChromium(self):
		os.system('chromium-browser')
	def startNetflix(self):
		netflixPath="chromium-browser https://www.netflix.com "
		os.system(netflixPath)

#Klasa odpowiadająca za CloseWindow, czyli za forms/close_window.py
#klasa odpowiada za okno zamykania aplikacji
from forms import close_window
class CloseWindow(QMainWindow, close_window.Ui_CloseWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self) 

		#przypisuje konkretną funkcję do przycisku i sygnał
		self.Restart.clicked.connect(lambda: self.restartPI())
		self.Desktop.clicked.connect(lambda: self.showDesktop())
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setStyleSheet(open("resources/style.qss", "r").read())
	
	#funkcję(sloty) do obsługi przycisków
	def restartPI(self):
		os.system('sudo reboot')
	def showDesktop(self):
		os.system('sudo pkill -9 arecord;sudo pkill -9 aplay;sudo killall python3')
