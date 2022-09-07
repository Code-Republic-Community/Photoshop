from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QCheckBox, QDialogButtonBox, QDialog
import cv2 as cv
import argparse
import numpy as np


class Buttons(QMainWindow):
    obj_photoshop = None

    def __init__(self):
        super().__init__()
        self.obj = None
        self.pos_x = QPoint()
        self.pos_y = QPoint()
        self.lastPoint = QPoint()

    def eyedropper(self, obj):
        global obj_photoshop
        obj_photoshop = obj

    def get_color(self, obj_scribble, pos_x, pos_y):
        img = obj_scribble.image.pixel(pos_x, pos_y)
        color = QColor(img).getRgb()
        obj_scribble.color_pen = color
        obj_photoshop.all_button_white()
        obj_scribble.pressed_button = None


class TextTypeCheckbox(QDialog):
    def __init__(self, obj):
        self.obj = obj
        super(TextTypeCheckbox, self).__init__()
        self.setFixedSize(200, 130)
        self.setWindowIcon(QIcon('../content/photoshop.png'))

        self.is_bold = False
        self.is_italic = False
        self.is_underline = False

        layout = QVBoxLayout()
        self.bold = QCheckBox("Bold")
        self.italic = QCheckBox("Italic")
        self.underline = QCheckBox("Underline")
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)

        layout.addWidget(self.italic)
        layout.addWidget(self.underline)
        layout.addWidget(self.bold)
        layout.addWidget(buttonBox)
        self.setLayout(layout)
        self.setWindowTitle("Text type")

        buttonBox.accepted.connect(self.accept)

    def accept(self):
        print(id(self.obj))
        if self.bold.isChecked():
            self.obj.bold = True
        if self.italic.isChecked():
            self.obj.italic = True
        if self.underline.isChecked():
            self.obj.underline = True
        self.close()
