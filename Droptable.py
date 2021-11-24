import sys, os
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, \
    QTableView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class TableLabel(QTableView):
    def __init__(self):
        super().__init__()


    def setPixmap(self, image):
        super().setPixmap(image)

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 400)
        self.setAcceptDrops(True)

        mainLayout = QVBoxLayout()

        self.tableViewer = TableLabel()
        mainLayout.addWidget(self.tableViewer)

        self.setLayout(mainLayout)

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            print('draged')
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            print('moving')
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            print('dropped')
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            print('get file path:', file_path)
            self.set_table(file_path)

            event.accept()
        else:
            event.ignore()

    def set_table(self, file_path):
        df = pd.read_csv(file_path)
        self.tableViewer

app = QApplication(sys.argv)
demo = AppDemo()
demo.show()

sys.exit(app.exec())