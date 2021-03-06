#Klasa przechwouje wszystkie sloty i sygnały w aplikacji

#Moduły wbudowane
import os
from PyQt5.QtWidgets import *
from PyQt5 import *
import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QThread
from PyQt5.QtSql import (QSqlDatabase, QSqlQuery)



#Moduły aplikacji
from forms import blank_window
from classes.CustomMessageBox import CustomMessageBox




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
		self.Settings.clicked.connect(lambda: self.showSettingsForm())
		self.Close.clicked.connect(lambda: self.showCloseForm())
		self.setStyleSheet(open("/home/pi/Desktop/CarPi/resources/style.qss", "r").read())
	
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
	def showSettingsForm(self):
		self.dialog = SettingsWindow()
		self.dialog.show()	
	def showCloseForm(self):
		self.dialog = CloseWindow()
		self.dialog.show()

from forms import settings_window
class SettingsWindow(QMainWindow, blank_window.Ui_BlankWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self) 
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setStyleSheet(open("/home/pi/Desktop/CarPi/resources/style.qss", "r").read()) 
		#dodaję przycisk do zapisu ustawień
		self.SaveSettingsButton=RadioPlayWindow.drawControlFMButton(self,"Zapisz",860,160,"#016285","save.png")
		self.SaveSettingsButton.show()
		#dodaje rysowanie etykiety
		self.SaveSettingsLabel=RadioPlayWindow.drawControlButtonLabel(self,860,320,"Zapisz")
		self.SaveSettingsLabel.show()
		

		#dodaję comboboxa i jego etykietę
		#etykieta comboboxa - sortowanie wg
		self.SortRadioLabel=RadioPlayWindow.drawControlButtonLabel(self,180,120,"Sortowanie stacji radiowych wg:")
		self.SortRadioLabel.show()
		
		#dodaję combox
		#pobieram aktualną wartość sortowania z bazy
		self.DatabaseObject=Database()
		SortOrderQuery="Select Value FROM Settings";
		self.QueryObject=QSqlQuery()
		self.QueryObject.exec_(SortOrderQuery)
		self.QueryObject.next()
		self.SortOrder=self.QueryObject.value(0)
		
		
		self.SortComboBox=QComboBox(self)
		self.SortComboBox.addItem(self.SortOrder)
		
		#wszystkie możliwe ustawienia
		self.OptionsList=["Liczba odtworzeń malejąco","Liczba odtworzeń rosnąco","Alfabetycznie A-Z","Alfabetycznie Z-A"]
		
		for i in range(len(self.OptionsList)):
			if(self.SortOrder!=self.OptionsList[i]):
				self.SortComboBox.addItem(self.OptionsList[i])
		#wymiary i pozycja comboboxa
		self.SortComboBox.setGeometry(QtCore.QRect(180, 150, 350, 50))


		
		#Dodanie slotu
		self.SortComboBox.activated.connect(self.saveSettings)
		self.SaveSettingsButton.clicked.connect(self.saveSettings)

		self.OptionValue="test"
	
	def saveSettings(self):
		if(self.sender().objectName()!="Zapisz"):
			self.OptionValue=self.sender().currentText()
		elif(self.OptionValue!="test"):
			self.DatabaseObject=Database()
			SettingsQuery="UPDATE Settings SET Value=\""+self.OptionValue+"\""+" WHERE Option=\"StationsSort\"";
			self.QueryObject=QSqlQuery()
			self.QueryObject.exec_(SettingsQuery)
			self.QueryObject.next()
			CustomMessageBox.showWithTimeout(1.5,"Ustawienia zostały zapisane!","success")

			
	
#Klasa odpowiadająca za MP3PlayerWindow czyli za forms/MP3_player_window.py
from forms import MP3_player_window
class MusicWindow(QMainWindow, MP3_player_window.Ui_MP3PlayerWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self) 
		
		#przypisuje konkretną funkcję do przycisku i sygnał
		self.Pendrive.clicked.connect(lambda: self.playPendrive())
		self.Memory_Card.clicked.connect(lambda: self.playMemoryCard())
		self.Playlist.clicked.connect(lambda: self.showPlaylistsWindowForm())
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setStyleSheet(open("/home/pi/Desktop/CarPi/resources/style.qss", "r").read())
	
	#funkcję(sloty) do obsługi przycisków
	def playPendrive(self):
		os.system('sudo pkill -9 aplay;sudo pkill -9 rtl_fm;vlc /media/pi/307E-6572 --fullscreen')
	def playMemoryCard(self):
		os.system('sudo pkill -9 aplay;sudo pkill -9 rtl_fm;vlc --no-media-library /home/pi/Music')
	def showPlaylistsWindowForm(self):
		self.dialog = PlaylistWindow()
		self.dialog.show()
		
