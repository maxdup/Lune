from PySide import QtGui
from PySide.QtCore import Qt
from views.playbackControls import PlaybackControls
from views.libraryView import LibraryView


class MainWindow(QtGui.QWidget):

    def __init__(self, player):
        QtGui.QWidget.__init__(self)
        library = LibraryView(player)
        controls = PlaybackControls(player)
        layout = QtGui.QGridLayout(self)
        layout.addWidget(library, 0, 0)
        layout.addWidget(controls, 0, 1)
        #self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon('lune.png'))
        self.setWindowTitle('Lune')
