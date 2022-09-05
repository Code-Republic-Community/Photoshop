from PyQt5.QtGui import QTransform, QImage
from PyQt5.QtWidgets import QGraphicsBlurEffect

from scribble_area import ScribbleArea


class Image():
    def __init__(self):
        super(Image, self).__init__()

    def image_size(self):
        pass

    def canvas_size(self):
        pass

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