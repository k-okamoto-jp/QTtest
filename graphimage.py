## -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets, QtGui


def main():
    app = QtWidgets.QApplication(sys.argv)
    graphics_view = QtWidgets.QGraphicsView()
    # create scene
    scene = QtWidgets.QGraphicsScene()
    image = QtGui.QImage('loading.gif')
    pixmap = QtGui.QPixmap.fromImage(image)
    scene.addPixmap(pixmap)
    # set scene
    graphics_view.setScene(scene)
    graphics_view.show()
    app.exec()


if __name__ == '__main__':
    main()