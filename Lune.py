import sys
from PySide.QtCore import QUrl, Qt
from PySide import QtGui
from PySide.QtDeclarative import QDeclarativeView
from .views.player import Player


def main():
    app = QtGui.QApplication(sys.argv)
    view = QDeclarativeView()
    view.setSource(QUrl('views/Lune.qml'))
    view.setResizeMode(QDeclarativeView.SizeRootObjectToView)
    #view.setWindowFlags(Qt.FramelessWindowHint)
    player = Player()
    player.play()
    view.show()
    app.exec_()

if __name__ == '__main__':
    main()
