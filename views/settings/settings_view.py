# -*- coding: utf-8 -*-

from PySide import QtGui

from views.settings.path_manager import PathManager
from views.settings.extension_manager import ExtensionManager
from views.settings.library_manager import LibraryManager

class SettingsView(QtGui.QWidget):
    def __init__(self, user_settings):
        QtGui.QWidget.__init__(self)
        layout = QtGui.QHBoxLayout()
        side = QtGui.QWidget()
        side.setLayout(QtGui.QVBoxLayout())

        path_manager = PathManager(user_settings.path_list)
        extension_manager = ExtensionManager(user_settings.extension_list)
        library_manager = LibraryManager(user_settings)

        layout.addWidget(path_manager)
        side.layout().addWidget(extension_manager)
        side.layout().addWidget(library_manager)
        layout.addWidget(side)

        self.setLayout(layout)
