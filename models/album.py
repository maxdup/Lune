class Album:
    def __init__(self, title='unknown', songs=[]):
        self.title = title
        self.songs = songs
        self.artwork = None

    def get_art(self):
        if self.songs and not self.artowrk:
            for song in songs:
                if song.trackinfo['artwork']:
                    self.artwork = song.trackinfo['artwork']
                    break
        return self.artwork
