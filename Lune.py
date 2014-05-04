import sys
from PySide.QtCore import QUrl, Qt
from PySide import QtGui
from PySide.QtDeclarative import QDeclarativeView
from views.player import Player
from DAL.collector import Collector
from models.library import Library
from models.songQueue import SongQueue
from views.mainWindow import MainWindow
from DAL.userSettings import UserSettings


def main():
    app = QtGui.QApplication(sys.argv)
    #view = QDeclarativeView()
    #view.setSource(QUrl('views/Lune.qml'))
    #view.setResizeMode(QDeclarativeView.SizeRootObjectToView)
    #view.setWindowFlags(Qt.FramelessWindowHint)
    settings = UserSettings()
    #settings.addPath('D:\Music\SebastiAn\Ross Ross Ross')
    #settings.addPath('D:\Music\Scratch Massive\Time')
    #settings.removePath('D:\Music\Scratch Massive\Time')
    library = Library()
    collector = Collector(library)
    for path in settings.getPaths():
        collector.searchDir(path)
    songQueue = SongQueue()
    songQueue.addLast(library.getLibrary())
    player = Player()
    player.SetQueue(songQueue)
    player.Play()

    view = MainWindow(player)
    view.show()
    app.exec_()

if __name__ == '__main__':
    main()
