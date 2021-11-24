from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        MainMenu.setObjectName("MainMenu")
        MainMenu.resize(1024, 760)
        # self.centralwidget = QtWidgets.QWidget(MainMenu)
        self.centralwidget = self.set_gif("loading.gif")
        # self.centralwidget.setObjectName("centralwidget")
        MainMenu.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainMenu)
        self.statusbar.setObjectName("statusbar")
        MainMenu.setStatusBar(self.statusbar)
        self.retranslateUi(MainMenu)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)

    def retranslateUi(self, MainMenu):
        _translate = QtCore.QCoreApplication.translate
        MainMenu.setWindowTitle(_translate("MainMenu", "MainWindow"))

    def set_gif(self, gif_path):
        movie = QtGui.QMovie()
        movie.setFileName(gif_path)
        movie_label = QtWidgets.QLabel()
        movie_label.setMovie(movie)
        movie.start()
        return movie_label


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainMenu = QtWidgets.QMainWindow()
    ui = Ui_MainMenu()
    ui.setupUi(MainMenu)
    MainMenu.show()
    sys.exit(app.exec_())