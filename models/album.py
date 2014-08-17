class Album:
    def __init__(self, title='unknown', songs=[]):
        self.title = title
        self.songs = songs

    def get_art(self):
        if self.songs:
            #todo: search all indexes adn save the path
            return self.songs[0].track_info['artwork']
