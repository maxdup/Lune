import os

from dal.settings_dao import read, save
from models.settings.path_list import PathList
from models.settings.extension_list import ExtensionList


class UserSettings:
    def __init__(self, operation_queue, library):

        self.filename = 'settings.json'
        self.operation_queue = operation_queue

        saved = read(self.filename)
        paths = saved['libpaths']
        exts = saved['extensions']
        self.path_list = PathList(self, operation_queue, library, paths)
        self.extension_list = ExtensionList(self, exts)

    def notify(self):
        save(self)
