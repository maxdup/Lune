from .song import Song
from .album import Album
from .artist import Artist
from views.library.qlistalbum import QListAlbum
from views.library.librarylistview import LibraryListView
from views.library.model_to_item_strategy import ModelToItemStrat, \
    get_song_item, get_album_item, get_artist_item

from views.library.lunesortfilterproxymodel import \
    LuneSortFilterProxyModel


class LibraryViewModel:
    def __init__(self, library):

        self.songs = LibraryListView(ModelToItemStrat(get_song_item))
        self.albums = QListAlbum(ModelToItemStrat(get_album_item))
        self.artists = LibraryListView(ModelToItemStrat(get_artist_item))

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

        if not something:
            self.songs.filter(ModelToItemStrat.ALBUM, "")
            self.songs.filter(ModelToItemStrat.ARTIST, "")
            self.albums.filter(ModelToItemStrat.ARTIST, "")

        elif type(something) == Album:
            self.songs.proxymodel.setSort(ModelToItemStrat.TRACK_NB)
            self.songs.filter(ModelToItemStrat.ALBUM, something.title)

        elif type(something) == Artist:
            self.songs.proxymodel.setSort(ModelToItemStrat.TRACK_TITLE)
            self.albums.proxymodel.setSort(ModelToItemStrat.DATE, False)

            self.albums.filter(ModelToItemStrat.ARTIST, something.name)
            self.songs.filter(ModelToItemStrat.ARTIST, something.name)
