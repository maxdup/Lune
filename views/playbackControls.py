from PySide import QtGui
from sys import platform


class PlaybackControls(QtGui.QWidget):

    STYLE = '''QPushButton{
        background-color: transparent;
        border-style: solid;
        border-width:3px;
        border-radius:15px;
        color:gray;
        min-height:24px;
        min-width:24px;
        max-height:24px;
        max-width:24px;
        font-size:15px;
        font-family:webdings;
    }
    QPushButton#stop{
        border-radius:18px;
        min-height:32px;
        min-width:32px;
        max-height:32px;
        max-width:32px;
        font-size:20px;
    }
    QPushButton#pauseresume{
        border-radius:22px;
        min-height:40px;
        min-width:40px;
        max-height:40px;
        max-width:40px;
        font-size:32px;
    }
    '''

    def __init__(self, player):
        QtGui.QWidget.__init__(self)
        self.setStyleSheet(self.STYLE)

        self.previous = QtGui.QPushButton('7')
        self.previous.clicked.connect(player.Previous)
        if platform == "linux" or platform == "linux2" or platform == 'darwin':
            self.previous.setText('prev')

        self.stop = QtGui.QPushButton('<')
        self.stop.clicked.connect(player.Stop)
        self.stop.setObjectName('stop')
        if platform == "linux" or platform == "linux2" or platform == 'darwin':
            self.stop.setText('stop')

        self.pauseresume = QtGui.QPushButton('4')
        self.pauseresume.clicked.connect(player.PlayPause)
        self.pauseresume.setObjectName('pauseresume')

        if platform == "linux" or platform == "linux2" or platform == 'darwin':
            self.pauseresume.setText('play')

        self.skip = QtGui.QPushButton('8')
        self.skip.clicked.connect(player.Skip)
        if platform == "linux" or platform == "linux2" or platform == 'darwin':
            self.skip.setText('skip')

        layout = QtGui.QHBoxLayout(self)

        layout.addWidget(self.previous)
        layout.addWidget(self.stop)
        layout.addWidget(self.pauseresume)
        layout.addWidget(self.skip)
