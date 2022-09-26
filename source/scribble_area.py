import io
from PyQt5 import QtWidgets, QtCore, QtGui
import numpy as np
import cv2 as cv
import PIL
import edit
import buttons


class ScribbleArea(QtWidgets.QWidget):
    def __init__(self):
        super(ScribbleArea, self).__init__()
        self.setAttribute(QtCore.Qt.WA_StaticContents)
        self.photoshop_obj = None
        self.image_draw = QtGui.QImage(self.size(), QtGui.QImage.Format_ARGB32)
        self.image = QtGui.QImage(self.size(), QtGui.QImage.Format_ARGB32)
        self.image.fill(QtGui.qRgb(255, 255, 255))
        self.image_width = 900
        self.image_height = 600
        self.buttons = buttons.Buttons()
        self.pressed_button = None
        self.last_point = QtCore.QPoint()
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
        self.undo_stack = QtWidgets.QUndoStack(self)
        self.undo_stack.setUndoLimit(20)
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.shape = QtCore.QRect()
        self.update()
        self.rubber_width = 10
        self.open = False
        self.rotated = 'None'
        self.selected = False

    def get_current_window_size(self):
        return self.width(), self.height()

    def open_image(self, img):
        self.open = True
        new_size = QtCore.QSize(img.shape[0], img.shape[1])
        self.resize_image(img)
        image_draw = QtGui.QImage(self.size(), QtGui.QImage.Format_ARGB32)
        self.image = self.convert_cv_to_q_image(img)
        image_draw.scaled(new_size)
        self.image_draw = image_draw
        self.check = True
        self.update()
        return True

    def resize_image(self, image, new_size=None):
        if new_size is None:
            new_image = QtGui.QImage(QtCore.QSize(self.image_width, self.image_height),
                                     QtGui.QImage.Format_RGB32)
        else:
            new_image = QtGui.QImage(QtCore.QSize(new_size), QtGui.QImage.Format_RGB32)

        new_image.fill(QtGui.qRgb(255, 255, 255))
        painter = QtGui.QPainter(new_image)
        image = self.convert_cv_to_q_image(image)
        painter.drawImage(QtCore.QPoint(0, 0), image)
        self.image = new_image

    def resize_image_draw(self, image, new_size=None):
        pixmap = QtGui.QPixmap()
        if new_size is None:
            pixamp = pixmap.fromImage(
                image.copy().scaled(self.image_width, self.image_height,
                                    QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation))
        else:
            width, height = self.get_current_window_size()
            pixamp = pixmap.fromImage(
                image.copy().scaled(width, height,
                                    QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation))

        self.image_copy = self.image.copy()

        self.image_draw = pixamp.toImage()
        self.update()

    def resizeEvent(self, event):
        if self.open:
            if self.get_current_window_size()[0] > self.image_width \
                    or self.get_current_window_size()[1] > self.image_height:
                img = cv.resize(self.convert_q_image_to_cv(self.image),
                                (self.image_width, self.image_height))
            else:
                img = cv.resize(self.convert_q_image_to_cv(self.image),
                                (self.get_current_window_size()))

            self.image = self.convert_cv_to_q_image(img)
        else:
            pixmap = QtGui.QPixmap()
            pixmap = pixmap.fromImage(self.image.copy().scaled(self.image_width, self.image_height,
                                                               QtCore.Qt.IgnoreAspectRatio,
                                                               QtCore.Qt.SmoothTransformation))
            self.image_copy = self.image.copy()
            self.image = pixmap.toImage()

        pixmap = QtGui.QPixmap()
        pixmap = pixmap.fromImage(
            self.image_draw.copy().scaled(self.image_width, self.image_height,
                                          QtCore.Qt.IgnoreAspectRatio,
                                          QtCore.Qt.SmoothTransformation))
        self.image_copy = self.image.copy()
        self.image_draw = pixmap.toImage()
        self.update()

        super(ScribbleArea, self).resizeEvent(event)

    def save_image(self, file_name=None, file_format=None):
        visible_image = self.merge_two_images(self.image_draw, self.image)
        self.resize_image(visible_image)

        if None is not (file_name and file_format):
            if visible_image.save(file_name, file_format):
                return True
            return False

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        dirty_rect = event.rect()
        painter.drawImage(dirty_rect, self.convert_cv_to_q_image(self.image), dirty_rect)
        painter.drawImage(dirty_rect, self.image_draw, dirty_rect)
        self.update()
        if self.pressed_button == 'paint':
            self.draw = True
            painter.drawImage(dirty_rect, self.image_draw, dirty_rect)

        if self.pressed_button == 'marquee':
            self.selected = False
            painter.setPen(QtGui.QPen(QtCore.Qt.black, 1, QtCore.Qt.DotLine))
            painter.drawImage(dirty_rect, self.image_draw, dirty_rect)
            if not self.begin.isNull() and not self.end.isNull():
                if self.begin.x() < self.end.x():
                    self.shape = QtCore.QRect(self.begin, self.end)
                else:
                    self.shape = QtCore.QRect(self.end, self.begin)
                painter.drawRect(QtCore.QRect(self.begin, self.end).normalized())
                self.selected = True

        if self.pressed_button == 'lasso':
            if not self.begin.isNull() and not self.end.isNull():
                if self.begin.x() < self.end.x():
                    self.shape = QtCore.QRect(self.begin, self.end)
                else:
                    self.shape = QtCore.QRect(self.end, self.begin)

    def mousePressEvent(self, event):
        self.make_undo_command()
        if event.button() == QtCore.Qt.LeftButton:
            self.last_point = event.pos()
            if self.pressed_button == 'eyedropper':
                self.buttons.get_color(self, event.pos().x(), event.pos().y())
            if self.pressed_button == 'marquee':
                self.begin = self.end = event.pos()
                self.update()
                super().mousePressEvent(event)
            if self.pressed_button == 'lasso':
                self.begin = self.end = event.pos()
                self.update()
                super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.pressed_button == 'paint':
            painter = QtGui.QPainter(self.image_draw)
            painter.setPen(QtGui.QPen(
                QtGui.QColor(self.color_pen[0], self.color_pen[1],
                             self.color_pen[2], self.color_pen[3]),
                self.pen_width, QtCore.Qt.SolidLine))
            painter.setBrush(QtGui.QColor(40, 50, 20, 240))
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()

            self.update()
            self.check = True

        if self.pressed_button == 'marquee':
            self.end = event.pos()
            self.update()
            super().mouseMoveEvent(event)

        if self.pressed_button == 'lasso':
            painter = QtGui.QPainter(self.image_draw)
            painter.setPen(QtGui.QPen(
                QtGui.QColor(self.color_pen[0], self.color_pen[1],
                             self.color_pen[2], self.color_pen[3]),
                self.pen_width, QtCore.Qt.SolidLine))
            painter.setBrush(QtGui.QColor(40, 50, 20, 240))
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()
            self.end = event.pos()
            super().mouseMoveEvent(event)

            self.update()
            self.check = True

        if self.pressed_button == 'transparent':
            painter = QtGui.QPainter(self.image_draw)
            rubber = QtCore.QRect(QtCore.QPoint(), self.rubber_width * QtCore.QSize())
            rubber.moveCenter(event.pos())
            painter.save()
            painter.setCompositionMode(QtGui.QPainter.CompositionMode_Clear)
            painter.eraseRect(rubber)
            painter.restore()
            painter.end()
            self.last_point = event.pos()
            self.update()

        elif self.pressed_button == 'all image':
            painters = [QtGui.QPainter(self.image), QtGui.QPainter(self.image_draw)]
            for painter in painters:
                painter.setPen(QtGui.QPen(QtGui.QColor(255, 255, 255, 255),
                                          self.rubber_width, QtCore.Qt.SolidLine))
                painter.setBrush(QtGui.QColor(40, 50, 20, 240))
                painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()
            self.update()
        self.check = True

    def mouseReleaseEvent(self, event):
        pass

    def set_pen_color(self, obj_photoshop_editor):
        color_dialog = QtWidgets.QColorDialog(self)
        color_dialog.setWindowIcon(QtGui.QIcon('../content/photoshop.png'))
        self.color_pen = color_dialog.getColor().getRgb()
        obj_photoshop_editor.paint()

    def set_tool_width(self, obj_photoshop_editor, tool: str):
        if tool == 'pen':
            num, accept = QtWidgets.QInputDialog.getInt(self, f'{tool.title()} width',
                                                    f'Choose the {tool} width',
                                                    0, 1, 50)
            if accept:
                self.pen_width = num
                obj_photoshop_editor.paint()

        elif tool == 'rubber':
            num, accept = QtWidgets.QInputDialog.getInt(self, f'{tool.title()} width',
                                                    f'Choose the {tool} width',
                                                    0, 1, 50)
            if accept:
                self.rubber_width = num
                if self.pressed_button == ('transparent' or 'all image'):
                    obj_photoshop_editor.eraser(self.pressed_button)
                else:
                    obj_photoshop_editor.eraser('all image')

    def make_undo_command(self):
        self.undo_stack.push(edit.UndoCommand(self))

    @classmethod
    def convert_q_image_to_cv(cls, img: QtGui.QImage):
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QBuffer.ReadWrite)
        img.save(buffer, 'PNG')
        img_stream = io.BytesIO((buffer.data()))
        img = cv.imdecode(np.frombuffer(img_stream.read(), np.uint8), 1)
        return img

    @classmethod
    def convert_cv_to_q_image(cls, img):
        if not isinstance(img, QtGui.QImage):
            is_success, buffer = cv.imencode('.jpg', img)
            io_buf = io.BytesIO(buffer)
            q_img = QtGui.QImage()
            q_img.loadFromData(io_buf.getvalue())
            return q_img
        return img

    @classmethod
    def q_image_to_pil(cls, img):
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QBuffer.ReadWrite)
        img.save(buffer, 'PNG')
        pil_im = PIL.Image.open(io.BytesIO(buffer.data()))
        return pil_im

    @classmethod
    def pil_to_q_image(cls, img):
        bytes_img = io.BytesIO()
        img.save(bytes_img, format='PNG')
        q_img = QtGui.QImage()
        q_img.loadFromData(bytes_img.getvalue())
        return q_img

    def get_photoshop_obj(self, photoshop_obj):
        self.photoshop_obj = photoshop_obj

    def merge_two_images(self, image1, image2):
        front_image = self.q_image_to_pil(image1).convert('RGBA')
        background = self.q_image_to_pil(image2).convert('RGBA')
        width = (background.width - front_image.width) // 2
        height = (background.height - front_image.height) // 2
        background.paste(front_image, (width, height), front_image)
        visible_image = self.pil_to_q_image(background)
        return visible_image
