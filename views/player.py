from models.songQueue import SongQueue
import vlc


class Player():
    def __init__(self):
        self.Queue = SongQueue()

        self.instance = vlc.Instance()
        self.PlayPrep()

    def PlayPrep(self):
        self.mediaplayer = self.instance.media_player_new()
        self.media = self.instance.media_new(self.Queue.getNext())
        self.mediaplayer.set_media(self.media)

        self.events = self.mediaplayer.event_manager()
        self.events.event_attach(
            vlc.EventType.MediaPlayerEndReached, self.songEnded, 1)

    def Play(self):
        self.mediaplayer.play()

    def Pause(self):
        if self.mediaplayer.is_playing():
            self.mediaplayer.pause()

    def Resume(self):
        if not self.mediaplayer.is_playing():
            self.mediaplayer.play()

    def Stop(self):
        self.mediaplayer.stop()

    def PlayPause(self):
        # need to test this
        self.mediaplayer.pause()

    def SetQueue(self, newQueue):
        return None

    def SetVolume(self, volume):
        return None

    def Seek(self, position):
        return None

    def IsPlaying(self):
        return self.mediaplayer.is_playing()

    #todo, figure out what's being sent by the callback'
    def songEnded(self, data, moredata):
        print(data)
        print(moredata)

        self.PlayPrep()
        self.Play()