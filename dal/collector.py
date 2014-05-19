# -*- coding: utf-8 -*-

import os

from models.song import Song
from dal.identifier import Identifier


class Collector():
    FORMATS = ['mp3', 'flac', 'aac', 'ogg']

    def __init__(self, library):
        self.library = library
        self.identifier = Identifier()

    def search_dir(self, path_obj):
        found = []
        directory = os.walk(path_obj.path)
        for root, dirs, files in directory:
            for file in files:
                if file.split('.').pop() in self.FORMATS:
                    song = Song(os.path.join(root, file))
                    self.identifier.identify(song)
                    found.append(song)

        self.library.add_song(found)
        print(('Found ' + str(len(self.library.songs)) + ' audio files'))
