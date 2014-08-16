# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore

from views.settings_view import SettingsView
from views.status.status import Status
from views.top_bar import TopBar
from views.nav import Nav


class MainWindow(QtGui.QWidget):
    def __init__(self, library, player, settings):
        QtGui.QWidget.__init__(self)

        with open('views/qss/general.qss', 'r') as stylesheet:
            self.setStyleSheet(stylesheet.read())
        self.setObjectName('mainwindow')

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon('lune.png'))
        self.setWindowTitle('Lune')

        window_ctrl_layout = QtGui.QGridLayout(self)
        window_ctrl_layout.setContentsMargins(0, 0, 0, 0)
        grip1 = QtGui.QSizeGrip(self)
        grip2 = QtGui.QSizeGrip(self)
        grip3 = QtGui.QSizeGrip(self)
        grip4 = QtGui.QSizeGrip(self)
        window_ctrl_layout.addWidget(grip1, 0, 0)
        window_ctrl_layout.addWidget(grip2, 0, 2)
        window_ctrl_layout.addWidget(grip3, 3, 2)
        window_ctrl_layout.addWidget(grip4, 3, 0)
        self.resize(600, 400)

        topbar = TopBar(self)
        app_container = QtGui.QWidget()
        window_ctrl_layout.addWidget(topbar, 1, 1)
        window_ctrl_layout.addWidget(app_container, 2, 1)
        self.setLayout(window_ctrl_layout)
        self.main_container = QtGui.QVBoxLayout()
        app_container.setLayout(self.main_container)


        self.content_v = QtGui.QWidget()
        self.stack_container = QtGui.QFrame()
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
        self.main_container.addWidget(self.nav)
        self.main_container.addWidget(self.stack_container)

