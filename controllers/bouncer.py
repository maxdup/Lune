from models.song import Song
from models.album import Album
from models.artist import Artist
from models.playlist import Playlist
from models.song_queue import SongQueue

class Bouncer():
    def __init__(self, player):
        self.player = player

    def ask_nicely(self, something):
        self.player.stop()

        if type(something) == Song:
            self.player.queue.add_last(something)

        elif isinstance(something, Playlist):
            self.player.queue = SongQueue(something.songs, something.start_at)
            if type(something) == Album:
                self.player.queue.order_by(SongQueue.Order.TRACKNB)

        elif type(something) == Artist:
            for album in something.albums:
                self.player.queue.add_last(album.songs)

        self.player.play()
        self.player.status_vm.update_track_list()
