"""This file open main window, and let you do photoshop"""

import sys
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtGui import QIcon
<<<<<<< HEAD
from PhotoshopClone.MainWindow import MainWindow


=======
from main_window import MainWindow

>>>>>>> 332aa786990e5f654400866d2c18db7ebf99193a
class PhotoshopEditor(MainWindow):
    def __init__(self):
        """In the constructor is designed main window, and call main functions"""
        super().__init__()
        self.setGeometry(250, 100, 900, 600)
        self.setWindowTitle("Photoshop Editor")
        self.setMinimumSize(600, 460)
        self.setWindowIcon(QIcon('content/photoshop.png'))
        self.setStyleSheet('background-color:#FFFFFF')
        self.button_list = [None] * 9
        self.toolbar()

        self.show()

    def toolbar(self):
        """This function is responsible for create and design buttons of tool"""

<<<<<<< HEAD
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

=======
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
>>>>>>> 332aa786990e5f654400866d2c18db7ebf99193a
        for key, value in dict_buttons.items():
            self.button_list[i] = QPushButton(self)
            self.button_list[i].resize(40, 40)
            self.button_list[i].move(1, y)
            self.button_list[i].setIcon(QIcon(key))
            self.button_list[i].clicked.connect(value)
            self.button_list[i].setStyleSheet("QPushButton::hover {background-color: lightgray}")
            y += 50
            i += 1
    def paint(self):
<<<<<<< HEAD
        self.button_list[0].setStyleSheet('background-color: red;')
    def move(self):
=======
        pass

    def move1(self):
>>>>>>> 332aa786990e5f654400866d2c18db7ebf99193a
        pass

    def marquee(self):
        pass

    def lasso(self):
        pass

    def crop(self):
        pass

    def eyedropper(self):
        pass

    def eraser(self):
        pass

    def type(self):
        pass

    def image_converter(self):
        pass

def run():
    app = QApplication(sys.argv)
    win = PhotoshopEditor()
    sys.exit(app.exec_())
run()
