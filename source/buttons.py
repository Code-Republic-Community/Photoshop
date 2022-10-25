"""This file is responsible for the tool buttons"""

from PyQt5 import QtWidgets, QtCore, QtGui
import PIL
from image import Image


class Buttons(QtWidgets.QMainWindow):
    """This class includes all the functions which are responsible for the actions of the buttons"""

    def __init__(self):
        super().__init__()
        self.image_type = ''

    @classmethod
    def get_color(cls, obj_scribble, pos_x, pos_y):
        img = obj_scribble.image.pixel(pos_x, pos_y)
        color = QtGui.QColor(img).getRgb()
        obj_scribble.color_pen = color
        obj_scribble.photoshop_obj.all_button_white()
        obj_scribble.photoshop_obj.paint()

    @classmethod
    def crop(cls, photoshop_obj):
        if photoshop_obj.scribble_area.selected:
            cropped = photoshop_obj.scribble_area.image.copy(photoshop_obj.scribble_area.shape)
            cropped_img_draw = photoshop_obj.scribble_area.image_draw \
                .copy(photoshop_obj.scribble_area.shape)

            photoshop_obj.scribble_area.image_draw.fill(QtCore.Qt.transparent)
            photoshop_obj.scribble_area.image.fill(QtGui.qRgb(255, 255, 255))

            photoshop_obj.scribble_area.resize_image_draw(photoshop_obj.scribble_area.image, 'image')

            painter = QtGui.QPainter(photoshop_obj.scribble_area.image)
            painter_draw = QtGui.QPainter(photoshop_obj.scribble_area.image_draw)
            painter.drawImage(photoshop_obj.scribble_area.shape, cropped)
            painter_draw.drawImage(photoshop_obj.scribble_area.shape, cropped_img_draw)
            photoshop_obj.scribble_area.check = True

            photoshop_obj.scribble_area.update()

    def image_converter(self, photoshop_obj):
        self.filename = ''
        self.filename, _ = QtWidgets.QFileDialog.getOpenFileName(photoshop_obj,
                                                                 'Open File',
                                                                 QtCore.QDir.currentPath(),
                                                                 'Image files (*.jpg *.png *.gif '
                                                                 '*.svg *.bmp *.jpeg *.jfif)')

        if self.filename != '':
            point_index = self.filename.rindex('.')
            ImgTypeComboBox(self).exec()

            if self.filename.endswith(('png', 'jpg', 'gif', 'bmp', 'jpeg', 'jfif')):
                PIL.Image.open(self.filename).convert('RGB'). \
                    save(f'{self.filename[:point_index + 1]}{self.image_type}')

        photoshop_obj.all_button_white()


class ImgTypeComboBox(QtWidgets.QDialog):
    def __init__(self, buttons_obj):
        super().__init__()
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.buttons_obj = buttons_obj
        layout = QtWidgets.QFormLayout(self)
        self.combo_box = QtWidgets.QComboBox(self)

        img_types = ['jpeg', 'jpg', 'png', 'bmp']
        self.combo_box.addItems(img_types)
        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok
                                                | QtWidgets.QDialogButtonBox.Cancel, self)

        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        button_box.button(QtWidgets.QDialogButtonBox.Ok).setMinimumSize(QtCore.QSize(60, 25))
        button_box.button(QtWidgets.QDialogButtonBox.Ok).setStyleSheet(
            "border-radius:8px;"
            "background:#D600C9;color: white"
        )
        button_box.button(QtWidgets.QDialogButtonBox.Cancel).setMinimumSize(QtCore.QSize(60, 25))
        button_box.button(QtWidgets.QDialogButtonBox.Cancel).setStyleSheet(
            "border-radius:8px;"
            "background: White;color: #D600C9"
        )

        layout.addWidget(self.combo_box)
        layout.addWidget(button_box)

    def accept(self):
        img_type = self.combo_box.currentText()
        self.buttons_obj.image_type = img_type
        self.close()


class MoveText(QtWidgets.QWidget):
    def __init__(self, text, text_width, text_font, text_color, bold, italic, underline,
                 scribble_obj, photoshop_obj, dragable=False):
        super(MoveText, self).__init__(scribble_obj)
        self.draggable = dragable
        self.scribble_obj = scribble_obj
        self.photoshop_obj = photoshop_obj
        self.dragging_threshold = 5
        self.mouse_press_pos = None
        self.mouse_move_pos = None
        self.border_radius = 0
        self.setWindowFlags(QtCore.Qt.SubWindow)
        self.setStyleSheet("background:transparent")
        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(
            QtWidgets.QSizeGrip(self), 0,
            QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        layout.addWidget(
            QtWidgets.QSizeGrip(self), 0,
            QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)

        my_font = QtGui.QFont(text_font)
        my_font.setBold(bold)
        my_font.setItalic(italic)
        my_font.setUnderline(underline)
        my_font.setPointSize(text_width)

        self.label = QtWidgets.QLabel(self)
        self.label.setText(text)
        self.label.setFont(my_font)
        self.label.setStyleSheet(f'color: rgba{text_color}')
        self.label.adjustSize()

        self.band = QtWidgets.QRubberBand(
            QtWidgets.QRubberBand.Rectangle, self)

        self.setGeometry(150, 150, 300, 50)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.show()

    def resizeEvent(self, event):
        self.band.resize(self.size())

    def paintEvent(self, event):
        if not self.photoshop_obj.is_clicked_move or self.photoshop_obj.is_clicked_move \
                and self.scribble_obj.rotated != 'None':
            painter = QtGui.QPainter(self.scribble_obj.image_draw)

            pen = QtGui.QPen(QtGui.QColor(self.scribble_obj.color_text[0],
                                          self.scribble_obj.color_text[1],
                                          self.scribble_obj.color_text[2],
                                          self.scribble_obj.color_text[3]))

            pen.setWidth(10)
            painter.setPen(pen)

            font = QtGui.QFont(self.scribble_obj.text_font)
            font.setBold(self.scribble_obj.bold)
            font.setItalic(self.scribble_obj.italic)
            font.setUnderline(self.scribble_obj.underline)
            font.setPointSize(self.scribble_obj.width_text)
            painter.setFont(font)

            painter.drawText(self.pos().x(), self.pos().y() + self.scribble_obj.width_text,
                             self.scribble_obj.text)
            painter.end()

            self.hide()
            if self.photoshop_obj.is_clicked_move and self.scribble_obj.rotated != 'None':
                Image.rotate(self.photoshop_obj, self.scribble_obj.rotated)

    def mousePressEvent(self, event):
        if self.draggable and event.button() == QtCore.Qt.LeftButton:
            self.mouse_press_pos = event.globalPos()
            self.mouse_move_pos = event.globalPos() - self.pos()

        super(MoveText, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.draggable and event.buttons() & QtCore.Qt.LeftButton:
            global_pos = event.globalPos()
            moved = global_pos - self.mouse_press_pos
            if moved.manhattanLength() > self.dragging_threshold:
                diff = global_pos - self.mouse_move_pos
                self.move(diff)
                self.mouse_move_pos = global_pos - self.pos()
        super(MoveText, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.mouse_press_pos is not None:
            if event.button() == QtCore.Qt.RightButton:
                moved = event.globalPos() - self.mouse_press_pos
                if moved.manhattanLength() > self.dragging_threshold:
                    event.ignore()
                self.mouse_press_pos = None
        super(MoveText, self).mouseReleaseEvent(event)
