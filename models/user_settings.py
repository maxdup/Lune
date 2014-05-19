import os

from dal.settings import Settings


class UserSettings:
    def __init__(self, collector):
        self.collector = collector
        self.settings = Settings()
        self.path_list = []
        for path in self.settings.get_paths():
            path_obj = Path(path, self)
            self.path_list.append(path_obj)  # use self.addPath instead?
            self.collector.search_dir(path_obj)

    def add_path(self, path):
        path_obj = Path(path, self)

        if self.path_list:
            for old_path in self.path_list:
                if path_obj.path.startswith(old_path.path):
                    # this means it's a subpath, we ignore it
                    return None

            marked_for_delete = []
            for old_path in self.path_list:
                if old_path.path.startswith(path_obj.path):
                    # this means a path has been made redundant by the new path
                    marked_for_delete.append(old_path)
            for path in marked_for_delete:
                self.path_list.remove(path)
                self.settings.del_path(path)

        self.settings.write_path(path_obj.path)
        self.path_list.append(path_obj)
        print(type(self.collector))
        self.collector.search_dir(path_obj)
        return path_obj


class Path:
    def __init__(self, path, user_settings):
        if os.path.exists(path):
            self.path = path
            self.user_settings = user_settings
        else:
            self = None
            # could be a permission error

    def remove(self):
        self.user_settings.path_list.remove(self)
        self.user_settings.settings.del_path(self.path)
        # todo clean the library of files that used this path
