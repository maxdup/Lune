# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
import time

class ProgressBar(QtGui.QWidget):
    def __init__(self, player):
        self.player = player
        QtGui.QWidget.__init__(self)

        self.player = player

        layout = QtGui.QVBoxLayout(self)

        self.position_slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.position_slider.setToolTip("Position")
        self.position_slider.setMaximum(500)
        self.position_slider.sliderPressed.connect(self._slider_lifted)
        self.position_slider.sliderReleased.connect(self._slider_dropped)

        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(200)
        self.connect(self.timer, QtCore.SIGNAL("timeout()"), self.update)
        self.player.set_timer(self.timer)

        self.time_in = QtGui.QLabel()
        self.time_left = QtGui.QLabel()

        time_container = QtGui.QWidget()
        time_container.setLayout(QtGui.QHBoxLayout())
        time_container.layout().addWidget(self.time_in)
        time_container.layout().addStretch()
        time_container.layout().addWidget(self.time_left)

        self.held = False

        layout.addWidget(self.position_slider)
        layout.addWidget(time_container)

    def update(self):
        if not self.held:
            self.position_slider.setValue(self.player.get_position() * 500)
            self.time_update()

    def time_update(self):
        time_total = self.player.get_length()/1000
        time_in = self.player.get_time()/1000
        time_left = time_total - time_in
        if self.player.queue:
            if time_total >= 3600:
                time_in = time.strftime("%H:%M:%S", time.gmtime(time_in))
                time_left = time.strftime("%H:%M:%S", time.gmtime(time_left))
            else:
                time_in = time.strftime("%M:%S", time.gmtime(time_in))
                time_left = time.strftime("%M:%S", time.gmtime(time_left))
        else:
            time_in = time_left = ''

        self.time_in.setText(time_in)
        self.time_left.setText(time_left)

    def _slider_lifted(self):
        self.held = True
        self.player.hold()
    def _slider_dropped(self):
        self.held = False
        self.player.seek(self.position_slider.value())
        self.player.unhold()
