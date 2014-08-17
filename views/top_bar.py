from PySide import QtGui, QtCore

class TopBar(QtGui.QWidget):
    def __init__(self, mainwindow):
        QtGui.QWidget.__init__(self)

        self.mw = mainwindow
        self.maxed = False
        self.setObjectName('topbar')
        layout = QtGui.QHBoxLayout()
        self.setLayout(layout)

        controls = QtGui.QWidget()
        controls.setObjectName('wcontrols')
        controls_l = QtGui.QBoxLayout(QtGui.QBoxLayout.Direction.RightToLeft)
        controls_l.setContentsMargins(0,0,0,0)
        controls.setLayout(controls_l)

        shutdown = QtGui.QPushButton(';')
        self.resize = QtGui.QPushButton('^')
        minimize = QtGui.QPushButton('_')
        settings = QtGui.QPushButton('?')
        shutdown.clicked.connect(self.shutdown)
        self.resize.clicked.connect(self.toggle_maximized)
        minimize.clicked.connect(self.minimize)
        settings.clicked.connect(self.settings)
        controls_l.addWidget(shutdown)
        controls_l.addWidget(self.resize)
        controls_l.addWidget(minimize)
        controls_l.addWidget(settings)

        layout.addWidget(QtGui.QLabel('Lune'))
        layout.addStretch()
        layout.addWidget(controls)
        layout.setContentsMargins(0,15,0,0)

    def shutdown(self):
        QtCore.QCoreApplication.instance().quit()
    def maximize(self):
        self.mw.showMaximized()
        self.maxed = True
        self.resize.setText('\\')
    def minimize(self):
        self.mw.showMinimized()
    def windowed(self):
        self.mw.showNormal()
        self.maxed = False
        self.resize.setText('^')
    def settings(self):
        self.mw.view_stack.setCurrentIndex(1)
    def toggle_maximized(self):
        if self.maxed:
            self.windowed()
        else:
            self.maximize()
