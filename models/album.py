import os

class Album:
    def __init__(self, title='unknown', songs=[], artist=None):
        self.title = title
        self.songs = songs
        self.artist = artist
        self.artwork = None
        self.placeholder = None

    def get_art(self):
        if not self.songs:
            return
        if not self.artwork or not os.path.exists(self.artwork):
            filenames = ['/Folder.jpg', '/folder.jpg']
            for name in filenames:
                path = os.path.split(self.songs[0].path)[0] + name
                if os.path.exists(path):
                    self.artwork = path
                if not self.artwork:
                    for song in self.songs:
                        if song.track_info['artwork'] and os.path.exists(
                                song.track_info['artwork']):
                            self.artwork = song.track_info['artwork']
                            break
        return self.artwork
