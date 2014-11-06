# -*- coding: utf-8 -*-
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
        self.album_list.verticalScrollBar().valueChanged.connect(self.test)
        self.album_list.setUniformItemSizes(True)

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

    def test(self):
        print(self.album_list.viewport().rect())
        index = self.album_list.indexAt(QtCore.QPoint(64,64))
        #QtCore.QPoint(0, self.album_list.visualRect(index).y() +
        #              self.album_list.visualRect(index).height()+1)))

        modelindex = self.album_list.model().mapToSource(index)

        album = modelindex.data(ModelToItemStrat.FILTER)
        item = self.library.albums_proxylist.model.itemFromIndex(modelindex)
        item.setIcon(QtGui.QIcon(album.get_art()))
