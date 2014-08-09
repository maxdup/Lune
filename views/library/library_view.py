# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

from PySide import QtGui

from views.status.status import Status
from models.libraryViewModel import LibraryViewModel


class LibraryView(QtGui.QWidget):
    def __init__(self, player, library_vm):
        QtGui.QWidget.__init__(self)

        self.player = player
        self.status_bar = Status(self.player)
        self.library = library_vm
        self.song_list = library_vm.songs
        self.song_list.itemDoubleClicked.connect(self._item_double_clicked)
        self.album_list = library_vm.albums
        self.album_list.itemClicked.connect(self._item_clicked)

    @abstractmethod
    def _item_clicked(self, item):
        self.library.filtering(item.data(1001))

    @abstractmethod
    def _item_double_clicked(self, item):
        if self.player.is_playing():
            self.player.stop()
        self.player.queue.add_last(item.data(1002))
        self.player.play_prep()
        self.player.play()
