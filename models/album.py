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
                if not self.artwork:
                    folderjpg = os.path.split(song.path)[0] + '/Folder.jpg'
                    #multiplatform?
                    if os.path.exists(folderjpg):
                        self.artwork = folderjpg
                if self.artwork:
                    break
        return self.artwork
