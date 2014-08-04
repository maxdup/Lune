from models.song import Song
from PySide.QtGui import QListWidget, QListWidgetItem

class LibraryViewModel:
    def __init__(self):
        self.songs = QListWidget()

        # todo implement
        self.albums = QListWidget()
        self.artists = QListWidget()
        self.genras = QListWidget()
        self.years = QlistWidget()

    def add_any(self, something):
        print(type(something))

        if type(something) == Song:
            print('added')
            item = QListWidgetItem(self.songs)
            item.setText(something.track_info['title'])
            item.setData(1000, something)
            self.songs.addItem(item)
