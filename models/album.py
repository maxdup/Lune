import os

class Album:
    def __init__(self, title='unknown', songs=[], artist=None):
        self.title = title
        self.songs = songs
        self.artist = artist
        self.artwork = None

    def get_art(self):
        if self.songs and not self.artwork:
            for song in self.songs:

                self.artwork = song.track_info['artwork']  #directly in track info
                if not self.artwork or not os.path.exists(self.artwork):
                    filenames = ['/Folder.jpg', '/folder.jpg']

                    for name in filenames:
                        path = os.path.split(song.path)[0] + name
                        if os.path.exists(path):
                            self.artwork = path
                            break
                if self.artwork:
                    break
        return self.artwork
