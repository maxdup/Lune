# -*- coding: utf-8 -*-

from PySide import QtGui

from views.library.album_v import Album_v
from views.library.song_v import Song_v

from views.settings_view import SettingsView


class MainWindow(QtGui.QWidget):
    def __init__(self, library, player, settings):
        QtGui.QWidget.__init__(self)
        self.stack_container = QtGui.QFrame()

        self.library_v = Album_v(player, library.lib_vm)
        self.settings_v = SettingsView(settings)

        self.view_stack = QtGui.QStackedLayout()
        self.view_stack.addWidget(self.library_v)
        self.view_stack.addWidget(self.settings_v)

        self.stack_container.setLayout(self.view_stack)

        self.goto_library = QtGui.QPushButton('Library')
        self.goto_library.clicked.connect(
            lambda: self.view_stack.setCurrentIndex(0))
        self.goto_settings = QtGui.QPushButton('Settings')
        self.goto_settings.clicked.connect(
            lambda: self.view_stack.setCurrentIndex(1))

        self.main_container = QtGui.QVBoxLayout()
        self.main_container.addWidget(self.goto_library)
        self.main_container.addWidget(self.goto_settings)
        self.main_container.addWidget(self.stack_container)
        self.setLayout(self.main_container)

        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon('lune.png'))
        self.setWindowTitle('Lune')
