from PyQt5 import QtSvg
from PyQt5.QtCore import QPoint, Qt, QSize, QDir
from PyQt5.QtGui import QColor, QIcon, QPen, QPainter, qRgb, QImage, QFont, QIntValidator, QPixmap
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QCheckBox, QDialogButtonBox, QDialog, QHBoxLayout, \
    QLabel, QLineEdit, QPushButton, QColorDialog, QFileDialog, QComboBox, QSizeGrip, QRubberBand, QApplication
import cv2 as cv
import argparse
import numpy as np
import sys
from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import QPainter, QPen, QBrush, QIcon
# import aspose.words as aw
from PIL import Image
from edit import MovePicrute
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM


class Buttons(QMainWindow):
    obj_photoshop = None

    def __init__(self):
        super().__init__()
        self.image_type = ''

    def eyedropper(self, obj):
        global obj_photoshop
        obj_photoshop = obj

    def get_color(self, obj_scribble, pos_x, pos_y):
        img = obj_scribble.image.pixel(pos_x, pos_y)
        color = QColor(img).getRgb()
        obj_scribble.color_pen = color
        obj_photoshop.allButtonWhite()
        obj_scribble.pressed_button = None

    def crop(self, obj):
        cropped = obj.scribble_area.image.copy(obj.scribble_area.shape)
        cropped_imgdr = obj.scribble_area.image_draw.copy(obj.scribble_area.shape)

        obj.scribble_area.image_draw.fill((Qt.transparent))
        obj.scribble_area.image.fill(qRgb(255, 255, 255))

        new_size = obj.scribble_area.image.size().expandedTo(obj.scribble_area.size())
        obj.scribble_area.resizeImage(obj.scribble_area.image)

        painter = QPainter(obj.scribble_area.image)
        painter2 = QPainter(obj.scribble_area.image_draw)
        painter.drawImage(obj.scribble_area.shape, cropped)
        painter2.drawImage(obj.scribble_area.shape, cropped_imgdr)
        obj.scribble_area.check = True

        obj.scribble_area.update()

    def image_converter(self, obj):
        self.filename = ''
        self.filename, _ = QFileDialog.getOpenFileName(obj, "Open File", QDir.currentPath(),
                                                       "Image files (*.jpg *.png *.gif *.svg *.bmp *.jpeg *.jfif)")

        if self.filename != '':
            point_index = self.filename.rindex('.')
            ImgTypeComboBox(self).exec()

            if self.image_type in 'svg':
                if self.filename.endswith(('png', 'jpg', 'gif', 'bmp', 'jpeg', 'jfif')):
                    doc = aw.Document()
                    builder = aw.DocumentBuilder(doc)
                    shape = builder.insert_image(self.filename)
                    save_options = aw.saving.ImageSaveOptions(aw.SaveFormat.SVG)
                    shape.get_shape_renderer().save(f'{self.filename[:point_index + 1]}{self.image_type}', save_options)
                    obj.allButtonWhite()
                    return

            elif self.image_type in ('png', 'bmp', 'jpeg', 'jpg'):
                if self.filename.endswith('svg'):
                    doc = aw.Document()
                    builder = aw.DocumentBuilder(doc)
                    shape = builder.insert_image(self.filename)
                    shape.image_data.save(f'{self.filename[:-3]}{self.image_type}')
                    obj.allButtonWhite()
                    return

                if self.filename.endswith(('png', 'jpg', 'gif', 'bmp', 'jpeg', 'jfif')):
                    Image.open(self.filename).convert('RGB'). \
                        save(f'{self.filename[:point_index + 1]}{self.image_type}')

        obj.allButtonWhite()


class ImgTypeComboBox(QDialog):
    def __init__(self, obj):
        self.obj = obj
        super().__init__()
        self.setFixedSize(250, 120)
        self.setWindowIcon(QIcon('../content/photoshop.png'))

        layout = QVBoxLayout()
        self.combo_box = QComboBox(self)
        img_types = ['jpeg', 'jpg', 'png', 'svg', 'bmp']
        self.combo_box.addItems(img_types)
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)

        layout.addWidget(self.combo_box)
        layout.addWidget(button_box)
        self.setLayout(layout)

        button_box.accepted.connect(self.accept)

    def accept(self):
        type = self.combo_box.currentText()
        self.obj.image_type = type
        self.close()


