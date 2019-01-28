from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import *
import os
from classes.XMLPlaylistsEditor import XMLPlaylistsEditor
import classes.SlotsAndSignals


class ListPlaylists(QWidget):
    def __init__(self, Path, Edit=False):
        super(ListPlaylists, self).__init__()
        self.Path = Path
        self.Edit = Edit

        # szerokość, wysokość
        self.resize(670, 540)
        self.move(10, 60)
        # usuwam górną belkę okna oraz okno dostaję flagę za na wierzchu
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.ListView = QListView()

        # definicja sygnału
        if (self.Path == "/home/michal/Playlists/"):
            self.ListView.clicked.connect(lambda: self.playPlaylist())
        self.FileSystemModel = QFileSystemModel(self.ListView)
        # tę meotodę musimy zawsze wykonać na początku
        self.FileSystemModel.setRootPath("/")
        # ustawiamy model obsługi danych dla modelu, który odpowiada za wyświetlanie tych danych
        self.ListView.setModel(self.FileSystemModel)
        Layout = QHBoxLayout(self)
        Layout.addWidget(self.ListView)
        self.setLayout(Layout)
        self.ListView.setRootIndex(self.FileSystemModel.index(self.Path))
        self.setStyleSheet(open("resources/style.qss", "r").read())
        # usuwam ikonę z listy
        self.ListView.setIconSize(QSize(0, 0))

        # to do!
        # generalnie jest ok, ale po przesunięcię przycisku edycji źle działa
        # jak to poprawić?

        # do sprawdzenia
        # pozycjonowanie tesktu w QListView
        # pozycjonowanie przycisku edycji za pomocą "czystego QT"

        # generuję listę modeli indexów na bazie QFileSystemModel
        # można wylistować listę plików i na jej podstawie wygenerować listę indexów
        # metoda index() z QFileSystemModel na bazie path zwraca obiekt QModelIndex

        # tworzę listę plików w katalogu playlists
        self.PlaylistFiles = os.listdir(self.Path)

        # liczba wszystkich playlist
        self.PlaylistCounter = len(self.PlaylistFiles)

        # na podstawie listy plików w katalogu, tworzę listę model index'ów
        self.ModelIndices = []
        for i in range(self.PlaylistCounter):
            self.ModelIndices.append(self.FileSystemModel.index(self.Path + str(self.PlaylistFiles[i])))

        # kolejność self.ModelIndices[i].data()
        # względem tego co się wyświetla jest różna!
        # może warto wszystko posortować?
        # chyba w przypadku playlisty nie warto

        # update
        # QModelIndex.isValid() zwraca True, jeśli
        # self.FileSystemModel.index() posiada bezwględną ścieżkę do pliku!

        # tworzę listę przycisków i dodaję je do indexów

        self.ButtonsList = []
        for i in range(self.PlaylistCounter):
            self.ButtonsList.append(QPushButton(self))
            self.ButtonsList[i].setGeometry(QtCore.QRect(0, 0, 50, 50))
            # widok edycji playlist
            if (self.Path == "/home/michal/Playlists/" and self.Edit == False):
                self.ButtonsList[i].setStyleSheet(
                    "QPushButton{background:#fe022c url(:/images/edit.png) no-repeat;max-width:50px;min-height:50px;margin-left:500px}")
                self.ButtonsList[i].clicked.connect(lambda: self.editPlaylist())
            # widok dodawania piosenek do playlisty
            if (self.Path == "/home/michal/Muzyka/" and self.Edit == False):
                self.ButtonsList[i].setStyleSheet(
                    "QPushButton{background:#168c24 url(:/images/add_small.png) no-repeat;max-width:50px;min-height:50px;margin-left:500px}")
                self.ButtonsList[i].clicked.connect(lambda: self.addToPlaylist())
            self.ButtonsList[i].setObjectName(self.PlaylistFiles[i])
            self.ListView.setIndexWidget(self.ModelIndices[i], self.ButtonsList[i])
        if (self.Edit == True):

            # wyświetlam przyciski "Plus" lub "Minus"
            self.XMLPlaylistsEditor = XMLPlaylistsEditor(self.sender().objectName())

            # tymaczosowa łatka!
            self.PlaylistFiles = os.listdir("/home/michal/Muzyka/")

            # lista tytułów
            self.TitlesList = self.XMLPlaylistsEditor.getTitlesList()

            l = 0
            for j in range(self.PlaylistCounter):
                Added = False
                for k in range(len(self.TitlesList)):
                    if (self.ModelIndices[j].data() == self.TitlesList[k]):
                        self.ButtonsList.append(QPushButton(self))
                        self.ButtonsList[l].setGeometry(QtCore.QRect(0, 0, 50, 50))
                        self.ButtonsList[l].setStyleSheet(
                            "QPushButton{background:#fe022c url(:/images/delete_small.png) no-repeat;max-width:50px;min-height:50px;margin-left:500px}")
                        self.ButtonsList[l].clicked.connect(lambda: self.removeFromPlaylist())
                        self.ButtonsList[l].setObjectName(self.TitlesList[k])
                        self.ListView.setIndexWidget(self.ModelIndices[j], self.ButtonsList[l])
                        l = l + 1
                        Added = True

                if (Added == False):
                    self.ButtonsList.append(QPushButton(self))
                    self.ButtonsList[l].setGeometry(QtCore.QRect(0, 0, 50, 50))
                    self.ButtonsList[l].setStyleSheet(
                        "QPushButton{background:#168c24 url(:/images/add_small.png) no-repeat;max-width:50px;min-height:50px;margin-left:500px}")
                    self.ButtonsList[l].clicked.connect(lambda: self.addToPlaylist())
                    self.ButtonsList[l].setObjectName(self.ModelIndices[j].data())
                    self.ListView.setIndexWidget(self.ModelIndices[j], self.ButtonsList[l])
                    l = l + 1

        self.PlaylistList = []
        if (self.Edit == True):
            self.XMLPlaylistsEditor = XMLPlaylistsEditor(self.sender().objectName())

            # lista przechwoująca nazwy piosenek
            self.PlaylistList = self.XMLPlaylistsEditor.getTitlesList()

    # przypisanie slotów
    # funkcja do odtwarzania wybranej playlisty w VLC
    def playPlaylist(self):
        # tutaj self.sender() to obiekt klasy QListView!
        # pobieram index wybranego elementu
        self.SenderIndex = self.sender().currentIndex()

        # ścieżka wybranej playlisty
        # self.sender().model() odpowiada obiektowi klasy QFileSystemModel?
        PlaylistPath = self.sender().model().filePath(self.SenderIndex)

        # uruchamiam playlistę w VLC
        Playlist = "vlc " + PlaylistPath
        os.system(Playlist)

    # funkcją modyfikująca play
    def editPlaylist(self):
        self.dialog = classes.SlotsAndSignals.PlaylistWindowCreate(True, self.sender().objectName())
        self.dialog.show()

    def addToPlaylist(self):
        # metoda dodająca piosenki do playlisty
        # chyba tutaj wystarczy dodanie elementu do listy
        # dopiero przycisk zapisz będzię tworzył odpowiedni plik
        self.TrackTittle = self.sender().objectName()

        # dodaję element do drzewa pliku xml

        # dodaję element do playlisty
        self.PlaylistList.append(self.TrackTittle)

        # sprawdzam jaki index przycisku
        # może lepiej dodać nr np. do object name?
        for i in range(self.PlaylistCounter):
            if (self.ButtonsList[i].objectName() == self.TrackTittle):
                ButtonIndex = i
                break

        # zmieniam formatowanie przycisku
        # stary slot usuwam
        # nowy ustawiam
        self.ButtonsList[ButtonIndex].setStyleSheet(
            "QPushButton{background:#fe022c url(:/images/delete_small.png) no-repeat;max-width:50px;min-height:50px;margin-left:500px}")
        self.ButtonsList[ButtonIndex].clicked.disconnect()
        self.ButtonsList[ButtonIndex].clicked.connect(lambda: self.removeFromPlaylist())

    # funkcją do usuwania z playlisty
    def removeFromPlaylist(self):
        self.TrackTittle = self.sender().objectName()
        self.PlaylistList.remove(self.TrackTittle)

        # sprawdzam jaki index przycisku
        # może lepiej dodać nr np. do object name?
        for i in range(self.PlaylistCounter):
            if (self.ButtonsList[i].objectName() == self.TrackTittle):
                ButtonIndex = i
                break

        # zmieniam formatowanie przycisku
        # stary slot usuwam
        # nowy ustawiam
        self.ButtonsList[ButtonIndex].setStyleSheet(
            "QPushButton{background:#168c24 url(:/images/add_small.png) no-repeat;max-width:50px;min-height:50px;margin-left:500px}")
        self.ButtonsList[ButtonIndex].clicked.disconnect()
        self.ButtonsList[ButtonIndex].clicked.connect(lambda: self.addToPlaylist())

    def addEditPlaylistButtons(self):
        self.ButtonsList = []
        for i in range(self.PlaylistCounter):
            self.ButtonsList.append(QPushButton(self))
            self.ButtonsList[i].setGeometry(QtCore.QRect(0, 0, 50, 50))
            # widok edycji playlist
            if (self.Path == "/home/michal/Playlists/" and self.Edit == False):
                self.ButtonsList[i].setStyleSheet(
                    "QPushButton{background:#fe022c url(:/images/edit.png) no-repeat;max-width:50px;min-height:50px;margin-left:500px}")
                self.ButtonsList[i].clicked.connect(lambda: self.editPlaylist())
            # widok dodawania piosenek do playlisty
            if (self.Path == "/home/michal/Muzyka/" and self.Edit == False):
                self.ButtonsList[i].setStyleSheet(
                    "QPushButton{background:#168c24 url(:/images/add_small.png) no-repeat;max-width:50px;min-height:50px;margin-left:500px}")
                self.ButtonsList[i].clicked.connect(lambda: self.addToPlaylist())
            self.ButtonsList[i].setObjectName(self.PlaylistFiles[i])
            self.ListView.setIndexWidget(self.ModelIndices[i], self.ButtonsList[i])







