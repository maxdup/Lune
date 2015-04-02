from PySide import QtGui, QtCore

from models.song import Song
from views.library.model_to_item_strategy import ModelToItemStrat, get_song_item
from views.library.librarylistview import LibraryListView


class StatusViewModel:
    def __init__(self, player):

        self.player = player
        self.title_display = QtGui.QLabel()
        self.album_display = QtGui.QLabel()
        self.artist_display = QtGui.QLabel()
        self.album_art_display = QtGui.QLabel()
        self.album_art_size = 70
        self.album_art = QtGui.QPixmap()

        self.pause_resume = QtGui.QPushButton(']')

        self.curr_song = None

        self.queue = LibraryListView(ModelToItemStrat(get_song_item))
        self.item_strat = ModelToItemStrat(get_song_item)

    def update(self):
        self.update_track_info()
        self.update_playback_state()
        self.update_track_list()

    def update_track_list(self):
        self.queue.itemmodel.clear()
        for song in self.player.queue:
            self.queue.add(song)

    def update_track_info(self):
        if self.player.get_current():
            self.song = self.player.get_current()
            if self.song.album:
                self.album_art = QtGui.QPixmap(self.song.album.get_art())
        else:
            self.album_art = None
            self.song = Song(None,
                             {'title':'', 'album':'', 'artist':'', 'artwork':''},
                             None)

        self.title_display.setText(self.song.track_info['title'])
        self.album_display.setText(self.song.track_info['album'])
        self.artist_display.setText(self.song.track_info['artist'])

        if self.album_art:
            self.album_art_display.setPixmap(self.album_art.scaled(
                QtCore.QSize(self.album_art_size,
                             self.album_art_size),
                QtCore.Qt.KeepAspectRatio))
        else:
            self.album_art_display.setPixmap(QtGui.QPixmap())

    def update_playback_state(self):
        #todo: handle disabled states for skip/previous buttons
        self.pause_resume.setText('[' if self.player.is_playing() else ']')
