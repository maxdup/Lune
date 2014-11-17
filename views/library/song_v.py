from PySide import QtGui

from .library_view import LibraryView


class Song_v(LibraryView):
    def __init__(self, player, lib_vm):
        super(Song_v, self).__init__(player, lib_vm)

        view = QtGui.QHBoxLayout()
        view.addWidget(self.lib_vm.songs)
        view.setContentsMargins(0,0,0,0)

        self.lib_vm.artists.hide()
        self.lib_vm.albums.hide()
        self.lib_vm.songs.show()

        self.setLayout(view)