from classes.ListPlaylists import ListPlaylists
class PlaylistWindow(QMainWindow, blank_window.Ui_BlankWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self) 
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setStyleSheet(open("/home/pi/Desktop/CarPi/resources/style.qss", "r").read()) 
		self.PlaylistsWindowSelect=ListPlaylists("/home/pi/Playlists/")
		self.PlaylistsWindowSelect.show()
		#dodaję przycisk do tworzenia nowej playlisty
		self.NewPlaylistButton=RadioPlayWindow.drawControlFMButton(self,"Dodaj",860,160,"#016285","add.png")
		self.NewPlaylistButton.show()
		#dodaje rysowanie etykiety
		self.NewPlaylistLabel=RadioPlayWindow.drawControlButtonLabel(self,860,320,"Nowa")
		self.NewPlaylistLabel.show()
		
		#Dodanie slotu
		self.NewPlaylistButton.clicked.connect(lambda: self.showNewPlaylistForm())		
		self.Back.clicked.connect(lambda: self.backToPlaylistWindow())
		

	def backToPlaylistWindow(self):
		self.close()
		self.PlaylistsWindowSelect.close()
		
	def showNewPlaylistForm(self):
		self.dialog = PlaylistWindowCreate()
		self.dialog.show()
		



#problem z długością playlisty!
#jeśli piosenki dodane do playlisty mieszczą się na liście odtwarzania bez przewijania
#to wtedy ta lista się wyświetli dopiero kiedy zacznie się odtwarzać druga piosenka
#na początku na liście wyświetla się tylko pozycja "biblioteka mediów"
#możliwe, że to wina źle zrobionego skinu dla VLC
#zrobić, żeby metoda sprawdzała, czy użytkownik dodał coś za pomocą plusów

#po zapisaniu nowej playlisty i cofnięciu trzeba dodać widżet edycji do listy playlist
#można np. zamknąć klasę PlaylistWindow i ją ponownie otworzyć
#albo dodać jakoś z palca ten widżet za pomocą QListView.setIndexWidget()
#zrobić sortowanie playlist
#albo np. później dodane na początek

#po dodaniu nowej playlisty musi się automatycznie dodawać przycisk edycji
#chyba najlepiej zamknąć i otworzyć listowanie playlsit
#może da się jakoś zamknąć wszystkie formularze będące instancją pewnej klasy?
#uporządkować kwestie ścieżek
#zbyt często jest podania bezwględnie, wykorzystać zamiast tego zmienną

#można kiedyś dodać możliwość usuwania plików mp3 i komunikat o braku mp3 lub playlist

#błąd podczas tworzenie playlisty
#jesli się po chwili edytuję to utworzy się nowa playlista


