# -*- coding: utf-8 -*-

from PySide import QtGui

from views.status import Status


class LibraryView(QtGui.QWidget):
    def __init__(self, player, library):
        QtGui.QWidget.__init__(self)

        self.player = player
        self.status_bar = Status(self.player)

        self.list = QtGui.QListWidget()
        self.list.itemDoubleClicked.connect(self._song_double_clicked)
        for idx, song in enumerate(library.songs):
            try:
                item = QtGui.QListWidgetItem(self.list)
                item.setText(song.track_info['title'])
                # role, index. Created a dummy role '1000' for now.
                item.setData(1000, idx)
            except KeyError:
                pass

        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.list)
        layout.addWidget(self.status_bar)


    def _song_double_clicked(self, item):
        index = item.data(1000)
        if self.player.is_playing():
            self.player.stop()
        self.player.queue.get_at_index(index)
        self.player.play_prep()
        self.player.play()

    def update(self):
        return None
