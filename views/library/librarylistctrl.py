from PySide import QtGui


class LibraryListCtrl(QtGui.QWidget):

    def __init__(self, listview, desc, sorts=[]):
        QtGui.QWidget.__init__(self)

        self.listview = listview
        self.setLayout(QtGui.QHBoxLayout())
        self.layout().setContentsMargins(0,0,0,0)
        self.count = QtGui.QLabel(str(self.listview.model().rowCount()))
        self.layout().addWidget(self.count)
        self.layout().addWidget(QtGui.QLabel(desc))
        self.layout().addStretch()


        self.sort = QtGui.QPushButton('sorts')
        self.sort.clicked.connect(self.cycle_sort)
        self.setSorts(sorts)

        self.layout().addWidget(self.sort)

    def setSorts(self, sorts):
        self.sorts = []
        for sort in sorts:
            self.sorts.append(sort)
        self.at=0

    def update(self):
        self.count.setText(str(self.listview.model().rowCount()))

    def cycle_sort(self):
        self.at += 1
        if self.at == len(self.sorts):
            self.at = 0
        self.sort.setText(str(self.sorts[self.at]))
        self.listview.proxymodel.setSortRole(self.sorts[self.at])
