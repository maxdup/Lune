from PySide import QtGui, QtCore
from PySide.QtGui import QListView
from views.library.model_to_item_strategy import ModelToItemStrat
from views.library.librarylistview import LibraryListView


class QListAlbum(LibraryListView):
    def __init__(self, strategy,  placeholder):
        LibraryListView.__init__(self, strategy)
        self.setGridSize(QtCore.QSize(128,148))
        self.setIconSize(QtCore.QSize(100,100))
        self.setUniformItemSizes(True)
        self.setObjectName('albums')
        self.setViewMode(QListView.IconMode)
        self.setResizeMode(QListView.Adjust)
        self.verticalScrollBar().valueChanged.connect(self.reload)

        self.placeholder = placeholder
        self.loaded_icons = []

    def resizeEvent(self, event):
        QListView.resizeEvent(self, event)
        self.reload()

    def filter(self, field, value):
        self.unload()
        LibraryListView.filter(self, field, value)
        self.load()

    def load(self):
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

    def unload(self):
        for id in self.loaded_icons:
            viewport = self.viewport().rect()
            modelindex = self.model().mapToSource(id)
            item = self.model().sourceModel().itemFromIndex(modelindex)
            item.setIcon(self.placeholder)
        self.loaded_icons = []

    def reload(self):
        for id in self.loaded_icons:
            viewport = self.viewport().rect()
            if not viewport.contains(self.visualRect(id)):
                modelindex = self.model().mapToSource(id)
                item = self.model().sourceModel().itemFromIndex(modelindex)
                item.setIcon(self.placeholder)
        self.loaded_icons = []
        self.load()
