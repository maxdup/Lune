import os

from dal.settings_dao import SettingsDAO
from models.settings.path_list import PathList
from models.settings.extension_list import ExtensionList


class UserSettings:
    def __init__(self, result_queue):
        self._settings_dao = SettingsDAO()
        self.path_list = PathList(self._settings_dao, result_queue)
        self.extension_list = ExtensionList(self._settings_dao)
