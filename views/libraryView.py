# -*- coding: utf-8 -*-

from PySide import QtGui

from views.playbackControls import PlaybackControls
from views.progressBar import ProgressBar

class LibraryView(QtGui.QWidget):

  def __init__(self, player, library):
    QtGui.QWidget.__init__(self)

    self.player = player

    self.controls = PlaybackControls(player)
    self.progress = ProgressBar(player)

    self.list = QtGui.QListWidget()
    self.list.itemDoubleClicked.connect(self._songDoubleClicked)
    index = 0
    for song in library.songs:
      try:
        item = QtGui.QListWidgetItem(self.list)
        item.setText(song.trackInfo['title'])
        item.setData(1000, index) # role, index. Created a dummy role '1000' for now.
      except KeyError: pass
      index += 1

    layout = QtGui.QGridLayout(self)
    layout.addWidget(self.list, 0, 0, 1, 0)
    layout.addWidget(self.progress, 1, 0)
    layout.addWidget(self.controls, 1, 1)

  def _songDoubleClicked(self, item):
    index = item.data(1000)
    if (self.player.IsPlaying()):
      self.player.Stop()
    self.player.queue.getAtIndex(index)
    self.player.PlayPrep()
    self.player.Play()

  def update(self):
    return None