#usunąć przyciski do edycji playlisty ze skina VLC
from classes.XMLPlaylistsEditor import XMLPlaylistsEditor
class PlaylistWindowCreate(QMainWindow, blank_window.Ui_BlankWindow):
	def __init__(self,Edit=False,Playlist="None"):
		super(self.__class__, self).__init__()
		self.Edit=Edit
		self.Playlist=Playlist
		self.setupUi(self) 
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setStyleSheet(open("/home/pi/Desktop/CarPi/resources/style.qss", "r").read()) 
		
		#ustawienia klasy dla widoku edycji lub tworzenia nowej playlisty
		#inicjacja obiektu, jeśli uruchomiony jest widok edycji
		if(self.Edit==True):
			self.PlaylistsWindowCreate=ListPlaylists("/home/pi/Music/",True)
			#opcjonalnie dodaję przycisk kasowania playlisty
			self.DeletePlaylistButton=RadioPlayWindow.drawControlFMButton(self,"Usun",700,160,"#fe022c","delete.png")
			self.DeletePlaylistButton.show()
			self.DeletePlaylistButton.clicked.connect(lambda: self.deletePlaylist())
			#dodaje rysowanie etykiety
			self.DeletePlaylistLabel=RadioPlayWindow.drawControlButtonLabel(self,700,320,"Usuń playlistę")
			self.DeletePlaylistLabel.show()
			
		else:
			self.PlaylistsWindowCreate=ListPlaylists("/home/pi/Music/")
		
		
		#ustawienia wspólne
		self.PlaylistsWindowCreate.show()
		#dodaję przycisk do zapisu nowej playlisty
		self.SavePlaylistButton=RadioPlayWindow.drawControlFMButton(self,"Zapisz",860,160,"#016285","add.png")
		self.SavePlaylistButton.show()
		#dodaje rysowanie etykiety
		self.SavePlaylistLabel=RadioPlayWindow.drawControlButtonLabel(self,860,320,"Zapisz")
		self.SavePlaylistLabel.show()
		
		#Dodanie slotu
		self.SavePlaylistButton.clicked.connect(lambda: self.savePlaylist(self.PlaylistsWindowCreate.PlaylistList))		
		self.Back.clicked.connect(lambda: self.backToPlaylistWindow())
		
		
		
	def backToPlaylistWindow(self):
		self.close()
		self.PlaylistsWindowCreate.close()
		
		#operacje po utworzeniu nowej playlisty
		#tutaj muszę zamknąć listowanie playlist, a potem jeszcze raz je otworzyć
		#dzięki temu, będzie od razu przycisk do edycji

			
		
	def savePlaylist(self,PlaylistList):
		#warunek, żeby nie tworzyć pustego pliku
		#jeśli podczas edycji odchaczy się wszystkie piosenki
		#to playlista się nie zmieni
		if(len(PlaylistList)>0):
			#działanie dla widoku tworzenia nowej playlisty
			if(self.Edit==False):
				self.PlaylistEditor=XMLPlaylistsEditor()
				#dodaję piosenki do pliku XML
				self.PlaylistEditor.createPlaylist(PlaylistList)
				self.close()
				self.PlaylistsWindowCreate.close()
				CustomMessageBox.showWithTimeout(1.5,"Pomyślnie utworzyłeś playlistę!","success")
			#działanie dla widoku edycji playlisty
			else:
				self.PlaylistEditor=XMLPlaylistsEditor(self.Playlist)
				self.PlaylistEditor.createPlaylist(PlaylistList)
				CustomMessageBox.showWithTimeout(1.5,"Playlista została edytowana!","success")
		else:
			CustomMessageBox.showWithTimeout(1.5,"Nie dodałeś żadnej piosenki do playlisty!","error")

	
	#metoda usuwa playlistę
	def deletePlaylist(self):
		os.system("rm /home/pi/Playlists/"+str(self.Playlist))
		self.close()
		self.PlaylistsWindowCreate.close()
		CustomMessageBox.showWithTimeout(1.5,"Pomyślnie skasowałeś playlistę!","success")






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
		self.setStyleSheet(open("/home/pi/Desktop/CarPi/resources/style.qss", "r").read()) 
	
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
from classes.Database import Database
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
		self.setStyleSheet(open("/home/pi/Desktop/CarPi/resources/style.qss", "r").read()) 
		
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
		
		self.DatabaseObject=Database(kind)

		#standardowe rysowanie przycisków
		#rysuje albo normalny widok albo widok ulubionych
		self.drawStationsButtons(kind,offset)
		
		#przypisuje konkretną funkcję do przycisku i sygnał
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
	
	#funkcję(sloty) do obsługi przycisków
	def playStation(self,sender,kind):
		global StationPlayed
		#pobieram z bazy częstotliwość stacja o danej nazwie (nazwa zawiera się w sender)
		Frequency=self.DatabaseObject.getStationFrequency(sender)
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
			CounterPlayed=self.DatabaseObject.increaseStationPlayed(sender)
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
		StationsList=self.DatabaseObject.getStationName(kind,offset)
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
		self.StationsCount=self.DatabaseObject.getCountStations(kind)
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
#moduł do obsługi czasu
import datetime
from PyQt5.QtGui import QPixmap

