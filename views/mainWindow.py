# -*- coding: utf-8 -*-

from PySide import QtGui

from views.libraryView import LibraryView
from views.settingsView import SettingsView


class MainWindow(QtGui.QWidget):

    def __init__(self, library, player, settings):
        QtGui.QWidget.__init__(self)
        self.StackContainer = QtGui.QFrame()

        self.vLibrary = LibraryView(player, library)
        self.vSettings = SettingsView(settings)

        self.viewStack = QtGui.QStackedLayout()
        self.viewStack.addWidget(self.vLibrary)
        self.viewStack.addWidget(self.vSettings)

        self.StackContainer.setLayout(self.viewStack)

        self.gotoLibrary = QtGui.QPushButton('Library')
        self.gotoLibrary.clicked.connect(self.gotoLib)
        self.gotoSettings = QtGui.QPushButton('Settings')
        self.gotoSettings.clicked.connect(lambda: self.viewStack.setCurrentIndex(1))

        self.mainContainer = QtGui.QVBoxLayout()
        self.mainContainer.addWidget(self.gotoLibrary)
        self.mainContainer.addWidget(self.gotoSettings)
        self.mainContainer.addWidget(self.StackContainer)
        self.setLayout(self.mainContainer)

        #self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon('lune.png'))
        self.setWindowTitle('Lune')

    def gotoLib(self):
        self.vLibrary.update()
        self.viewStack.setCurrentIndex(0)


