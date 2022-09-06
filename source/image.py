from PyQt5.QtGui import QTransform, QImage, QIcon, QIntValidator
from PyQt5.QtWidgets import QGraphicsBlurEffect, QLineEdit, QDialogButtonBox, QFormLayout, QDialog

from scribble_area import ScribbleArea


class InputDialog(QDialog):
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
        width = int(self.width.text())
        height = int(self.height.text())
        self.obj.set_window_size(width, height)
        self.close()

class Image():
    def __init__(self):
        super(Image, self).__init__()

    def image_size(self):
        pass

    def canvas_size(self, obj):
        InputDialog(obj).exec()

    def rotate_left(self, obj):
        transform90 = QTransform()
        transform90.rotate(-90)

        obj.scribbleArea.image = obj.scribbleArea.image.transformed(transform90)
        obj.scribbleArea.update()

    def rotate_right(self, obj):
        transform90 = QTransform()
        transform90.rotate(90)
        obj.scribbleArea.image = obj.scribbleArea.image.transformed(transform90)
        obj.scribbleArea.update()
