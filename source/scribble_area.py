import io
import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QPoint, Qt, QSize, QBuffer, QRect, QThread, QFile, QIODevice, QRectF
from PyQt5.QtGui import QImage, qRgb, QPainter, QPen, QColor, QIcon, QTextCharFormat, QFont, QBrush, QPolygon, QPixmap
from PyQt5.QtWidgets import QWidget, QColorDialog, QInputDialog, QUndoStack, QApplication
import numpy as np
import cv2 as cv
from PyQt5.QtCore import Qt
from PIL import Image, ImageFilter

from source.edit import UndoCommand
from source.buttons import Buttons
from source.buttons import MoveText


class ScribbleArea(QWidget):
    def __init__(self):
        super(ScribbleArea, self).__init__()
        # self.x = 0
        # self.y = 0
        self.setAttribute(Qt.WA_StaticContents)
        self.photoshop_obj = None
        self.image_draw = QImage(self.size(), QImage.Format_ARGB32)
        self.image = QImage(self.size(), QImage.Format_ARGB32)
        self.image.fill(qRgb(255, 255, 255))
        self.image_size_x = 900
        self.image_size_y = 600
        self.buttons = Buttons()
        self.pressed_button = None
        # newSize = self.image.size().expandedTo(self.size())
        # self.resizeImage(self.image, QSize(newSize))
        self.update()
        self.last_point = QPoint()
        self.check = False
        self.draw = False
        self.color_pen = (0, 0, 0, 255)
        self.color_text = (0, 0, 0, 255)
        self.pen_width = 3
        self.width_text = 15
        self.bold = False
        self.italic = False
        self.underline = False
        self.text = ''
        self.undo_stack = QUndoStack(self)
        self.undo_stack.setUndoLimit(20)
        self.begin = QPoint()
        self.end = QPoint()
        self.shape = QRect()
        self.update()
        self.rubber_width = 10
        self.open = False
        self.rotated = "None"
        self.is_text = False

    def currentWindowSize(self):
        return self.width(), self.height()

    def openImage(self, img):
        self.open = True
        new_size = QSize(img.shape[0], img.shape[1])
        self.resizeImage(img)
        image_draw = QImage(self.size(), QImage.Format_ARGB32)
        self.image = self.CvToQimage(img)
        image_draw.scaled(new_size)
        self.image_draw = image_draw
        self.check = True
        self.update()
        return True

    def resizeImage(self, image, new_size=None):
        if new_size is None:
            new_image = QImage(QSize(self.image_size_x, self.image_size_y), QImage.Format_RGB32)
        else:
            new_image = QImage(QSize(new_size), QImage.Format_RGB32)

        new_image.fill(qRgb(255, 255, 255))
        painter = QPainter(new_image)
        image = self.CvToQimage(image)
        painter.drawImage(QPoint(0, 0), image)
        self.image = new_image

    def resizeEvent(self, event):
        if self.open:
            if self.currentWindowSize()[0] != self.image_size_x \
                    or self.currentWindowSize()[1] != self.image_size_y:
                img = cv.resize(self.QimageToCv(self.image), (self.image_size_x, self.image_size_y))
            else:
                img = cv.resize(self.QimageToCv(self.image), (self.currentWindowSize()))

            self.image = self.CvToQimage(img)
        else:
            pixmap = QPixmap()
            pixamp2 = pixmap.fromImage(self.image.copy().scaled(self.image_size_x, self.image_size_y,
                                                                Qt.IgnoreAspectRatio,
                                                                Qt.SmoothTransformation))
            self.image_copy = self.image.copy()
            self.image = pixamp2.toImage()

        pixmap = QPixmap()
        pixamp2 = pixmap.fromImage(
            self.image_draw.copy().scaled(self.image_size_x, self.image_size_y,
                                          Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        self.image_copy = self.image.copy()
        self.image_draw = pixamp2.toImage()
        self.update()

        super(ScribbleArea, self).resizeEvent(event)

    def resizeImageDraw(self, image, new_size=None):
        pixmap = QPixmap()
        if new_size is None:
            pixamp2 = pixmap.fromImage(
                image.copy().scaled(self.image_size_x, self.image_size_y,
                                    Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        else:
            width, height = self.currentWindowSize()
            pixamp2 = pixmap.fromImage(
                image.copy().scaled(width, height,
                                    Qt.IgnoreAspectRatio, Qt.SmoothTransformation))

        self.image_copy = self.image.copy()

        self.image_draw = pixamp2.toImage()
        self.update()

    def saveImage(self, file_name=None, file_format=None):
        front_image = self.QimageToPil(self.image_draw).convert("RGBA")
        background = self.QimageToPil(self.image).convert("RGBA")
        width = (background.width - front_image.width) // 2
        height = (background.height - front_image.height) // 2
        background.paste(front_image, (width, height), front_image)
        visible_image = self.PilToQimage(background)
        self.resizeImage(visible_image)

        if None != (file_name and file_format):
            if visible_image.save(file_name, file_format):
                return True
            return False

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        dirty_rect = event.rect()
        painter.drawImage(dirty_rect, self.CvToQimage(self.image), dirty_rect)
        painter.drawImage(dirty_rect, self.image_draw, dirty_rect)
        self.update()
        if self.pressed_button == "paint":
            self.draw = True
            painter.drawImage(dirty_rect, self.image_draw, dirty_rect)

        if self.pressed_button == "marquee":
            painter.setPen(QPen(Qt.black, 1, Qt.DotLine))
            painter.drawImage(dirty_rect, self.image_draw, dirty_rect)
            if not self.begin.isNull() and not self.end.isNull():
                if self.begin.x() < self.end.x():
                    self.shape = QRect(self.begin, self.end)
                else:
                    self.shape = QRect(self.end, self.begin)
                # self.coords = self.shape.getCoords()
                # painter.drawRect(self.shape.normalized())
                painter.drawRect(QRect(self.begin, self.end).normalized())

    def mousePressEvent(self, event):
        self.makeUndoCommand()
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
                self.pen_width, Qt.SolidLine))
            painter.setBrush(QColor(40, 50, 20, 240))
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()

            self.update()
            self.check = True

        if self.pressed_button == "marquee":
            self.end = event.pos()
            self.update()
            super().mouseMoveEvent(event)

        if self.pressed_button == "transparent":
            painter = QPainter(self.image_draw)
            r = QRect(QPoint(), self.rubber_width * QSize())
            r.moveCenter(event.pos())
            painter.save()
            painter.setCompositionMode(QPainter.CompositionMode_Clear)
            painter.eraseRect(r)
            painter.restore()
            painter.end()
            self.last_point = event.pos()
            self.update()

        elif self.pressed_button == 'all image':
            painters = [QPainter(self.image), QPainter(self.image_draw)]
            for painter in painters:
                painter.setPen(QPen(QColor(255, 255, 255, 255), self.rubber_width, Qt.SolidLine))
                painter.setBrush(QColor(40, 50, 20, 240))
                painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()
            self.update()
        self.check = True

    def mouseReleaseEvent(self, event):
        pass

    def penColor(self, obj_photoshop_editor, obj1):
        color_dialog = QColorDialog(self)
        color_dialog.setWindowIcon(QIcon('../content/photoshop.png'))
        self.color_pen = color_dialog.getColor().getRgb()
        obj_photoshop_editor.paint()

    def toolWidth(self, obj_photoshop_editor, obj1, tool: str):
        if tool == 'pen':
            num, ok = QInputDialog.getInt(self, f'{tool.title()} width', f'Choose the {tool} width',
                                          0, 1, 30)
            if ok:
                self.pen_width = num
                obj_photoshop_editor.paint()

        elif tool == 'rubber':
            num, ok = QInputDialog.getInt(self, f'{tool.title()} width', f'Choose the {tool} width',
                                          0, 1, 50)
            if ok:
                self.rubber_width = num
                if self.pressed_button == ('transparent' or 'all image'):
                    obj_photoshop_editor.eraser(self.pressed_button)
                else:
                    obj_photoshop_editor.eraser('all image')

    def makeUndoCommand(self):
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

    def photoshopObj(self, photoshop_obj):
        self.photoshop_obj = photoshop_obj
