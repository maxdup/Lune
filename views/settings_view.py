# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore

from views.settings.path_manager import PathManager

class SettingsView(QtGui.QWidget):
    def __init__(self, user_settings):
        QtGui.QWidget.__init__(self)
        layout = QtGui.QVBoxLayout()
        path_manager = PathManager(user_settings)

        layout.addWidget(path_manager)
        self.setLayout(layout)
