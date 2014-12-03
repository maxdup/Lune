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

        self.sort = QtGui.QPushButton('sorts')
        self.sort.clicked.connect(self.cycle_sort)

        self.layout().addWidget(QtGui.QLabel('sorted by'))
        self.layout().addWidget(self.sort)

        self.sorts = listview.item_strat.get_sorts()
        self.set_sort(0)
        self.update()

    def set_sort(self, index):
        self.at = index
        if self.at  == len(self.sorts):
            self.at = 0
        self.sort.setText(self.sorts[self.at].text)
        self.listview.proxymodel.setSortOrder(self.sorts[self.at].order)
        self.listview.proxymodel.setSortRole(self.sorts[self.at].role)

    def cycle_sort(self):
        self.set_sort(self.at + 1)

    def update(self):
        self.count.setText(str(self.listview.model().rowCount()))
