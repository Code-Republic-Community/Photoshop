from PyQt5.QtCore import QBuffer, QIODevice
import io
from PyQt5.QtCore import QBuffer
from PIL import Image, ImageFilter
from PIL.ImageQt import ImageQt, QPixmap
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QMainWindow

from scribble_area import ScribbleArea
import numpy as np
import cv2 as cv


# from google.colab.patches import cv2_imshow

class Filter():
    def __init__(self):
        super(Filter, self).__init__()
        self.obj = self

    def qimage_to_cv(self, img: QImage):
        buffer = QBuffer()
        buffer.open(QBuffer.ReadWrite)
        img.save(buffer, "PNG")
        img_stream = io.BytesIO((buffer.data()))
        img = cv.imdecode(np.frombuffer(img_stream.read(), np.uint8), 1)
        return img

    def cv_to_qimage(self, img):
        is_success, buffer = cv.imencode(".jpg", img)
        io_buf = io.BytesIO(buffer)
        qimg = QImage()
        qimg.loadFromData(io_buf.getvalue())
        return qimg

    def blur(self, obj):
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

    def noise(self, obj):
        img = Filter().qimage_to_cv(obj.scribbleArea.image)

        row, col, ch = img.shape
        gauss = np.random.randn(row, col, ch)
        gauss = gauss.reshape(row, col, ch)
        speckle_noisy = img + img * gauss

        qimg = Filter().cv_to_qimage(speckle_noisy)
        obj.scribbleArea.image = qimg
        obj.scribbleArea.update()

    def distort(self, obj):
        pass

    def pixelate(self, obj):
        img = Filter().qimage_to_cv(obj.scribbleArea.image)
        height, width = img.shape[:2]
        w, h = (16, 16)
        temp = cv.resize(img, (w, h), interpolation=cv.INTER_LINEAR)
        output = cv.resize(temp, (width, height), interpolation=cv.INTER_NEAREST)
        qimg = Filter().cv_to_qimage(output)
        obj.scribbleArea.image = qimg
        obj.scribbleArea.update()
