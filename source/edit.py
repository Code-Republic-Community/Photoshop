from PyQt5 import QtWidgets, QtCore, QtGui

CROPPED_IMAGE = QtGui.QImage()
CROPPED_DRAW_IMAGE = QtGui.QImage


class Edit:
    def __init__(self):
        super(MovePicture).__init__()

    @classmethod
    def undo(cls, photoshop_obj):
        photoshop_obj.is_clicked_move = False
        undo = UndoCommand(photoshop_obj.scribble_area)
        undo.undo()
        photoshop_obj.scribble_area.undo_stack.undo()
        photoshop_obj.scribble_area.update()

    @classmethod
    def redo(cls, photoshop_obj):
        photoshop_obj.is_clicked_move = False
        photoshop_obj.scribble_area.undo_stack.redo()
        redo = UndoCommand(photoshop_obj.scribble_area)
        redo.redo()

    @classmethod
    def cut(cls, photoshop_obj):
        photoshop_obj.is_clicked_move = False
        image = QtGui.QImage(100, 100, QtGui.QImage.Format_RGB32)
        image.fill(QtGui.qRgb(255, 255, 255))

        painter = QtGui.QPainter(photoshop_obj.scribble_area.image)
        painter.drawImage(photoshop_obj.scribble_area.shape, image)

        painter_draw = QtGui.QPainter(photoshop_obj.scribble_area.image_draw)
        painter_draw.drawImage(photoshop_obj.scribble_area.shape, image)
        photoshop_obj.scribble_area.check = True

        photoshop_obj.scribble_area.update()

    @classmethod
    def copy(cls, photoshop_obj):
        photoshop_obj.is_clicked_move = False
        global CROPPED_IMAGE, CROPPED_DRAW_IMAGE
        CROPPED_IMAGE = photoshop_obj.scribble_area.image.copy(photoshop_obj.scribble_area.shape)
        CROPPED_DRAW_IMAGE = photoshop_obj.scribble_area.image_draw.copy(photoshop_obj.scribble_area.shape)
        CROPPED_IMAGE = photoshop_obj.scribble_area.merge_two_images(CROPPED_DRAW_IMAGE, CROPPED_IMAGE)
        photoshop_obj.scribble_area.check = True

    @classmethod
    def paste(cls, photoshop_obj):
        photoshop_obj.is_clicked_move = False
        photoshop_obj.move_text()
        band = MovePicture(photoshop_obj, photoshop_obj.scribble_area)
        band.adjustSize()
        photoshop_obj.scribble_area.check = True

    @classmethod
    def clear_screen(cls, photoshop_obj):
        photoshop_obj.scribble_area.image_draw.fill(QtCore.Qt.transparent)

        photoshop_obj.scribble_area.resize_image_draw(photoshop_obj.scribble_area.image, 'image')
        photoshop_obj.scribble_area.image.fill(QtGui.qRgb(255, 255, 255))

        photoshop_obj.scribble_area.resize_image_draw(photoshop_obj.scribble_area.image_draw, 'image_draw')
        photoshop_obj.scribble_area.check = False

        photoshop_obj.scribble_area.update()

    @classmethod
    def keyboard_shortcuts(cls, photoshop_obj):
        photoshop_obj.is_clicked_move = False
        KeyShortcut().exec()


class UndoCommand(QtWidgets.QUndoCommand):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.m_prev_image = parent.image_draw.copy()
        self.m_curr_image = parent.image_draw.copy()

    def undo(self):
        self.m_curr_image = self.parent.image_draw.copy()
        self.parent.image_draw = self.m_prev_image
        self.parent.update()

    def redo(self):
        self.parent.image_draw = self.m_curr_image
        self.parent.update()


