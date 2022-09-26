from PyQt5.QtCore import QSize, Qt, QPoint
from PyQt5.QtGui import QImage, QColor, QPainter, qRgb, QIcon, QPen, QFont
from PyQt5.QtWidgets import QUndoCommand, QWidget, QDialog, QDialogButtonBox, QVBoxLayout, QLabel, QHBoxLayout
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage
from PyQt5.QtCore import QRect
cropped_image = QImage()
cropped_drawimage = QImage



class Edit():
    def __init__(self):
        super(MovePicrute).__init__()

    def undo(self, obj):
        obj.is_clicked_move = False
        undo = UndoCommand(obj.scribble_area)
        undo.undo()
        obj.scribble_area.undo_stack.undo()
        obj.scribble_area.update()

    def redo(self, obj):
        obj.is_clicked_move = False
        obj.scribble_area.undo_stack.redo()
        redo = UndoCommand(obj.scribble_area)
        redo.redo()

    def cut(self, obj):
        obj.is_clicked_move = False
        image = QImage(100, 100, QImage.Format_RGB32)
        image.fill(qRgb(255, 255, 255))

        painter = QPainter(obj.scribble_area.image)
        painter.drawImage(obj.scribble_area.shape, image)

        painter_draw = QPainter(obj.scribble_area.image_draw)
        painter_draw.drawImage(obj.scribble_area.shape, image)
        obj.scribble_area.check = True

        obj.scribble_area.update()

    def copy(self, obj):
        obj.is_clicked_move = False
        global cropped_image, cropped_drawimage
        cropped_image = obj.scribble_area.image.copy(obj.scribble_area.shape)
        cropped_drawimage = obj.scribble_area.image_draw.copy(obj.scribble_area.shape)
        cropped_image = obj.scribble_area.merge_two_images(cropped_drawimage,cropped_image)
        obj.scribble_area.check = True

    def paste(self, obj):
        obj.is_clicked_move = False
        obj.moveText()
        band = MovePicrute(obj, obj.scribble_area)
        band.adjustSize()
        obj.scribble_area.check = True

    def clearScreen(self, obj):

        obj.scribble_area.image_draw = QImage(1000,1000, QImage.Format_ARGB32)

        #obj.scribble_area.image = QImage(obj.scribble_area.size(), QImage.Format_ARGB32)
        new_size = obj.scribble_area.image.size().expandedTo(obj.scribble_area.size())
        obj.scribble_area.resizeImage(obj.scribble_area.image)
        obj.scribble_area.image.fill(qRgb(255,255,255))

        new_size = obj.scribble_area.image_draw.size().expandedTo(obj.scribble_area.size())
        obj.scribble_area.resizeImage(obj.scribble_area.image_draw)
        obj.scribble_area.check = False

        obj.scribble_area.update()

    def keyboardShortcuts(self, obj):
        obj.is_clicked_move = False
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
    def __init__(self, photoshop_obj, parent=None):
        super(MovePicrute, self).__init__(parent)
        self.photoshop_obj = photoshop_obj
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

        pixmap01 = QtGui.QPixmap.fromImage(cropped_image)
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
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.drawRoundedRect(0, 0, window_size.width(), window_size.height(),
                           self.borderRadius, self.borderRadius)
        painter.end()

        if not self.photoshop_obj.is_clicked_move:
            self.x_pos = self.pos()
            self.y_pos = self.geometry()
            painter = QPainter(self.parent.image_draw)
            global cropped_image
            painter.drawImage(self.y_pos, cropped_image)
            self.parent.update()
            self.hide()

    def mousePressEvent(self, event):
        if self.draggable and event.button() == QtCore.Qt.LeftButton:
            self.mouse_press_pos = event.globalPos()
            self.mouse_move_pos = event.globalPos() - self.pos()

        super(MovePicrute, self).mousePressEvent(event)


    def mouseMoveEvent(self, event):
        if self.draggable and event.buttons() & QtCore.Qt.LeftButton:
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



class KeyShortcut(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Keyboard shortcuts")
        self.setWindowIcon(QIcon('../content/photoshop.png'))
        self.setFixedSize(400, 650)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

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

        myFont = QtGui.QFont()
        myFont.setBold(True)
        for key in dictionary_shortcuts.keys():
            label = QLabel(self)
            label.setText(key)
            label.setFont(myFont)
            self.verticalLayout_4.addWidget(label)

        for value in dictionary_shortcuts.values():
            label = QLabel(self)
            label.setText(value)
            self.verticalLayout_5.addWidget(label)

        layout.addLayout(self.verticalLayout_4)
        layout.addLayout(self.verticalLayout_5)

        self.setLayout(self.horizontalLayout_2)


