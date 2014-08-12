# -*- coding: utf-8 -*-

from sys import platform

from PySide import QtGui


class PlaybackControls(QtGui.QWidget):
    def __init__(self, player):
        QtGui.QWidget.__init__(self)
        with open('views/qss/playback_controls.qss','r') as stylesheet:
            self.setStyleSheet(stylesheet.read())

        self.previous = QtGui.QPushButton('7')
        self.previous.clicked.connect(player.previous)
        if platform == "linux" or platform == "linux2" or platform == 'darwin':
            self.previous.setText('prev')

        self.stop = QtGui.QPushButton('<')
        self.stop.clicked.connect(player.stop)
        self.stop.setObjectName('stop')
        if platform == "linux" or platform == "linux2" or platform == 'darwin':
            self.stop.setText('stop')

        self.pause_resume = QtGui.QPushButton('4')
        self.pause_resume.clicked.connect(player.play_pause)
        self.pause_resume.setObjectName('pauseresume')

        if platform == "linux" or platform == "linux2" or platform == 'darwin':
            self.pause_resume.setText('play')

        self.skip = QtGui.QPushButton('8')
        self.skip.clicked.connect(player.skip)
        if platform == "linux" or platform == "linux2" or platform == 'darwin':
            self.skip.setText('skip')

        layout = QtGui.QHBoxLayout(self)

        layout.addWidget(self.previous)
        layout.addWidget(self.stop)
        layout.addWidget(self.pause_resume)
        layout.addWidget(self.skip)
