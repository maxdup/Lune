# -*- coding: utf-8 -*-

from PySide import QtGui

from views.status.status import Status
from models.libraryViewModel import LibraryViewModel


class LibraryView(QtGui.QWidget):
    def __init__(self, player, library_vm):
        QtGui.QWidget.__init__(self)

        self.player = player
        self.status_bar = Status(self.player)
        self.library = library_vm
        self.songlist = library_vm.songs
        self.songlist.itemDoubleClicked.connect(self._song_double_clicked)

        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.songlist)
        layout.addWidget(self.status_bar)

    def _song_double_clicked(self, item):
        if self.player.is_playing():
            self.player.stop()
        self.player.queue.add_last(item.data)
        self.player.play_prep()
        self.player.play()

