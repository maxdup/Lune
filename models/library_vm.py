from PySide.QtGui import QListWidget, QListWidgetItem, QIcon, QSortFilterProxyModel, QListView
from PySide import QtGui, QtCore

from models.song import Song
from models.album import Album
from models.artist import Artist
from views.library.qlistalbum import QListAlbum
from views.library.model_to_item_strategy import ModelToItemStrat, get_song_item, get_album_item, get_artist_item

from views.library.librarylistview import LibraryListView


class LibraryViewModel:
    def __init__(self, library):

        self.placeholder = QIcon(':img/placeholder.jpg')

        self.songs = LibraryListView(ModelToItemStrat(get_song_item))
        self.albums = QListAlbum(
            ModelToItemStrat(get_album_item), self.placeholder)
        self.artists = LibraryListView(ModelToItemStrat(get_artist_item))

        self.library = library


    def add_any(self, something):

        if type(something) == Song:
            self.songs.add(something)

        elif type(something) == Album:
            item = self.albums.add(something)
            item.setIcon(self.placeholder)

        elif type(something) == Artist:
            self.artists.add(something)

        #elif type(something) == Record:
        #elif type(something) == Genre:
        #elif type(something) == Year:

    def filtering(self, something=None):

        if not something:
            self.songs.filter(ModelToItemStrat.ALBUM, "")
            self.songs.filter(ModelToItemStrat.ARTIST, "")
            self.albums.filter(ModelToItemStrat.ARTIST, "")

        elif type(something) == Album:
            self.songs.filter(ModelToItemStrat.ALBUM, something.title)

        elif type(something) == Artist:
            self.albums.filter(ModelToItemStrat.ARTIST, something.name)
            self.songs.filter(ModelToItemStrat.ARTIST, something.name)
