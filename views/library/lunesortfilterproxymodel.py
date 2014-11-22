from PySide.QtGui import QSortFilterProxyModel
class LuneSortFilterProxyModel(QSortFilterProxyModel):
    def __init__(self):
        QSortFilterProxyModel.__init__(self)
    def lessThan(self, left, right):
        return left.data(1001) < right.data(1001)
    
        
