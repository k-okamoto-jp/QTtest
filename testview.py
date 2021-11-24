# -*- coding: utf-8 -*-

"""This module provides the FileNameEditor main window."""

from collections import deque
from datetime import datetime
from pathlib import Path
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QFileDialog, QWidget, QMessageBox
from ui.test import Ui_Form


class Window(QWidget, Ui_Form):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self._setupUI()
        self.setAcceptDrops(True)
        # self.tableView.setAcceptDrops(True)
        # self.tableWidget.setAcceptDrops(True)

    def _setupUI(self):
        self.setupUi(self)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                print(url)
            print("dragEnterEvent and accept")
            event.acceptProposedAction()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        pass

    def dropEvent(self, event):
        event.accept()
        print("dropEvent")