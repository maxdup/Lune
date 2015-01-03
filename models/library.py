# -*- coding: utf-8 -*-

from models.song import Song
from models.album import Album
from models.artist import Artist
from models.library_vm import LibraryViewModel
from models.lib_operation import LibOperation, remove_song
from dal.library_db import LibraryDB


class Library:
    def __init__(self):
        self.songs = []
        self.albums = []
        self.artists = []
        self.genres = []
        self.record = []
        self.lib_vm = LibraryViewModel(self)
        self.library_db = LibraryDB()

    def load(self):
        for song in self.library_db.get_all_songs():
            self.group(song)
            self.songs.append(song)
            self.lib_vm.add_any(song)
        self.lib_vm.sort()

    def add_song(self, song):

        if type(song) == Song:
            self.group(song)
            self.songs.append(song)
            self.lib_vm.add_any(song)
            self.library_db.add_song(song)
        elif type(song) == list:
            for s in song:
                self.add_song(s)

    def remove_song(self, song):
        self.library_db.del_song(song)
        self.lib_vm.remove_any(song)
        self.songs.remove(song)

        for album in [album for album in self.albums if song in album.songs]:
            album.songs.remove(song)
        if len(album.songs) == 0:
            self.remove_album(album)

    def remove_album(self, album):
        self.lib_vm.filtering()
        self.lib_vm.remove_any(album)
        self.albums.remove(album)

        for artist in [artist for artist in self.artists if album in artist.albums]:
            artist.albums.remove(album)
        if len(artist.albums) == 0:
            self.remove_artist(artist)

    def remove_artist(self, artist):
        self.lib_vm.filtering()
        self.lib_vm.remove_any(artist)
        self.artists.remove(artist)

    def remove_path(self, path, operation_queue):
        # startswith() is not 100% accurate
        for song in [song for song in self.songs if song.path.startswith(path)]:
            operation_queue.push(LibOperation(song, remove_song))

    def group(self, song):

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
            album = Album(song.track_info['album'], [song], artist)
            self.albums.append(album)
            self.lib_vm.add_any(album)
            artist.albums.append(album)
        song.album = album
