import os
from models.song import Song


class Collector():

    FORMATS = ['mp3', 'flac', 'aac', 'ogg']

    def __init__(self, library):
        self.library = library

    def searchDir(self, dir):
        found = []
        directory = os.walk(dir)
        for root, dirs, files in directory:
            for file in files:
                if file.split('.').pop() in self.FORMATS:
                    found.append(Song(os.path.join(root, file)))
        self.library.addSong(found)
        print(('Found ' + str(len(self.library.getLibrary())) + ' audio files'))