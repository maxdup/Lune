# -*- coding: utf-8 -*-

import os
from models.song import Song
from models.userSettings import Path
from DAL.identifier import Identifier


class Collector():

    FORMATS = ['mp3', 'flac', 'aac', 'ogg']

    def __init__(self, library):
        self.library = library
        self.identifier = Identifier()

    def searchDir(self, pathObj):
        found = []
        directory = os.walk(pathObj.path)
        for root, dirs, files in directory:
            for file in files:
                if file.split('.').pop() in self.FORMATS:
                    song = Song(os.path.join(root, file))
                    self.identifier.identify(song)
                    found.append(song)

        self.library.addSong(found)
        print(('Found ' + str(len(self.library.getLibrary())) + ' audio files'))
