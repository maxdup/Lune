import sys
from PySide.QtCore import QUrl, Qt
from PySide import QtGui
from PySide.QtDeclarative import QDeclarativeView
from views.player import Player
from DAL.collector import Collector


def main():
    app = QtGui.QApplication(sys.argv)
    view = QDeclarativeView()
    view.setSource(QUrl('views/Lune.qml'))
    view.setResizeMode(QDeclarativeView.SizeRootObjectToView)
    #view.setWindowFlags(Qt.FramelessWindowHint)
    collector = Collector()
    collector.searchDir("D:\Music")
    player = Player()
    player.Play()
    view.show()
    app.exec_()

if __name__ == '__main__':
    main()
