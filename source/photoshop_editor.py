"""This file open main window, and let you do photoshop"""

import sys

from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QVBoxLayout, QWidget, QBoxLayout
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QPen

from main_window import MainWindow


class PhotoshopEditor(MainWindow, QWidget):
    def __init__(self):
        """In the constructor is designed main window, and call main functions"""
        super().__init__()
        QWidget().__init__()
        self.setGeometry(250, 100, 900, 600)
        self.setWindowTitle("Photoshop Editor")
        self.setMinimumSize(600, 460)
        self.setWindowIcon(QIcon('content/photoshop.png'))
        self.setStyleSheet('background-color:#FFFFFF')
        self.button_list = [None] * 9
        global vbox
        vbox = QVBoxLayout()
        #vbox.addStretch()
        self.toolbar()

        #self.setLayout(vbox)


        #self.label = QLabel(self)
        #self.label.resize(860, 580)
        #self.label.move(40, 20)
        self.drawing = False
        self.lastPoint = QPoint()

        self.image = QPixmap("content/nissan-gtr.jpg")
        #self.label.setPixmap(self.image)
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
        i = 0
        for key, value in dict_buttons.items():
            self.button_list[i] = QPushButton(self)
            self.button_list[i].resize(40, 40)
            self.button_list[i].move(1, y)
            self.button_list[i].setIcon(QIcon(key))
            self.button_list[i].clicked.connect(value)
            self.button_list[i].setStyleSheet("QPushButton::hover {background-color: lightgray}")
            vbox.addWidget(self.button_list[i])
            #self.vbox.addStretch()

            y += 50
            i += 1


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.image)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() and Qt.LeftButton and self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(Qt.red, 3, Qt.SolidLine))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            self.drawing = False


    def all_button_white(self):
        for i in range(9):
            self.button_list[i].setStyleSheet('background-color: white;')

    def paint(self):
        self.all_button_white()
        self.button_list[0].setStyleSheet('background-color: red;')

    def move1(self):
        self.all_button_white()
        self.button_list[1].setStyleSheet('background-color: red;')

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
    sys.exit(app.exec_())
