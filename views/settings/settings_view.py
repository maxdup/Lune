# -*- coding: utf-8 -*-

from PySide import QtGui

from views.settings.path_manager import PathManager
from views.settings.extension_manager import ExtensionManager
from views.settings.library_manager import LibraryManager

class SettingsView(QtGui.QWidget):
    def __init__(self, user_settings):
        QtGui.QWidget.__init__(self)
        layout = QtGui.QHBoxLayout()

        path_manager = PathManager(user_settings.path_list)
        extension_manager = ExtensionManager(user_settings.extension_list)
        library_manager = LibraryManager()

        layout.addWidget(path_manager)
        layout.addWidget(extension_manager)
        layout.addWidget(library_manager)

        self.setLayout(layout)
