# -*- coding: utf-8 -*-

import vlc

from models.song_queue import SongQueue
from models.status_vm import StatusViewModel
from controllers.bouncer import Bouncer


class Player():
    def __init__(self):
        self.__state = {'playing': False,
                      'prepped': False}
        self.queue = SongQueue()
        self.timer = None
        self.instance = vlc.Instance()
        self.bouncer = Bouncer(self)
        self.status_vm = StatusViewModel(self)

    def __setitem__(self, key, value):
        self.__state[key] = value
        if key == 'playing':
            self.status_vm.update_playback_state()
        else:
            self.status_vm.update_track_info()

    def get_count(self):
        return self.queue.count()

    def get_current(self):
        return self.queue.get_current()

    def play_prep(self):
        self.media_player = self.instance.media_player_new()
        self.media = self.instance.media_new(self.queue.get_current().path)
        self.media_player.set_media(self.media)
        self.events = self.media_player.event_manager()
        self.events.event_attach(
            vlc.EventType.MediaPlayerEndReached, self.songEnded, 1)
        self.__state['prepped'] = True

    def play(self):
        if not self.__state['prepped']:
            self.play_prep()
        self.media_player.play()
        self['playing'] = True
        if self.timer:
            self.timer.start()

    def stop(self):
        if self.__state['prepped']:
            self.media_player.stop()
            self['playing'] = False
            self['prepped'] = False
            self.queue = SongQueue()


    def play_pause(self):
        if self.__state['prepped']:
            if self.media_player.get_time() == -1:
                self.media_player.play()
            else:
                self.media_player.pause()
                if not self.__state['playing']:
                    self.timer.start()
            self['playing'] = not self.__state['playing']

    def skip(self):
        if self.__state['prepped']:
            self.media_player.stop()
            self.queue.get_text()
            self.play_prep()
            if self.__state['playing']:
                self.play()

    def previous(self):
        if self.__state['prepped']:
            time = self.media_player.get_time() < 2500
            self.media_player.stop()
            if time:
                self.queue.get_prev()
            self.play_prep()
            if self.__state['playing']:
                self.media_player.play()

    def set_queue(self, queue):
        self.queue = queue
        if not queue.is_empty():
            self.play_prep()

    def set_volume(self, volume):
        return None

    def seek(self, position):
        self.media_player.set_position(position / 500)

    def get_position(self):
        return self.media_player.get_position()

    def is_playing(self):
        return self.__state['playing']

    def set_timer(self, timer):
        self.timer = timer

    # todo, figure out what's being sent by the callback
    # altho it's probably not useful all that useful
    def songEnded(self, data, moredata):
        if self.queue.get_text():
            self.play_prep()
            self.play()
        else:
            self.__state['playing'] = False
            self.queue.reset_queue()
            self.play_prep()
