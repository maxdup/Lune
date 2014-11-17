from PySide import QtGui

from .library_view import LibraryView


class Artist_v(LibraryView):
    def __init__(self, player, lib_vm):
        super(Artist_v, self).__init__(player, lib_vm)

        view = QtGui.QHBoxLayout()
        splitter = QtGui.QSplitter()
        splitter.addWidget(self.lib_vm.artists)
        splitter.addWidget(self.lib_vm.albums)
        splitter.addWidget(self.lib_vm.songs)
        splitter.setStretchFactor(1, 2)
        view.addWidget(splitter)
        view.setContentsMargins(0, 0, 0, 0)

        self.lib_vm.artists.show()
        self.lib_vm.albums.show()
        self.lib_vm.songs.show()

        self.setLayout(view)

