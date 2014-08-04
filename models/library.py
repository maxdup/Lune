# -*- coding: utf-8 -*-

from models.song import Song
from models.libraryViewModel import LibraryViewModel


class Library:
    def __init__(self):
        self.songs = []
        self.lib_vm = LibraryViewModel()

    def add_song(self, songs):
        if type(songs) == Song:
            self.songs.append(songs)
            self.lib_vm.add_any(songs)
        elif type(songs) == list:
            for song in songs:
                self.songs.append(song)
                self.lib_vm.add_any(song)
