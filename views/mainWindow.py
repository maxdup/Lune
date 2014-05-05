from PySide import QtGui

from views.playbackControls import PlaybackControls
from views.libraryView import LibraryView
from views.progressBar import ProgressBar


class MainWindow(QtGui.QWidget):

    def __init__(self, player):
        QtGui.QWidget.__init__(self)
        self.library = LibraryView(player)
        self.controls = PlaybackControls(player)
        self.progress = ProgressBar(player)

        layout = QtGui.QGridLayout(self)
        layout.addWidget(self.library, 0, 0, 1, 0)
        layout.addWidget(self.progress, 1, 0)
        layout.addWidget(self.controls, 1, 1)

        #self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon('lune.png'))
        self.setWindowTitle('Lune')


