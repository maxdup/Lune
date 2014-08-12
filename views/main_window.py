# -*- coding: utf-8 -*-

from PySide import QtGui

from views.settings_view import SettingsView
from views.status.status import Status
from views.nav import Nav


class MainWindow(QtGui.QWidget):
    def __init__(self, library, player, settings):
        QtGui.QWidget.__init__(self)
        with open('views/qss/general.qss', 'r') as stylesheet:
            self.setStyleSheet(stylesheet.read())
        self.setObjectName('mainwindow')
        self.stack_container = QtGui.QFrame()

        self.content_v = QtGui.QWidget()
        self.content_v.setLayout(QtGui.QVBoxLayout())
        self.library_v = QtGui.QWidget()
        self.status_v = Status(player)
        self.settings_v = SettingsView(settings)

        self.content_v.layout().addWidget(self.library_v)
        self.content_v.layout().addWidget(self.status_v)

        self.view_stack = QtGui.QStackedLayout()
        self.view_stack.addWidget(self.content_v)
        self.view_stack.addWidget(self.settings_v)

        self.stack_container.setLayout(self.view_stack)
        self.nav = Nav(self.view_stack, library, self.library_v, player)

        self.main_container = QtGui.QVBoxLayout()

        self.main_container.addWidget(self.nav)
        self.main_container.addWidget(self.stack_container)
        self.setLayout(self.main_container)

        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon('lune.png'))
        self.setWindowTitle('Lune')
