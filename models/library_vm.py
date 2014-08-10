from models.song import Song
from models.album import Album
from models.artist import Artist
from PySide.QtGui import QListWidget, QListWidgetItem

class LibraryViewModel:
    def __init__(self):
        self.songs = QListWidget()
        self.albums = QListWidget()
        self.artists = QListWidget()
        self.genras = QListWidget()
        self.years = QListWidget()

    def add_any(self, something):
        if type(something) == Song:
            item = QListWidgetItem(self.songs)
            item.setText(something.track_info['title'])
            item.setData(1002, something)
            self.songs.addItem(item)
        elif type(something) == Album:
            item = QListWidgetItem(self.albums)
            item.setText(something.title)
            item.setData(1001, something)
            item.setData(1002, something)
            self.albums.addItem(item)
        elif type(something) == Artist:
            item = QListWidgetItem(self.artists)
            item.setText(something.name)
            item.setData(1001, something)
            item.setData(1002, something)
            self.artists.addItem(item)
        #elif type(something) == Record:
        #elif type(something) == Genre:
        #elif type(something) == Year:

    def filtering(self, something):
        if type(something) == Album:
            self.songs.clear()
            for song in something.songs:
                self.add_any(song)
        if type(something) == Artist:
            self.albums.clear()
            self.songs.clear()
            for album in something.albums:
                self.add_any(album)
                for song in album.songs:
                    self.add_any(song)

    def rebuild(self, library):
        self.songs.clear()
        self.albums.clear()
        self.artists.clear()
        for artist in library.artists:
            self.add_any(artist)
        for album in library.albums:
            self.add_any(album)
        for song in library.songs:
            self.add_any(song)
