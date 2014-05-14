# -*- coding: utf-8 -*-

from PySide import QtGui

from views.libraryView import LibraryView
from views.settingsView import SettingsView


class MainWindow(QtGui.QWidget):

    def __init__(self, player, settings):
        QtGui.QWidget.__init__(self)
        self.StackContainer = QtGui.QFrame()

        self.library = LibraryView(player)
        self.settings = SettingsView(settings)

        self.viewStack = QtGui.QStackedLayout()
        self.viewStack.addWidget(self.library)
        self.viewStack.addWidget(self.settings)

        self.StackContainer.setLayout(self.viewStack)

        self.viewSwitch = QtGui.QHBoxLayout()

        self.gotoLibrary = QtGui.QPushButton('Library')
        self.gotoLibrary.clicked.connect(lambda: self.viewStack.setCurrentIndex(0))
        self.gotoSettings = QtGui.QPushButton('Settings')
        self.gotoSettings.clicked.connect(lambda: self.viewStack.setCurrentIndex(1))

        #self.viewSwitch.addWidget(self.gotoSettings)
        #self.viewSwitch.addWidget(self.gotoLibrary)

        self.mainContainer = QtGui.QVBoxLayout()
        #self.mainContainer.addWidget(self.viewSwitch)
        self.mainContainer.addWidget(self.gotoLibrary)
        self.mainContainer.addWidget(self.gotoSettings)
        self.mainContainer.addWidget(self.StackContainer)
        self.setLayout(self.mainContainer)

        #self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon('lune.png'))
        self.setWindowTitle('Lune')


