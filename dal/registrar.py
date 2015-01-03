import os

from models.lib_operation import LibOperation, remove_song

class Registrar():
    def __init__(self, library):
        self.library = library

    def clean_library(self, operation_queue):
        operations = []
        for song in self.library.songs:
            if not os.path.isfile(song.path):
                operation_queue.push(LibOperation(song, remove_song))
