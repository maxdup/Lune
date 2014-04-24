class song:
    #todo: find a library for id3 tags
    def __init__(self, path = None):
        self.path = path
        self.trackInfo = {}

    def getPath(self):
        return self.path
	  	  
    def getFileImage(self):
        return None
    
    
