from PySide import QtGui


class Trackinfo(QtGui.QWidget):
    def __init__(self, player):
        self.player = player
        QtGui.QWidget.__init__(self)
        
        layout = QtGui.QVBoxLayout(self)

        layout.addWidget(self.player.status_vm.title_display)
        layout.addWidget(self.player.status_vm.album_display)
        layout.addWidget(self.player.status_vm.artist_display)
