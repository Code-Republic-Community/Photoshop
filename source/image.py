"""asdas"""

from PyQt5 import QtWidgets, QtGui, QtCore
import cv2 as cv


class Image:
    """asfsd"""

    @classmethod
    def image_size(cls, photoshop_obj):
        """ffffff"""
        photoshop_obj.is_clicked_move = False
        InputSize(photoshop_obj, 'image size').exec()

    @classmethod
    def canvas_size(cls, photoshop_obj):
        """kjl"""
        photoshop_obj.is_clicked_move = False
        InputSize(photoshop_obj, 'canvas size').exec()

    @classmethod
    def rotate_left(cls, photoshop_obj):
        """ytutyu"""
        photoshop_obj.scribble_area.rotated = 'left'
        if not photoshop_obj.is_clicked_move:
            Image().rotate(photoshop_obj, 'left')

    @classmethod
    def rotate_right(cls, photoshop_obj):
        """hjghgvn"""
        photoshop_obj.scribble_area.rotated = 'right'
        if not photoshop_obj.is_clicked_move:
            Image().rotate(photoshop_obj, 'right')

    @classmethod
    def rotate(cls, photoshop_obj, rotate_type):
        """hguty"""
        photoshop_obj.is_clicked_move = False
        transform90 = QtGui.QTransform()

        if rotate_type == 'right':
            transform90.rotate(90)
        else:
            transform90.rotate(-90)

        image = photoshop_obj.scribble_area.image.transformed(transform90)
        photoshop_obj.scribble_area.resize_image_draw(image, 'image')

        image_draw = photoshop_obj.scribble_area.image_draw.transformed(transform90)
        photoshop_obj.scribble_area.resize_image_draw(image_draw, 'image_draw')

        photoshop_obj.scribble_area.check = True
        photoshop_obj.scribble_area.update()


class InputSize(QtWidgets.QDialog):
    """gfdgdfg"""

    def __init__(self, photoshop_obj, btn_accepted, parent=None):
        """fgdgdf"""
        super().__init__(parent)
        self.setFixedSize(0, 0)
        self.btn_accepted = btn_accepted
        self.photoshop_obj = photoshop_obj
        self.only_int = QtGui.QIntValidator()
        self.width = QtWidgets.QLineEdit(self)
        self.height = QtWidgets.QLineEdit(self)
        self.width.setValidator(self.only_int)
        self.height.setValidator(self.only_int)
        self.width.setStyleSheet("QLineEdit { border-radius: 8px; }""")
        self.height.setStyleSheet("QLineEdit { border-radius: 8px; }""")

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok
                                                | QtWidgets.QDialogButtonBox.Cancel, self)

        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        button_box.button(QtWidgets.QDialogButtonBox.Ok).setMinimumSize(QtCore.QSize(60, 25))
        button_box.button(QtWidgets.QDialogButtonBox.Ok).setStyleSheet(
            "border-radius:8px;"
            "background:#D600C9;color: white"
        )
        button_box.button(QtWidgets.QDialogButtonBox.Cancel).setMinimumSize(QtCore.QSize(60, 25))
        button_box.button(QtWidgets.QDialogButtonBox.Cancel).setStyleSheet(
            "border-radius:8px;"
            "background: White;color: #D600C9"
        )


        layout = QtWidgets.QFormLayout(self)
        layout.addRow('Width', self.width)
        layout.addRow('Height', self.height)
        layout.addWidget(button_box)

    def accept(self):
        """gfdfg"""
        if self.btn_accepted == 'image size':
            if len(self.width.text()) != 0 and len(self.height.text()):
                width = int(self.width.text())
                height = int(self.height.text())
                img = self.photoshop_obj.scribble_area.image
                image_draw = self.photoshop_obj.scribble_area.image_draw
                self.photoshop_obj.scribble_area.image_width = width
                self.photoshop_obj.scribble_area.image_height = height
                self.photoshop_obj.scribble_area.resize_image_draw(img, 'image')
                self.photoshop_obj.scribble_area.resize_image_draw(image_draw, 'image_draw')

                self.photoshop_obj.scribble_area.update()
                self.close()
        else:
            if len(self.width.text()) != 0 and len(self.height.text()):
                width = int(self.width.text())
                height = int(self.height.text())
                if width < 600:
                    width = 600
                if height < 400:
                    height = 400
                self.photoshop_obj.scribble_area.image_width = width
                self.photoshop_obj.scribble_area.image_height = height
                self.photoshop_obj.set_window_size(width, height)
                self.close()
