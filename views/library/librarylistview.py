
from PySide import QtGui, QtCore
from PySide.QtGui import QListView, QStandardItemModel, QSortFilterProxyModel
from views.library.lunesortfilterproxymodel import LuneSortFilterProxyModel


class LibraryListView(QListView):
    def __init__(self, strategy):
        QListView.__init__(self)

        self.item_strat = strategy

        self.itemmodel = QStandardItemModel()
        self.proxymodel = LuneSortFilterProxyModel()
        self.proxymodel.setSourceModel(self.itemmodel)
        self.setModel(self.proxymodel)
        self.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.proxymodel.setSortCaseSensitivity(QtCore.Qt.CaseSensitivity.CaseInsensitive)
        self.proxymodel.sort(0)

    def add(self, obj):
        item = self.item_strat.get_item(obj)
        self.itemmodel.appendRow(item)
        if self.ctrl:
            self.ctrl.update()

        return item

    def remove(self, obj):
        for i in range(0, self.model().sourceModel().rowCount()):
            if obj == self.model().sourceModel().index(i,0).data(1101):
                self.model().sourceModel().removeRow(i)
                break
        return

    def filter(self, field, value):
        self.proxymodel.setFilterRole(field)
        self.proxymodel.setFilterFixedString(value)
        if self.ctrl:
            self.ctrl.update()

    def sort(self, sort):
        self.ctrl.set_sort(sort)

    def set_ctrl(self, ctrl):
        self.ctrl = ctrl
