from models.song import Song
from models.album import Album
from models.artist import Artist

class Bouncer():
    def __init__(self, player):
        self.player = player

    def ask_nicely(self, something):
        self.player.stop()
        if type(something) == Song:
            print(something.path)
            self.player.queue.add_last(something)
        elif type(something) == Album:
            self.player.queue.add_last(something.songs)
        self.player.play()
