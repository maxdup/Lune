# -*- coding: utf-8 -*-

import os

from dal.identifier import Identifier
from models.song import Song
from models.lib_operation import LibOperation, add_song


class Collector():
    def __init__(self):
        self.identifier = Identifier()

    def search_dir(self, multiprocess_queue, path, extension_list):
        directory = os.walk(path)
        for root, dirs, files in directory:
            for file in files:
                if file.split('.').pop() in extension_list:
                    song = Song(os.path.join(root, file))
                    self.identifier.identify(song)
                    op = LibOperation(song, add_song)
                    multiprocess_queue.put(op)
