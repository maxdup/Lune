from models.songQueue import SongQueue
import vlc

class Player():
    def __init__(self):
        self.instance = vlc.Instance()
        self.mediaplayer = self.instance.media_player_new()
        self.Queue = SongQueue()
        self.playing = False

    def setQueue(self, newQueue):
        self.Queue = newQueue

    def setVolume(self, volume):
        self.mediaplayer.audio_set_volume(volume)

    def seek(self, position):
        self.mediaplayer.set_position(position / 500)

    def isPlaying(self):
        return self.playing

    def play(self):
        self.media = self.instance.media_new(self.Queue.getCurrent())
        self.mediaplayer.set_media(self.media)
        self.mediaplayer.play()
        self.playing = True

    def pause(self):
        self.mediaplayer.pause()
        self.playing = False

    def resume(self):
        self.mediaplayer.play()
        self.playing = True

    def stop(self):
        self.mediaplayer.stop()
        self.playing = False

    def playPause(self):
        if self.playing:
            self.pause()
        elif self.mediaplayer.play() == -1:
            self.play()
        else:
            self.resume()
