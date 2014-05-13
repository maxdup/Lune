# -*- coding: utf-8 -*-

from models.songQueue import SongQueue
import vlc


class Player():
    def __init__(self):
        self.queue = SongQueue()
        self.playing = False
        self.instance = vlc.Instance()
        self.prepped = False

    def getCount(self):
        return self.queue.count()

    def PlayPrep(self):
        self.mediaplayer = self.instance.media_player_new()
        self.media = self.instance.media_new(self.queue.getCurrent().getPath())
        self.mediaplayer.set_media(self.media)
        self.events = self.mediaplayer.event_manager()
        self.events.event_attach(
            vlc.EventType.MediaPlayerEndReached, self.songEnded, 1)
        self.prepped = True

    def Play(self):
        self.mediaplayer.play()
        self.playing = True
        if self.timer is not None:
            self.timer.start()

    def Stop(self):
        if self.prepped:
            self.mediaplayer.stop()
            self.playing = False

    def PlayPause(self):
        if self.prepped:
            if self.mediaplayer.get_time() == -1:
                self.mediaplayer.play()
            else:
                self.mediaplayer.pause()
                if not self.playing:
                    self.timer.start()
            self.playing = not self.playing

    def Skip(self):
        if self.prepped:
            self.mediaplayer.stop()
            self.queue.getNext()
            self.PlayPrep()
            if self.playing:
                self.Play()

    def Previous(self):
        if self.prepped:
            time = self.mediaplayer.get_time() < 2500
            self.mediaplayer.stop()
            if time:
                self.queue.getPrev()
            self.PlayPrep()
            if self.playing:
                self.mediaplayer.play()

    def SetQueue(self, queue):
        self.queue = queue
        if not queue.isEmpty():
            self.PlayPrep()

    def SetVolume(self, volume):
        return None

    def Seek(self, position):
        self.mediaplayer.set_position(position / 500)

    def getPosition(self):
        return self.mediaplayer.get_position()

    def IsPlaying(self):
        return self.mediaplayer.is_playing()

    def setTimer(self, timer):
        self.timer = timer

    # todo, figure out what's being sent by the callback
    # altho it's probably not useful all that useful
    def songEnded(self, data, moredata):
        if self.queue.getNext():
            self.PlayPrep()
            self.Play()
        else:
            self.playing = False
            self.queue.resetQueue()
            self.PlayPrep()
