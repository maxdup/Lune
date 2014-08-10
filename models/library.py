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

    def remove_song(self, r_song):
        for album in [album for album in self.albums if r_song in album.songs]:
            album.songs = [song for song in album.songs if song is not r_song]
        if len(album.songs) == 0:
            self.remove_album(album)
            self.albums.remove(album)

    def remove_album(self, r_album):
        for artist in [artist for artist in self.artists if r_album in artist.albums]:
            artist.albums = [album for album in artist.albums if album is not r_album]
        if len(artist.albums) == 0:
            self.remove_artist(artist)

    def remove_artist(self, artist):
        self.artists.remove(artist)

    def remove_path(self, path):
        for song in [song for song in self.songs if song.path.startswith(path)]:
            self.remove_song(song)
        self.songs = [song for song in self.songs if not song.path.startswith(path)]
        self.lib_vm.rebuild(self)