from subprocess import check_output
FMName=0
class RadioPlayWindow(QMainWindow, blank_window.Ui_BlankWindow):
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
		self.DatabaseObject=Database(kind)

		#wyświetlam logo stacji
		#tworze etykiete, w której wyświetlą się obiekt QPixmap, czyli logo
		self.LogoLabel = QLabel(self)
		#ustalam pozycję i wymiary: x, y, szerokość, wysokość
		self.LogoLabel.setGeometry(QtCore.QRect(387, 20, 250, 250))
		
		#tworzę dynamiczną nazwę pliku, który zawiera logo stacji radiowej
		FileLogo=FMName+".png"
		
		#uruchamiam konstruktor taki?
		#QImage(const QString &fileName, const char *format = nullptr)
		self.QImageLogo = QtGui.QImage("/home/pi/Desktop/CarPi/resources/FMLogo/"+FileLogo)
			
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
		self.isFavourited=self.DatabaseObject.isStationFavourited(FMName)
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
		self.setStyleSheet(open("/home/pi/Desktop/CarPi/resources/style.qss", "r").read()) 
		
	
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
				self.DatabaseObject.addFMStationToFavourited(FMName)
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
				CustomMessageBox.showWithTimeout(1.5,"Stacja dodana do ulubionych!","success")

		#usuwanie z ulubionych
		#analogicznie jak wyżej
		if(sender=="Usun"): #jeśli wciśnięto przycisk "Usuń z ulubionych"
				self.DatabaseObject.deleteFMStationFromFavourited(FMName)
				self.trigger.emit()
				self.close()
				FMWindowList = SelectFMWindow('normal')
				FMWindowList.show()
				self.dialog = RadioPlayWindow(FMName,"normal")
				self.dialog.show()
				CustomMessageBox.showWithTimeout(1.5,"Stacja usunięta z ulubionych!","success")

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
		self.ControlFMButtonLabel.setGeometry(QtCore.QRect(offset_x, offset_y, 381, 31))
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
		self.setStyleSheet(open("/home/pi/Desktop/CarPi/resources/style.qss", "r").read())
	
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
		self.setStyleSheet(open("/home/pi/Desktop/CarPi/resources/style.qss", "r").read())
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
		os.system("rm /home/pi/Desktop/CarPi/temp/stream")
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
		self.setStyleSheet(open("/home/pi/Desktop/CarPi/resources/style.qss", "r").read()) 
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
		os.system("rm /home/pi/Desktop/CarPi/temp/stream")
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
		self.setStyleSheet(open("/home/pi/Desktop/CarPi/resources/style.qss", "r").read())
	
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
		self.setStyleSheet(open("/home/pi/Desktop/CarPi/resources/style.qss", "r").read())
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
		os.system("rm /home/pi/Desktop/CarPi/temp/stream")
		self.close()
	#slot, który wyświetla w etykiecie VideoLabel obiekt QPixmap otrzymany od obiektu klasy Camera
	def streamFromFrontWebcam(self,ResizedFrame):
		self.VideoLabel.setPixmap(ResizedFrame)
		self.VideoLabel.show()
	def takePhoto(self):
		os.system("touch /home/pi/Desktop/CarPi/temp/photo")
		CustomMessageBox.showWithTimeout(1.5,"Zostało wykonane zdjęcie!","success")


#Klasa odpowiadająca za BackCameraWindow, czyli za forms/back_camera_window.py
class BackCameraWindow(QMainWindow, blank_window.Ui_BlankWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self) 

		#przypisuje konkretną funkcję do przycisku i sygnał
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setStyleSheet(open("/home/pi/Desktop/CarPi/resources/style.qss", "r").read())
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
		os.system("rm /home/pi/Desktop/CarPi/temp/stream")
		self.close()
	#slot, który wyświetla w etykiecie VideoLabel obiekt QPixmap otrzymany od obiektu klasy Camera
	def streamFromBackWebcam(self,ResizedFrame):
		self.VideoLabel.setPixmap(ResizedFrame)
		self.VideoLabel.show()
	def takePhoto(self):
		os.system("touch /home/pi/Desktop/CarPi/temp/photo")
		CustomMessageBox.showWithTimeout(1.5,"Zostało wykonane zdjęcie!","success")


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
		self.Photos.clicked.connect(lambda: self.showCameraForm())
		self.Videos.clicked.connect(lambda: self.showCamcorderForm())
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setStyleSheet(open("/home/pi/Desktop/CarPi/resources/style.qss", "r").read()) 

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
	def showCameraForm(self):
		self.Dialog=ImagesGalleryWindow()
		self.Dialog.show()
	def showCamcorderForm(self):
		self.Dialog=VideosGalleryWindow()
		self.Dialog.show()	

