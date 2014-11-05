class Album:
    def __init__(self, title='unknown', songs=[], artist=None):
        self.title = title
        self.songs = songs
        self.artist = artist
        self.artwork = None

    def get_art(self):
        if self.songs and not self.artwork:
            for song in self.songs:
                if song.track_info['artwork']:
                    self.artwork = song.track_info['artwork']
                    break
        return self.artwork
