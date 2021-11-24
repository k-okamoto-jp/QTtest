import sys

from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem

from .ui.GraphicsViewdemo import Ui_Form
from PyQt5.QtGui import *


class MyForm(QtGui.QWidget):
    def __init__(self, pixmap, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.scene = QGraphicsScene(self)
        item = QGraphicsPixmapItem(pixmap)
        self.scene.addItem(item)
        self.ui.graphicsView.setScene(self.scene)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    pixmap = QtGui.QPixmap()
    pixmap.load("loading.gif")

    myapp = MyForm(pixmap)
    myapp.show()
    sys.exit(app.exec_())