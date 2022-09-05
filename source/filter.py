from PyQt5.QtCore import QBuffer, QIODevice
import io
from PyQt5.QtCore import QBuffer
from PIL import Image, ImageFilter
from PIL.ImageQt import ImageQt, QPixmap
from PyQt5.QtGui import QImage
from scribble_area import  ScribbleArea

class Filter():
    def __init__(self):
        super(Filter, self).__init__()


    def blur(self,obj):
        img = obj.scribbleArea.image
        buffer = QBuffer()
        buffer.open(QBuffer.ReadWrite)
        img.save(buffer, "PNG")
        pil_im = Image.open(io.BytesIO(buffer.data())).filter(ImageFilter.BLUR)

        bytes_img = io.BytesIO()
        pil_im.save(bytes_img, format='PNG')

        qimg = QImage()
        qimg.loadFromData(bytes_img.getvalue())

        obj.scribbleArea.image = qimg
        obj.scribbleArea.update()

    def noise(self,obj):
        pass
    def distort(self,obj):
        pass

    def pixelate(self,obj):
        pass