class MovePicture(QtWidgets.QWidget):
    def __init__(self, photoshop_obj, parent=None):
        super(MovePicture, self).__init__(parent)
        self.photoshop_obj = photoshop_obj
        self.draggable = True
        self.dragging_threshold = 5
        self.mouse_press_pos = None
        self.mouse_move_pos = None
        self.border_radius = 5
        self.moved = QtCore.QPoint()
        self.parent = parent

        self.setWindowFlags(QtCore.Qt.SubWindow)

        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        self.label = QtWidgets.QLabel(self)
        self.rect = self.label.rect()
        self.label.setStyleSheet('border-style:transparent; background-color: transparent')
        layout.addWidget(self.label)
        self.rectangle = QtCore.QRect()

        pixmap = QtGui.QPixmap.fromImage(CROPPED_IMAGE)
        self.label.setPixmap(pixmap)
        self.band = QtWidgets.QRubberBand(
            QtWidgets.QRubberBand.Rectangle, self)
        self.rect = self.band.rect().getRect()
        self.band.show()
        self.show()

    def resizeEvent(self, event):
        self.band.resize(self.size())

    def paintEvent(self, event):
        window_size = self.size()
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        painter.drawRoundedRect(0, 0, window_size.width(), window_size.height(),
                                self.border_radius, self.border_radius)
        painter.end()

        if not self.photoshop_obj.is_clicked_move:
            painter = QtGui.QPainter(self.parent.image_draw)
            global CROPPED_IMAGE
            painter.drawImage(self.geometry(), CROPPED_IMAGE)
            self.parent.update()
            self.hide()

    def mousePressEvent(self, event):
        if self.draggable and event.button() == QtCore.Qt.LeftButton:
            self.mouse_press_pos = event.globalPos()
            self.mouse_move_pos = event.globalPos() - self.pos()

        super(MovePicture, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.draggable and event.buttons() & QtCore.Qt.LeftButton:
            global_pos = event.globalPos()
            self.moved = global_pos - self.mouse_press_pos
            if self.moved.manhattanLength() > self.dragging_threshold:
                diff = global_pos - self.mouse_move_pos
                self.move(diff)
                self.mouse_move_pos = global_pos - self.pos()

        super(MovePicture, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.mouse_press_pos is not None:
            if event.button() == QtCore.Qt.RightButton:
                self.moved = event.globalPos() - self.mouse_press_pos
                if self.moved.manhattanLength() > self.dragging_threshold:
                    event.ignore()
                self.mouse_press_pos = None
        super(MovePicture, self).mouseReleaseEvent(event)


class KeyShortcut(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Keyboard shortcuts')
        self.setWindowIcon(QtGui.QIcon('../content/logo.png'))
        self.setFixedSize(400, 650)
        self.horizontal_layout_2 = QtWidgets.QHBoxLayout(self)
        self.horizontal_layout_2.setObjectName('horizontalLayout_2')
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.setObjectName('horizontalLayout')
        self.vertical_layout_4 = QtWidgets.QVBoxLayout(self)
        self.vertical_layout_4.setObjectName('verticalLayout_4')
        self.horizontal_layout.addLayout(self.vertical_layout_4)
        self.vertical_layout_5 = QtWidgets.QVBoxLayout(self)
        self.vertical_layout_5.setObjectName('verticalLayout_5')
        self.horizontal_layout.addLayout(self.vertical_layout_5)
        self.horizontal_layout_2.addLayout(self.horizontal_layout)
        self.setStyleSheet("background:#686868")

        layout = QtWidgets.QHBoxLayout(self)
        dictionary_shortcuts = {'New': 'Ctrl+N', 'Open': 'Ctrl+O', 'Save': 'Ctrl+S',
                                'Save As': 'Ctrl+Shift+S', 'Print': 'Ctrl+P', 'Close': 'Ctrl+W',
                                'Undo': 'Ctrl+Z', 'Redo': 'Ctrl+Y', 'Cut': 'Ctrl+X',
                                'Copy': 'Ctrl+C', 'Paste': 'Ctrl+V', 'Clear screen': 'Ctrl+L',
                                'Keyboard shortcuts': 'Ctrl+K', 'Image size': 'Ctrl+Alt+I',
                                'Canvas size': 'Ctrl+Alt+C', 'Rotate left': 'Shift+Ctrl+L',
                                'Rotate right': 'Shift+Ctrl+R', 'Blur': 'Shift+Ctrl+B',
                                'Noise': 'Shift+Ctrl+N', 'Twirling spirals': 'Shift+Ctrl+P',
                                'Pixelate': 'Shift+Ctrl+P', 'Help': 'Ctrl+H',
                                'Documentation': 'Ctrl+D'}

        my_font = QtGui.QFont()
        my_font.setBold(True)

        for key in dictionary_shortcuts.keys():
            label = QtWidgets.QLabel(self)
            label.setText(key)
            label.setFont(my_font)
            label.setStyleSheet("color:white")
            self.vertical_layout_4.addWidget(label)

        for value in dictionary_shortcuts.values():
            label = QtWidgets.QLabel(self)
            label.setText(value)
            label.setStyleSheet("color:white")
            self.vertical_layout_5.addWidget(label)

        layout.addLayout(self.vertical_layout_4)
        layout.addLayout(self.vertical_layout_5)

        self.setLayout(self.horizontal_layout_2)
