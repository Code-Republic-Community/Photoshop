import io
import sys

from PyQt5.QtCore import QPoint, Qt, QSize, QBuffer
from PyQt5.QtGui import QImage, qRgb, QPainter, QPen, QColor, QIcon, QTextCharFormat, QFont
from PyQt5.QtWidgets import QWidget, QColorDialog, QInputDialog, QUndoStack, QApplication
import numpy as np
import cv2 as cv
from source.edit import UndoCommand
from source.buttons import Buttons
from source.buttons import TextTypeCheckbox


class ScribbleArea(QWidget):
    def __init__(self):
        super(ScribbleArea, self).__init__()

        self.setAttribute(Qt.WA_StaticContents)
        self.image = QImage()
        self.buttons = Buttons()
        self.pressed_button = None
        newSize = self.image.size().expandedTo(self.size())
        self.resizeImage(self.image, QSize(newSize))
        self.update()
        self.a = ''
        self.lastPoint = QPoint()
        self.check = False
        self.color_pen = (0, 0, 0, 255)
        self.color_text = (0, 0, 0, 255)
        self.width_pen = 3
        self.width_text = 15
        self.bold = False
        self.italic = False
        self.underline = False
        self.text = None
        self.image_width = 0
        self.image_height = 0
        self.mUndoStack = QUndoStack(self)
        self.mUndoStack.setUndoLimit(20)
        # self.mUndoStack.canUndo()
        # self.mUndoStack.canRedo()

    def is_pressed(self, value):
        self.pressed = value
        return self.pressed

    def current_window_size(self):
        return self.width(), self.height()


    def openImage(self, img):
        # newSize = img.size().expandedTo(self.size())
        newSize = QSize(img.shape[0], img.shape[1])
        self.resizeImage(img, newSize)
        self.image = self.cv_to_qimage(img)
        self.update()
        return True

    def resizeImage(self, image, newSize):
        # if image.size() == newSize:
        # return

        newImage = QImage(newSize, QImage.Format_RGB32)
        newImage.fill(qRgb(255, 255, 255))
        painter = QPainter(newImage)
        image = self.cv_to_qimage(image)
        painter.drawImage(QPoint(0, 0), image)
        self.image = newImage

    def resizeEvent(self, event):
        # if self.width() > self.image.width() or self.height() > self.image.height():
        # newWidth = max(self.width() + 128, self.image.width())
        # newHeight = max(self.height() + 128, self.image.height())
        # self.resizeImage(self.image, QSize(self.width(), self.height()))
        img = cv.resize(self.qimage_to_cv(self.image), self.current_window_size())
        self.openImage(img)
        self.image = self.cv_to_qimage(img)
        self.update()

        super(ScribbleArea, self).resizeEvent(event)

    def foo(self):
        return ScribbleArea()

    def saveImage(self, fileName, fileFormat):
        visibleImage = self.image
        self.resizeImage(visibleImage, self.size())

        if visibleImage.save(fileName, fileFormat):
            return True
        return False


    def paintEvent(self, event):
        painter = QPainter(self)
        dirtyRect = event.rect()
        painter.drawImage(dirtyRect, self.cv_to_qimage(self.image), dirtyRect)
        myFont = QFont()
        myFont.setBold(self.bold)
        myFont.setItalic(self.italic)
        myFont.setUnderline(self.underline)
        myFont.setPointSize(self.width_text)
        painter.setFont(myFont)
        painter.drawText(350, 280, self.text)

    def mousePressEvent(self, event):
        self.make_undo_command()
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()
            # self.buttons.pos_x = event.pos().x()
            # self.buttons.pos_y = event.pos().y()
            if self.pressed_button == 'eyedropper':
                self.buttons.get_color(self, event.pos().x(), event.pos().y())
            if self.pressed_button == 'type':
                pass

    def mouseMoveEvent(self, event):
        if self.pressed_button == 'paint':
            painter = QPainter(self.image)
            painter.setPen(QPen(
                QColor(self.color_pen[0], self.color_pen[1], self.color_pen[2], self.color_pen[3]),
                self.width_pen, Qt.SolidLine))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()
            self.check = True

    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            pass

    def pen_color(self):
        color_dialog = QColorDialog(self)
        color_dialog.setWindowIcon(QIcon('../content/photoshop.png'))
        self.color_pen = color_dialog.getColor().getRgb()

    def pen_width(self):
        num, ok = QInputDialog.getInt(self, "Pen width", "Choose the pen width")
        self.width_pen = num

    def text_write(self):
        #text, done1 = QInputDialog.getText(self, 'Write text', '')
        #self.text = text
        if self.bold:
            pass
        if self.italic:
            pass
        if self.underline:
            pass


    def text_type(self):
        TextTypeCheckbox(self).exec()


    def text_width(self):
        num, ok = QInputDialog.getInt(self, "Text width", "Choose the text width")
        self.width_text = num

    def text_color(self):
        self.color_text = QColorDialog().getColor().getRgb()

    def make_undo_command(self):
        self.mUndoStack.push(UndoCommand(self))

    def qimage_to_cv(self, img: QImage):
        buffer = QBuffer()
        buffer.open(QBuffer.ReadWrite)
        img.save(buffer, "PNG")
        img_stream = io.BytesIO((buffer.data()))
        img = cv.imdecode(np.frombuffer(img_stream.read(), np.uint8), 1)
        return img

    def cv_to_qimage(self, img):
        if not isinstance(img, QImage):
            is_success, buffer = cv.imencode(".jpg", img)
            io_buf = io.BytesIO(buffer)
            qimg = QImage()
            qimg.loadFromData(io_buf.getvalue())
            return qimg
        return img
