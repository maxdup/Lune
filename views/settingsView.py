# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
from models.userSettings import Path

class SettingsView(QtGui.QWidget):

    def __init__(self, usettings):
        QtGui.QWidget.__init__(self)
        layout = QtGui.QVBoxLayout()
        pathManager = PathManager(usettings)

        layout.addWidget(pathManager)
        self.setLayout(layout)


class PathManager(QtGui.QWidget):
    def __init__(self, usettings):
        QtGui.QWidget.__init__(self)
        layout = QtGui.QVBoxLayout()
        self.usettings = usettings
        self.libraryList = QtGui.QListWidget()

        def addPathDialog():
            path = QtGui.QFileDialog.getExistingDirectory()
            pathObj = self.usettings.addPath(path)
            self.addPath(pathObj)

        btnAddPaths = QtGui.QPushButton('add paths')
        btnAddPaths.clicked.connect(addPathDialog)

        for pathObj in self.usettings.pathList:
            self.addPath(pathObj)

        layout.addWidget(self.libraryList)
        layout.addWidget(btnAddPaths)
        self.setLayout(layout)

    def addPath(self, pathObj):
        size = QtCore.QSize(40,40)
        item = QtGui.QListWidgetItem(self.libraryList)
        item.setSizeHint(size)
        itemWidget = ItemPath(pathObj, item, self)
        self.libraryList.setItemWidget(item, itemWidget)


class ItemPath(QtGui.QWidget):
    def __init__(self, pathObj, item, pathManager):
        self.pathObj = pathObj
        self.item = item
        self.pathManager = pathManager

        QtGui.QWidget.__init__(self)
        layout = QtGui.QHBoxLayout()

        label = QtGui.QLabel(pathObj.path)
        remove = QtGui.QPushButton('x')
        remove.clicked.connect(self.remove)

        layout.addWidget(label)
        layout.addWidget(remove)
        self.setLayout(layout)

    def remove(self):
        self.pathObj.remove()
        index = self.item.listWidget().row(self.item)
        self.pathManager.libraryList.takeItem(index)