class ImagesGalleryWindow(QMainWindow, camera_window.Ui_CameraWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self) 
		#przypisuje konkretną funkcję do przycisku i sygnał
		self.Front_Camera.clicked.connect(lambda: self.showCameraPhotos("FrontCamera"))
		self.Back_Camera.clicked.connect(lambda: self.showCameraPhotos("BackCamera"))
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setStyleSheet(open("/home/pi/Desktop/CarPi/resources/style.qss", "r").read())
	
	#metoda do obsługi wyświetlania zdjęć
	#tworzy obiekt klasy ImagesGalleryView
	#która odpowiada za wyświetlanie zdjęć
	def showCameraPhotos(self,Camera):
		self.Dialog=ImagesGalleryView(Camera)




#Klasa odpowiedzialna za widok wyboru filmów z kamer
#filmy z przedniej lub tylnej kamery
from forms import camcorder_window
class VideosGalleryWindow(QMainWindow, camcorder_window.Ui_CamcorderWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self) 

		#przypisuje konkretną funkcję do przycisku i sygnał
		self.Front_Camcorder.clicked.connect(lambda: self.showCamcorderVideos("FrontCamcorder"))		
		self.Back_Camcorder.clicked.connect(lambda: self.showCamcorderVideos("BackCamcorder"))
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setStyleSheet(open("/home/pi/Desktop/CarPi/resources/style.qss", "r").read())
	
	#funkcję(sloty) do obsługi przycisków
	#tworzy obiekt klasy FrontCamcorderWindow
	#która wyświetla formularz przedniej kamery (rejestrator)
	def showCamcorderVideos(self,Camcorder):
		self.Dialog=VideosGalleryView(Camcorder)		
		
