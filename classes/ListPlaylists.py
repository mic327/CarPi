from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import *
import os

class ListPlaylists(QWidget):
	def __init__(self):
		super(ListPlaylists, self).__init__()
		self.resize(450, 540)
		self.move(220,60)
		#usuwam górną belkę okna oraz okno dostaję flagę za na wierzchu
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)  
		self.ListView = QListView()
		#definicja sygnału
		self.ListView.clicked.connect(self.playPlaylist)
		self.FileSystemModel = QFileSystemModel(self.ListView)
		#tę meotodę musimy zawsze wykonać na początku
		self.FileSystemModel.setRootPath("/")
		# ustawiamy model obsługi danych dla modelu, który odpowiada za wyświetlanie tych danych
		self.ListView.setModel(self.FileSystemModel)
		Layout = QHBoxLayout(self)
		Layout.addWidget(self.ListView)
		self.setLayout(Layout)
		#self.listView.setRootIndex(self.fileSystemModel.index("/home/michal/Muzyka"))
		self.ListView.setRootIndex(self.FileSystemModel.index("/home/pi/Music/Playlists"))
		self.setStyleSheet(open("resources/style.qss", "r").read()) 

	#przypisanie slotów
	#funkcja do odtwarzania wybranej playlisty w VLC
	def playPlaylist(self, index):
		Path = self.sender().model().filePath(index)
		Playlist="vlc "+Path
		os.system(Playlist)  
