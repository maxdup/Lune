import os.path

from models.song import Song


class argParser():
    def get_queue(args):
        songs = []
        FORMATS = ['mp3', 'flac', 'aac', 'ogg']
        for arg in args:
            arg = str(arg)
            if os.path.isfile(arg) and arg.split('.').pop() in FORMATS:
                songs.append(Song(arg))
        return songs
