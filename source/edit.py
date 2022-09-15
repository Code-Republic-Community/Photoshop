from turtle import delay

from PyQt5.QtCore import QSize, Qt, QPoint
from PyQt5.QtGui import QImage, QColor, QPainter, qRgb
from PyQt5.QtWidgets import QUndoCommand, QWidget
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage
from PyQt5.QtCore import QRect

cropped = QImage()


class Edit():
    def __init__(self):
        super(MovePicrute).__init__()

    def undo(self, object):
        self.undo = UndoCommand(object.scribbleArea)
        self.undo.undo()
        object.scribbleArea.mUndoStack.undo()
        object.scribbleArea.update()

    def redo(self, obj):
        obj.scribbleArea.mUndoStack.redo()
        from scribble_area import ScribbleArea
        obj = ScribbleArea()
        self.redo = UndoCommand(obj)
        self.redo.redo()

    def cut(self, obj):
        painter = QPainter(obj.scribbleArea.image)
        image2 = QImage(100, 100, QImage.Format_RGB32)
        image2.fill(qRgb(255, 255, 255))
        painter.drawImage(obj.scribbleArea.shape, image2)
        obj.scribbleArea.update()

    def copy(self, obj):
        global cropped
        cropped = obj.scribbleArea.image.copy(obj.scribbleArea.shape)

    def paste(self, obj):
        self.band = MovePicrute(obj.scribbleArea)
        self.band.adjustSize()

    def clear_screen(self, obj):
        obj.scribbleArea.image = QImage(self.size(), QImage.Format_ARGB32)
        newSize = obj.scribbleArea.image.size().expandedTo(obj.scribbleArea.size())
        obj.scribbleArea.resizeImage(obj.scribbleArea.image, QSize(newSize))

        obj.scribbleArea.image_draw = QImage(self.size(), QImage.Format_ARGB32)
        newSize = obj.scribbleArea.image_draw.size().expandedTo(obj.scribbleArea.size())
        obj.scribbleArea.resizeImage(obj.scribbleArea.image_draw, QSize(newSize))

        obj.scribbleArea.update()

    def keyboard_shortcuts(self):
        pass


class UndoCommand(QUndoCommand):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.mPrevImage = parent.image_draw.copy()
        self.mCurrImage = parent.image_draw.copy()

    def undo(self):
        self.mCurrImage = self.parent.image_draw.copy()
        self.parent.image_draw = self.mPrevImage
        self.parent.update()

    def redo(self):
        self.parent.image_draw = self.mCurrImage
        self.parent.update()


class MovePicrute(QtWidgets.QWidget):
    def __init__(self, parent=None):
        from scribble_area import ScribbleArea
        super(MovePicrute, self).__init__(parent)
        self.draggable = True
        self.dragging_threshold = 5
        self.mousePressPos = None
        self.mouseMovePos = None
        self.borderRadius = 5
        self.step = False
        self.moved = QPoint()
        self.parent = parent

        self.setWindowFlags(QtCore.Qt.SubWindow)
        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        self.label = QtWidgets.QLabel(self)
        self.rect = self.label.rect()
        self.label.setStyleSheet("border-style:transparent; background-color: transparent")
        layout.addWidget(self.label)
        self.rectangle = QRect()

        pixmap01 = QtGui.QPixmap.fromImage(cropped)
        self.label.setPixmap(pixmap01)
        self._band = QtWidgets.QRubberBand(
            QtWidgets.QRubberBand.Rectangle, self)
        self.rect = self._band.rect().getRect()
        self.x_pos = 0
        self.y_pos = 0
        self._band.show()
        self.show()

    def resizeEvent(self, event):
        self._band.resize(self.size())

    def paintEvent(self, event):
        window_size = self.size()
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing, True)
        qp.drawRoundedRect(0, 0, window_size.width(), window_size.height(),
                           self.borderRadius, self.borderRadius)
        qp.end()

    def mousePressEvent(self, event):
        if self.draggable and event.button() == QtCore.Qt.RightButton:
            self.mousePressPos = event.globalPos()
            self.mouseMovePos = event.globalPos() - self.pos()

        super(MovePicrute, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.draggable and event.buttons() & QtCore.Qt.RightButton:
            globalPos = event.globalPos()
            self.moved = globalPos - self.mousePressPos
            if self.moved.manhattanLength() > self.dragging_threshold:
                diff = globalPos - self.mouseMovePos
                self.move(diff)
                self.mouseMovePos = globalPos - self.pos()

        super(MovePicrute, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.mousePressPos is not None:
            if event.button() == QtCore.Qt.RightButton:
                self.moved = event.globalPos() - self.mousePressPos
                if self.moved.manhattanLength() > self.dragging_threshold:
                    event.ignore()
                self.mousePressPos = None
            self.step = True
        super(MovePicrute, self).mouseReleaseEvent(event)

        self.x_pos = self.pos()
        print(self.x_pos)
        self.y_pos = self.geometry()
        print(self.y_pos, type(self.y_pos))
        painter = QPainter(self.parent.image_draw)
        global cropped
        painter.drawImage(self.y_pos, cropped)
        self.parent.update()
        self.hide()
