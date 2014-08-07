from PySide import QtGui


class Trackinfo(QtGui.QWidget):
    def __init__(self, player):
        self.player = player
        QtGui.QWidget.__init__(self)
        
        layout = QtGui.QVBoxLayout(self)
    
        if player.get_current():
            self.info = player.get_current().track_info
        else:
            self.info = {
                'title':'',
                'album':'',
                'artist':''
                }

        self.title_display = QtGui.QLabel(self.info['title'])
        self.album_display = QtGui.QLabel(self.info['album'])
        self.artist_display = QtGui.QLabel(self.info['artist'])
        layout.addWidget(self.title_display)
        layout.addWidget(self.album_display)
        layout.addWidget(self.artist_display)

    def update(self):
        self.info = player.get_current().trackInfo
        self.title_display.setText(self.info['title'])
        self.album_display.setText(self.info['album'])
        self.artist_display.setText(self.info['artist'])
        self.repaint()