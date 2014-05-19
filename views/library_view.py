# -*- coding: utf-8 -*-

from PySide import QtGui

from views.playback_controls import PlaybackControls
from views.progress_bar import ProgressBar


class LibraryView(QtGui.QWidget):
    def __init__(self, player, library):
        QtGui.QWidget.__init__(self)

        self.player = player

        self.controls = PlaybackControls(player)
        self.progress = ProgressBar(player)

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

        layout = QtGui.QGridLayout(self)
        layout.addWidget(self.list, 0, 0, 1, 0)
        layout.addWidget(self.progress, 1, 0)
        layout.addWidget(self.controls, 1, 1)

    def _song_double_clicked(self, item):
        index = item.data(1000)
        if self.player.is_playing():
            self.player.stop()
        self.player.queue.get_at_index(index)
        self.player.play_prep()
        self.player.play()

    def update(self):
        return None