offset=0
#wyczyścić kod
#dużo kodu się powtarza z klasą SelectFMWindow?
#poprawić działanie wmctrl
#teraz wmctrl działa dobrze tylko raz: przykładowo
#uruchomić film (przyciskiem z listy filmów)
#poczekać aż się skończy film
#wcisnąć przycisk play
#okno wideo będzie ucięte i przesunięte w lewo
class VideosGalleryView(QMainWindow, blank_window.Ui_BlankWindow):
	def __init__(self,Camera):
		super(self.__class__, self).__init__()
		#nazwa zdjęcia, które zostanie otworzone
		#przechowuje, która została kamera wybrana
		#przednia / tylna
		self.Camera=Camera
		self.setupUi(self) 
		self.setStyleSheet(open("/home/pi/Desktop/CarPi/resources/style.qss", "r").read()) 
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		
		#wyświetlam formularz
		self.show()

	
		#pobieram listę obrazków z folderu
		#można dodać obsługę tylko obrazków
		#zrobić do tego walidację
		#dodaję napis Wszystkie stacje lub Ulubione stację
		self.test=QtWidgets.QLabel("sd",self)
		#parametry: x, y, width, height
		self.test.setGeometry(QtCore.QRect(80, 70, 281, 31))
		_translate = QtCore.QCoreApplication.translate
		
		if self.Camera=="FrontCamcorder":
			self.ImagesPath="/home/pi/Videos/FrontCamcorder/"
			self.ImagesList=os.listdir(self.ImagesPath)
			self.VideosCount=len(self.ImagesList)
			self.test.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Filmy z przedniej kamery:</span></p><p><br/></p></body></html>"))
			#wyświetlam etykietę
			self.test.show()
		elif self.Camera=="BackCamcorder":
			self.ImagesPath="/home/pi/Videos/BackCamcorder/"
			self.ImagesList=os.listdir(self.ImagesPath)
			self.VideosCount=len(self.ImagesList)
			self.test.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Filmy z tylnej kamery:</span></p><p><br/></p></body></html>"))
			#wyświetlam etykietę
			self.test.show()

		#dodaję dalszą obsługę tylko jeśli są jakieś pliki
		#jesli ich nie ma to wyświetlam stosowny komunikat
		if len(self.ImagesList)>0:

			#rysuję przyciski tylko wtedy, gdy są jakieś pliki
			self.drawStationsButtons(offset)

	
		else:
			#tutaj wyświetlić komunikat o braku zdjęć
			#komunikat o braku zdjęć
			self.EmptyFolder=QtWidgets.QLabel("sd",self)
			#parametry: x, y, width, height
			self.EmptyFolder.setGeometry(QtCore.QRect(280, 220, 450, 31))
			_translate = QtCore.QCoreApplication.translate
			self.EmptyFolder.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Folder jest pusty. Nie ma żadnych zdjęć!</span></p><p><br/></p></body></html>"))
			#wyświetlam etykietę
			self.EmptyFolder.show()	

	def drawStationsButtons(self,offset):
		#tworzę listę ze stacjami
		#tutaj muszę stworzyć listę z 4 plikami
		StationsList=[]
		for i in range(0,4):
			try:
				StationsList.append(self.ImagesList[offset+i])
			except:	
				pass
			else:
				pass

				
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
			self.StationsListButtons[self.i].setStyleSheet("QPushButton{background:#26d8fc url(:/images/video.png)}")
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
			self.StationsListButtons[self.i].clicked.connect(lambda: self.playStation(self.sender().objectName(),self.Camera))
			self.i=self.i+1
			
			

		#rysuję przycisk do przodu jeśli jest więcej wyników
		
		if(self.VideosCount>(offset+4)):
			self.ButtonNext=QPushButton(self)
			self.ButtonNext.setGeometry(QtCore.QRect(522, 350, 150, 150))
			self.ButtonNext.setStyleSheet("QPushButton{background:#168c24 url(:/images/forward.png)}")
			#dodaje rysowanie etykiet
			self.LabelForward=QtWidgets.QLabel("sd",self)
			self.LabelForward.setGeometry(QtCore.QRect(522, 510, 181, 31))
			_translate = QtCore.QCoreApplication.translate
			self.LabelForward.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Następne</span></p><p><br/></p></body></html>"))
			self.LabelForward.show()
			
			self.ButtonNext.show()
			self.ButtonNext.clicked.connect(lambda: self.showNextStations(offset))
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
			self.ButtonPrev.setGeometry(QtCore.QRect(348, 350, 150, 150))
			self.ButtonPrev.setStyleSheet("QPushButton{background:#168c24 url(:/images/backward.png)}")
			self.ButtonPrev.show()
			self.ButtonPrev.clicked.connect(lambda: self.showPreviousStations(offset))
			
			#dodaje rysowanie etykiet
			self.LabelBackward=QtWidgets.QLabel("sd",self)
			self.LabelBackward.setGeometry(QtCore.QRect(348, 510, 181, 31))
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
	def cleanStationsButtons(self):
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
		
	def playStation(self,sender,Camera):
		#buduję ścieżkę do odpalenia pliku wideo
		VideoPath="/home/pi/Videos/"+str(Camera)+"/"+str(sender)
		VLCString="vlc "+VideoPath+" &"
		os.system(VLCString)
		os.system("sh /home/pi/Desktop/window.sh")
		

	def showNextStations(self,offset):
		#analogicznie jak w funkcji wyżej
		self.cleanStationsButtons()
		self.drawStationsButtons(offset=offset+4)
		#funkcja, która rysuję przyciski do stacji
		#oraz rysuję przyciski nawigacji


	def showPreviousStations(self,offset):
		#czyszczę poprzednie przyciski do stacji
		#czyszczę przyciski nawigacji (dalej, wstecz)
		self.cleanStationsButtons()
		self.drawStationsButtons(offset=offset-4)

		#rysuję przyciski do poprzednich stacji
		#rysuję przyciski nawigacji

#ekran wyboru zdjęć
#albo z przedniego aparatu
#albo z tylnego
class ImagesGalleryWindow(QMainWindow, camera_window.Ui_CameraWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self) 
		#przypisuje konkretną funkcję do przycisku i sygnał
		self.Front_Camera.clicked.connect(lambda: self.showCameraPhotos("FrontCamera"))
		self.Back_Camera.clicked.connect(lambda: self.showCameraPhotos("BackCamera"))
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setStyleSheet(open("/home/pi/Desktop/CarPi/resources/style.qss", "r").read())
	
	#metoda do obsługi wyświetlania zdjęć
	#tworzy obiekt klasy ImagesGalleryView
	#która odpowiada za wyświetlanie zdjęć
	def showCameraPhotos(self,Camera):
		self.Dialog=ImagesGalleryView(Camera)
		

