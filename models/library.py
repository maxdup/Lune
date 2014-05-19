# -*- coding: utf-8 -*-

from models.song import Song


class Library:
    def __init__(self):
        self.songs = []

    def add_song(self, songs):
        if type(songs) == Song:
            self.songs.append(songs)
        elif type(songs) == list:
            for song in songs:
                self.songs.append(song)
