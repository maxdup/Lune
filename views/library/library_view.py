# -*- coding: utf-8 -*-
import os

from PySide import QtGui, QtCore
from PySide.QtCore import QModelIndex

from views.status.status import Status
from models.library_vm import LibraryViewModel
from views.library.model_to_item_strategy import ModelToItemStrat


class LibraryView(QtGui.QWidget):
    def __init__(self, player, library_vm):
        QtGui.QWidget.__init__(self)

        self.player = player
        self.library = library_vm

        self.song_list = library_vm.songs
        self.song_list.doubleClicked.connect(self._item_double_clicked)

        self.album_list = library_vm.albums
        model = self.album_list.selectionModel()
        model.selectionChanged.connect(
            self._album_selection_changed)
        self.album_list.doubleClicked.connect(self._item_double_clicked)
        self.album_list.verticalScrollBar().valueChanged.connect(
            self._album_viewport_moved)
        self.album_list.setGridSize(QtCore.QSize(128,148))
        self.album_list.setIconSize(QtCore.QSize(100,100))
        self.album_list.setUniformItemSizes(True)
        self.album_list.setObjectName('albums')
        self._album_viewport_moved()

        self.artist_list = library_vm.artists
        model = self.artist_list.selectionModel()
        model.selectionChanged.connect(
            self._artist_selection_changed)
        self.artist_list.doubleClicked.connect(self._item_double_clicked)

    def _artist_selection_changed(self):
        for index in self.artist_list.selectedIndexes():
            item = self.artist_list.model().mapToSource(index)
            self.library.filtering(
                item.data(ModelToItemStrat.FILTER))

    def _album_selection_changed(self):
        for index in self.album_list.selectedIndexes():
            item = self.album_list.model().mapToSource(index)
            self.library.filtering(
                item.data(ModelToItemStrat.FILTER))

    def _item_double_clicked(self, item):
        self.player.bouncer.ask_nicely(
            item.data(ModelToItemStrat.PLAY))

    def _album_viewport_moved(self):
        indexes = []
        height = self.album_list.size().height() + 128
        x, y = 64, 64

        index = self.album_list.indexAt(QtCore.QPoint(x,y))
        if not index.isValid():
            y -= 32
            index = self.album_list.indexAt(QtCore.QPoint(x,y))

        while(index.isValid() and y < height):

            indexes.append(index)

            while(index.isValid()):
                indexes.append(index)
                x += 148
                index = self.album_list.indexAt(QtCore.QPoint(x,y))
            x = 64

            y += 128
            index = self.album_list.indexAt(QtCore.QPoint(x,y))

        for id in indexes:
            modelindex = self.album_list.model().mapToSource(id)
            album = modelindex.data(ModelToItemStrat.PLAY)
            item = self.library.albums_proxylist.model.itemFromIndex(modelindex)
            if item.icon().cacheKey() == self.library.albums_proxylist.placeholder.cacheKey():
                artwork = album.get_art()
                if artwork:
                    item.setIcon(QtGui.QIcon(artwork))
