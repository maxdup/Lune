# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore


class ProgressBar(QtGui.QWidget):
    def __init__(self, player):
        self.player = player
        QtGui.QWidget.__init__(self)

        layout = QtGui.QHBoxLayout(self)

        self.position_slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.position_slider.setToolTip("Position")
        self.position_slider.setMaximum(500)
        self.connect(self.position_slider,
                     QtCore.SIGNAL("sliderMoved(int)"), player.seek)

        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(200)
        self.connect(self.timer, QtCore.SIGNAL("timeout()"), self.update)
        self.player.set_timer(self.timer)

        layout.addWidget(self.position_slider)

    def update(self):
        self.position_slider.setValue(self.player.get_position() * 500)
