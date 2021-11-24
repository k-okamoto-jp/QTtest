import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QMainWindow
from PyQt5.QtCore import Qt, QRect, QSize
from PyQt5.QtGui import QPixmap, QMovie

# class ImageLabel(QLabel):
#     def __init__(self):
#         super().__init__()
#
#         # self.setAlignment(Qt.AlignCenter)
#         # self.setText('\n\n Drop Image here \n\n')
#         # self.setStyleSheet('''
#         #     QLabel{
#         #         border: 4px dashed #aaa
#         #     }
#         # ''')
#
#
#     def setPixmap(self, image):
#         super().setPixmap(image)

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 400)
        self.setAcceptDrops(True)

        mainLayout = QVBoxLayout()

        self.photoViewer = QLabel()
        mainLayout.addWidget(self.photoViewer)

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
            self.movie = QMovie("loading.gif")
            self.photoViewer.setMovie(self.movie)
            self.startAnimation()
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            print('dropped')
            self.stopAnimation()
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            print('get file path:', file_path)
            self.set_image(file_path)
            event.accept()

        else:
            event.ignore()

    def set_image(self, file_path):
        self.photoViewer.setPixmap(QPixmap(file_path))

    def startAnimation(self):
        self.movie.start()

    # Stop Animation(According to need)
    def stopAnimation(self):
        self.movie.stop()


app = QApplication(sys.argv)
demo = AppDemo()
demo.show()

sys.exit(app.exec())