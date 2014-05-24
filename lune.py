# -*- coding: utf-8 -*-

import sys
import signal

from PySide import QtGui

from dal.collector import Collector
from models.user_settings import UserSettings
from models.library import Library
from models.song_queue import SongQueue
from views.main_window import MainWindow
from views.player import Player


def main():
    app = QtGui.QApplication(sys.argv)

    signal.signal(signal.SIGINT, signal.SIG_DFL)

    library = Library()
    collector = Collector(library)
    settings = UserSettings(collector)

    song_queue = SongQueue()
    song_queue.add_last(library.songs)

    player = Player()
    player.set_queue(song_queue)

    if sys.platform == 'win32':
        import ctypes
        myappid = 'Lune.Atlas'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    view = MainWindow(library, player, settings)
    view.show()

    app.exec_()

if __name__ == '__main__':
    main()
