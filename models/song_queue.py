# -*- coding: utf-8 -*-

from models.song import Song


class SongQueue:
    def __init__(self, queue=[], start_from=0):
        self.queue = []
        if len(queue) != 0:
            self.add_last(queue)
        self.start_from = start_from
        self.at = None

    def add_last(self, songs):
        if type(songs) == list:
            for song in songs:
                self.queue.append(song)
        else:
            self.queue.append(songs)

    def __nonzero__(self):
        return len(self.queue) == 0

    def __len__(self):
        return len(self.queue)

    def get_current(self):
        if self.is_empty():
            return None
        if self.at is None:
            self.at = self.start_from
        return self.queue[self.at]

    def has_next(self):
        return not self.is_empty() and self.at + 1 != len(self.queue)

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
        return self.at != self.start_from and not self.is_empty()

    def get_prev(self):
        if not self.at:
            self.at = self.start_from
        else:
            if self.has_prev():
                self.at -= 1
        return self.get_current()

    def has_index(self, index):
        return index < len(self.queue)

    def get_at_index(self, index):
        if self.has_index(index):
            self.at = index

    def reset_queue(self):
        self.at = None
