from PySide import QtGui


class PlaybackControls(QtGui.QWidget):

    def __init__(self, player):
        QtGui.QWidget.__init__(self)
        self.previous = QtGui.QPushButton('previous')
        self.previous.clicked.connect(player.Previous)

        self.pauseresume = QtGui.QPushButton('play/pause/resume')
        self.pauseresume.clicked.connect(player.PlayPause)

        self.stop = QtGui.QPushButton('stop')
        self.stop.clicked.connect(player.Stop)

        self.skip = QtGui.QPushButton('skip')
        self.skip.clicked.connect(player.Skip)

        layout = QtGui.QVBoxLayout(self)

        layout.addWidget(self.previous)
        layout.addWidget(self.pauseresume)
        layout.addWidget(self.stop)
        layout.addWidget(self.skip)