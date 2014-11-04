from models.song import Song

from PySide import QtGui, QtCore
from PySide.QtGui import QSortFilterProxyModel


class SongFilterProxy:
    
    SONG, ARTIST, ALBUM = range(20,23)

    def __init__(self, qlist):

        self.qlist = qlist

        self.model = QtGui.QStandardItemModel(self.qlist)

        self.proxymodel = QSortFilterProxyModel()
        self.proxymodel.setSourceModel(self.model)
        self.proxymodel.setDynamicSortFilter(True)
x
        self.qlist.setModel(self.proxymodel)

    def add(self, song):
        item = QtGui.QStandardItem()
        item.setData(song.track_info['title'], self.SONG)
        item.setData(song.track_info['artist'], self.ARTIST)
        item.setData(song.track_info['album'], self.ALBUM)
        item.setData(song, 1001)
        item.setData(song, 1002)
        item.setText(song.track_info['title'])
        self.model.appendRow(item)

    def filter(self, field, value):
        self.proxymodel.setFilterRole(field)
        self.proxymodel.setFilterFixedString(value)
