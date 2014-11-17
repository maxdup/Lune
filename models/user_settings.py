import os

from dal.settings_dao import SettingsDAO


class UserSettings:
    def __init__(self, collector):
        self.collector = collector
        self.settings_dao = SettingsDAO()
        self.path_list = []
        for path in self.settings_dao.get_paths():
            path_obj = LibPath(path, self)
            self.path_list.append(path_obj)  # use self.addPath instead?
            self.collector.search_dir(path_obj)

    def add_path(self, path):
        path_obj = LibPath(path, self)

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
                self.settings_dao.del_path(path)

        self.settings_dao.add_path(path_obj.path)
        self.path_list.append(path_obj)
        self.collector.search_dir(path_obj)
        return path_obj


class LibPath:
    def __init__(self, path, user_settings):
        if os.path.exists(path):
            self.path = path
        else:
            self.path = ''
            # could be a permission error
        self.user_settings = user_settings

    def remove(self):
        self.user_settings.path_list.remove(self)
        self.user_settings.settings_dao.del_path(self.path)
        self.user_settings.collector.library.remove_path(self.path)
