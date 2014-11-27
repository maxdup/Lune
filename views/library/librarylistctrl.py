from PySide import QtGui

class LibraryListCtrl(QtGui.QWidget):
    def __init__(self, listview, desc):
        QtGui.QWidget.__init__(self)

        self.listview = listview

        self.setLayout(QtGui.QHBoxLayout())
        self.layout().setContentsMargins(0,0,0,0)
        self.count = QtGui.QLabel(str(self.listview.model().rowCount()))
        self.layout().addWidget(self.count)
        self.layout().addWidget(QtGui.QLabel(desc))
        self.layout().addStretch()

    def update(self):
        self.count.setText(str(self.listview.model().rowCount()))

