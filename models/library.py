# -*- coding: utf-8 -*-

from models.song import Song


class Library:

    def __init__(self):
        self.songs = []

    def addSong(self, songs):
        if type(songs) == Song:
            self.songs.append(songs)
        elif type(songs) == list:
            for song in songs:
                self.songs.append(song)

    def getLibrary(self):
        return self.songs
