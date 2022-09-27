from PyQt5 import QtWidgets, QtCore, QtGui
import aspose.words as aw
from PIL import Image

class Buttons(QtWidgets.QMainWindow):
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

            photoshop_obj.scribble_area.resize_image(photoshop_obj.scribble_area.image)

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

            if self.image_type in 'svg':
                if self.filename.endswith(('png', 'jpg', 'gif', 'bmp', 'jpeg', 'jfif')):
                    doc = aw.Document()
                    builder = aw.DocumentBuilder(doc)
                    shape = builder.insert_image(self.filename)
                    save_options = aw.saving.ImageSaveOptions(aw.SaveFormat.SVG)
                    shape.get_shape_renderer(). \
                        save(f'{self.filename[:point_index + 1]}{self.image_type}',
                             save_options)
                    photoshop_obj.all_button_white()
                    return

            elif self.image_type in ('png', 'bmp', 'jpeg', 'jpg'):
                if self.filename.endswith('svg'):
                    doc = aw.Document()
                    builder = aw.DocumentBuilder(doc)
                    shape = builder.insert_image(self.filename)
                    shape.image_data.save(f'{self.filename[:-3]}{self.image_type}')
                    photoshop_obj.all_button_white()
                    return

                if self.filename.endswith(('png', 'jpg', 'gif', 'bmp', 'jpeg', 'jfif')):
                    Image.open(self.filename).convert('RGB'). \
                        save(f'{self.filename[:point_index + 1]}{self.image_type}')

        photoshop_obj.all_button_white()


class ImgTypeComboBox(QtWidgets.QDialog):
    def __init__(self, buttons_obj):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('../content/photoshop.png'))
        self.buttons_obj = buttons_obj
        self.setFixedSize(250, 120)

        layout = QtWidgets.QVBoxLayout()
        self.combo_box = QtWidgets.QComboBox(self)
        img_types = ['jpeg', 'jpg', 'png', 'svg', 'bmp']
        self.combo_box.addItems(img_types)
        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok
                                                | QtWidgets.QDialogButtonBox.Cancel, self)

        layout.addWidget(self.combo_box)
        layout.addWidget(button_box)
        self.setLayout(layout)

        button_box.accepted.connect(self.accept)

    def accept(self):
        img_type = self.combo_box.currentText()
        self.buttons_obj.image_type = img_type
        self.close()


class TextType(QtWidgets.QDialog):
    def __init__(self, text_window_obj, text):
        super().__init__()
        self.setWindowTitle('Text Font')
        self.setWindowIcon(QtGui.QIcon('../content/photoshop.png'))
        self.text_window_obj = text_window_obj
        self.text = text
        self.font_size = self.text.font()
        self.setFixedSize(0, 0)

        layout = QtWidgets.QVBoxLayout()
        checkbox_layout = QtWidgets.QHBoxLayout()

        label = QtWidgets.QLabel('Font Size', self)
        label.setFont(QtGui.QFont('Arial', 10))
        label.move(12, 0)

        self.size = QtWidgets.QLineEdit(self)
        font_size = self.size.font()
        font_size.setPointSize(13)
        self.size.setFont(font_size)
        self.size.setStyleSheet('border : 1px solid black')
        self.size.move(140, 185)
        self.size.resize(150, 35)
        only_int = QtGui.QIntValidator()
        self.size.setValidator(only_int)
        self.size.setText(f'{self.text_window_obj.is_size}')

        self.bold = QtWidgets.QCheckBox('Bold')
        self.bold.setChecked(self.text_window_obj.is_bold)
        self.italic = QtWidgets.QCheckBox('Italic')
        self.italic.setChecked(self.text_window_obj.is_italic)
        self.underline = QtWidgets.QCheckBox('Underline')
        self.underline.setChecked(self.text_window_obj.is_underline)

        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok
                                                | QtWidgets.QDialogButtonBox.Cancel, self)
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
        if self.size.text() != '' and 1 <= int(self.size.text()) <= 50:
            self.text_window_obj.is_bold = False
            self.text_window_obj.is_italic = False
            self.text_window_obj.is_underline = False
            self.font_size = self.text.font()
            if len(self.size.text()) != 0:
                self.font_size.setPointSize(int(self.size.text()))
                self.text_window_obj.is_size = int(self.size.text())
            if self.bold.isChecked():
                self.text_window_obj.is_bold = True
            if self.italic.isChecked():
                self.text_window_obj.is_italic = True
            if self.underline.isChecked():
                self.text_window_obj.is_underline = True

            self.font_size.setUnderline(self.text_window_obj.is_underline)
            self.font_size.setItalic(self.text_window_obj.is_italic)
            self.font_size.setBold(self.text_window_obj.is_bold)
            self.text.setFont(self.font_size)
            self.close()


