from PySide import QtGui
from views.library.librarylistview import LibraryListView

class NowPlaying(QtGui.QWidget):
    def __init__(self, player):
        QtGui.QWidget.__init__(self)

        self.trackinfo = TrackInfo(player.status_vm)
        self.art = AlbumArt(player.status_vm)
        self.queue = player.status_vm.queue

        layout = QtGui.QHBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(self.queue)
        layout.addWidget(self.art)
        layout.addWidget(self.trackinfo)
        layout.addStretch()

    def set_compact(self, compact):
        if compact:
            self.queue.hide()
        else:
            self.queue.show()

class AlbumArt(QtGui.QWidget):
    def __init__(self, status_vm):
        QtGui.QWidget.__init__(self)

        layout = QtGui.QVBoxLayout(self)
        layout.addStretch()
        layout.addWidget(status_vm.album_art_display)

class TrackInfo(QtGui.QWidget):
    def __init__(self, status_vm):
        QtGui.QWidget.__init__(self)

        layout = QtGui.QVBoxLayout(self)

        layout.addStretch()
        layout.addWidget(status_vm.title_display)
        layout.addWidget(status_vm.album_display)
        layout.addWidget(status_vm.artist_display)
