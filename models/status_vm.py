from PySide import QtGui, QtCore


class StatusViewModel:
    def __init__(self, player):

        self.player = player
        self.title_display = QtGui.QLabel()
        self.album_display = QtGui.QLabel()
        self.artist_display = QtGui.QLabel()
        self.art = QtGui.QLabel()
        
    def update(self):
        if self.player.get_current():
            self.info = self.player.get_current().track_info
        else:
            self.info = {'title':'', 'album':'', 'artist':'', 'artwork':''}

        self.title_display.setText(self.info['title'])
        self.album_display.setText(self.info['album'])
        self.artist_display.setText(self.info['artist'])

        art = QtGui.QPixmap(self.info['artwork'])
        self.art.setPixmap(art.scaled(QtCore.QSize(70,70), QtCore.Qt.KeepAspectRatio))
