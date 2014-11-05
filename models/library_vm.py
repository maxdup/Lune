from PySide.QtGui import QListWidget, QListWidgetItem, QIcon, QSortFilterProxyModel, QListView
from PySide import QtGui, QtCore

from models.song import Song
from models.album import Album
from models.artist import Artist
from views.library.model_to_item_strategy import ModelToItemStrat, get_song_item
from views.library.sort_filter_proxy import SortFilterProxy


class LibraryViewModel:
    def __init__(self, library):
        self.songs = QListView()
        self.songs.setEditTriggers(
            QtGui.QAbstractItemView.NoEditTriggers)

        self.songs_proxylist = SortFilterProxy(
            self.songs, ModelToItemStrat(get_song_item))

        self.albums = QListWidget()
        self.albums.setObjectName('list_albums')

        self.artists = QListWidget()

        self.genres = QListWidget()
        self.years = QListWidget()
        self.records = QListWidget()
        self.library = library

    def add_any(self, something):

        if type(something) == Song:
            self.songs_proxylist.add(something)

        elif type(something) == Album:
            item = QListWidgetItem(self.albums)
            item.setText(something.title)
            item.setData(ModelToItemStrat.FILTER, something)
            item.setData(ModelToItemStrat.PLAY, something)
            item.setIcon(QIcon(something.get_art()))
            self.albums.addItem(item)

        elif type(something) == Artist:
            item = QListWidgetItem(self.artists)
            item.setText(something.name)
            item.setData(ModelToItemStrat.FILTER, something)
            item.setData(ModelToItemStrat.PLAY, something)
            self.artists.addItem(item)
        #elif type(something) == Record:
        #elif type(something) == Genre:
        #elif type(something) == Year:

    def filtering(self, something=None):

        if not something:
            self.albums.clear()
            self.artists.clear()
            for artist in self.library.artists:
                self.add_any(artist)
            for album in self.library.albums:
                self.add_any(album)

        elif type(something) == Album:
            self.songs_proxylist.filter(ModelToItemStrat.ALBUM, something.title)

        elif type(something) == Artist:
            self.albums.clear()
            for album in something.albums:
                self.add_any(album)
            self.songs_proxylist.filter(ModelToItemStrat.ARTIST, something.name)

    def rebuild(self, library):

        self.albums.clear()
        self.artists.clear()
        for artist in library.artists:
            self.add_any(artist)
        for album in library.albums:
            self.add_any(album)
        #for song in library.songs:
        #    self.add_any(song)
