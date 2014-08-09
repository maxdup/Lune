from models.song import Song
from models.album import Album
from PySide.QtGui import QListWidget, QListWidgetItem

class LibraryViewModel:
    def __init__(self):
        self.songs = QListWidget()

        # todo implement
        self.albums = QListWidget()
        self.artists = QListWidget()
        self.genras = QListWidget()
        self.years = QListWidget()

    def add_any(self, something):
        if type(something) == Song:
            item = QListWidgetItem(self.songs)
            item.setText(something.track_info['title'])
            item.setData(1000, something)
            self.songs.addItem(item)

    def filter(self, something):
        if type(something) == Album:
            self.songs.clear()
            for song in something.songs:
                self.add_any(song)
