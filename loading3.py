import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMainWindow

class MainWindow (QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow,self).__init__(parent)
        self.setGeometry(50,50,240,320)
        self.home()

    def home(self):
        but = QPushButton("Example", self) # Creates the brew coffee button
        but.clicked.connect(self.gif_display)
        but.resize(200,80)
        but.move(20,50)
        self.show()

    @QtCore.pyqtSlot()
    def gif_display(self):
        l = QMovieLabel('loading.gif', self)
        l.adjustSize()
        l.show()

class QMovieLabel(QLabel):
    def __init__(self, fileName, parent=None):
        super(QMovieLabel, self).__init__(parent)
        m = QtGui.QMovie(fileName)
        self.setMovie(m)
        m.start()

    def setMovie(self, movie):
        super(QMovieLabel, self).setMovie(movie)
        s=movie.currentImage().size()
        self._movieWidth = s.width()
        self._movieHeight = s.height()

def run():
    app = QApplication(sys.argv)
    GUI = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()