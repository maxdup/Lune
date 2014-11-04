from models.song import Song

from PySide import QtGui, QtCore
from PySide.QtGui import QSortFilterProxyModel


class SongFilterProxy:
    
    SONG, ARTIST, ALBUM = range(0,3)

    def __init__(self, qlist):

        self.qlist = qlist

        self.proxymodel = QSortFilterProxyModel()
        self.proxymodel.setDynamicSortFilter(True)
        
        self.model = QtGui.QStandardItemModel(0, 3, self.qlist)
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, 'song')
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, 'artist')
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, 'album')
        
        self.proxymodel.setSourceModel(self.model)
        self.qlist.setModel(self.proxymodel)

    def add(self, song):
        self.model.insertRow(0)
        self.model.setData(self.model.index(0, 0), song.track_info['title'])
        self.model.setData(self.model.index(1, 1), song.track_info['artist'])
        self.model.setData(self.model.index(2, 2), song.track_info['album'])
        
    def filter(self, field, value):
        self.proxymodel.setFilterKeyColumn(field)
        self.proxymodel.setFilterFixedString(value)
