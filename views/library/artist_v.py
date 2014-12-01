from PySide import QtGui

from .library_view import LibraryView


class Artist_v(LibraryView):
    def __init__(self, player, lib_vm):
        super(Artist_v, self).__init__(player, lib_vm)

        view = QtGui.QHBoxLayout()
        splitter = QtGui.QSplitter()
        splitter.addWidget(self.column(self.lib_vm.artists, self.lib_vm.artists_ctrl))
        splitter.addWidget(self.column(self.lib_vm.albums, self.lib_vm.albums_ctrl))
        splitter.addWidget(self.column(self.lib_vm.songs, self.lib_vm.songs_ctrl))
        splitter.setStretchFactor(1, 2)
        view.addWidget(splitter)
        view.setContentsMargins(0, 0, 0, 0)

        self.lib_vm.artists.show()
        self.lib_vm.albums.show()
        self.lib_vm.songs.show()

        self.setLayout(view)


    def column(self, listview, ctrl):
        col = QtGui.QWidget()
        col.setLayout(QtGui.QVBoxLayout())
        col.layout().addWidget(listview)
        col.layout().addWidget(ctrl)
        col.layout().setContentsMargins(0, 0, 0, 0)
        return col
