"""This file open main window, and let you do photoshop"""

import sys
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtGui import QIcon
from source.main_window import MainWindow

class PhotoshopEditor(MainWindow):
    def __init__(self):
        """In the constructor is designed main window, and call main functions"""
        super().__init__()
        self.setGeometry(250, 100, 900, 600)
        self.setWindowTitle("Photoshop Editor")
        self.setMinimumSize(600, 460)
        self.setWindowIcon(QIcon('content/photoshop.png'))
        self.setStyleSheet('background-color:#FFFFFF')
        self.toolbar()

        self.show()

    def toolbar(self):
        """This function is responsible for create and design buttons of tool"""

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
        for key, value in dict_buttons.items():
            self.button = QPushButton(self)
            self.button.resize(40, 40)
            self.button.move(1, y)
            self.button.setIcon(QIcon(key))
            self.button.clicked.connect(value)
            self.button.setStyleSheet("QPushButton::hover {background-color: lightgray}")
            y += 50

    def paint(self):
        pass

    def move1(self):
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
