from PySide import QtGui


class Trackinfo(QtGui.QWidget):
    def __init__(self, status_vm):
        self.status = status_vm
        QtGui.QWidget.__init__(self)
        
        layout = QtGui.QVBoxLayout(self)

        layout.addWidget(self.status.title_display)
        layout.addWidget(self.status.album_display)
        layout.addWidget(self.status.artist_display)
