"""This file open main window, and let you do photoshop"""
import functools
import sys
<<<<<<< HEAD
from functools import partial
from source.scribble_area import ScribbleArea
from PyQt5.QtWidgets import QApplication, QPushButton, \
    QLabel, QVBoxLayout, QWidget, QBoxLayout, QMainWindow, QAction
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QPen
import file
import edit
import image
import filter


class PhotoshopEditor(QMainWindow):
=======
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtGui import QIcon
from PhotoshopClone.MainWindow import MainWindow


from main_window import MainWindow

class PhotoshopEditor(MainWindow):
>>>>>>> main
    def __init__(self):

        """In the constructor is designed main window, and call main functions"""
        super().__init__()
        self.setGeometry(280, 90, 900, 600)
        self.setMinimumSize(600, 460)
        self.setWindowTitle("Photoshop Editor")
        self.setWindowIcon(QIcon('content/photoshop.png'))
        self.setStyleSheet('background-color:#FFFFFF')
        self.button_list = [None] * 9
        self.connected = False


        self.scribbleArea = ScribbleArea()
        self.scribbleArea.move(50, 20)
        self.setCentralWidget(self.scribbleArea)

<<<<<<< HEAD
        self.toolbar()
        self.menu_bar()

        #self.show()

    def menu_bar(self):
        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('&File')
        edit_menu = main_menu.addMenu('&Edit')
        image_menu = main_menu.addMenu('&Image')
        filter_menu = main_menu.addMenu('&Filter')

        dict_file = {'New': file.File.new, 'Open': file.File.open,
                     'Save': file.File.save, 'Save As': file.File.save_as,
                     'Print': file.File.print, 'Close': file.File.close}

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

        for key, value in dict_file.items():
            extractAction = QAction(key, self)
            file_menu.addAction(extractAction)
            extractAction.triggered.connect(functools.partial(value, self, self))

        for key, value in dict_edit.items():
            extractAction = QAction(key, self)
            edit_menu.addAction(extractAction)
            extractAction.triggered.connect(value)

        for key, value in dict_image.items():
            extractAction = QAction(key, self)
            image_menu.addAction(extractAction)
            extractAction.triggered.connect(value)

        for key, value in dict_filter.items():
            extractAction = QAction(key, self)
            filter_menu.addAction(extractAction)
            extractAction.triggered.connect(value)

    def toolbar(self):
        """This function is responsible for create and design buttons of tool"""
=======
        dict_buttons = {'../content/paint-brush.png': self.paint,
                        '../content/move.png': self.move,
                        '../content/marquee.png': self.marquee,
                        '../content/lasso.png': self.lasso,
                        '../content/crop.png': self.crop,
                        '../content/eyedropper.png': self.eyedropper,
                        '../content/eraser.png': self.eraser,
                        '../content/font.png': self.type,
                        '../content/recovery.png': self.image_converter}
        y = 0
        i = 0

>>>>>>> main
        dict_buttons = {'content/paint-brush.png': self.paint,
                        'content/move.png': self.move1,
                        'content/marquee.png': self.marquee,
                        'content/lasso.png': self.lasso,
                        'content/crop.png': self.crop,
                        'content/eyedropper.png': self.eyedropper,
                        'content/eraser.png': self.eraser,
                        'content/font.png': self.type,
                        'content/recovery.png': self.image_converter}
        y = 20
<<<<<<< HEAD
        i = 0
=======
>>>>>>> main
        for key, value in dict_buttons.items():
            self.button_list[i] = QPushButton(self)
            self.button_list[i].resize(40, 40)
            self.button_list[i].move(1, y)
            self.button_list[i].setIcon(QIcon(key))
            self.button_list[i].clicked.connect(value)
            #print(self.button_list[1])
            self.button_list[i].setStyleSheet("QPushButton::hover "
                                              "{background-color: lightgray}")
            #vbox.addWidget(self.button_list[i])
            #self.vbox.addStretch()

            y += 50
            i += 1


    def all_button_white(self):
        for i in range(9):
            self.button_list[i].setStyleSheet('background-color: white;')

    def paint(self):
<<<<<<< HEAD
        self.scribbleArea.is_pressed(True)
        self.all_button_white()
        self.button_list[0].setStyleSheet('background-color: red;')


    def move1(self):
        self.scribbleArea.is_pressed(False)
        self.all_button_white()
        self.button_list[1].setStyleSheet('background-color: red;')
=======
        self.button_list[0].setStyleSheet('background-color: red;')
    def move(self):
        pass

    def move1(self):
        pass
>>>>>>> main

    def marquee(self):
        self.all_button_white()
        self.button_list[2].setStyleSheet('background-color: red;')

    def lasso(self):
        self.all_button_white()
        self.button_list[3].setStyleSheet('background-color: red;')

    def crop(self):
        self.all_button_white()
        self.button_list[4].setStyleSheet('background-color: red;')

    def eyedropper(self):
        self.all_button_white()
        self.button_list[5].setStyleSheet('background-color: red;')

    def eraser(self):
        self.all_button_white()
        self.button_list[6].setStyleSheet('background-color: red;')

    def type(self):
        self.all_button_white()
        self.button_list[7].setStyleSheet('background-color: red;')

    def image_converter(self):
        self.all_button_white()
        self.button_list[8].setStyleSheet('background-color: red;')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = PhotoshopEditor()
    win.show()
    sys.exit(app.exec_())
