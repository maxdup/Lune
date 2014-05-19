# -*- coding: utf-8 -*-

from models.song import Song


class SongQueue:

    def __init__(self, queue=[], startFrom=0):
        self.queue = []
        if len(queue) != 0:
            self.addLast(queue)
        self.startFrom = startFrom
        self.at = None

    def addLast(self, songs):
        def appendSong(song):
            if type(song) == Song:
                self.queue.append(song)
        if type(songs) == list:
            for song in songs:
                appendSong(song)
        else:
            appendSong(songs)

    def isEmpty(self):
        return len(self.queue) == 0

    def getCurrent(self):
        if self.isEmpty():
            return None
        if self.at is None:
            self.at = self.startFrom
        return self.queue[self.at]

    def hasNext(self):
        return not self.isEmpty() and self.at + 1 != len(self.queue)

    def getNext(self):
        if self.at is None:
            self.at = self.startFrom
        else:
            if self.hasNext():
                self.at += 1
            else:
                return None
        return self.getCurrent()

    def hasPrev(self):
        return self.at != self.startFrom and not self.isEmpty()

    def getPrev(self):
        if not self.at:
            self.at = self.startFrom
        else:
            if self.hasPrev():
                self.at -= 1
        return self.getCurrent()

    def hasIndex(self, index):
        return index < len(self.queue)

    def getAtIndex(self, index):
        if self.hasIndex(index):
            self.at = index

    def resetQueue(self):
        self.at = None
