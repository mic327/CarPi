#obsługa baz danych powinna być jakoś lepiej zaimplementowana
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import *
from PyQt5 import QtWidgets
from PyQt5.QtSql import (QSqlDatabase, QSqlQuery)
OpenDatabase=0
Offset=0


class Database(QWidget):
	def __init__(self,kind="other"):
		super(Database, self).__init__()
		#zapytania do bazy danych
		#Widok normalny:
		NormalQueryString="SELECT Name, Frequency FROM StationsFM ORDER BY Listened DESC"
		#Widok ulubionych:
		FavouritedQueryString="SELECT Name, Frequency FROM StationsFM WHERE Favourited=1 ORDER BY Listened DESC"
		#Łączę się z bazą danych		
		
		#sprawdzam czy baza nie została już otwarta
		#lepiej wykorzystać QSqlDatabase.isOpen()
		#zamiast globalnej zmiennej
		global OpenDatabase
		global Offset
		if(OpenDatabase==0):
			self.db= QSqlDatabase.addDatabase("QSQLITE")
			self.db.setDatabaseName("/home/pi/Desktop/CarPi/resources/activity.sqlite")
			boolean_ok=self.db.open()
			OpenDatabase=1
		self.QueryObject=QSqlQuery()
	
	#pobiera listę nazw stacji z bazy
	def getStationName(self,kind,offset=0,limit=4):
		self.SortOrder=self.getSortOrder()
		if(kind=='normal'):
			NormalFMQuery="SELECT Name FROM StationsFM "+str(self.SortOrder)+" LIMIT "+str(limit)+" OFFSET "+str(offset)
			self.QueryObject.exec_(NormalFMQuery)
		elif(kind=='favourited'):
			FavouritedFMQuery="SELECT Name FROM StationsFM WHERE Favourited=1 "+str(self.SortOrder)+" LIMIT "+str(limit)+" OFFSET "+str(offset)
			self.QueryObject.exec_(FavouritedFMQuery)
		self.StationsList=[]
		#tworzę lsitę stacji, które zostaną wyświetlone
		#lista będzie zawierać maksymalnie 4 stację
		#wynika to z wykorzystania limit=4
		while self.QueryObject.next():
			self.StationsList.append(self.QueryObject.value(0))
		return self.StationsList
	
	#pobiera w jaki sposób stacje radiowe będą sortowane
	def getSortOrder(self):
		SortOrderQuery="SELECT * FROM Settings"
		self.QueryObject.exec_(SortOrderQuery)
		self.QueryObject.next()
		self.SortOrder=self.QueryObject.value(2)
		
		if(self.SortOrder=="Liczba odtworzeń rosnąco"):
			self.Sort="ORDER BY Listened ASC"
		elif(self.SortOrder=="Liczba odtworzeń malejąco"):
			self.Sort="ORDER BY Listened DESC"
		elif(self.SortOrder=="Alfabetycznie A-Z"):
			self.Sort="ORDER BY Name ASC"
		elif(self.SortOrder=="Alfabetycznie Z-A"):
			self.Sort="ORDER BY Name DESC"
		return self.Sort
	
	#pobiera częstotliwość stacji na podstawie przekazanej nazwy stacji
	def getStationFrequency(self,name):
		FrequenceQuery="SELECT Frequency FROM StationsFM WHERE Name=\""+name+"\""
		self.QueryObject.exec_(FrequenceQuery)
		self.QueryObject.next()
		self.FrequencyStation=self.QueryObject.value(0)
		return self.FrequencyStation
	def getCountStations(self,kind):
		#pobieram liczbę wszystkich stacji
		if(kind=='normal'):
			NormalCountQuery="SELECT Count(Name) FROM StationsFM"
			self.QueryObject.exec_(NormalCountQuery)
		#pobieram liczbę stacji dodanych do ulubionych
		else:
			FavouritedCountQuery="SELECT COUNT(Name) FROM StationsFM WHERE Favourited=1"
			self.QueryObject.exec_(FavouritedCountQuery)
		#bez linijki nie działa. Dlaczego?
		self.QueryObject.next()
		self.CountStations=self.QueryObject.value(0)
		return self.CountStations
		
	#Można dodać, żeby lista się aktualizowała nie tylko podczas generowania listy
	#ale też podczas powrotu ze stacji
	#funkcja służy do zwiększania liczby odtworzeń danej stacji
	#lista stacji wyświetlana jest wg. tej wartości
	#najpierw wyświetlą się stacje najczęściej odtwarzane
	def increaseStationPlayed(self,name):
		#pobieram ile razy stacja została dotąd odtworzona
		CounterListenedQuery="SELECT Listened FROM StationsFM WHERE Name=\""+name+"\""
		self.QueryObject.exec_(CounterListenedQuery)
		self.QueryObject.next()
		self.CounterPlayed=self.QueryObject.value(0)
		#modyfikuję wartość
		#zwiększam o 1
		self.CounterPlayed+=1
		IncreaseCounterListenedQuery="UPDATE StationsFM SET Listened="+str(self.CounterPlayed)+" WHERE Name=\""+name+"\""
		self.QueryObject.exec_(IncreaseCounterListenedQuery)
		self.QueryObject.next()
		return
		
	#Funkcja dodająca stację do ulubionych:
	def addFMStationToFavourited(self,name):
		AddToFavouritedStationQuery="UPDATE StationsFM SET Favourited=1 WHERE Name=\""+name+"\""
		self.QueryObject.exec_(AddToFavouritedStationQuery)
		self.QueryObject.next()
		
	#Funkcja usuwająca stację z ulubionych:
	def deleteFMStationFromFavourited(self,name):
		DeleteFromFavouritedStationQuery="UPDATE StationsFM SET Favourited=0 WHERE Name=\""+name+"\""
		self.QueryObject.exec_(DeleteFromFavouritedStationQuery)
		self.QueryObject.next()

	#funkcja sprawdza, czy stacja jest w ulubionych
	def isStationFavourited(self,name):
		IsStationFavouritedQuery="SELECT Favourited FROM StationsFM WHERE Name=\""+name+"\""
		self.QueryObject.exec_(IsStationFavouritedQuery)
		self.QueryObject.next()
		self.isFavourited=self.QueryObject.value(0)
		return self.isFavourited


