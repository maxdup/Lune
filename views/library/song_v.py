from PySide import QtGui

from . library_view import LibraryView


class Song_v(LibraryView):
    def __init__(self, player, lib_vm):
        super(Song_v, self).__init__(player, lib_vm)

        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.library.songs)
        layout.addWidget(self.status_bar)
