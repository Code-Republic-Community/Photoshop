import functools
import io
import sys
from functools import partial

from PyQt5.QtCore import QBuffer

from source.scribble_area import ScribbleArea
from PyQt5.QtWidgets import QApplication, QPushButton, \
    QLabel, QVBoxLayout, QWidget, QBoxLayout, QMainWindow, QAction, QSizePolicy, QHBoxLayout, QMenuBar, QMenu, \
    QColorDialog, QSpinBox
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QPen, QColor, QImage
from PyQt5 import QtCore, QtWidgets
import file
import edit
import image
import filter
from scribble_area import ScribbleArea
from source.buttons import Buttons
from help import Help, Documentation
import numpy as np
import cv2 as cv

class PhotoshopEditor(QMainWindow):
    def __init__(self):
        super(PhotoshopEditor, self).__init__()
        self.scribbleArea = ScribbleArea()
        self.buttons_obj = Buttons()
        self.pressed_button = None
        self.main_window: QMainWindow = None
        # QMainWindow.setCentralWidget(self,self.scribbleArea)

    def setupUi(self, MainWindow):
        self.main_window = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Photoshop Editor")
        MainWindow.setGeometry(280, 90, 900, 600)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        MainWindow.setWindowIcon(QIcon('../content/photoshop.png'))

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_list = [None] * 9
        self.colorname = QColor()
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addWidget(self.scribbleArea)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName("actionNesssw")
        self.menuFile.addAction(self.actionNew)
        self.menubar.addAction(self.menuFile.menuAction())
        self.toolbar()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        main_menu = QMenuBar(MainWindow)
        main_menu.setGeometry(QtCore.QRect(0, 0, 800, 24))
        MainWindow.setMenuBar(main_menu)
        file_menu = QMenu(main_menu)
        edit_menu = QMenu(main_menu)
        image_menu = QMenu(main_menu)
        filter_menu = QMenu(main_menu)
        help_menu = QMenu(main_menu)
        _translate = QtCore.QCoreApplication.translate
        dict_file = {'New': file.File.new, 'Open': file.File.open,
                     'Save': file.File.save, 'Save As': file.File.save_as,
                     'Print': file.File.print, 'Close': file.File.close_window}

        dict_edit = {'Undo': edit.Edit.undo, 'Redo': edit.Edit.redo,
                     'Cut': edit.Edit.cut, 'Copy': edit.Edit.copy,
                     'Paste': edit.Edit.paste, 'Clear screen': edit.Edit.clear_screen,
                     'Keyboard shortcuts': edit.Edit.keyboard_shortcuts}

        dict_image = {'Image size': image.Image.image_size,
                      'Canvas size': image.Image.canvas_size,
                      'Rotate left': image.Image.rotate_left,
                      'Rotate right': image.Image.rotate_right}

        dict_filter = {'Blur': filter.Filter.blur, 'Noise': filter.Filter.noise,
                       'Distort': filter.Filter.distort,
                       'Pixelate': filter.Filter.pixelate}

        dict_help = {'Help': self.help, 'Documentation': self.documentation}

        # action_save = QAction("Save", self)
        # action_save.setShortcut('Ctrl+S')
        # file_menu.addAction(action_save)
        lst_file_shortcut = ['Ctrl+N', 'Ctrl+O', 'Ctrl+S', 'Ctrl+Shift+S', 'Ctrl+P', 'Ctrl+W']
        i = 0
        for key, value in dict_file.items():
            extractAction = QAction(MainWindow)
            extractAction.setShortcut(lst_file_shortcut[i])
            file_menu.addAction(extractAction)
            main_menu.addAction(file_menu.menuAction())
            extractAction.triggered.connect(functools.partial(value, self, self))
            extractAction.setText(_translate("MainWindow", key))
            i += 1

        lst_edit_shortcut = ['Ctrl+Z', 'Ctrl+Y', 'Ctrl+X', 'Ctrl+C', 'Ctrl+V', 'Ctrl+L', 'Ctrl+K']
        i = 0

        for key, value in dict_edit.items():
            extractAction = QAction(MainWindow)
            extractAction.setShortcut(lst_edit_shortcut[i])
            edit_menu.addAction(extractAction)
            main_menu.addAction(edit_menu.menuAction())
            extractAction.triggered.connect(functools.partial(value, self, self))
            extractAction.setText(_translate("MainWindow", key))
            i += 1

        lst_image_shortcut = ['Ctrl+Alt+I', 'Ctrl+Alt+C', 'Shift+Ctrl+L', 'Shift+Ctrl+R']
        i = 0

        for key, value in dict_image.items():
            extractAction = QAction(MainWindow)
            extractAction.setShortcut(lst_image_shortcut[i])
            image_menu.addAction(extractAction)
            main_menu.addAction(image_menu.menuAction())
            extractAction.triggered.connect(functools.partial(value, self, self))
            extractAction.setText(_translate("MainWindow", key))
            i += 1

        lst_filter_shortcut = ['Shift+Ctrl+B', 'Shift+Ctrl+N', 'Shift+Ctrl+D', 'Shift+Ctrl+P']
        i = 0

        for key, value in dict_filter.items():
            extractAction = QAction(MainWindow)
            extractAction.setShortcut(lst_filter_shortcut[i])
            filter_menu.addAction(extractAction)
            main_menu.addAction(filter_menu.menuAction())
            extractAction.triggered.connect(functools.partial(value, self, self))
            extractAction.setText(_translate("MainWindow", key))
            i += 1

        lst_help_shortcut = ['Ctrl+H', 'Ctrl+D']
        i = 0

        for key, value in dict_help.items():
            extractAction = QAction(MainWindow)
            extractAction.setShortcut(lst_help_shortcut[i])
            help_menu.addAction(extractAction)
            main_menu.addAction(help_menu.menuAction())
            extractAction.triggered.connect(functools.partial(value, self, self))
            extractAction.setText(_translate("MainWindow", key))
            i += 1

        file_menu.setTitle(_translate("MainWindow", "File"))
        edit_menu.setTitle(_translate("MainWindow", "Edit"))
        image_menu.setTitle(_translate("MainWindow", "Image"))
        filter_menu.setTitle(_translate("MainWindow", "Filter"))
        help_menu.setTitle(_translate("MainWindow", "Help"))

    def toolbar(self):
        """This function is responsible for create and design buttons of tool"""
        dict_buttons = {'../content/paint-brush.png': self.paint,
                        '../content/move.png': self.move_text,
                        '../content/marquee.png': self.marquee,
                        '../content/lasso.png': self.lasso,
                        '../content/crop.png': self.crop,
                        '../content/eyedropper.png': self.eyedropper,
                        '../content/eraser.png': self.eraser,
                        '../content/font.png': self.type,
                        '../content/recovery.png': self.image_converter}
        i = 0
        for key, value in dict_buttons.items():
            self.button_list[i] = QPushButton(self.centralwidget)

            self.button_list[i].setMaximumSize(QtCore.QSize(50, 50))
            sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.button_list[i].sizePolicy().hasHeightForWidth())
            self.button_list[i].setSizePolicy(sizePolicy)
            self.button_list[i].setMaximumSize(QtCore.QSize(50, 50))
            self.button_list[i].setIcon(QIcon(key))
            self.button_list[i].clicked.connect(value)
            # print(self.button_list[1])
            self.button_list[i].setStyleSheet("QPushButton:hover "
                                              "{background-color: lightgray}")
            self.verticalLayout.addWidget(self.button_list[i])
            i += 1

        pen_menu = QMenu()
        pen_menu.addAction('Paint', self.paint)
        pen_menu.addAction('Color', self.scribbleArea.pen_color)
        pen_menu.addAction('Width', self.scribbleArea.pen_width)
        self.button_list[0].setMenu(pen_menu)

        text_menu = QMenu()
        text_menu.addAction('Write', self.scribbleArea.text_write)
        text_menu.addAction('Size', self.scribbleArea.text_width)
        text_menu.addAction('Type', self.scribbleArea.text_type)
        text_menu.addAction('Color', self.scribbleArea.text_color)
        self.button_list[7].setMenu(text_menu)

    def all_button_white(self):
        for i in range(9):
            self.button_list[i].setStyleSheet('background-color: white;')

    def paint(self):
        self.scribbleArea.pressed_button = 'paint'
        self.all_button_white()
        self.button_list[0].setStyleSheet('background-color: red;')

    def move_text(self):
        self.scribbleArea.pressed_button = 'move'
        self.all_button_white()
        self.button_list[1].setStyleSheet('background-color: red;')

    def marquee(self):
        self.scribbleArea.pressed_button = 'marquee'
        self.all_button_white()
        self.button_list[2].setStyleSheet('background-color: red;')

    def lasso(self):
        self.scribbleArea.pressed_button = 'lasso'
        self.all_button_white()
        self.button_list[3].setStyleSheet('background-color: red;')

    def crop(self):
        self.scribbleArea.pressed_button = 'crop'
        self.all_button_white()
        self.button_list[4].setStyleSheet('background-color: red;')

    def eyedropper(self):
        self.scribbleArea.pressed_button = 'eyedropper'
        self.all_button_white()
        self.button_list[5].setStyleSheet('background-color: red;')
        self.buttons_obj.eyedropper(self)

    def eraser(self):
        self.scribbleArea.pressed_button = 'eraser'
        self.all_button_white()
        self.button_list[6].setStyleSheet('background-color: red;')

    def type(self):
        self.scribbleArea.pressed_button = 'type'
        self.all_button_white()
        self.button_list[7].setStyleSheet('background-color: red;')

    def image_converter(self):
        self.scribbleArea.pressed_button = 'image_converter'
        self.all_button_white()
        self.button_list[8].setStyleSheet('background-color: red;')



    def help(self,obj1,obj2):
        self.window = QtWidgets.QDialog()
        self.ui = Help()
        self.ui.setupUi(self.window)
        self.window.show()

    def documentation(self):
        self.window = QtWidgets.QDialog()
        self.ui = Documentation()
        self.ui.setupUi(self.window)
        self.window.show()

    def set_window_size(self, width, height):
        self.main_window.setGeometry(280, 90, width, height)

    def qimage_to_cv(self, img: QImage):
        buffer = QBuffer()
        buffer.open(QBuffer.ReadWrite)
        img.save(buffer, "PNG")
        img_stream = io.BytesIO((buffer.data()))
        img = cv.imdecode(np.frombuffer(img_stream.read(), np.uint8), 1)
        return img

    def cv_to_qimage(self, img):
        is_success, buffer = cv.imencode(".jpg", img)
        io_buf = io.BytesIO(buffer)
        qimg = QImage()
        qimg.loadFromData(io_buf.getvalue())
        return qimg

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    Frame = QMainWindow()
    ui = PhotoshopEditor()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())