from PySide import QtGui, QtCore

class TopBar(QtGui.QWidget):
    def __init__(self, mainwindow):
        QtGui.QWidget.__init__(self)
        self.mw = mainwindow

        self.setObjectName('topbar')
        layout = QtGui.QHBoxLayout()
        self.setLayout(layout)

        shutdown = QtGui.QPushButton(';')
        maximize = QtGui.QPushButton('^')
        minimize = QtGui.QPushButton('_')
        windowed = QtGui.QPushButton('\\')
        settings = QtGui.QPushButton('?')
        shutdown.clicked.connect(self.shutdown)
        maximize.clicked.connect(self.maximize)
        minimize.clicked.connect(self.minimize)
        windowed.clicked.connect(self.windowed)
        settings.clicked.connect(self.settings)
        layout.addWidget(shutdown)
        layout.addWidget(maximize)
        layout.addWidget(minimize)
        layout.addWidget(windowed)
        layout.addWidget(settings)

    def shutdown(self):
        QtCore.QCoreApplication.instance().quit()
    def maximize(self):
        self.mw.showMaximized()
    def minimize(self):
        self.mw.showMinimized()
    def windowed(self):
        self.mw.showNormal()
    def settings(self):
        self.mw.view_stack.setCurrentIndex(1)
