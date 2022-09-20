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
        super().__init__()

    def blur(self, obj):
        img = obj.scribble_area.image
        buffer = QBuffer()
        buffer.open(QBuffer.ReadWrite)
        img.save(buffer, "PNG")
        pil_im = Image.open(io.BytesIO(buffer.data())).filter(ImageFilter.BLUR)

        bytes_img = io.BytesIO()
        pil_im.save(bytes_img, format='PNG')

        qimg = QImage()
        qimg.loadFromData(bytes_img.getvalue())

        obj.scribble_area.image = qimg

        img_draw = obj.scribble_area.image_draw
        buffer_draw = QBuffer()
        buffer_draw.open(QBuffer.ReadWrite)
        img_draw.save(buffer_draw, "PNG")
        pil_im_draw = Image.open(io.BytesIO(buffer_draw.data())).filter(ImageFilter.BLUR)

        bytes_img_draw = io.BytesIO()
        pil_im_draw.save(bytes_img_draw, format='PNG')

        qimg_draw = QImage()
        qimg_draw.loadFromData(bytes_img_draw.getvalue())

        obj.scribble_area.image_draw = qimg_draw
        obj.scribble_area.update()

    def noise(self, obj):
        img = obj.scribble_area.QimageToCv(obj.scribble_area.image)

        row, col, ch = img.shape
        gauss = np.random.randn(row, col, ch)
        gauss = gauss.reshape(row, col, ch)
        speckle_noisy = img + img * gauss

        qimg = obj.scribble_area.CvToQimage(speckle_noisy)
        obj.scribble_area.image = qimg

        obj.scribble_area.update()

    def twirling_spirals(self, obj):
        im = obj.scribble_area.QimageToCv(obj.scribble_area.image)
        cx = im.shape[1] / 2
        cy = im.shape[0] / 2
        a = -1
        b = 2
        c = 1
        r = 1

        x = np.linspace(0, im.shape[1], im.shape[1], dtype=np.float32)
        y = np.linspace(0, im.shape[0], im.shape[0], dtype=np.float32)
        xv, yv = np.meshgrid(x - cx, y - cy)

        mag, ang = cv.cartToPolar(xv, yv)
        nmag = cv.normalize(mag, None, norm_type=cv.NORM_MINMAX)

        sxv, syv = cv.polarToCart(mag, (ang + (a + b * np.pi * nmag ** (1.0 / c)) * (nmag < r)))
        spiral = cv.remap(im,
                          sxv + cx,
                          syv + cy,
                          cv.INTER_LINEAR)

        qimg = obj.scribble_area.CvToQimage(spiral)
        obj.scribble_area.image = qimg

        obj.scribble_area.update()

    def pixelate(self, obj):
        img = obj.scribble_area.QimageToCv(obj.scribble_area.image)
        height, width = img.shape[:2]
        w, h = (16, 16)
        temp = cv.resize(img, (w, h), interpolation=cv.INTER_LINEAR)
        output = cv.resize(temp, (width, height), interpolation=cv.INTER_NEAREST)
        qimg = obj.scribble_area.CvToQimage(output)
        obj.scribble_area.image = qimg
        obj.scribble_area.update()
