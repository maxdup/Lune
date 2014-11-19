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
from controllers.arg_parser import argParser

import multiprocessing

def main():

    app = QtGui.QApplication(sys.argv)

    signal.signal(signal.SIGINT, signal.SIG_DFL)

    library = Library()
    settings = UserSettings()

    song_queue = SongQueue() #this should not be here tho
    argsongs = None
    if len(sys.argv) > 1:
        argsongs = argParser.get_queue(sys.argv)
    if argsongs:
        song_queue.add_last(argsongs)

    player = Player()
    player.set_queue(song_queue)
    if song_queue:
        player.play()


    if sys.platform == 'win32':
        import ctypes
        myappid = 'Lune.Atlas'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


    result_queue = multiprocessing.Queue()
    for path in settings.path_list:
        p = multiprocessing.Process(target=worker, args=(result_queue,path,))
        p.start()

    view = MainWindow(library, player, settings, result_queue)
    view.show()

    app.exec_()

def worker(result_queue, path):
    collect = Collector()
    collect.search_dir(result_queue, path)

if __name__ == '__main__':
    main()
