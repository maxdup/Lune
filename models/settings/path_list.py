import os
import multiprocessing

from dal.collector import Collector

class PathList(list):
    def __init__(self, settings_dao, result_queue, *args):
        self.result_queue = result_queue
        list.__init__(self, *args)
        self._settings_dao = settings_dao
        for path in self._settings_dao.get_paths():
            libpath = LibPath(path, self)
            list.append(self, libpath)

    def append(self, path):
        libpath = LibPath(path, self)
        if self:
            for old_path in self:
                if libpath.path.startswith(old_path.path):
                    # this means it's a subpath, we ignore it
                    return None

            marked_for_delete = []
            for old_path in self:
                if old_path.path.startswith(libpath.path):
                    # this means a path has been made redundant by the new path
                    marked_for_delete.append(old_path)
            for path in marked_for_delete:
                self.remove(path)

        self._settings_dao.add_path(libpath.path)
        list.append(self, libpath)

        p = multiprocessing.Process(target=worker,
                                    args=(self.result_queue,libpath,self._settings_dao.get_exts(),))
        p.start()

        return libpath

    def remove(self, libpath):
        list.remove(self, libpath)
        self._settings_dao.del_path(libpath.path)

def worker(result_queue, path, exts):
    collect = Collector()
    collect.search_dir(result_queue, path, exts)

class LibPath:
    def __init__(self, path, path_list):
        self._path_list = path_list
        if os.path.exists(path):
            self.path = path
        else:
            self.path = 'error'
            # could be a permission error
            # could be an unmounted drive

    def remove(self):
        self._path_list.remove(self)

