# -*- coding: utf-8 -*-

from models.song import Song
from models.album import Album
from models.libraryViewModel import LibraryViewModel


class Library:
    def __init__(self):
        self.songs = []
        self.albums = []
        self.artists = []
        self.genres = []
        self.lib_vm = LibraryViewModel()

    def add_song(self, song):
        if type(song) == Song:
            self.songs.append(song)
            self.lib_vm.add_any(song)

            album = list(album for album in self.albums \
                     if album.title == song.track_info['album'])
            if album:
                album[0].songs.append(song)
            else:
                album = Album(song.track_info['album'], [song])
                self.albums.append(album)
                self.lib_vm.add_any(album)

        elif type(song) == list:
            for s in song:
                self.add_song(s)
