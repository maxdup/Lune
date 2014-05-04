from PySide import QtGui
from PySide.QtCore import Qt
from views.playbackControls import PlaybackControls


class MainWindow(QtGui.QWidget):

    def __init__(self, player):
        QtGui.QWidget.__init__(self)
        controls = PlaybackControls(player)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(controls)
        #self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon('lune.png'))
        self.setWindowTitle('Lune')
