# -*- coding: utf-8 -*-

import os

from dal.identifier import Identifier
from models.song import Song


class Collector():
    FORMATS = ['mp3', 'flac', 'aac', 'ogg', 'ape', 'wav', 'pcm', 'aiff', 'm4a', 'oga', 'opus', 'mpc']

    def __init__(self):
        self.identifier = Identifier()

    def search_dir(self, work_queue, path_obj):
        found = []
        directory = os.walk(path_obj.path)
        for root, dirs, files in directory:
            for file in files:
                if file.split('.').pop() in self.FORMATS:
                    song = Song(os.path.join(root, file))
                    self.identifier.identify(song)
                    found.append(song)
        work_queue.put(found)
