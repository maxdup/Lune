# -*- coding: utf-8 -*-

from models.song import Song


class SongQueue:

    class Order:
        RANDOM = -1
        TRACKNB = 0
        ALPHA = 1

    def __init__(self, queue=[], start_from=0):
        self.queue = []
        self.add_last(queue)
        self.start_from = start_from
        self.at = None

    def __nonzero__(self):
        return len(self.queue) == 0

    def __len__(self):
        return len(self.queue)

    def add_last(self, songs):
        if songs and type(songs) != list:
            songs = [songs]
        self.queue += songs

    def get_current(self):
        if not self:
            return None
        if self.at is None:
            self.at = self.start_from
        return self.queue[self.at]

    def has_next(self):
        return self and self.at + 1 != len(self.queue)

    def get_next(self):
        if self.at is None:
            self.at = self.start_from
        else:
            if self.has_next():
                self.at += 1
            else:
                return None
        return self.get_current()

    def has_prev(self):
        return self.at != self.start_from and self

    def get_prev(self):
        if not self.at:
            self.at = self.start_from
        if self.has_prev():
            self.at -= 1
        return self.get_current()

    def has_index(self, index):
        return index < len(self.queue)

    def get_at_index(self, index):
        if self.has_index(index):
            self.at = index

    def order_by(self, order, reverted=False):
        if order == self.Order.TRACKNB:
            self.queue.sort(
                key=lambda x: x.track_info['track_nb'], reverse=reverted)

    def reset_queue(self):
        self.at = None
