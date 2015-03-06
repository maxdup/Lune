# -*- coding: utf-8 -*-

from PySide import QtGui

from views.status.playback_controls import PlaybackControls
from views.status.progress_bar import ProgressBar
from views.status.trackinfo import Trackinfo

from views.status.status import Status


class NowView(QtGui.QWidget):
    def __init__(self, player):
        QtGui.QWidget.__init__(self)
        self.setLayout(QtGui.QHBoxLayout())
