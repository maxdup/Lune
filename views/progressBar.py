# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore


class ProgressBar(QtGui.QWidget):
    def __init__(self, player):
        self.player = player
        QtGui.QWidget.__init__(self)

        layout = QtGui.QHBoxLayout(self)

        self.PositionSlider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.PositionSlider.setToolTip("Position")
        self.PositionSlider.setMaximum(500)
        self.connect(self.PositionSlider,
                     QtCore.SIGNAL("sliderMoved(int)"), player.Seek)

        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(200)
        self.connect(self.timer, QtCore.SIGNAL("timeout()"), self.update)
        self.player.setTimer(self.timer)

        layout.addWidget(self.PositionSlider)

    def update(self):
        if not self.player.IsPlaying():
            self.timer.stop()
        self.PositionSlider.setValue(self.player.getPosition() * 500)
