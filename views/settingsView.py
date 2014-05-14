# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore

class SettingsView(QtGui.QWidget):

    def __init__(self, settings):
        self.settings = settings
        QtGui.QWidget.__init__(self)
        layout = QtGui.QVBoxLayout()
        pathManager = PathManager(settings)

        layout.addWidget(pathManager)
        self.setLayout(layout)


class PathManager(QtGui.QWidget):
    def __init__(self, settings):
        QtGui.QWidget.__init__(self)
        layout = QtGui.QVBoxLayout()
        libraryList = QtGui.QListWidget()
        btnAddPaths = QtGui.QPushButton('add paths') # todo

        size = QtCore.QSize(40,40)

        for path in settings.getPaths():
            item = QtGui.QListWidgetItem(libraryList)
            item.setSizeHint(size)
            itemWidget = ItemPath(path)
            libraryList.setItemWidget(item, itemWidget)

        layout.addWidget(libraryList)
        layout.addWidget(btnAddPaths)
        self.setLayout(layout)


class ItemPath(QtGui.QWidget):
    #we will eventually want to receive a Path object instead of a string
    def __init__(self, text):
        QtGui.QWidget.__init__(self)
        layout = QtGui.QHBoxLayout()

        label = QtGui.QLabel(text)
        remove = QtGui.QPushButton('x')
        # todo bind this button to path removal

        layout.addWidget(label)
        layout.addWidget(remove)
        self.setLayout(layout)
