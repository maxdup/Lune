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
                'title': media.get_meta(vlc.Meta.Title),
                'album': media.get_meta(vlc.Meta.Artist),
                'artist': media.get_meta(vlc.Meta.Album),
                'genre': media.get_meta(vlc.Meta.Genre),
                'track_nb': media.get_meta(vlc.Meta.TrackNumber),
                'date': media.get_meta(vlc.Meta.Date),
                'label': media.get_meta(vlc.Meta.Publisher)
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