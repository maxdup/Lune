import vlc


class Identifier():
    def __init__(self):
        self.instance = vlc.Instance()

    def identify(self, song):
        media = self.instance.media_new(song.getPath())
        media.parse()
        media.get_meta(vlc.Meta.Album)
        try:
            trackinfo = {
                'track_nb': media.get_meta(vlc.Meta.TrackNumber),
                'title': media.get_meta(vlc.Meta.Title),
                'album': media.get_meta(vlc.Meta.Album),
                'artist': media.get_meta(vlc.Meta.Artist),
                'label': media.get_meta(vlc.Meta.Publisher),
                'date': media.get_meta(vlc.Meta.Date),
                'genre': media.get_meta(vlc.Meta.Genre),
            }
            print(trackinfo)
        except:
            '''
            todo:
            - clean messed up tags
            - figure out why TagLib won't shut up about "invalid sample rate"'
            '''
            pass
        return trackinfo