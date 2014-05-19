import os

from DAL.settings import Settings


class UserSettings:
    def __init__(self, collector):
        self.collector = collector
        self.settings = Settings()
        self.pathList = []
        for path in self.settings.getPaths():
            pathObj = Path(path, self)
            self.pathList.append(pathObj)  # use self.addPath instead?
            self.collector.searchDir(pathObj)

    def addPath(self, path):
        pathObj = Path(path, self)

        if self.pathList:
            for oldpath in self.pathList:
                if pathObj.path.startswith(oldpath.path):
                    # this means it's a subpath, we ignore it
                    return None

            marked_for_delete = []
            for oldpath in self.pathList:
                if oldpath.path.startswith(pathObj.path):
                    # this means a path has been made redundant by the new path
                    marked_for_delete.append(oldpath)
            for path in marked_for_delete:
                self.pathList.remove(path)
                self.settings.delPath(path)

        self.settings.writePath(pathObj.path)
        self.pathList.append(pathObj)
        print(type(self.collector))
        self.collector.searchDir(pathObj)
        return pathObj


class Path:
    def __init__(self, path, usettings):
        if os.path.exists(path):
            self.path = path
            self.usettings = usettings
        else:
            self = None
            # could be a permission error

    def remove(self):
        self.usettings.pathList.remove(self)
        self.usettings.settings.delPath(self.path)
        # todo clean the library of files that used this path
