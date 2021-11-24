from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import numpy as np
import pandas as pd
import glob
import os
import csv
from itertools import combinations
from PyQt5.QtWidgets import QDialog, QApplication


class DataFrameModel(QtCore.QAbstractTableModel):
    DtypeRole = QtCore.Qt.UserRole + 1000
    ValueRole = QtCore.Qt.UserRole + 1001

    def __init__(self, df=pd.DataFrame(), parent=None):
        super(DataFrameModel, self).__init__(parent)
        self._dataframe = df

    def setDataFrame(self, dataframe):
        self.beginResetModel()
        self._dataframe = dataframe.copy()
        self.endResetModel()

    def dataFrame(self):
        return self._dataframe

    dataFrame = QtCore.pyqtProperty(pd.DataFrame, fget=dataFrame, fset=setDataFrame)

    @QtCore.pyqtSlot(int, QtCore.Qt.Orientation, result=str)
    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int = QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self._dataframe.columns[section]
            else:
                return str(self._dataframe.index[section])
        return QtCore.QVariant()

    def rowCount(self, parent=QtCore.QModelIndex()):
        if parent.isValid():
            return 0
        return len(self._dataframe.index)

    def columnCount(self, parent=QtCore.QModelIndex()):
        if parent.isValid():
            return 0
        return self._dataframe.columns.size

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if not index.isValid() or not (0 <= index.row() < self.rowCount() \
            and 0 <= index.column() < self.columnCount()):
            return QtCore.QVariant()
        row = self._dataframe.index[index.row()]
        col = self._dataframe.columns[index.column()]
        dt = self._dataframe[col].dtype

        val = self._dataframe.iloc[row][col]
        if role == QtCore.Qt.DisplayRole:
            return str(val)
        elif role == DataFrameModel.ValueRole:
            return val
        if role == DataFrameModel.DtypeRole:
            return dt
        return QtCore.QVariant()

    def roleNames(self):
        roles = {
            QtCore.Qt.DisplayRole: b'display',
            DataFrameModel.DtypeRole: b'dtype',
            DataFrameModel.ValueRole: b'value'
        }
        return roles


class Ui_Rulepriority(object):
    def setupUi(self, Rulepriority):
        Rulepriority.setObjectName("Rulepriority")
        Rulepriority.resize(820, 480)
        self.verticalLayout = QtWidgets.QVBoxLayout(Rulepriority)
        self.verticalLayout.setObjectName("verticalLayout")
        self.OpenCsv = QtWidgets.QPushButton(Rulepriority)
        self.OpenCsv.setObjectName("OpenCsv")
        self.verticalLayout.addWidget(self.OpenCsv)
        self.OpenCsv.clicked.connect(self.file_open)
        self.tableView = QtWidgets.QTableView(Rulepriority)
        self.tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        QtCore.QFileSystemWatcher()
        self.retranslateUi(Rulepriority)
        self.OpenCsv.clicked.connect(self.tableView.show)
        QtCore.QMetaObject.connectSlotsByName(Rulepriority)

    def retranslateUi(self, Rulepriority):
        _translate = QtCore.QCoreApplication.translate
        Rulepriority.setWindowTitle(_translate("Rulepriority", "Violation Solving Prioritization tool"))
        self.OpenCsv.setText(_translate("Rulepriority", "Browse excel and get solving probability"))
        Rulepriority.setWindowIcon(QtGui.QIcon('favicon.ico'))

    def file_open(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(Rulepriority, 'Open csv', QtCore.QDir.rootPath(),
                                                        '*.csv')

        df1 = pd.read_csv(path)

        # cols = df1.columns.values
        # dm = df1[cols].apply(lambda x: x.duplicated())
        # df1[cols] = df1[cols].mask(dm, '')
        model = DataFrameModel(df1)
        self.tableView.setModel(model)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Rulepriority = QtWidgets.QDialog()
    ui = Ui_Rulepriority()
    ui.setupUi(Rulepriority)
    Rulepriority.show()
    sys.exit(app.exec_())