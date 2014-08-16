from PySide import QtGui, QtCore

class TopBar(QtGui.QWidget):
    def __init__(self, mainwindow):
        QtGui.QWidget.__init__(self)
        self.mw = mainwindow
        self.setStyleSheet(self.mw.style)

        self.setObjectName('topbar')

        layout = QtGui.QHBoxLayout()
        self.setLayout(layout)

        controls = QtGui.QWidget()
        controls.setObjectName('wcontrols')
        controls_l = QtGui.QBoxLayout(QtGui.QBoxLayout.Direction.RightToLeft)
        controls.setLayout(controls_l)

        shutdown = QtGui.QPushButton(';')
        maximize = QtGui.QPushButton('^')
        windowed = QtGui.QPushButton('\\')
        minimize = QtGui.QPushButton('_')
        settings = QtGui.QPushButton('?')
        shutdown.clicked.connect(self.shutdown)
        maximize.clicked.connect(self.maximize)
        windowed.clicked.connect(self.windowed)
        minimize.clicked.connect(self.minimize)
        settings.clicked.connect(self.settings)
        controls_l.addWidget(shutdown)
        controls_l.addWidget(maximize)
        controls_l.addWidget(windowed)
        controls_l.addWidget(minimize)
        controls_l.addWidget(settings)

        layout.addWidget(QtGui.QLabel('Lune'))
        layout.addStretch()
        layout.addWidget(controls)

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
