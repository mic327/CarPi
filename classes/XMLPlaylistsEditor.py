from xml.dom import minidom
import datetime

#jak klasa zostanie wywołana z Edit==True
#to metody nie mają dostępu do self.PlaylistXMLDoc !
#poprawić
#trzeba do klasy przekazać jakoś ścieżkę playlisty!


class XMLPlaylistsEditor():
	def __init__(self,Playlist="None"):
		self.Path="/home/michal/Playlists/"+Playlist

		#wykona się podczas tworzenia nowej playlisty
		if(Playlist=="None"):
			#tworzę plik playlisty
			i = datetime.datetime.now()
			DateTime=("%s-%s-%s_%s:%s:%s" % (i.day, i.month, i.year, i.hour, i.minute, i.second))
			self.Path="/home/michal/Playlists/"+str(DateTime)+".xspf"
	
			#tworzę plik XML
			self.FileHandler=self.getPlaylistHandle()
			#zapisuję pusty plik XML
			self.FileHandler.close()
		else:
			self.PlaylistXMLDoc=minidom.parse(self.Path)


	#metoda zwraca uchwyt do pliku
	def getPlaylistHandle(self):
		self.PlaylistFile=open(self.Path,"w+")
		return self.PlaylistFile
		
	
	def createPlaylist(self,TitlesList):
		#tworzę plik XML
		self.FileHandler=self.getPlaylistHandle()
		
		#dodaję string, który stanie się szkieletem pliku
		#może być stałą
		self.Skeleton="<?xml version=\"1.0\" encoding=\"UTF-8\"?><playlist xmlns=\"http://xspf.org/ns/0/\" xmlns:vlc=\"http://www.videolan.org/vlc/playlist/ns/0/\" version=\"1\"><trackList></trackList></playlist>"
		self.PlaylistXMLDoc=minidom.parseString(self.Skeleton)	
		
		for i in range(len(TitlesList)):
			#tworzę elementy
			Track=self.PlaylistXMLDoc.createElement("track")
			Location=self.PlaylistXMLDoc.createElement("location")
			Title=self.PlaylistXMLDoc.createElement("title")
			
			#tworzę zawartość elementów
			TextLocation=self.PlaylistXMLDoc.createTextNode("file:///home/michal/Muzyka/"+str(TitlesList[i]))
			TextTitle=self.PlaylistXMLDoc.createTextNode(str(TitlesList[i]))
			
			#wypełniam elementy
			Location.appendChild(TextLocation)
			Title.appendChild(TextTitle)
			Track.appendChild(Location)
			Track.appendChild(Title)
			
			#dodaję <track> do <trackList>
			self.PlaylistXMLDoc.childNodes[0].childNodes[0].appendChild(Track)
		

		#zamieniam na pretty xml
		self.FileHandler.write(self.PlaylistXMLDoc.toprettyxml(newl='\n'))
		
		#zamykam plik
		self.FileHandler.close()

	#metoda generuję listę piosenek z pliku
	def getTitlesList(self):
		TitleList=[]
		TitleList=self.PlaylistXMLDoc.getElementsByTagName('title')
		for i in range(len(TitleList)):
			TitleList[i]=TitleList[i].firstChild.toxml()
		return TitleList

	#metoda określa ilość piosenek w pliku
	def getCounterTitles(self):
		TitleList=[]
		TitleList=self.PlaylistXMLDoc.getElementsByTagName('title')
		return len(TitleList)
		
	
	
	

		

