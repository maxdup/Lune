from PySide import QtGui, QtCore
from PySide.QtGui import QSortFilterProxyModel


class SortFilterProxy:

    def __init__(self, qlist, strategy):        
        self.qlist = qlist
        self.item_strat = strategy

        self.model = QtGui.QStandardItemModel(self.qlist)

        self.proxymodel = QSortFilterProxyModel()
        self.proxymodel.setSourceModel(self.model)
        self.proxymodel.setDynamicSortFilter(True)
        self.qlist.setModel(self.proxymodel)

    def add(self, obj):
        self.model.appendRow(self.item_strat.get_item(obj))

    def filter(self, field, value):
        self.proxymodel.setFilterRole(field)
        self.proxymodel.setFilterFixedString(value)
