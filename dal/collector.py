# -*- coding: utf-8 -*-

import os

from dal.identifier import Identifier
from models.song import Song


class Collector():
    def __init__(self):
        self.identifier = Identifier()

    def search_dir(self, work_queue, path_obj, extension_list):
        found = []
        directory = os.walk(path_obj.path)
        for root, dirs, files in directory:
            for file in files:
                if file.split('.').pop() in extension_list:
                    song = Song(os.path.join(root, file))
                    self.identifier.identify(song)
                    found.append(song)
        work_queue.put(found)
