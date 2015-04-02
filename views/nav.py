from PySide import QtGui

from views.library.artist_v import Artist_v
from views.library.album_v import Album_v
from views.library.song_v import Song_v


class Nav(QtGui.QWidget):
    def __init__(self, mainwindow, library, bouncer):
        QtGui.QWidget.__init__(self)
        self.setObjectName('nav')

        self.library = library
        self.library_v = mainwindow.library_v

        self.layout = QtGui.QHBoxLayout()

        self.nav_group = QtGui.QButtonGroup()
        self.nav_group.setExclusive(True)

        self.goto_song = QtGui.QPushButton('Song')
        self.goto_song.setCheckable(True)
        self.goto_song.clicked.connect(
            lambda: self.set_lib_view(Song_v(bouncer, library.lib_vm)))
        self.goto_album = QtGui.QPushButton('Album')
        self.goto_album.setCheckable(True)
        self.goto_album.clicked.connect(
            lambda: self.set_lib_view(Album_v(bouncer, library.lib_vm)))
        self.goto_artist = QtGui.QPushButton('Artist')
        self.goto_artist.setCheckable(True)
        self.goto_artist.clicked.connect(
            lambda: self.set_lib_view(Artist_v(bouncer, library.lib_vm)))
        self.goto_lib = QtGui.QPushButton('Back')
        self.goto_lib.clicked.connect(
            lambda: mainwindow.change_view('lib'))
        self.goto_now = QtGui.QPushButton('Now')
        self.goto_now.clicked.connect(
            lambda: mainwindow.change_view('now'))

        self.layout.addWidget(self.goto_artist)
        self.nav_group.addButton(self.goto_artist)
        self.layout.addWidget(self.goto_album)
        self.nav_group.addButton(self.goto_album)
        self.layout.addWidget(self.goto_song)
        self.nav_group.addButton(self.goto_song)
        self.layout.addWidget(self.goto_lib)
        self.layout.addStretch()

        self.layout.addWidget(self.goto_now)
        self.nav_group.addButton(self.goto_now)


        self.goto_lib.hide()

        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 25, 0, 0)

        self.set_lib_view(Artist_v(bouncer, library.lib_vm))
        self.goto_artist.setChecked(True)

    def set_lib_view(self, view):
        self.library_v.setLayout(QtGui.QHBoxLayout())
        while self.library_v.layout().count() != 0:
            self.library_v.layout().takeAt(0)
        if view:
            self.library_v.layout().addWidget(view)
            self.library_v.layout().setContentsMargins(0, 0, 0, 0)
            self.library.lib_vm.filtering()

    def change_area(self, area):
        if area == 'lib':
            self.goto_song.show()
            self.goto_album.show()
            self.goto_artist.show()
            self.goto_now.show()
            self.goto_lib.hide()
        else:
            self.goto_song.hide()
            self.goto_album.hide()
            self.goto_artist.hide()
            self.goto_now.hide()
            self.goto_lib.show()
