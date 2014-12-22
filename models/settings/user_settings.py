import os

from dal.settings_dao import read, save
from models.settings.path_list import PathList
from models.settings.extension_list import ExtensionList


class UserSettings:
    def __init__(self, operation_queue, library):

        self.filename = 'settings.json'

        saved = read(self.filename)

        self.path_list = PathList(self, operation_queue, library, saved['libpaths'])
        self.extension_list = ExtensionList(self, saved['extensions'])

    def notify(self):
        save(self)
