import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt


class LoadingGif(object):

    def mainUI(self, FrontWindow):
        FrontWindow.setObjectName("FTwindow")
        FrontWindow.resize(250, 250)
        self.centralwidget = QtWidgets.QWidget(FrontWindow)
        self.centralwidget.setObjectName("main-widget")

        # Label Create
        self.label = QtWidgets.QLabel(FrontWindow)
        self.label.setGeometry(QtCore.QRect(25, 25, 200, 200))
        # self.label.setMinimumSize(QtCore.QSize(250, 250))
        # self.label.setMaximumSize(QtCore.QSize(250, 250))
        self.label.setObjectName("lb1")
        # FrontWindow.setCentralWidget(self.centralwidget)

        # Loading the GIF
        self.movie = QMovie("loading.gif")
        self.label.setMovie(self.movie)
        self.movie.start()
        # self.startAnimation()

    # Start Animation

    def startAnimation(self):
        self.movie.start()

    # Stop Animation(According to need)
    def stopAnimation(self):
        self.movie.stop()


app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
demo = LoadingGif()
demo.mainUI(window)
window.show()
sys.exit(app.exec_())