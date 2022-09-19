from turtle import delay

from PyQt5.QtCore import QSize, Qt, QPoint
from PyQt5.QtGui import QImage, QColor, QPainter, qRgb, QIcon
from PyQt5.QtWidgets import QUndoCommand, QWidget, QDialog, QDialogButtonBox, QVBoxLayout, QLabel, QHBoxLayout
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage
from PyQt5.QtCore import QRect

cropped = QImage()


class Edit():
    def __init__(self):
        super(MovePicrute).__init__()

    def undo(self, obj):
        undo = UndoCommand(obj.scribble_area)
        undo.undo()
        obj.scribble_area.undo_stack.undo()
        obj.scribble_area.update()

    def redo(self, obj):
        obj.scribble_area.undo_stack.redo()
        redo = UndoCommand(obj.scribble_area)
        redo.redo()

    def cut(self, obj):
        painter = QPainter(obj.scribble_area.image)
        image2 = QImage(100, 100, QImage.Format_RGB32)
        image2.fill(qRgb(255, 255, 255))
        painter.drawImage(obj.scribble_area.shape, image2)
        obj.scribble_area.update()

    def copy(self, obj):
        global cropped
        cropped = obj.scribble_area.image.copy(obj.scribble_area.shape)

    def paste(self, obj):
        band = MovePicrute(obj.scribble_area)
        band.adjustSize()

    def clear_screen(self, obj):
        obj.scribble_area.image = QImage(self.size(), QImage.Format_ARGB32)
        new_size = obj.scribble_area.image.size().expandedTo(obj.scribble_area.size())
        obj.scribble_area.resizeImage(obj.scribble_area.image, QSize(new_size))

        obj.scribble_area.image_draw = QImage(self.size(), QImage.Format_ARGB32)
        new_size = obj.scribble_area.image_draw.size().expandedTo(obj.scribble_area.size())
        obj.scribble_area.resizeImage(obj.scribble_area.image_draw, QSize(new_size))

        obj.scribble_area.update()

    def keyboard_shortcuts(self, obj):
        KeyShortcut().exec()


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
        super(MovePicrute, self).__init__(parent)
        self.draggable = True
        self.dragging_threshold = 5
        self.mouse_press_pos = None
        self.mouse_move_pos = None
        self.borderRadius = 5
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
            self.mouse_press_pos = event.globalPos()
            self.mouse_move_pos = event.globalPos() - self.pos()

        super(MovePicrute, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.draggable and event.buttons() & QtCore.Qt.RightButton:
            global_pos = event.globalPos()
            self.moved = global_pos - self.mouse_press_pos
            if self.moved.manhattanLength() > self.dragging_threshold:
                diff = global_pos - self.mouse_move_pos
                self.move(diff)
                self.mouse_move_pos = global_pos - self.pos()

        super(MovePicrute, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.mouse_press_pos is not None:
            if event.button() == QtCore.Qt.RightButton:
                self.moved = event.globalPos() - self.mouse_press_pos
                if self.moved.manhattanLength() > self.dragging_threshold:
                    event.ignore()
                self.mouse_press_pos = None
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

class KeyShortcut(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Keyboard shortcuts")
        self.setWindowIcon(QIcon('../content/photoshop.png'))
        self.setFixedSize(400, 410)

        layout_options = QVBoxLayout(self)
        layout_shortcuts = QVBoxLayout(self)
        layout = QHBoxLayout(self)
        dictionary_shortcuts = {'New': 'Ctrl+N', 'Open': 'Ctrl+O', 'Save': 'Ctrl+S',
                                'Save As': 'Ctrl+Shift+S', 'Print': 'Ctrl+P', 'Close': 'Ctrl+W',
                                'Undo': 'Ctrl+Z', 'Redo': 'Ctrl+Y', 'Cut': 'Ctrl+X', 'Copy': 'Ctrl+C',
                                'Paste': 'Ctrl+V', 'Clear screen': 'Ctrl+L',
                                'Keyboard shortcuts': 'Ctrl+K', 'Image size': 'Ctrl+Alt+I',
                                'Canvas size': 'Ctrl+Alt+C', 'Rotate left': 'Shift+Ctrl+L',
                                'Rotate right': 'Shift+Ctrl+R', 'Blur': 'Shift+Ctrl+B',
                                'Noise': 'Shift+Ctrl+N', 'Twirling spirals': 'Shift+Ctrl+P',
                                'Pixelate': 'Shift+Ctrl+P', 'Help': 'Ctrl+H', 'Documentation': 'Ctrl+D'}

        y = 0
        myFont = QtGui.QFont()
        myFont.setBold(True)
        for key in dictionary_shortcuts.keys():
            label = QLabel(self)
            label.setText(key)
            label.move(50, y)
            label.setFont(myFont)
            layout_options.addWidget(label)
            y += 20

        y = 4
        for value in dictionary_shortcuts.values():
            label = QLabel(self)
            label.setText(value)
            label.move(200, y)
            layout_shortcuts.addWidget(label)
            y += 17

        layout.addLayout(layout_options)
        layout.addLayout(layout_shortcuts)

        self.setLayout(layout)
    def accept(self):
        self.obj.bold = self.is_bold
        self.obj.italic = self.is_italic
        self.obj.underline = self.is_underline
        self.obj.text = self.text.text()
        self.obj.width_text = self.is_size
        self.close()