# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from PySide import QtGui
from PySide.QtCore import QModelIndex

from views.status.status import Status
from models.library_vm import LibraryViewModel

FILTER = 1001
PLAY = 1002

class LibraryView(QtGui.QWidget):
    def __init__(self, player, library_vm):
        QtGui.QWidget.__init__(self)

        self.player = player
        self.library = library_vm

        self.song_list = library_vm.songs
        self.song_list.doubleClicked.connect(self._item_double_clicked)

        self.album_list = library_vm.albums
        self.album_list.itemClicked.connect(self._item_clicked)
        self.album_list.itemDoubleClicked.connect(self._item_double_clicked)

        self.artist_list = library_vm.artists
        self.artist_list.itemClicked.connect(self._item_clicked)
        self.artist_list.itemDoubleClicked.connect(self._item_double_clicked)

    def _item_clicked(self, item):
        self.library.filtering(item.data(FILTER))

    def _item_double_clicked(self, item):
        self.player.bouncer.ask_nicely(item.data(PLAY))
