from PySide import QtGui

from .playback_controls import PlaybackControls
from .progress_bar import ProgressBar
from .trackinfo import NowPlaying


class Status(QtGui.QWidget):
    def __init__(self, player):
        QtGui.QWidget.__init__(self)
        self.player = player

        self.controls = PlaybackControls(player)
        self.progress = ProgressBar(player)
        self.playing = NowPlaying(player)
        
        self.layout = QtGui.QGridLayout(self)
        self.layout.setContentsMargins(0,10,0,0)
        self.make_small()

    def make_large(self):
        self.clear()
        self.playing.set_compact(False)
        self.layout.addWidget(self.playing,1,0,0)
        self.layout.addWidget(self.progress,2,0,3,0,0)
        self.layout.addWidget(self.controls,3,0,0)
        self.setObjectName('status')
        self.player.status_vm.album_art_size = 250
        self.player.status_vm.update_track_info()
        self.update_style()

    def make_small(self):
        self.clear()
        self.playing.set_compact(True)
        self.layout.addWidget(self.playing,0,1,0)
        self.layout.addWidget(self.progress,0,2,0)
        self.layout.addWidget(self.controls,0,3,0)
        self.setObjectName('statuscompact')
        self.player.status_vm.album_art_size = 50
        self.player.status_vm.update_track_info()
        self.update_style()

    def clear(self):
        while self.layout.count() != 0:
            self.layout.takeAt(0)

    def update_style(self):
        self.style().unpolish(self)
        self.style().polish(self)


