import os

from dal.settings_dao import SettingsDAO
from models.settings.path_list import PathList


class UserSettings:
    def __init__(self, result_queue):
        self._settings_dao = SettingsDAO()
        self.path_list = PathList(self._settings_dao, result_queue)
