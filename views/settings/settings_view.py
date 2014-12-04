# -*- coding: utf-8 -*-

from PySide import QtGui

from views.settings.path_manager import PathManager
from views.settings.extension_manager import ExtensionManager

class SettingsView(QtGui.QWidget):
    def __init__(self, user_settings):
        QtGui.QWidget.__init__(self)
        layout = QtGui.QHBoxLayout()
        path_manager = PathManager(user_settings.path_list)
        extension_manager = ExtensionManager(user_settings.extension_list)

        layout.addWidget(path_manager)
        layout.addWidget(extension_manager)

        self.setLayout(layout)
