import os
import multiprocessing

from dal.collector import Collector

class PathList(list):
    def __init__(self, user_settings, operation_queue, library, *args):
        list.__init__(self)

        self.user_settings = user_settings
        self.operation_queue = operation_queue
        self.library = library

        for path in args[0]:
            list.append(self, path)

    def append(self, path):
        if self:
            for old_path in self:
                if path.startswith(old_path):
                    # this means it's a subpath, we ignore it
                    return None

            marked_for_delete = []
            for old_path in self:
                if old_path.startswith(path):
                    # this means a path has been made redundant by the new path
                    marked_for_delete.append(old_path)
            for path in marked_for_delete:
                self.remove(path)

        list.append(self, path)
        self.user_settings.notify()

        p = multiprocessing.Process(target=worker,
            args=(self.operation_queue.multi_queue,path,
                  self.user_settings.extension_list,))
        p.start()

        return LibPath(path, self)

    def remove(self, path):
        list.remove(self, path)
        self.library.remove_path(path, self.operation_queue)
        self.user_settings.notify()

    def get_LibPaths(self):
        return [LibPath(path, self) for path in self]

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
        self._path_list.remove(self.path)

