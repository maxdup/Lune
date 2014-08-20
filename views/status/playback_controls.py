# -*- coding: utf-8 -*-

from sys import platform

from PySide import QtGui


class PlaybackControls(QtGui.QWidget):
    def __init__(self, player):
        QtGui.QWidget.__init__(self)
        with open('views/qss/playback_controls.qss','r') as stylesheet:
            self.setStyleSheet(stylesheet.read())

        self.previous = QtGui.QPushButton('<')
        self.previous.clicked.connect(player.previous)

        self.stop = QtGui.QPushButton('\\')
        self.stop.clicked.connect(player.stop)
        self.stop.setObjectName('stop')

        player.status_vm.pause_resume.clicked.connect(player.play_pause)
        player.status_vm.pause_resume.setObjectName('pauseresume')

        self.skip = QtGui.QPushButton('>')
        self.skip.clicked.connect(player.skip)

        layout = QtGui.QHBoxLayout(self)

        layout.addWidget(self.previous)
        layout.addWidget(self.stop)
        layout.addWidget(player.status_vm.pause_resume)
        layout.addWidget(self.skip)
