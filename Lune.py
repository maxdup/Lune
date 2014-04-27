import sys
from PySide.QtCore import QUrl, Qt
from PySide import QtGui
from PySide.QtDeclarative import QDeclarativeView
from views.player import Player
from DAL.collector import Collector
from models.library import Library
from models.songQueue import SongQueue


def main():
    app = QtGui.QApplication(sys.argv)
    view = QDeclarativeView()
    view.setSource(QUrl('views/Lune.qml'))
    view.setResizeMode(QDeclarativeView.SizeRootObjectToView)
    #view.setWindowFlags(Qt.FramelessWindowHint)
    library = Library()
    collector = Collector(library)
    collector.searchDir("D:\Music")  # path to your library
    songQueue = SongQueue()
    songQueue.addLast(library.getLibrary())
    player = Player()
    player.SetQueue(songQueue)
    player.Play()

    view.show()
    app.exec_()

if __name__ == '__main__':
    main()
