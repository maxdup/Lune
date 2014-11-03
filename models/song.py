# -*- coding: utf-8 -*-


class Song:
    def __init__(self, path=None, track_info={}, album=None):
        self.path = path
        self.track_info = track_info
        self.album = album

    def setAlbum(self, album):
        self.album = album
