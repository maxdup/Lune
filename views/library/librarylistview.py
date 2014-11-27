
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
        self.proxymodel.setDynamicSortFilter(True)
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

    def filter(self, field, value):
        self.proxymodel.setFilterRole(field)
        self.proxymodel.setFilterFixedString(value)
        if self.ctrl:
            self.ctrl.update()

    def set_ctrl(self, ctrl):
        self.ctrl = ctrl
