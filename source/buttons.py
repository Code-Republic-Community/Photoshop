from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtWidgets import QMainWindow
import cv2 as cv
import argparse
import numpy as np

class Buttons(QMainWindow):
    def __init__(self):
        super(Buttons, self).__init__()
        self.obj = None
        self.lastPoint = QPoint()

    def eyedropper(self, obj):
        self.obj = obj
        print(obj.scribbleArea.a)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            print(event.pos())