class TextType(QDialog):
    def __init__(self, obj, text):
        super().__init__()
        self.setWindowTitle("Text Font")
        self.setWindowIcon(QIcon('../content/photoshop.png'))
        self.obj = obj
        self.text = text
        self.font_size = self.text.font()
        self.setFixedSize(0, 0)

        layout = QVBoxLayout()
        checkbox_layout = QHBoxLayout()

        label = QLabel("Font Size", self)
        label.setFont(QFont("Arial", 10))
        label.move(12, 0)

        self.size = QLineEdit(self)
        font_size = self.size.font()
        font_size.setPointSize(13)
        self.size.setFont(font_size)
        self.size.setStyleSheet("border : 1px solid black")
        self.size.move(140, 185)
        self.size.resize(150, 35)
        only_int = QIntValidator()
        self.size.setValidator(only_int)
        self.size.setText(f'{self.obj.is_size}')

        self.bold = QCheckBox("Bold")
        self.bold.setChecked(self.obj.is_bold)
        self.italic = QCheckBox("Italic")
        self.italic.setChecked(self.obj.is_italic)
        self.underline = QCheckBox("Underline")
        self.underline.setChecked(self.obj.is_underline)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        checkbox_layout.addWidget(self.bold)
        checkbox_layout.addWidget(self.italic)
        checkbox_layout.addWidget(self.underline)
        layout.addWidget(label)
        layout.addWidget(self.size)
        layout.addLayout(checkbox_layout)
        layout.addWidget(button_box)
        self.setLayout(layout)

    def accept(self):
        if self.size.text() != '' and int(self.size.text()) >= 1:
            if self.bold.isChecked() or self.italic.isChecked() \
                    or self.underline.isChecked():
                self.obj.is_bold = False
                self.obj.is_italic = False
                self.obj.is_underline = False
                self.font_size = self.text.font()
                if len(self.size.text()) != 0:
                    self.font_size.setPointSize(int(self.size.text()))
                    self.obj.is_size = int(self.size.text())
                if self.bold.isChecked():
                    self.obj.is_bold = True
                if self.italic.isChecked():
                    self.obj.is_italic = True
                if self.underline.isChecked():
                    self.obj.is_underline = True

                self.font_size.setUnderline(self.obj.is_underline)
                self.font_size.setItalic(self.obj.is_italic)
                self.font_size.setBold(self.obj.is_bold)
                self.text.setFont(self.font_size)
                self.close()


class InputTextDialog(QDialog):
    def __init__(self, obj_scribble_area):
        super().__init__()
        self.setWindowTitle("Input size")
        self.setWindowIcon(QIcon('../content/photoshop.png'))
        self.setFixedSize(600, 500)

        self.obj = obj_scribble_area

        self.color_text = (0, 0, 0, 255)
        self.is_bold = False
        self.is_italic = False
        self.is_underline = False
        self.is_size = 15

        self.text = QLineEdit(self)
        font = self.text.font()
        font.setPointSize(15)
        self.text.setFixedSize(580, 400)
        self.text.setFont(font)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        btn_select_color = QPushButton(self)
        btn_select_color.setText("Select Color")
        btn_select_color.resize(100, 40)
        btn_select_color.move(20, 445)
        btn_select_color.setFont(QFont("Arial", 12))
        btn_select_color.setStyleSheet("border-radius:5; border:1px solid black;")
        btn_select_color.clicked.connect(self.select_color)

        btn_select_type = QPushButton(self)
        btn_select_type.setText("Select Font")
        btn_select_type.resize(100, 40)
        btn_select_type.move(150, 445)
        btn_select_type.setFont(QFont("Arial", 12))
        btn_select_type.setStyleSheet("border-radius:5; border:1px solid black;")
        btn_select_type.clicked.connect(self.select_font)

        layout = QVBoxLayout(self)
        layout.addWidget(self.text)
        layout.addWidget(button_box)

    def select_color(self):
        self.color_text = QColorDialog().getColor().getRgb()
        self.obj.color_text = self.color_text
        self.text.setStyleSheet(f'color: rgb{self.color_text};')

    def select_font(self):
        TextType(self, self.text).exec()

    def accept(self):
        if self.text.text():
            self.obj.bold = self.is_bold
            self.obj.italic = self.is_italic
            self.obj.underline = self.is_underline
            self.obj.text = self.text.text()
            self.obj.width_text = self.is_size
            self.obj.color_text = self.color_text
            self.close()