class TextWindow(QtWidgets.QDialog):
    def __init__(self, obj_scribble_area):
        super().__init__()
        self.setWindowTitle('Input size')
        self.setWindowIcon(QtGui.QIcon('../content/photoshop.png'))
        self.setFixedSize(600, 500)
        self.closed_window = True

        self.obj_scribble_area = obj_scribble_area
        self.color_text = (0, 0, 0, 255)
        self.is_bold = False
        self.is_italic = False
        self.is_underline = False
        self.is_size = 15

        self.text = QtWidgets.QLineEdit(self)
        font = self.text.font()
        font.setPointSize(15)
        self.text.setFixedSize(580, 400)
        self.text.setFont(font)

        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok
                                                | QtWidgets.QDialogButtonBox.Cancel, self)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject_window)

        btn_select_color = QtWidgets.QPushButton(self)
        btn_select_color.setText('Select Color')
        btn_select_color.resize(100, 40)
        btn_select_color.move(20, 445)
        btn_select_color.setFont(QtGui.QFont('Arial', 12))
        btn_select_color.setStyleSheet('border-radius:5; border:1px solid black;')
        btn_select_color.clicked.connect(self.select_color)

        btn_select_type = QtWidgets.QPushButton(self)
        btn_select_type.setText('Select Font')
        btn_select_type.resize(100, 40)
        btn_select_type.move(150, 445)
        btn_select_type.setFont(QtGui.QFont('Arial', 12))
        btn_select_type.setStyleSheet('border-radius:5; border:1px solid black;')
        btn_select_type.clicked.connect(self.select_font)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.text)
        layout.addWidget(button_box)

    def select_color(self):
        self.color_text = QtWidgets.QColorDialog().getColor().getRgb()
        self.obj_scribble_area.color_text = self.color_text
        self.text.setStyleSheet(f'color: rgb{self.color_text};')
        self.obj_scribble_area.text = ''

    def select_font(self):
        TextType(self, self.text).exec()

    def accept(self):
        if self.text.text():
            self.closed_window = False
            self.obj_scribble_area.bold = self.is_bold
            self.obj_scribble_area.italic = self.is_italic
            self.obj_scribble_area.underline = self.is_underline
            self.obj_scribble_area.text = self.text.text()
            self.obj_scribble_area.width_text = self.is_size
            self.obj_scribble_area.color_text = self.color_text
            self.close()

    def reject_window(self):
        self.obj_scribble_area.text = ''
        self.close()

    def closeEvent(self, event):
        if self.closed_window:
            self.reject_window()


class MoveText(QtWidgets.QWidget):
    def __init__(self, text, text_width, text_color, bold, italic, underline,
                 parent, photoshop_obj, dragable=False):
        super(MoveText, self).__init__(parent)
        self.draggable = dragable
        self.scribble_obj = parent
        self.photoshop_obj = photoshop_obj
        self.dragging_threshold = 5
        self.mouse_press_pos = None
        self.mouse_move_pos = None
        self.border_radius = 0
        self.setWindowFlags(QtCore.Qt.SubWindow)

        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(
            QtWidgets.QSizeGrip(self), 0,
            QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        layout.addWidget(
            QtWidgets.QSizeGrip(self), 0,
            QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)

        my_font = QtGui.QFont()
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

            font = QtGui.QFont()
            font.setBold(self.scribble_obj.bold)
            font.setItalic(self.scribble_obj.italic)
            font.setUnderline(self.scribble_obj.underline)
            font.setPointSize(self.scribble_obj.width_text)
            painter.setFont(font)
            painter.drawText(self.geometry().x(), self.geometry().y(), self.scribble_obj.text)
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
