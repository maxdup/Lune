from PySide import QtGui

class LibraryView(QtGui.QWidget):

  def __init__(self, player):
    QtGui.QWidget.__init__(self)
    
    self.player = player
    
    self.layout = QtGui.QVBoxLayout(self)
    self.list = QtGui.QListWidget()
    self.list.itemDoubleClicked.connect(self._songDoubleClicked)
    index = 0
    for song in player.queue.queue:
      try:
        item = QtGui.QListWidgetItem(self.list)
        item.setText(song.trackInfo['title'])
        item.setData(1000, index) # role, index. Created a dummy role '1000' for now.
      except KeyError: pass
      index += 1
    self.layout.addWidget(self.list)
    
  def _songDoubleClicked(self, item):
    index = item.data(1000)
    if (self.player.IsPlaying()):
      self.player.Stop()
    self.player.queue.getAtIndex(index)
    self.player.PlayPrep()
    self.player.Play()