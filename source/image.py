"""asdas"""

from PyQt5 import QtCore, QtWidgets, QtGui
import cv2 as cv


class Image:
    """asfsd"""

    @classmethod
    def image_size(cls, obj, obj1, obj2):
        """ffffff"""
        obj.is_clicked_move = False
        InputSize(obj, 'image size').exec()

    @classmethod
    def canvas_size(cls, obj, obj1, obj2):
        """kjl"""
        obj.is_clicked_move = False
        InputSize(obj, 'canvas size').exec()

    @classmethod
    def rotate_left(cls, obj, obj1, obj2):
        """ytutyu"""
        Image().rotate(obj, 'left')

    @classmethod
    def rotate_right(cls, obj, obj1, obj2):
        """hjghgvn"""
        Image().rotate(obj, 'right')

    @classmethod
    def rotate(cls, obj, rotate_type):
        """hguty"""
        obj.is_clicked_move = False
        transform90 = QtGui.QTransform()

        if rotate_type == 'right':
            transform90.rotate(90)
        else:
            transform90.rotate(-90)

        image = obj.scribble_area.image.transformed(transform90)
        image = obj.scribble_area.QimageToCv(image)
        image = cv.resize(image, obj.scribble_area.currentWindowSize())
        width, height = obj.scribble_area.currentWindowSize()
        obj.scribble_area.resizeImage(image, QtCore.QSize(width, height))

        image_draw = obj.scribble_area.image_draw.transformed(transform90)
        obj.scribble_area.resizeImageDraw(image_draw)
        obj.scribble_area.check = True
        obj.scribble_area.update()


class InputSize(QtWidgets.QDialog):
    """gfdgdfg"""

    def __init__(self, obj, btn_accepted, parent=None):
        """fgdgdf"""
        super().__init__(parent)
        self.setWindowTitle("Input size")
        self.setWindowIcon(QtGui.QIcon('../content/photoshop.png'))
        self.setFixedSize(0, 0)
        self.btn_accepted = btn_accepted
        self.obj = obj
        self.only_int = QtGui.QIntValidator()
        self.width = QtWidgets.QLineEdit(self)
        self.height = QtWidgets.QLineEdit(self)
        self.width.setValidator(self.only_int)
        self.height.setValidator(self.only_int)

        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok
                                                | QtWidgets.QDialogButtonBox.Cancel, self)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        layout = QtWidgets.QFormLayout(self)
        layout.addRow("Width", self.width)
        layout.addRow("Height", self.height)
        layout.addWidget(button_box)

    def accept(self):
        """gfdfg"""
        if self.btn_accepted == 'image size':
            if len(self.width.text()) != 0 and len(self.height.text()):
                width = int(self.width.text())
                height = int(self.height.text())
                img = self.obj.scribble_area.image
                img = self.obj.scribble_area.QimageToCv(img)
                image = cv.resize(img, (width, height))
                self.obj.scribble_area.resizeImage(image, QtCore.QSize(width, height))
                self.obj.scribble_area.image = self.obj.scribble_area.CvToQimage(image)

                self.obj.scribble_area.resizeImageDraw(self.obj.scribble_area.image_draw,
                                                       width, height)

                self.obj.scribble_area.update()
                self.close()
        else:
            if len(self.width.text()) != 0 and len(self.height.text()):
                width = int(self.width.text())
                height = int(self.height.text())
                self.obj.setWindowSize(width, height)
                self.close()
