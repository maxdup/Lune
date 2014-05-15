# -*- coding: utf-8 -*-

import sys
from sys import platform
from PySide.QtCore import QUrl, Qt
from PySide import QtGui
from PySide.QtDeclarative import QDeclarativeView
from views.player import Player
from DAL.collector import Collector
from models.library import Library
from models.songQueue import SongQueue
from views.mainWindow import MainWindow
from models.userSettings import UserSettings

def main():
    app = QtGui.QApplication(sys.argv)

    settings = UserSettings()
    library = Library()

    collector = Collector(library)
    for path in settings.pathList:
        collector.searchDir(path)

    songQueue = SongQueue()
    songQueue.addLast(library.getLibrary())

    player = Player()
    player.SetQueue(songQueue)

    if platform == "win32":
        import ctypes
        myappid = 'Lune.Atlas'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    view = MainWindow(player, settings)
    view.show()

    app.exec_()

if __name__ == '__main__':
    main()
