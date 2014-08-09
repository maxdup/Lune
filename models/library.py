# -*- coding: utf-8 -*-

from models.song import Song
from models.album import Album
from models.artist import Artist
from models.library_vm import LibraryViewModel


class Library:
    def __init__(self):
        self.songs = []
        self.albums = []
        self.artists = []
        self.genres = []
        self.record = []
        self.lib_vm = LibraryViewModel()

    def add_song(self, song):
        if type(song) == Song:
            artist = list(artist for artist in self.artists \
                          if artist.name == song.track_info['artist'])
            if artist:
                artist = artist[0]
            else:
                artist = Artist(song.track_info['artist'])
                self.artists.append(artist)
                self.lib_vm.add_any(artist)

            album = list(album for album in artist.albums \
                     if album.title == song.track_info['album'])

            if album:
                album = album[0]
                album.songs.append(song)
            else:
                album = Album(song.track_info['album'], [song])
                self.albums.append(album)
                self.lib_vm.add_any(album)
                artist.albums.append(album)


            self.songs.append(song)
            self.lib_vm.add_any(song)

        elif type(song) == list:
            for s in song:
                self.add_song(s)
