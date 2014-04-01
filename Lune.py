import sys
from PyQt4.QtCore import QUrl, Qt
from PyQt4 import QtGui
from PyQt4.QtDeclarative import QDeclarativeView


def main():
    app = QtGui.QApplication(sys.argv)
    view = QDeclarativeView()
    view.setSource(QUrl('views/Lune.qml'))
    view.setResizeMode(QDeclarativeView.SizeRootObjectToView)
    #view.setWindowFlags(Qt.FramelessWindowHint)
    view.show()
    app.exec_()

    
if __name__ == '__main__':
    main()
