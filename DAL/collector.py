import os


class Collector():

    FORMATS = ['mp3', 'flac', 'aac', 'ogg']

    def __init__(self):
        self.library = []

    def searchDir(self, dir):
        directory = os.walk(dir)
        for root, dirs, files in directory:
            for file in files:
                if file.split('.').pop() in self.FORMATS:
                    self.library.append(os.path.join(root, file))
        print(('Found ' + str(len(self.library)) + ' audio files'))