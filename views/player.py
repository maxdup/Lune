from models.songQueue import SongQueue
import vlc


class Player():
    def __init__(self):
        self.queue = SongQueue()
        self.playing = False
        self.instance = vlc.Instance()

    def getCount(self):
        print((self.queue.count()))
        return self.queue.count()

    def PlayPrep(self):
        self.mediaplayer = self.instance.media_player_new()
        self.media = self.instance.media_new(self.queue.getCurrent().getPath())
        self.mediaplayer.set_media(self.media)

        self.events = self.mediaplayer.event_manager()
        self.events.event_attach(
            vlc.EventType.MediaPlayerEndReached, self.songEnded, 1)

    def Play(self):
        self.mediaplayer.play()
        self.playing = True

    def Stop(self):
        self.mediaplayer.stop()
        self.playing = False

    def PlayPause(self):
        if self.mediaplayer.get_time() == -1:
            self.mediaplayer.play()
        else:
            self.mediaplayer.pause()
        self.playing = not self.playing

    def Skip(self):
        self.mediaplayer.stop()
        self.queue.getNext()
        self.PlayPrep()
        if self.playing:
            self.Play()

    def Previous(self):
        time = self.mediaplayer.get_time() < 2500
        self.mediaplayer.stop()
        if time:
            self.queue.getPrev()
        self.PlayPrep()
        if self.playing:
            self.mediaplayer.play()

    def SetQueue(self, queue):
        self.queue = queue
        self.PlayPrep()

    def SetVolume(self, volume):
        return None

    def Seek(self, position):
        return None

    def IsPlaying(self):
        return self.mediaplayer.is_playing()

    # todo, figure out what's being sent by the callback
    # altho it's probably not useful all that useful
    def songEnded(self, data, moredata):
        self.mediaplayer.stop()
        self.queue.getNext()
        self.PlayPrep()
        self.Play()