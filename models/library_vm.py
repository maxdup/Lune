from PySide import QtCore

from .song import Song
from .album import Album
from .artist import Artist
from views.library.qlistalbum import QListAlbum
from views.library.librarylistview import LibraryListView
from views.library.librarylistctrl import LibraryListCtrl
from views.library.model_to_item_strategy import ModelToItemStrat, \
    get_song_item, get_album_item, get_artist_item

from views.library.lunesortfilterproxymodel import \
    LuneSortFilterProxyModel


class LibraryViewModel:
    def __init__(self, library):

        self.songs = LibraryListView(ModelToItemStrat(get_song_item))
        self.songs_ctrl = LibraryListCtrl(self.songs, 'songs')
        self.songs.set_ctrl(self.songs_ctrl)
        self.albums = QListAlbum(ModelToItemStrat(get_album_item))
        self.albums_ctrl = LibraryListCtrl(self.albums, 'albums')
        self.albums.set_ctrl(self.albums_ctrl)
        self.artists = LibraryListView(ModelToItemStrat(get_artist_item))
        self.artists_ctrl = LibraryListCtrl(self.artists, 'artists')
        self.artists.set_ctrl(self.artists_ctrl)

        self.library = library

    def add_any(self, something):

        if type(something) == Song:
            self.songs.add(something)

        elif type(something) == Album:
            self.albums.add(something)

        elif type(something) == Artist:
            self.artists.add(something)

        #elif type(something) == Record:
        #elif type(something) == Genre:
        #elif type(something) == Year:

    def filtering(self, something=None):
        #hardcoded indexes are prone to break
        if not something:
            self.songs.filter(ModelToItemStrat.ALBUM, "")
            self.songs.filter(ModelToItemStrat.ARTIST, "")
            self.albums.filter(ModelToItemStrat.ARTIST, "")

        elif type(something) == Album:
            self.songs.sort(1)
            self.songs.filter(ModelToItemStrat.ALBUM, something.title)

        elif type(something) == Artist:
            self.songs.sort(0)
            self.albums.sort(1)

            self.albums.filter(ModelToItemStrat.ARTIST, something.name)
            self.songs.filter(ModelToItemStrat.ARTIST, something.name)
