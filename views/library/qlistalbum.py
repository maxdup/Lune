from PySide import QtGui, QtCore
from PySide.QtGui import QListView
from views.library.model_to_item_strategy import ModelToItemStrat


class QListAlbum(QtGui.QListView):
    def __init__(self, placeholder):
        QListView.__init__(self)
        self.setGridSize(QtCore.QSize(128,148))
        self.setIconSize(QtCore.QSize(100,100))
        self.setUniformItemSizes(True)
        self.setObjectName('albums')
        self.setViewMode(QListView.IconMode)
        self.setResizeMode(QListView.Adjust)
        self.verticalScrollBar().valueChanged.connect(
            self._album_viewport_moved)

        self.placeholder = placeholder
        self.loaded_icons = []

    def resizeEvent(self, event):
        QListView.resizeEvent(self, event)
        self._album_viewport_moved()

    def _album_viewport_moved(self):

        # lazy unloading
        for id in self.loaded_icons:
            viewport = self.viewport().rect()
            if not viewport.contains(self.visualRect(id)):
                modelindex = self.model().mapToSource(id)
                item = self.model().sourceModel().itemFromIndex(modelindex)
                item.setIcon(self.placeholder)
        self.loaded_icons = []

        # lazy loading
        indexes = []
        height = self.size().height() + 128
        x, y = 64, 64

        index = self.indexAt(QtCore.QPoint(x,y))

        while index.isValid() and y < height:

            indexes.append(index)

            while index.isValid():
                indexes.append(index)
                x += 128
                index = self.indexAt(QtCore.QPoint(x,y))
            x = 64

            y += 148
            index = self.indexAt(QtCore.QPoint(x,y))

        for id in indexes:
            modelindex = self.model().mapToSource(id)
            album = modelindex.data(ModelToItemStrat.PLAY)
            item = self.model().sourceModel().itemFromIndex(modelindex)
            self.loaded_icons.append(id)

            if item.icon().cacheKey() == self.placeholder.cacheKey():
                artwork = album.get_art()
                if artwork:
                    item.setIcon(QtGui.QIcon(artwork))
