from PySide.QtGui import QListWidget, QListWidgetItem, QIcon, QSortFilterProxyModel, QListView
from PySide import QtGui, QtCore

from models.song import Song
from models.album import Album
from models.artist import Artist
from views.library.model_to_item_strategy import ModelToItemStrat, get_song_item, get_album_item, get_artist_item
from views.library.sort_filter_proxy import SortFilterProxy


class LibraryViewModel:
    def __init__(self, library):
        self.songs = QListView()
        self.songs.setEditTriggers(
            QtGui.QAbstractItemView.NoEditTriggers)

        self.albums = QListView()
        self.albums.setEditTriggers(
            QtGui.QAbstractItemView.NoEditTriggers)
        self.albums.setObjectName('list_albums')
        self.albums.setGridSize(QtCore.QSize(100,100))
        self.albums.setIconSize(QtCore.QSize(80,80))
        self.albums.setViewMode(QListView.IconMode)
        self.albums.setResizeMode(QListView.Adjust)

        self.artists = QListView()
        self.artists.setEditTriggers(
            QtGui.QAbstractItemView.NoEditTriggers)

        self.songs_proxylist = SortFilterProxy(
            self.songs, ModelToItemStrat(get_song_item))
        self.albums_proxylist = SortFilterProxy(
            self.albums, ModelToItemStrat(get_album_item))
        self.artists_proxylist = SortFilterProxy(
            self.artists, ModelToItemStrat(get_artist_item))

        self.genres = QListWidget()
        self.years = QListWidget()
        self.records = QListWidget()
        self.library = library

    def add_any(self, something):

        if type(something) == Song:
            self.songs_proxylist.add(something)

        elif type(something) == Album:
            self.albums_proxylist.add(something)

        elif type(something) == Artist:
            self.artists_proxylist.add(something)

        #elif type(something) == Record:
        #elif type(something) == Genre:
        #elif type(something) == Year:

    def filtering(self, something=None):

        if not something:
            #reset filters
            return NotImplemented

        elif type(something) == Album:
            self.songs_proxylist.filter(ModelToItemStrat.ALBUM, something.title)

        elif type(something) == Artist:
            self.albums_proxylist.filter(ModelToItemStrat.ARTIST, something.name)
            self.songs_proxylist.filter(ModelToItemStrat.ARTIST, something.name)
