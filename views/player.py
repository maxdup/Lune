from models.songQueue import SongQueue
import vlc


class Player():
    def __init__(self):
        self.queue = SongQueue()

        self.instance = vlc.Instance()

    def getCount(self):
        print((self.queue.count()))
        return self.queue.count()

    def PlayPrep(self):
        self.mediaplayer = self.instance.media_player_new()
        self.media = self.instance.media_new(self.queue.getNext().getPath())
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

    def Skip(self):
        return None

    def Previous():
        return None

    def SetQueue(self, queue):
        self.queue = queue
        self.PlayPrep()

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