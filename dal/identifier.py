# -*- coding: utf-8 -*-

import vlc
from urllib.request import url2pathname

class Identifier():
    def __init__(self):
        self.instance = vlc.Instance()

    def identify(self, song):
        media = self.instance.media_new(song.path)
        media.parse()
        media.get_meta(vlc.Meta.Album)
        track_info = {}
        try:
            track_info = {
                'track_nb': int(media.get_meta(vlc.Meta.TrackNumber)),
                'title': media.get_meta(vlc.Meta.Title),
                'album': media.get_meta(vlc.Meta.Album),
                'artist': media.get_meta(vlc.Meta.Artist),
                'label': media.get_meta(vlc.Meta.Publisher),
                'date': media.get_meta(vlc.Meta.Date) or 0,
                'genre': media.get_meta(vlc.Meta.Genre),
                'artwork': media.get_meta(vlc.Meta.ArtworkURL)
            }
            if track_info['artwork'] is not None:
                track_info['artwork'] = url2pathname(track_info['artwork'][7:])

            #print(track_info)

        except:
            # TODO:
            # - clean messed up tags
            # - create empty trackinfos
            pass
        # return track_info
        song.track_info = track_info
