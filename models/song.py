# -*- coding: utf-8 -*-


class Song:
    def __init__(self, path=None, track_info={}):
        self.path = path
        self.track_info = track_info

    def get_track_info(self):
        return self.track_info

    def get_path(self):
        return self.path

    def get_file_image(self):
        return None
