class SongQueue:
    
    def __init__(self, queue = [], startFrom = 0):
        self.queue = queue
        self.startFrom = startFrom

    def isEmpty(self):
        if len(queue) != 0: 
            return false
        else:
            return true

    def hasNext(self):
        if not self.isEmpty() and self.at not in [self.startFrom, len(self.queue) ]:
            return true
        return false

    def getNext(self):
        if not self.at:
            self.at = self.startFrom
        else:
            if self.hasNext():
                self.at += 1
        return self.getCurrent();

    def hasPrev():
        if self.at != self.startFrom and not self.isEmpty():
            return true
        return false           

    def getPrev():
        if not self.at:
            self.at = self.startFrom 
        else:
            if self.hasPrev():
                self.at -= 1
        return self.getCurrent();

    def getCurrent(self):
        #return self.queue[self.at]
        return "Beyond_the_Golden_Valleys.mp3"
