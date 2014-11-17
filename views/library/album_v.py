from PySide import QtGui

from .library_view import LibraryView


class Album_v(LibraryView):
    def __init__(self, player, lib_vm):
        super(Album_v, self).__init__(player, lib_vm)
        
        view = QtGui.QHBoxLayout()
        splitter = QtGui.QSplitter()
        splitter.addWidget(self.library.albums)
        splitter.addWidget(self.library.songs)
        splitter.setStretchFactor(0,2)
        view.addWidget(splitter)
        view.setContentsMargins(0,0,0,0)

        self.library.artists.hide()
        self.library.albums.show()
        self.library.songs.show()

        self.setLayout(view)
