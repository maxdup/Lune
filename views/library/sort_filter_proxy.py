from PySide.QtGui import QSortFilterProxyModel, QStandardItemModel, QIcon
from PySide.QtCore import QSize
from models.album import Album


class SortFilterProxy:

    def __init__(self, qlist, strategy):        
        self.qlist = qlist
        self.item_strat = strategy

        self.model = QStandardItemModel(self.qlist)

        self.proxymodel = QSortFilterProxyModel()
        self.proxymodel.setSourceModel(self.model)
        self.proxymodel.setDynamicSortFilter(True)
        self.qlist.setModel(self.proxymodel)

    def add(self, obj):
        item = self.item_strat.get_item(obj)
        self.model.appendRow(item)
        return item

    def filter(self, field, value):
        self.proxymodel.setFilterRole(field)
        self.proxymodel.setFilterFixedString(value)
