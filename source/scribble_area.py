import io
import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QPoint, Qt, QSize, QBuffer, QRect, QThread, QFile, QIODevice
from PyQt5.QtGui import QImage, qRgb, QPainter, QPen, QColor, QIcon, QTextCharFormat, QFont, QBrush, QPolygon, QPixmap
from PyQt5.QtWidgets import QWidget, QColorDialog, QInputDialog, QUndoStack, QApplication
import numpy as np
import cv2 as cv
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PIL import Image, ImageFilter
from source.edit import UndoCommand
from source.buttons import Buttons


class ScribbleArea(QWidget):
    def __init__(self):
        super(ScribbleArea, self).__init__()
        self.setAttribute(Qt.WA_StaticContents)
        #self.image = QImage()
        self.buttons = Buttons()
        self.pressed_button = None
        # newSize = self.image.size().expandedTo(self.size())
        # self.resizeImage(self.image, QSize(newSize))
        self.update()
        self.last_point = QPoint()
        self.check = False
        self.color_pen = (0, 0, 0, 255)
        self.color_text = (0, 0, 0, 255)
        self.width_pen = 3
        self.width_text = 15
        self.bold = False
        self.italic = False
        self.underline = False
        self.text = None
        self.undo_stack = QUndoStack(self)
        self.undo_stack.setUndoLimit(20)
        self.begin = QPoint()
        self.end = QPoint()
        self.shape = QRect()
        self.image_draw = QtGui.QImage(self.size(), QtGui.QImage.Format_ARGB32)
        self.image = QImage(QtGui.QImage(self.size(), QtGui.QImage.Format_ARGB32))
        self.image.fill(qRgb(255, 255, 255))
        self.update()
        self.brush_size = 2
        self.clear_size = 20
        self.brush_color = QtGui.QColor(QtCore.Qt.black)
        self.open = False

    def current_window_size(self):
        return self.width(), self.height()

    def openImage(self, img):
        self.open = True
        # new_size = img.size().expandedTo(self.size())
        new_size = QSize(img.shape[0], img.shape[1])
        self.resizeImage(img, new_size)
        self.image = self.CvToQimage(img)
        self.update()
        return True

    def resizeImage(self, image, new_size):
        new_image = QImage(new_size, QImage.Format_RGB32)
        new_image.fill(qRgb(255, 255, 255))
        painter = QPainter(new_image)
        image = self.CvToQimage(image)
        painter.drawImage(QPoint(0, 0), image)
        self.image = new_image

    def resizeEvent(self, event):
        if self.open:
            img = cv.resize(self.QimageToCv(self.image), self.current_window_size())
            self.image = self.CvToQimage(img)
        else:
            pixmap = QPixmap()
            pixamp2 = pixmap.fromImage(self.image.copy().scaled(self.width(), self.height(),
                                                                Qt.IgnoreAspectRatio,
                                                                Qt.SmoothTransformation))
            self.image_copy = self.image.copy()
            self.image = pixamp2.toImage()

        pixmap = QPixmap()
        pixamp2 = pixmap.fromImage(
            self.image_draw.copy().scaled(self.width(), self.height(),
                                          Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        self.image_copy = self.image.copy()
        self.image_draw = pixamp2.toImage()
        self.update()

        super(ScribbleArea, self).resizeEvent(event)

    def resize_image_draw(self, image, width=None, height=None):
        if (width and height) == None:
            width = self.width()
            height = self.height()
        pixmap = QPixmap()
        pixamp2 = pixmap.fromImage(
            image.copy().scaled(width, height,
                                Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        self.image_copy = self.image.copy()

        self.image_draw = pixamp2.toImage()
        self.update()

    def saveImage(self, file_name, file_format):
        front_image = self.QimageToPil(self.image_draw).convert("RGBA")
        background = self.QimageToPil(self.image).convert("RGBA")
        width = (background.width - front_image.width) // 2
        height = (background.height - front_image.height) // 2
        background.paste(front_image, (width, height), front_image)
        visible_image = self.PilToQimage(background)
        self.resizeImage(visible_image, self.size())

        if visible_image.save(file_name, file_format):
            return True
        return False

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        dirty_rect = event.rect()
        painter.drawImage(dirty_rect, self.CvToQimage(self.image), dirty_rect)
        painter.drawImage(dirty_rect, self.image_draw, dirty_rect)
        painter.drawText(150, 250, self.text)
        self.update()
        if self.pressed_button == "paint":
            painter.drawImage(dirty_rect, self.image_draw, dirty_rect)
            painter.drawText(150, 250, self.text)

        if self.pressed_button == "marquee":
            painter.setPen(QPen(Qt.black, 1, Qt.DotLine))
            painter.drawImage(dirty_rect, self.image_draw, dirty_rect)
            painter.drawText(150, 250, self.text)
            if not self.begin.isNull() and not self.end.isNull():
                self.shape = QRect(self.begin, self.end)
                # self.coords = self.shape.getCoords()
                # painter.drawRect(self.shape.normalized())
                painter.drawRect(QRect(self.begin, self.end).normalized())

    def mousePressEvent(self, event):
        self.make_undo_command()
        if event.button() == Qt.LeftButton:
            self.last_point = event.pos()
            # self.buttons.pos_x = event.pos().x()
            # self.buttons.pos_y = event.pos().y()
            if self.pressed_button == 'eyedropper':
                self.buttons.get_color(self, event.pos().x(), event.pos().y())
            if self.pressed_button == 'marquee':
                self.begin = self.end = event.pos()
                self.update()
                super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.pressed_button == 'paint':
            painter = QPainter(self.image_draw)
            painter.setPen(QPen(
                QColor(self.color_pen[0], self.color_pen[1], self.color_pen[2], self.color_pen[3]),
                self.width_pen, Qt.SolidLine))
            painter.setBrush(QColor(40, 50, 20, 240))
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()

            self.update()
            self.check = True
        if self.pressed_button == "marquee":
            self.end = event.pos()
            self.update()
            super().mouseMoveEvent(event)

        if self.pressed_button == "eraser":
            painter = QtGui.QPainter(self.image_draw)
            painter.setPen(QtGui.QPen(self.brush_color, self.brush_size,
                                      QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
            r = QtCore.QRect(QtCore.QPoint(), self.clear_size * QtCore.QSize())
            r.moveCenter(event.pos())
            painter.save()
            painter.setCompositionMode(QPainter.CompositionMode_Clear)
            painter.eraseRect(r)
            painter.restore()
            painter.end()
            self.last_point = event.pos()
            self.update()

            self.last_point = event.pos()
            self.update()
            self.update()
            self.check = True

    def mouseReleaseEvent(self, event):
        pass

    def pen_color(self):
        color_dialog = QColorDialog(self)
        color_dialog.setWindowIcon(QIcon('../content/photoshop.png'))
        self.color_pen = color_dialog.getColor().getRgb()

    def pen_width(self, obj1, obj2):
        num, ok = QInputDialog.getInt(self, "Pen width", "Choose the pen width")
        self.width_pen = num
        obj1.paint()

    def make_undo_command(self):
        self.undo_stack.push(UndoCommand(self))

    def QimageToCv(self, img: QImage):
        buffer = QBuffer()
        buffer.open(QBuffer.ReadWrite)
        img.save(buffer, "PNG")
        img_stream = io.BytesIO((buffer.data()))
        img = cv.imdecode(np.frombuffer(img_stream.read(), np.uint8), 1)
        return img

    def CvToQimage(self, img):
        if not isinstance(img, QImage):
            is_success, buffer = cv.imencode(".jpg", img)
            io_buf = io.BytesIO(buffer)
            qimg = QImage()
            qimg.loadFromData(io_buf.getvalue())
            return qimg
        return img

    def QimageToPil(self, img):
        buffer = QBuffer()
        buffer.open(QBuffer.ReadWrite)
        img.save(buffer, "PNG")
        pil_im = Image.open(io.BytesIO(buffer.data()))
        return pil_im

    def PilToQimage(self, img):
        bytes_img = io.BytesIO()
        img.save(bytes_img, format='PNG')

        qimg = QImage()
        qimg.loadFromData(bytes_img.getvalue())
        return qimg
