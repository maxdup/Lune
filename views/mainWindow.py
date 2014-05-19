# -*- coding: utf-8 -*-

from PySide import QtGui

from views.libraryView import LibraryView
from views.settingsView import SettingsView


class MainWindow(QtGui.QWidget):
    def __init__(self, library, player, settings):
        QtGui.QWidget.__init__(self)
        self.stack_container = QtGui.QFrame()

        self.v_library = LibraryView(player, library)
        self.v_settings = SettingsView(settings)

        self.view_stack = QtGui.QStackedLayout()
        self.view_stack.addWidget(self.v_library)
        self.view_stack.addWidget(self.v_settings)

        self.stack_container.setLayout(self.view_stack)

        self.goto_library = QtGui.QPushButton('Library')
        self.goto_library.clicked.connect(self.goto_lib)
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

    def goto_lib(self):
        self.v_library.update()
        self.view_stack.setCurrentIndex(0)
