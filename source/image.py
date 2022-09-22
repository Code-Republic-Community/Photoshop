from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QTransform, QIcon, QIntValidator
from PyQt5.QtWidgets import QLineEdit, QDialogButtonBox, QFormLayout, QDialog
import cv2 as cv


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
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)

        layout = QFormLayout(self)
        layout.addRow("Width", self.width)
        layout.addRow("Height", self.height)
        layout.addWidget(button_box)

        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

    def accept(self):
        if len(self.width.text()) != 0 and len(self.height.text()):
            width = int(self.width.text())
            height = int(self.height.text())
            self.obj.setWindowSize(width, height)
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
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)

        layout = QFormLayout(self)
        layout.addRow("Width", self.width)
        layout.addRow("Height", self.height)
        layout.addWidget(button_box)

        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

    def accept(self):
        if len(self.width.text()) != 0 and len(self.height.text()):
            width = int(self.width.text())
            height = int(self.height.text())
            img = self.obj.scribble_area.image
            img = self.obj.scribble_area.QimageToCv(img)
            image = cv.resize(img, (width, height))
            self.obj.scribble_area.openImage(image)
            self.obj.scribble_area.image = self.obj.scribble_area.CvToQimage(image)

            self.obj.scribble_area.resizeImageDraw(self.obj.scribble_area.image_draw, width, height)

            self.obj.scribble_area.update()
            self.close()


class Image():
    def __init__(self):
        super(Image, self).__init__()

    def image_size(self, obj):
        obj.is_clicked_move = False
        InputDialogImageSize(obj).exec()

    def canvas_size(self, obj):
        obj.is_clicked_move = False
        InputDialogCanvasSize(obj).exec()

    def rotate_left(self, obj):
        obj.is_clicked_move = False

        transform90 = QTransform()
        transform90.rotate(-90)

        image = obj.scribble_area.image.transformed(transform90)
        image = obj.scribble_area.QimageToCv(image)
        image = cv.resize(image, obj.scribble_area.currentWindowSize())
        obj.scribble_area.openImage(image)

        image_draw = obj.scribble_area.image_draw.transformed(transform90)
        obj.scribble_area.resizeImageDraw(image_draw)
        #self.photoshop.band[0].label.setStyle(myStyle(-45, QPoint(0, 100)))

        obj.scribble_area.update()


    def rotate_right(self, obj):
        obj.is_clicked_move = False

        transform90 = QTransform()
        transform90.rotate(90)

        image = obj.scribble_area.image.transformed(transform90)
        image = obj.scribble_area.QimageToCv(image)
        image = cv.resize(image, obj.scribble_area.currentWindowSize())
        obj.scribble_area.openImage(image)

        image_draw = obj.scribble_area.image_draw.transformed(transform90)
        obj.scribble_area.resizeImageDraw(image_draw)

        obj.scribble_area.update()