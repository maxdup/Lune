# -*- coding: utf-8 -*-

import sys
from sys import platform

from PySide import QtGui

from views.player import Player
from DAL.collector import Collector
from models.library import Library
from models.songQueue import SongQueue
from views.mainWindow import MainWindow
from models.userSettings import UserSettings


def main():
    app = QtGui.QApplication(sys.argv)

    library = Library()
    collector = Collector(library)
    settings = UserSettings(collector)

    song_queue = SongQueue()
    song_queue.add_last(library.songs)

    player = Player()
    player.set_queue(song_queue)

    if platform == 'win32':
        import ctypes
        myappid = 'Lune.Atlas'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    view = MainWindow(library, player, settings)
    view.show()

    app.exec_()

if __name__ == '__main__':
    main()
