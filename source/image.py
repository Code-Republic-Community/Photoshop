from PyQt5.QtCore import QSize
from PyQt5.QtGui import QTransform, QImage, QIcon, QIntValidator
from PyQt5.QtWidgets import QGraphicsBlurEffect, QLineEdit, QDialogButtonBox, QFormLayout, QDialog
import cv2 as cv

from scribble_area import ScribbleArea


class InputDialogCanvasSize(QDialog):
    def __init__(self, obj, parent=None):
        self.obj = obj
        self.only_int = QIntValidator()
        super().__init__(parent)
        self.width = QLineEdit(self)
        self.height = QLineEdit(self)
        self.width.setValidator(self.only_int)
        self.height.setValidator(self.only_int)
        self.setWindowTitle("Input size")
        self.setWindowIcon(QIcon('../content/photoshop.png'))
        self.setFixedSize(200, 100)
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)

        layout = QFormLayout(self)
        layout.addRow("Width", self.width)
        layout.addRow("Height", self.height)
        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def accept(self):
        if len(self.width.text()) != 0 and len(self.height.text()):
            width = int(self.width.text())
            height = int(self.height.text())
            self.obj.set_window_size(width, height)
            self.close()

class InputDialogImageSize(QDialog):
    def __init__(self, obj, parent=None):
        self.obj = obj
        self.only_int = QIntValidator()
        super().__init__(parent)
        self.width = QLineEdit(self)
        self.height = QLineEdit(self)
        self.width.setValidator(self.only_int)
        self.height.setValidator(self.only_int)
        self.setWindowTitle("Input size")
        self.setWindowIcon(QIcon('../content/photoshop.png'))
        self.setFixedSize(200, 100)
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)

        layout = QFormLayout(self)
        layout.addRow("Width", self.width)
        layout.addRow("Height", self.height)
        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def accept(self):
        if len(self.width.text()) != 0 and len(self.height.text()):
            width = int(self.width.text())
            height = int(self.height.text())
            img = self.obj.scribbleArea.image
            img = self.obj.qimage_to_cv(img)
            image = cv.resize(img, (width, height))
            self.obj.scribbleArea.openImage(image)
            self.obj.scribbleArea.image = self.obj.cv_to_qimage(image)
            self.obj.scribbleArea.update()
            self.close()

class Image():
    def __init__(self):
        super(Image, self).__init__()

    def image_size(self, obj):
        InputDialogImageSize(obj).exec()

    def canvas_size(self, obj):
        InputDialogCanvasSize(obj).exec()

    def rotate_left(self, obj):
        transform90 = QTransform()
        transform90.rotate(-90)

        image = obj.scribbleArea.image.transformed(transform90)
        image = obj.qimage_to_cv(image)
        image = cv.resize(image, obj.scribbleArea.current_window_size())
        obj.scribbleArea.openImage(image)
        obj.scribbleArea.update()

    def rotate_right(self, obj):
        transform90 = QTransform()
        transform90.rotate(90)

        image = obj.scribbleArea.image.transformed(transform90)
        image = obj.qimage_to_cv(image)
        image = cv.resize(image, obj.scribbleArea.current_window_size())
        obj.scribbleArea.openImage(image)
        obj.scribbleArea.update()