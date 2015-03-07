# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
from PySide.QtGui import QSizePolicy

from .settings.settings_view import SettingsView
from .status.status import Status
from .top_bar import TopBar
from .nav import Nav

from models.lib_operation import LibOperation, load_song

import resources

class MainWindow(QtGui.QWidget):

    def __init__(self, library, player, settings, operation_queue):
        QtGui.QWidget.__init__(self)

        QtGui.QFontDatabase.addApplicationFont(":/fonts/luneicons.otf")

        stylesheet = QtCore.QFile(':/views/qss/general.qss')
        if stylesheet.open(QtCore.QIODevice.ReadOnly | QtCore.QIODevice.Text):
            self.setStyleSheet(str(stylesheet.readAll()))
        self.setObjectName('mainwindow')

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon(':/img/lune.png'))
        self.setWindowTitle('Lune')

        self.library = library
        self.operation_queue = operation_queue

        window_ctrl_layout = QtGui.QGridLayout(self)
        window_ctrl_layout.setContentsMargins(0, 0, 0, 0)
        window_ctrl_layout.setSpacing(0)

        grip1 = QtGui.QSizeGrip(self)
        grip2 = QtGui.QSizeGrip(self)
        grip3 = QtGui.QSizeGrip(self)
        grip4 = QtGui.QSizeGrip(self)
        grip1.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        grip2.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        window_ctrl_layout.addWidget(grip1, 0, 0)
        window_ctrl_layout.addWidget(grip2, 0, 2)
        window_ctrl_layout.addWidget(grip3, 2, 2)
        window_ctrl_layout.addWidget(grip4, 2, 0)

        self.resize(600, 400)

        topbar = TopBar(self)
        app_container = QtGui.QWidget()
        window_ctrl_layout.addWidget(topbar, 0, 1)
        window_ctrl_layout.addWidget(app_container, 1, 1)

        self.setLayout(window_ctrl_layout)
        main_container = QtGui.QVBoxLayout()
        app_container.setLayout(main_container)

        content_v = QtGui.QWidget()
        stack_container = QtGui.QFrame()

        self.library_v = QtGui.QWidget()
        self.status_v = Status(player)

        content_v.setLayout(QtGui.QVBoxLayout())
        content_v.layout().addWidget(self.library_v)
        content_v.layout().addWidget(self.status_v)
        content_v.layout().setContentsMargins(0, 0, 0, 0)

        settings_v = SettingsView(settings)


        self.view_stack = QtGui.QStackedLayout()
        self.view_stack.addWidget(content_v)
        self.view_stack.addWidget(settings_v)

        stack_container.setLayout(self.view_stack)
        self.nav = Nav(self, library, player.bouncer)
        main_container.addWidget(self.nav)
        main_container.addWidget(stack_container)

        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(200)
        self.connect(self.timer, QtCore.SIGNAL("timeout()"), self.work_queue)
        self.timer.start()

        for song in self.library.library_db.get_all_songs():
            operation_queue.push(LibOperation(song, load_song))

        self.chrono = QtCore.QTime()


    def change_view(self, view):
        if view == 'lib':
            self.status_v.make_small()
            self.library_v.show()
            self.view_stack.setCurrentIndex(0)
            self.nav.change_area(view)
        elif view == 'now':
            self.status_v.make_large()
            self.library_v.hide()
            self.view_stack.setCurrentIndex(0)
            self.nav.change_area(view)
        elif view == 'settings':
            self.view_stack.setCurrentIndex(1)
            self.nav.change_area(view)

    def work_queue(self):
        if self.operation_queue:
            self.chrono.restart()
            while self.chrono.elapsed() < 150:
                operation = self.operation_queue.shift()
                if operation:
                    operation.execute(self.library)