#zrobić odpowiednie skalowanie zdjęć, niech póki co zostanie
#dodać ładny napis z nazwą pliku
#można dodać ramkę dla zdjęcia lub tło
#wykrywać wielkość zdjęcia: zbyt duże, zbyt małe, raczej się obędzie
#weryfikować czy plik z folderu jest plikiem graficznym!!!
#zbyt szybkie naciskanie strza strzałek "wrzuca" na dół warstw formularz!!!
#może nie moze być zamykany formularz, by potem jeszcze raz go otwierać?
#na 99% to jest powodem błędu
#dodać estetyczny komunikat o braku zdjęć
#zrobić walidację przy listowaniu plików
#wyświetlać zdjęcia od najnowszych


#klasa odpowiedzialna za rysowanie podglądu zdjęcia, przycisków do nawigacji oraz do kasowania
class ImagesGalleryView(QMainWindow, blank_window.Ui_BlankWindow):
	def __init__(self,Camera,Image="first"):
		super(self.__class__, self).__init__()
		#nazwa zdjęcia, które zostanie otworzone
		self.Image=Image
		#przechowuje, która została kamera wybrana
		#przednia / tylna
		self.Camera=Camera
		self.setupUi(self) 
		self.setStyleSheet(open("/home/pi/Desktop/CarPi/resources/style.qss", "r").read()) 
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		
		#wyświetlam formularz
		self.show()

		#pobieram listę obrazków z folderu
		#można dodać obsługę tylko obrazków
		#zrobić do tego walidację
		if self.Camera=="FrontCamera":
			self.ImagesPath="/home/pi/Pictures/FrontCamcorder/"
			ImagesList=os.listdir(self.ImagesPath)
		elif self.Camera=="BackCamera":
			self.ImagesPath="/home/pi/Pictures/BackCamcorder/"
			ImagesList=os.listdir(self.ImagesPath)

		#dodaję dalszą obsługę tylko jeśli są jakieś pliki
		#jesli ich nie ma to wyświetlam stosowny komunikat
		if len(ImagesList)>0:
			#wyświetlam pierwszą grafikę
			#tworze etykiete, w której wyświetlą się obiekt QPixmap, czyli logo
			self.ImageLabel = QLabel(self)
			#ustalam pozycję i wymiary: x, y, szerokość, wysokość
			self.ImageLabel.setGeometry(QtCore.QRect(162, 40, 700, 280))
		
			#uruchamiam konstruktor taki?
			#QImage(const QString &fileName, const char *format = nullptr)
			#wyświetlam pierwszy obrazek
			if(self.Image=="first"):
				self.QImage = QtGui.QImage(self.ImagesPath+str(ImagesList[0]))
				#nazwa aktualnie otwartego zdjęcia
				ViewedImage=ImagesList[0]
			else:
				self.QImage = QtGui.QImage(self.ImagesPath+str(self.Image))
				#nazwa aktualnie otwartego zdjęcia
				ViewedImage=self.Image

			#konwertuję obiekt QImage na obiekt QPixmap
			self.QPixmap = QtGui.QPixmap.fromImage(self.QImage)
			
			#tworzę instancję obiektu QPixmao
			self.Pixmap = QPixmap(self.QPixmap)
		
			#skaluję obrazek
			self.Pixmap = self.Pixmap.scaled(700, 280)

			#"wklejam: obiekt QPixmap do obiektu QLabel, czyli do etykiety
			self.ImageLabel.setPixmap(self.Pixmap)
		
			#wyświetlam etykietę, czyli zdjęcie
			self.ImageLabel.show()
			
			#dodaję nazwę zdjęcia
			self.PhotoName=QtWidgets.QLabel("sd",self)
			#parametry: x, y, width, height
			self.PhotoName.setGeometry(QtCore.QRect(162, 10, 250, 31))
			_translate = QtCore.QCoreApplication.translate
			self.PhotoName.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">"+str(ViewedImage)+"</span></p><p><br/></p></body></html>"))
			#wyświetlam etykietę
			self.PhotoName.show()			
			
			#tworzę przyciski nawigacyjne
			#jeśli jest co usuwać
			if len(ImagesList)>0:
				#usuń zdjęcie
				self.DeleteImageButton=RadioPlayWindow.drawControlFMButton(self,"Usun",525,350,"#fe022c","delete.png")
				self.DeleteImageButton.show()
				#Dodanie slotu
				self.DeleteImageButton.clicked.connect(lambda: self.deleteImage(ViewedImage,ImagesList))
				#dodaje rysowanie etykiety
				self.DeleteImageLabel=RadioPlayWindow.drawControlButtonLabel(self,525,510,"Usuń zdjęcie")
				self.DeleteImageLabel.show()
		
			#wyświetlam tylko jeśli aktualnie otworzone zdjęcie jest różne od ostatniego
			if ViewedImage!=ImagesList[-1] and len(ImagesList)>1:		
				#następny
				self.NextImageButton=RadioPlayWindow.drawControlFMButton(self,"Nastepny",355,350,"#168c24","forward.png")
				self.NextImageButton.show()
				#Dodanie slotu
				self.NextImageButton.clicked.connect(lambda: self.showNextImage(ViewedImage,ImagesList))
				#dodaje rysowanie etykiety
				self.NextImageLabel=RadioPlayWindow.drawControlButtonLabel(self,355,510,"Następne zdjęcie")
				self.NextImageLabel.show()
		
		
			#wyświetlam tylko jeśli aktualnie otworzone zdjęcie jest różne od pierwszego
			if  ViewedImage!=ImagesList[0] and len(ImagesList)>1:
				#poprzedni
				self.PreviousImageButton=RadioPlayWindow.drawControlFMButton(self,"Poprzedni",185,350,"#168c24","backward.png")
				self.PreviousImageButton.show()
				#Dodanie slotu
				self.PreviousImageButton.clicked.connect(lambda: self.showPreviousImage(ViewedImage,ImagesList))
				#dodaje rysowanie etykiety
				self.PreviousImageLabel=RadioPlayWindow.drawControlButtonLabel(self,185,510,"Poprzednie zdjęcie")
				self.PreviousImageLabel.show()
		else:
			#tutaj wyświetlić komunikat o braku zdjęć
			#komunikat o braku zdjęć
			self.EmptyFolder=QtWidgets.QLabel("sd",self)
			#parametry: x, y, width, height
			self.EmptyFolder.setGeometry(QtCore.QRect(280, 220, 450, 31))
			_translate = QtCore.QCoreApplication.translate
			self.EmptyFolder.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Folder jest pusty. Nie ma żadnych zdjęć!</span></p><p><br/></p></body></html>"))
			#wyświetlam etykietę
			self.EmptyFolder.show()	
	
	#zle działa uswanie pierwszej stacji oraz kolejnych
	#działa dobrze tylko usuwanie ostatniej
	#zamiast kolejnej to się wyświetla ostania
	def deleteImage(self,ViewedImage,ImageList):
		print("Za chwilę usunę zdjęcie...")
		ImagePath=self.ImagesPath+str(ViewedImage)
		os.system('rm '+str(self.ImagesPath)+'"'+str(ViewedImage)+'"')
		self.close()
		for i in range(0,len(ImageList)):
			if ImageList[i]==ViewedImage:
				if ViewedImage==ImageList[-1]:
					self.Dialog=ImagesGalleryView(self.Camera,ImageList[i-1])
				else:
					self.Dialog=ImagesGalleryView(self.Camera,ImageList[i+1])
		
	def showPreviousImage(self,ViewedImage,ImageList):
		print("Za chwilę wyświetlę poprzednie zdjęcie...")
		self.close()
		for i in range(0,len(ImageList)):
			if ImageList[i]==ViewedImage:
				self.Dialog=ImagesGalleryView(self.Camera,ImageList[i-1])

	def showNextImage(self,ViewedImage,ImageList):
		print("Za chwilę wyświetlę kolejne zdjęcie...")
		self.close()
		for i in range(0,len(ImageList)):
			if ImageList[i]==ViewedImage:
				self.Dialog=ImagesGalleryView(self.Camera,ImageList[i+1])

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
		self.setStyleSheet(open("/home/pi/Desktop/CarPi/resources/style.qss", "r").read())
	
	#funkcję(sloty) do obsługi przycisków
	def restartPI(self):
		os.system('sudo reboot')
	def showDesktop(self):
		os.system('sudo pkill -9 arecord;sudo pkill -9 aplay;sudo killall python3')
