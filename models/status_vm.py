from PySide import QtGui, QtCore

from models.song import Song

class StatusViewModel:
    def __init__(self, player):

        self.player = player
        self.title_display = QtGui.QLabel()
        self.album_display = QtGui.QLabel()
        self.artist_display = QtGui.QLabel()
        self.album_art_display = QtGui.QLabel()

        self.album_art = QtGui.QPixmap()
        
        self.pause_resume = QtGui.QPushButton(']')

        self.curr_song = None

    def update(self):
        self.update_track_info()
        self.update_playback_state()

    def update_track_info(self):
        if self.player.get_current():
            self.song = self.player.get_current()
            if self.song.album:
                self.album_art = QtGui.QPixmap(self.song.album.get_art())
        else:
            self.song = Song(None,
                             {'title':'', 'album':'', 'artist':'', 'artwork':''},
                             None)

        self.title_display.setText(self.song.track_info['title'])
        self.album_display.setText(self.song.track_info['album'])
        self.artist_display.setText(self.song.track_info['artist'])

        self.album_art_display.setPixmap(self.album_art.scaled(QtCore.QSize(70,70),
                                      QtCore.Qt.KeepAspectRatio))

    def update_playback_state(self):
        #todo: handle disabled states for skip/previous buttons
        self.pause_resume.setText('[' if self.player.is_playing() else ']')
