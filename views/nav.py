from PySide import QtGui

from views.library.artist_v import Artist_v
from views.library.album_v import Album_v
from views.library.song_v import Song_v


class Nav(QtGui.QWidget):
    def __init__(self, view_stack, library, library_v, player):
        QtGui.QWidget.__init__(self)
        self.setObjectName('nav')

        self.view_stack = view_stack
        self.library = library
        self.library_v = library_v

        self.layout = QtGui.QHBoxLayout()

        self.goto_song = QtGui.QPushButton('song')
        self.goto_song.clicked.connect(
            lambda: self.set_lib_view(Song_v(player, library.lib_vm)))
        self.goto_album = QtGui.QPushButton('album')
        self.goto_album.clicked.connect(
            lambda: self.set_lib_view(Album_v(player, library.lib_vm)))
        self.goto_artist = QtGui.QPushButton('artist')
        self.goto_artist.clicked.connect(
            lambda: self.set_lib_view(Artist_v(player, library.lib_vm)))
        self.goto_lib = QtGui.QPushButton('back')
        self.goto_lib.clicked.connect(
            lambda: self.view_stack.setCurrentIndex(0))

        self.layout.addWidget(self.goto_artist)
        self.layout.addWidget(self.goto_album)
        self.layout.addWidget(self.goto_song)
        self.layout.addWidget(self.goto_lib)
        self.layout.addStretch()

        self.setLayout(self.layout)        

        self.set_lib_view(Artist_v(player, library.lib_vm))

    def set_lib_view(self, view):
        self.library_v.setLayout(QtGui.QHBoxLayout())
        while self.library_v.layout().count() != 0:
            self.library_v.layout().takeAt(0)
        self.library_v.layout().addWidget(view)
        self.library.lib_vm.filtering()
