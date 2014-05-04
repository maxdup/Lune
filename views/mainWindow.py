from PySide import QtGui
from views.playbackControls import PlaybackControls


class MainWindow(QtGui.QWidget):

    def __init__(self, player):
        QtGui.QWidget.__init__(self)
        controls = PlaybackControls(player)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(controls)
