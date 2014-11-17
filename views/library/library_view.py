# -*- coding: utf-8 -*-
import os

from PySide import QtGui

from models.playlist import Playlist
from models.library_vm import LibraryViewModel

from .model_to_item_strategy import ModelToItemStrat


class LibraryView(QtGui.QWidget):
    def __init__(self, bouncer, library_vm):
        QtGui.QWidget.__init__(self)

        self.bouncer = bouncer
        self.lib_vm = library_vm

        self.song_list = self.lib_vm.songs
        self.song_list.doubleClicked.connect(self._song_double_clicked)

        self.album_list = self.lib_vm.albums
        model = self.album_list.selectionModel()
        model.selectionChanged.connect(self._album_selection_changed)
        self.album_list.doubleClicked.connect(self._item_double_clicked)

        self.artist_list = self.lib_vm.artists
        model = self.artist_list.selectionModel()
        model.selectionChanged.connect(self._artist_selection_changed)
        self.artist_list.doubleClicked.connect(self._item_double_clicked)

    def _artist_selection_changed(self):
        for index in self.artist_list.selectedIndexes():
            item = self.artist_list.model().mapToSource(index)
            self.lib_vm.filtering(
                item.data(ModelToItemStrat.FILTER))

    def _album_selection_changed(self):
        for index in self.album_list.selectedIndexes():
            item = self.album_list.model().mapToSource(index)
            self.lib_vm.filtering(
                item.data(ModelToItemStrat.FILTER))

    def _item_double_clicked(self, item):
        self.bouncer.ask_nicely(
            item.data(ModelToItemStrat.PLAY))

    def _song_double_clicked(self, item):
        songs = []
        start_at = None
        for i in range(0, self.song_list.model().rowCount()):
            song = self.song_list.model().index(i,0).data(ModelToItemStrat.PLAY)
            if not start_at and song == item.data(ModelToItemStrat.PLAY):
                start_at = i
            songs.append(song)
        self.bouncer.ask_nicely(Playlist(songs, start_at))
