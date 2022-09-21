import functools
import io
import sys
from functools import partial

from PyQt5.QtCore import QBuffer, Qt

from PyQt5.QtWidgets import QApplication, QPushButton, \
    QLabel, QVBoxLayout, QWidget, QBoxLayout, QMainWindow, QAction, QSizePolicy, QHBoxLayout, QMenuBar, QMenu, \
    QColorDialog, QSpinBox, QDialog
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QPen, QColor, QImage, QCursor
from PyQt5 import QtCore, QtWidgets
import file
import edit
import image
import filter
import buttons
from scribble_area import ScribbleArea
from source.buttons import Buttons, InputTextDialog
from help import Help, Documentation
import numpy as np
import cv2 as cv
from source.buttons import MoveText

gl_draggable = False


class PhotoshopEditor(QMainWindow):
    def __init__(self):
        super(PhotoshopEditor, self).__init__()
        self.scribble_area = ScribbleArea()
        self.buttons_obj = Buttons()
        self.pressed_button = None
        self.main_window: QMainWindow = None
        self.button_list = [None] * 9
        self.vertical_layout = QVBoxLayout()
        self.screen_width = 0
        self.screen_height = 0
        self.band = []

    def setupUi(self, main_window):
        screen = app.primaryScreen()
        rect = screen.availableGeometry()
        self.screen_width = rect.width()
        self.screen_height = rect.height()
        self.main_window = main_window
        main_window.setObjectName("MainWindow")
        main_window.setWindowTitle("Photoshop Editor")
        main_window.setGeometry((self.screen_width - 826)//2, (self.screen_height - 561)//2, 900, 600)
        main_window.setMinimumSize(QtCore.QSize(600, 400))
        main_window.setMaximumSize(self.screen_width, self.screen_height)
        main_window.setWindowIcon(QIcon('../content/photoshop.png'))

        self.central_widget = QWidget(main_window)
        self.central_widget.setObjectName("centralwidget")
        horizontal_layout = QHBoxLayout(self.central_widget)
        horizontal_layout.setObjectName("horizontalLayout")
        horizontal_layout_2 = QHBoxLayout()
        horizontal_layout_2.setObjectName("horizontalLayout_2")
        self.vertical_layout.setObjectName("verticalLayout")
        horizontal_layout_2.addLayout(self.vertical_layout)
        horizontal_layout_2.addWidget(self.scribble_area)
        horizontal_layout.addLayout(horizontal_layout_2)
        main_window.setCentralWidget(self.central_widget)
        menubar = QMenuBar(main_window)
        menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        menubar.setObjectName("menubar")
        menu_file = QMenu(menubar)
        menu_file.setObjectName("menuFile")
        main_window.setMenuBar(menubar)
        action_new = QAction(main_window)
        action_new.setObjectName("actionNesssw")
        menu_file.addAction(action_new)
        menubar.addAction(menu_file.menuAction())
        self.toolbar()
        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, Main_window):
        main_menu = QMenuBar(Main_window)
        main_menu.setGeometry(QtCore.QRect(0, 0, 800, 24))
        Main_window.setMenuBar(main_menu)
        file_menu = QMenu(main_menu)
        edit_menu = QMenu(main_menu)
        image_menu = QMenu(main_menu)
        filter_menu = QMenu(main_menu)
        help_menu = QMenu(main_menu)
        translate = QtCore.QCoreApplication.translate
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
                       'Twirling spirals': filter.Filter.twirling_spirals,
                       'Pixelate': filter.Filter.pixelate}

        dict_help = {'Help': self.help, 'Documentation': self.documentation}

        lst_file_shortcut = ['Ctrl+N', 'Ctrl+O', 'Ctrl+S', 'Ctrl+Shift+S', 'Ctrl+P', 'Ctrl+W']
        i = 0
        for key, value in dict_file.items():
            extract_action = QAction(Main_window)
            extract_action.setShortcut(lst_file_shortcut[i])
            file_menu.addAction(extract_action)
            main_menu.addAction(file_menu.menuAction())
            extract_action.triggered.connect(functools.partial(value, self, self))
            extract_action.setText(translate("MainWindow", key))
            i += 1

        lst_edit_shortcut = ['Ctrl+Z', 'Ctrl+Y', 'Ctrl+X', 'Ctrl+C', 'Ctrl+V', 'Ctrl+L', 'Ctrl+K']
        i = 0

        for key, value in dict_edit.items():
            extract_action = QAction(Main_window)
            extract_action.setShortcut(lst_edit_shortcut[i])
            edit_menu.addAction(extract_action)
            main_menu.addAction(edit_menu.menuAction())
            extract_action.triggered.connect(functools.partial(value, self, self))
            extract_action.setText(translate("MainWindow", key))
            i += 1

        lst_image_shortcut = ['Ctrl+Alt+I', 'Ctrl+Alt+C', 'Shift+Ctrl+L', 'Shift+Ctrl+R']
        i = 0

        for key, value in dict_image.items():
            extract_action = QAction(Main_window)
            extract_action.setShortcut(lst_image_shortcut[i])
            image_menu.addAction(extract_action)
            main_menu.addAction(image_menu.menuAction())
            extract_action.triggered.connect(functools.partial(value, self, self))
            extract_action.setText(translate("MainWindow", key))
            i += 1

        lst_filter_shortcut = ['Shift+Ctrl+B', 'Shift+Ctrl+N', 'Shift+Ctrl+P', 'Shift+Ctrl+P']
        i = 0

        for key, value in dict_filter.items():
            extract_action = QAction(Main_window)
            extract_action.setShortcut(lst_filter_shortcut[i])
            filter_menu.addAction(extract_action)
            main_menu.addAction(filter_menu.menuAction())
            extract_action.triggered.connect(functools.partial(value, self, self))
            extract_action.setText(translate("MainWindow", key))
            i += 1

        lst_help_shortcut = ['Ctrl+H', 'Ctrl+D']
        i = 0

        for key, value in dict_help.items():
            extract_action = QAction(Main_window)
            extract_action.setShortcut(lst_help_shortcut[i])
            help_menu.addAction(extract_action)
            main_menu.addAction(help_menu.menuAction())
            extract_action.triggered.connect(functools.partial(value, self, self))
            extract_action.setText(translate("MainWindow", key))
            i += 1

        file_menu.setTitle(translate("MainWindow", "File"))
        edit_menu.setTitle(translate("MainWindow", "Edit"))
        image_menu.setTitle(translate("MainWindow", "Image"))
        filter_menu.setTitle(translate("MainWindow", "Filter"))
        help_menu.setTitle(translate("MainWindow", "Help"))

    def toolbar(self):
        """This function is responsible for create and design buttons of tool"""
        dict_buttons = {'../content/paint-brush.png': self.paint,
                        '../content/move.png': self.moveText,
                        '../content/marquee.png': self.marquee,
                        '../content/lasso.png': self.lasso,
                        '../content/crop.png': self.crop,
                        '../content/eyedropper.png': self.eyedropper,
                        '../content/eraser.png': self.eraser,
                        '../content/font.png': self.type,
                        '../content/recovery.png': self.imageConverter}
        i = 0
        for key, value in dict_buttons.items():
            self.button_list[i] = QPushButton(self.central_widget)

            self.button_list[i].setMaximumSize(QtCore.QSize(50, 50))
            size_policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
            size_policy.setHorizontalStretch(0)
            size_policy.setVerticalStretch(0)
            size_policy.setHeightForWidth(self.button_list[i].sizePolicy().hasHeightForWidth())
            self.button_list[i].setSizePolicy(size_policy)
            self.button_list[i].setMaximumSize(QtCore.QSize(50, 50))
            self.button_list[i].setIcon(QIcon(key))
            self.button_list[i].clicked.connect(value)
            self.button_list[i].setStyleSheet("QPushButton:hover "
                                              "{background-color: lightgray}")
            self.vertical_layout.addWidget(self.button_list[i])
            i += 1

        # self.button_list[4].clicked.connect(functools.partial(buttons.Buttons.crop, self, self))

        pen_menu = QMenu()
        pen_menu.addAction('Paint', self.paint)
        pen_menu.addAction('Color', functools.partial(self.scribble_area.penColor, self, self, ))
        pen_menu.addAction('Width', functools.partial(self.scribble_area.toolWidth, self, self, 'pen'))
        self.button_list[0].setMenu(pen_menu)

        rubber_menu = QMenu()
        rubber_menu.addAction('Rubber', self.eraser)
        rubber_menu.addAction('Width', functools.partial(self.scribble_area.toolWidth, self, self, 'rubber'))
        self.button_list[6].setMenu(rubber_menu)

    def allButtonWhite(self):
        for i in range(9):
            self.button_list[i].setStyleSheet('background-color: white;')

    def paint(self):
        self.scribble_area.pressed_button = 'paint'
        self.allButtonWhite()
        self.button_list[0].setStyleSheet('background-color: red;')

        icon = QIcon('../content/paint-brush.png')
        pixmap = QPixmap('../content/paint-brush.png')
        pixmap = pixmap.scaled(20 + self.scribble_area.pen_width, 20 + self.scribble_area.pen_width,
                               Qt.IgnoreAspectRatio, Qt.SmoothTransformation)

        mask = pixmap.createMaskFromColor(Qt.red)
        pixmap.setMask(mask)
        cursor = QCursor(pixmap)
        app.setOverrideCursor(cursor)

    def moveText(self):
        # cursor = QCursor().bitmap()
        # app.setOverrideCursor(cursor)
        self.scribble_area.pressed_button = 'move'
        self.allButtonWhite()
        self.button_list[1].setStyleSheet('background-color: red;')
        for i in self.band:
            i.draggable = True

    def marquee(self):
        self.scribble_area.pressed_button = 'marquee'
        self.allButtonWhite()
        self.button_list[2].setStyleSheet('background-color: red;')
        for i in self.band:
            i.draggable = False

    def lasso(self):
        self.scribble_area.pressed_button = 'lasso'
        self.allButtonWhite()
        self.button_list[3].setStyleSheet('background-color: red;')
        for i in self.band:
            i.draggable = False

    def crop(self):
        self.scribble_area.pressed_button = 'crop'
        self.allButtonWhite()
        self.button_list[4].setStyleSheet('background-color: red;')
        self.buttons_obj.crop(self)
        for i in self.band:
            i.draggable = False

    def eyedropper(self):
        self.scribble_area.pressed_button = 'eyedropper'
        self.allButtonWhite()
        self.button_list[5].setStyleSheet('background-color: red;')
        self.buttons_obj.eyedropper(self)
        for i in self.band:
            i.draggable = False

    def eraser(self):
        self.scribble_area.pressed_button = 'eraser'
        self.allButtonWhite()
        self.button_list[6].setStyleSheet('background-color: red;')
        for i in self.band:
            i.draggable = False

        pixmap = QPixmap('../content/square.png')
        pixmap = pixmap.scaled(self.scribble_area.rubber_width, self.scribble_area.rubber_width,
                               Qt.IgnoreAspectRatio, Qt.SmoothTransformation)

        mask = pixmap.createMaskFromColor(Qt.red)
        pixmap.setMask(mask)
        cursor = QCursor(pixmap)
        app.setOverrideCursor(cursor)

    def type(self):
        self.scribble_area.pressed_button = 'type'
        self.allButtonWhite()
        self.button_list[7].setStyleSheet('background-color: red;')
        InputTextDialog(self.scribble_area).exec()
        obj = MoveText(self.scribble_area.text,
                       self.scribble_area.width_text, self.scribble_area.color_text,
                       self.scribble_area.bold, self.scribble_area.italic,
                       self.scribble_area.underline, self.scribble_area, dragable=False)
        self.band.append(obj)

    def imageConverter(self):
        self.scribble_area.pressed_button = 'image_converter'
        self.allButtonWhite()
        self.button_list[8].setStyleSheet('background-color: red;')
        self.buttons_obj.image_converter(self)
        for i in self.band:
            i.draggable = False

    def help(self, obj1, obj2):
        self.window = QDialog()
        self.ui = Help()
        self.ui.setupUi(self.window)
        self.window.show()

    def documentation(self, obj1, obj2):
        self.window = QDialog()
        self.ui = Documentation()
        self.ui.setupUi(self.window)
        self.window.show()

    def setWindowSize(self, width, height):
        bigger = False
        if height > 701:
            height = 701
            bigger = True
        elif height < 400:
            height = 400

        if width > 1360:
            width = 1360
        elif width < 600:
            width = 600

        if bigger:
            self.main_window.setGeometry((self.screen_width - width) // 2,
                                        (self.screen_height - height + 27) // 2, width, height)
        else:
            self.main_window.setGeometry((self.screen_width - width) // 2,
                                        (self.screen_height - height) // 2, width, height)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    frame = QMainWindow()
    ui = PhotoshopEditor()
    ui.setupUi(frame)
    frame.show()
    sys.exit(app.exec_())
