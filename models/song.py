# -*- coding: utf-8 -*-


class Song:
    def __init__(self, path=None, trackinfo={}):
        self.path = path
        self.trackInfo = trackinfo

    def getTrackInfo(self):
        return self.trackinfo

    def getPath(self):
        return self.path

    def getFileImage(self):
        return None
