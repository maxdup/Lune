from PySide.QtGui import QStandardItem
from PySide.QtCore import QSize


class ModelToItemStrat:

    TRACK_TITLE, TRACK_NB, ARTIST, ALBUM, DATE = range(1000, 1005)
    FILTER, PLAY = range(1101, 1103)

    def __init__(self, func=None):
        if func:
            self.get_item = func
            self.get_sorts = self.get_item(None)

    @classmethod
    def get_item(self, obj):
        return NotImplemented

    @classmethod
    def get_sorts(self, obj):
        return NotImplemented

def get_song_item(song):
    if not song:
        return get_song_sorts
    item = QStandardItem()
    item.setData(song.track_info['title'], ModelToItemStrat.TRACK_TITLE)
    item.setData(song.track_info['track_nb'], ModelToItemStrat.TRACK_NB)
    item.setData(song.track_info['artist'], ModelToItemStrat.ARTIST)
    item.setData(song.track_info['album'], ModelToItemStrat.ALBUM)
    item.setData(song, ModelToItemStrat.FILTER)
    item.setData(song, ModelToItemStrat.PLAY)
    item.setText(song.track_info['title'])
    return item

def get_song_sorts():
    return [ModelToItemStrat.TRACK_TITLE, ModelToItemStrat.TRACK_NB]

def get_album_item(album):
    if not album:
        return get_album_sorts
    item = QStandardItem()
    item.setData(album.title, ModelToItemStrat.ALBUM)
    item.setData(album.songs[0].track_info['date'], ModelToItemStrat.DATE)
    item.setData(album.artist.name, ModelToItemStrat.ARTIST)
    item.setData(album, ModelToItemStrat.FILTER)
    item.setData(album, ModelToItemStrat.PLAY)
    item.setText(album.title)
    item.setSizeHint(QSize(128,148))
    return item

def get_album_sorts():
    return [ModelToItemStrat.ALBUM, ModelToItemStrat.DATE]

def get_artist_item(artist):
    if not artist:
        return get_artist_sorts
    item = QStandardItem()
    item.setData(artist.name, ModelToItemStrat.ARTIST)
    item.setData(artist, ModelToItemStrat.FILTER)
    item.setData(artist, ModelToItemStrat.PLAY)
    item.setText(artist.name)
    return item

def get_artist_sorts():
    return [ModelToItemStrat.ARTIST]
