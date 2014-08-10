from PySide import QtGui

from . library_view import LibraryView


class Album_v(LibraryView):
    def __init__(self, player, lib_vm):
        super(Album_v, self).__init__(player, lib_vm)
        
        view = QtGui.QHBoxLayout()
        view.addWidget(self.library.albums)
        view.addWidget(self.library.songs)
        self.library.artists.hide()
        self.library.albums.show()
        self.library.songs.show()

        self.setLayout(view)
