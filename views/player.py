from models.songQueue import SongQueue
import vlc

class Player():
    def __init__(self):
        self.instance = vlc.Instance()
        self.mediaplayer = self.instance.media_player_new()
        self.Queue = SongQueue()

    def play(self):
        self.media = self.instance.media_new(self.Queue.getCurrent())
        self.mediaplayer.set_media(self.media)
        self.mediaplayer.play()

    def setQueue(self, newQueue):
        self.Queue = newQueue
