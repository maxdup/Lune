# -*- coding: utf-8 -*-


class Song:
    def __init__(self, path=None, track_info={}, album=None):
        self.path = path
        self.track_info = track_info
        self.album = album
        self.item = None

    def setAlbum(self, album):
        self.album = album
