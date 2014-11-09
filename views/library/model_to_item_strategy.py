from PySide.QtGui import QStandardItem, QIcon
from PySide.QtCore import QSize


class ModelToItemStrat:

    TRACK_TITLE, ARTIST, ALBUM = range(1000, 1003)
    FILTER, PLAY = range(1101, 1103)

    def __init__(self, func=None):
        if func:
            self.get_item = func

    @classmethod
    def get_item(self, obj):
        return NotImplemented

def get_song_item(song):
    item = QStandardItem()
    item.setData(song.track_info['title'], ModelToItemStrat.TRACK_TITLE)
    item.setData(song.track_info['artist'], ModelToItemStrat.ARTIST)
    item.setData(song.track_info['album'], ModelToItemStrat.ALBUM)
    item.setData(song, ModelToItemStrat.FILTER)
    item.setData(song, ModelToItemStrat.PLAY)
    item.setText(song.track_info['title'])
    return item
    
def get_album_item(album):
    item = QStandardItem()
    item.setData(album.title, ModelToItemStrat.ALBUM)
    item.setData(album.artist.name, ModelToItemStrat.ARTIST)
    item.setData(album, ModelToItemStrat.FILTER)
    item.setData(album, ModelToItemStrat.PLAY)
    item.setText(album.title)
    item.setSizeHint(QSize(128,148))
    return item

def get_artist_item(artist):
    item = QStandardItem()
    item.setData(artist, ModelToItemStrat.FILTER)
    item.setData(artist, ModelToItemStrat.PLAY)
    item.setText(artist.name)
    return item
