from models.song import Song


class SongQueue:

    def __init__(self, queue=[], startFrom=0):
        self.queue = []
        self.addLast(queue)
        #testdata
        self.addLast(Song("Avalanche Rock.mp3"))
        self.addLast([Song("Beyond_the_Golden_Valleys.mp3"),
                    Song("Ocean.flac")])

        self.startFrom = startFrom
        self.at = None

    def addLast(self, songs):
        def appendSong(song):
            if type(song) == Song:
                self.queue.append(song)
        if type(songs) == list:
            for song in songs:
                appendSong(song)
        else:
            appendSong(songs)

    def isEmpty(self):
        if len(self.queue) != 0:
            return False
        else:
            return True

    def getCurrent(self):
        return self.queue[self.at]

    def hasNext(self):
        if (not self.isEmpty() and self.at + 1 != len(self.queue)):
            return True
        return False

    def getNext(self):
        if self.at is None:
            self.at = self.startFrom
        else:
            if self.hasNext():
                self.at += 1
            else:
                return None
        return self.getCurrent()

    def hasPrev(self):
        if self.at != self.startFrom and not self.isEmpty():
            return True
        return False

    def getPrev(self):
        if not self.at:
            self.at = self.startFrom
        else:
            if self.hasPrev():
                self.at -= 1
        return self.getCurrent()
