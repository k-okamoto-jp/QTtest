from PyQt5 import QtWidgets, QtGui, QtCore


class Main(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # create table:
        self.table = QtWidgets.QTableWidget()
        self.table.setRowCount(3)
        self.table.setColumnCount(4)
        for i, letter in enumerate("ABC"):
            self.table.setItem(i, 0, QtWidgets.QTableWidgetItem(letter))
        for i in range(self.table.rowCount()):
            # checkbox
            ch = QtWidgets.QCheckBox(parent=self.table)
            ch.clicked.connect(self.onStateChanged)
            self.table.setCellWidget(i, 1, ch)
            # combobox
            co = QtWidgets.QComboBox(parent=self.table)
            co.row = i
            co.addItem('')
            co.addItem('最初', 100)
            co.addItem('2番目', 110)
            co.addItem('尻尾', 300)
            co.currentIndexChanged.connect(self.oncurrentIndexChanged)
            self.table.setCellWidget(i, 2, co)
        self.setCentralWidget(self.table)
        self.setWindowTitle('TableWidget, CheckBoxes')
        self.show()

    def onStateChanged(self):
        ch = self.sender()
        print(ch.parent())
        ix = self.table.indexAt(ch.pos())
        print(ix.row(), ix.column(), ch.isChecked())

    def oncurrentIndexChanged(self, ele):
        print(ele)
        co = self.sender()
        self.table.setItem(co.row, 3,
                           QtWidgets.QTableWidgetItem(str(co.currentData())))


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())