class MoveText(QWidget):
    def __init__(self, text, text_width, text_color, bold, italic, underline,
                 parent, phj_obj, dragable=False):
        super(MoveText, self).__init__(parent)
        self.draggable = dragable
        self.scribble_obj = parent
        self.phj_obj = phj_obj
        self.dragging_threshold = 5
        self.mouse_press_pos = None
        self.mouse_move_pos = None
        self.border_radius = 0
        self.setWindowFlags(Qt.SubWindow)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(
            QSizeGrip(self), 0,
            Qt.AlignLeft | Qt.AlignTop)
        layout.addWidget(
            QSizeGrip(self), 0,
            Qt.AlignRight | Qt.AlignBottom)

        my_font = QFont()
        my_font.setBold(bold)
        my_font.setItalic(italic)
        my_font.setUnderline(underline)
        my_font.setPointSize(text_width)

        self.label = QLabel(self)
        self.label.setText(text)
        self.label.setFont(my_font)
        self.label.setStyleSheet(f'color: rgba{text_color}')
        self.label.adjustSize()

        self._band = QRubberBand(
            QRubberBand.Rectangle, self)

        self.setGeometry(150, 150, 300, 50)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.show()

    def resizeEvent(self, event):
        self._band.resize(self.size())

    def paintEvent(self, event):
        # if not self.phj_obj.is_clicked_move:
        #     painter = QPainter(self.scribble_obj.image_draw)
        #
        #     pen = QPen(QColor(self.scribble_obj.color_text[0], self.scribble_obj.color_text[1],
        #                       self.scribble_obj.color_text[2],
        #                       self.scribble_obj.color_text[3]))
        #
        #     pen.setWidth(10)
        #     painter.setPen(pen)
        #
        #     font = QFont()
        #     font.setBold(self.scribble_obj.bold)
        #     font.setItalic(self.scribble_obj.italic)
        #     font.setUnderline(self.scribble_obj.underline)
        #     font.setPointSize(self.scribble_obj.width_text)
        #     painter.setFont(font)
        #     painter.drawText(self.geometry().x(), self.geometry().y(), self.scribble_obj.text)
        #     self.hide()
        pass

    def mousePressEvent(self, event):

        if self.draggable and event.button() == Qt.LeftButton:
            self.mouse_press_pos = event.globalPos()  # global
            self.mouse_move_pos = event.globalPos() - self.pos()  # local

        super(MoveText, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.draggable and event.buttons() & Qt.LeftButton:
            global_pos = event.globalPos()
            moved = global_pos - self.mouse_press_pos
            if moved.manhattanLength() > self.dragging_threshold:
                # Move when user drag window more than dragging_threshold
                diff = global_pos - self.mouse_move_pos
                self.move(diff)
                self.mouse_move_pos = global_pos - self.pos()
        super(MoveText, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):

        if self.mouse_press_pos is not None:
            if event.button() == Qt.RightButton:
                moved = event.globalPos() - self.mouse_press_pos
                if moved.manhattanLength() > self.dragging_threshold:
                    # Do not call click event or so on
                    event.ignore()
                self.mouse_press_pos = None
        super(MoveText, self).mouseReleaseEvent(event)
