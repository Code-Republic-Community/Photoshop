import io
from PyQt5 import QtCore, QtGui
from PIL import Image, ImageFilter
import numpy as np
import cv2 as cv


class Filter:
    @classmethod
    def blur(cls, photoshop_obj):
        photoshop_obj.scribble_area.save_image()
        photoshop_obj.scribble_area.image_draw.fill(QtCore.Qt.transparent)
        photoshop_obj.is_clicked_move = False
        img = photoshop_obj.scribble_area.image
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QBuffer.ReadWrite)
        img.save(buffer, "PNG")
        pil_im = Image.open(io.BytesIO(buffer.data())).filter(ImageFilter.BLUR)

        bytes_img = io.BytesIO()
        pil_im.save(bytes_img, format='PNG')

        q_img = QtGui.QImage()
        q_img.loadFromData(bytes_img.getvalue())

        photoshop_obj.scribble_area.image = q_img
        photoshop_obj.scribble_area.check = True
        photoshop_obj.scribble_area.update()

    @classmethod
    def noise(cls, photoshop_obj):
        photoshop_obj.scribble_area.save_image()
        photoshop_obj.scribble_area.image_draw.fill(QtCore.Qt.transparent)

        photoshop_obj.is_clicked_move = False
        img = photoshop_obj.scribble_area.convert_q_image_to_cv(photoshop_obj.scribble_area.image)

        row, col, ch_s = img.shape
        gauss = np.random.randn(row, col, ch_s)
        gauss = gauss.reshape(row, col, ch_s)
        speckle_noisy = img + img * gauss

        q_img = photoshop_obj.scribble_area.convert_cv_to_q_image(speckle_noisy)
        photoshop_obj.scribble_area.image = q_img
        photoshop_obj.scribble_area.check = True

        photoshop_obj.scribble_area.update()

    @classmethod
    def twirling_spirals(cls, photoshop_obj):
        photoshop_obj.scribble_area.save_image()
        photoshop_obj.scribble_area.image_draw.fill(QtCore.Qt.transparent)

        photoshop_obj.is_clicked_move = False
        img = photoshop_obj.scribble_area.convert_q_image_to_cv(photoshop_obj.scribble_area.image)
        c_x = img.shape[1] / 2
        c_y = img.shape[0] / 2
        a_p = -1
        b_p = 2
        c_p = 1
        r_p = 1

        x_axis = np.linspace(0, img.shape[1], img.shape[1], dtype=np.float32)
        y_ord = np.linspace(0, img.shape[0], img.shape[0], dtype=np.float32)
        x_v, y_v = np.meshgrid(x_axis - c_x, y_ord - c_y)

        mag, ang = cv.cartToPolar(x_v, y_v)
        n_mag = cv.normalize(mag, None, norm_type=cv.NORM_MINMAX)

        sxv, syv = cv.polarToCart(mag, (ang + (a_p + b_p * np.pi * n_mag ** (1.0 / c_p))
                                        * (n_mag < r_p)))
        spiral = cv.remap(img,
                          sxv + c_x,
                          syv + c_y,
                          cv.INTER_LINEAR)

        q_img = photoshop_obj.scribble_area.convert_cv_to_q_image(spiral)
        photoshop_obj.scribble_area.image = q_img
        photoshop_obj.scribble_area.check = True
        photoshop_obj.scribble_area.update()

    @classmethod
    def pixelate(cls, photoshop_obj):
        photoshop_obj.scribble_area.save_image()
        photoshop_obj.scribble_area.image_draw.fill(QtCore.Qt.transparent)

        photoshop_obj.is_clicked_move = False
        img = photoshop_obj.scribble_area.convert_q_image_to_cv(photoshop_obj.scribble_area.image)
        height, width = img.shape[:2]
        width_, height_ = (16, 16)
        temp = cv.resize(img, (width_, height_), interpolation=cv.INTER_LINEAR)
        output = cv.resize(temp, (width, height), interpolation=cv.INTER_NEAREST)
        q_img = photoshop_obj.scribble_area.convert_cv_to_q_image(output)
        photoshop_obj.scribble_area.image = q_img
        photoshop_obj.scribble_area.check = True
        photoshop_obj.scribble_area.update()
        
