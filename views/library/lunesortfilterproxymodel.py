from PySide.QtGui import QSortFilterProxyModel
class LuneSortFilterProxyModel(QSortFilterProxyModel):
    def __init__(self):
        QSortFilterProxyModel.__init__(self)
        self.sortBy = 0
        self.ascending = True

    def setSort(self, sortValue, ascending=True):
        self.sortBy = sortValue
        self.ascending = ascending

    def lessThan(self, left, right):
        ordered = left.data(self.sortBy) < right.data(self.sortBy)
        if not self.ascending:
            return not ordered
        else:
            return ordered
    
        
