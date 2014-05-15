from DAL.settings import Settings

class UserSettings:
    def __init__(self):
        self.settings = Settings()
        self.pathList = []
        for path in self.settings.getPaths():
            path = Path(path, self)
            self.pathList.append(path)

    def addPath(self, path):
        pathObj = Path(path, self)

        if self.pathList:
            for oldpath in self.pathList:
                if pathObj.path.startswith(oldpath.path):
                    #this means it's a subpath, we ignore it
                    return None
        
            for oldpath in self.pathList:
                if oldpath.path.startswith(pathObj.path):
                    print('subpaths created, deleting')
                    #todo clean subpaths created

        self.settings.writePath(pathObj.path)
        self.pathList.append(pathObj)
        return pathObj

class Path:
    def __init__(self, path, usettings):
        #todo validate path
        self.path = path
        self.usettings = usettings

    def remove(self):
        self.usettings.pathList.remove(self)

        self.usettings.settings.delPath(self.path)

