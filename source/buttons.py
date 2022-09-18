from PyQt5 import QtSvg
from PyQt5.QtCore import QPoint, Qt, QSize, QDir
from PyQt5.QtGui import QColor, QIcon, QPen, QPainter, qRgb, QImage, QFont, QIntValidator
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QCheckBox, QDialogButtonBox, QDialog, QHBoxLayout, \
    QLabel, QLineEdit, QPushButton, QColorDialog, QFileDialog, QComboBox
import cv2 as cv
import argparse
import numpy as np
import sys
from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import QPainter, QPen, QBrush, QIcon
import aspose.words as aw
from PIL import Image
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
        obj_photoshop.all_button_white()
        obj_scribble.pressed_button = None

    def crop(self, obj):
        cropped = obj.scribble_area.image.copy(obj.scribble_area.shape)
        obj.scribble_area.image = QImage()
        new_size = obj.scribble_area.image.size().expandedTo(obj.scribble_area.size())
        obj.scribble_area.resizeImage(obj.scribble_area.image, QSize(new_size))
        painter = QPainter(obj.scribble_area.image)
        painter.drawImage(obj.scribble_area.shape, cropped)
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
                    obj.all_button_white()
                    return

            elif self.image_type in ('png', 'bmp', 'jpeg', 'jpg'):
                if self.filename.endswith('svg'):
                    doc = aw.Document()
                    builder = aw.DocumentBuilder(doc)
                    shape = builder.insert_image(self.filename)
                    shape.image_data.save(f'{self.filename[:-3]}{self.image_type}')
                    obj.all_button_white()
                    return

                if self.filename.endswith(('png', 'jpg', 'gif', 'bmp', 'jpeg', 'jfif')):
                    Image.open(self.filename).convert('RGB'). \
                        save(f'{self.filename[:point_index + 1]}{self.image_type}')

        obj.all_button_white()


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
        self.obj = obj
        self.text = text
        super().__init__()
        self.setFixedSize(250, 150)
        self.setWindowIcon(QIcon('../content/photoshop.png'))

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

        self.bold = QCheckBox("Bold")
        self.bold.setChecked(self.obj.is_bold)
        self.italic = QCheckBox("Italic")
        self.italic.setChecked(self.obj.is_italic)
        self.underline = QCheckBox("Underline")
        self.underline.setChecked(self.obj.is_underline)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)

        checkbox_layout.addWidget(self.bold)
        checkbox_layout.addWidget(self.italic)
        checkbox_layout.addWidget(self.underline)
        layout.addWidget(self.size)
        layout.addLayout(checkbox_layout)
        layout.addWidget(button_box)
        self.setLayout(layout)
        self.setWindowTitle("Text Font")

        button_box.accepted.connect(self.accept)

    def accept(self):
        self.obj.is_bold = False
        self.obj.is_italic = False
        self.obj.is_underline = False
        font_size = self.text.font()
        if len(self.size.text()) != 0:
            font_size.setPointSize(int(self.size.text()))
            self.obj.is_size = int(self.size.text())
        if self.bold.isChecked():
            self.obj.is_bold = True
        if self.italic.isChecked():
            self.obj.is_italic = True
        if self.underline.isChecked():
            self.obj.is_underline = True

        font_size.setUnderline(self.obj.is_underline)
        font_size.setItalic(self.obj.is_italic)
        font_size.setBold(self.obj.is_bold)
        self.text.setFont(font_size)
        self.close()


class InputTextDialog(QDialog):
    def __init__(self, obj):
        self.obj = obj
        super().__init__()

        self.is_bold = False
        self.is_italic = False
        self.is_underline = False
        self.is_size = 15

        self.setWindowTitle("Input size")
        self.setWindowIcon(QIcon('../content/photoshop.png'))
        self.setFixedSize(600, 500)

        self.text = QLineEdit(self)
        font = self.text.font()
        font.setPointSize(15)
        self.text.setFixedSize(580, 400)
        self.text.setFont(font)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)

        btn_select_color = QPushButton(self)
        btn_select_color.setText("Select Color")
        btn_select_color.resize(100, 40)
        btn_select_color.move(20, 445)
        btn_select_color.setFont(QFont("Arial", 12))
        btn_select_color.setStyleSheet("border-radius:5; border:1px solid black;")
        btn_select_color.clicked.connect(self.select_color)

        btn_select_Type = QPushButton(self)
        btn_select_Type.setText("Select Font")
        btn_select_Type.resize(100, 40)
        btn_select_Type.move(150, 445)
        btn_select_Type.setFont(QFont("Arial", 12))
        btn_select_Type.setStyleSheet("border-radius:5; border:1px solid black;")
        btn_select_Type.clicked.connect(self.select_font)

        layout = QVBoxLayout(self)
        layout.addWidget(self.text)
        layout.addWidget(button_box)

        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

    def select_color(self):
        self.obj.color_text = QColorDialog().getColor().getRgb()
        color = self.obj.color_text
        self.text.setStyleSheet(f'color: rgb{color};')

    def select_font(self):
        TextType(self, self.text).exec()

    def accept(self):
        self.obj.bold = self.is_bold
        self.obj.italic = self.is_italic
        self.obj.underline = self.is_underline
        self.obj.text = self.text.text()
        self.obj.width_text = self.is_size
        self.close()
