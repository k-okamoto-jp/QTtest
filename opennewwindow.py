#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import QMovie
import sys


class LoadingGif(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(LoadingGif, self).__init__(parent)

    # def mainUI(self, FrontWindow):
        self.setObjectName("FTwindow")
        self.resize(250, 250)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("main-widget")

        # Label Create
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(25, 25, 200, 200))
        # self.label.setMinimumSize(QtCore.QSize(250, 250))
        # self.label.setMaximumSize(QtCore.QSize(250, 250))
        self.label.setObjectName("lb1")
        # FrontWindow.setCentralWidget(self.centralwidget)

        # Loading the GIF
        self.movie = QMovie("loading.gif")
        self.label.setMovie(self.movie)
        self.startAnimation()

    # Start Animation

    def startAnimation(self):
        self.movie.start()

    # Stop Animation(According to need)
    def stopAnimation(self):
        self.movie.stop()

class Second(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Second, self).__init__(parent)


class First(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(First, self).__init__(parent)
        self.pushButton = QtWidgets.QPushButton("click me")

        self.setCentralWidget(self.pushButton)

        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.dialog = LoadingGif()

    def on_pushButton_clicked(self):
        self.dialog.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = First()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()