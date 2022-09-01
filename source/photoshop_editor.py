from PyQt5 import QtCore, QtGui, QtWidgets
import functools
import sys
from functools import partial
from source.scribble_area import ScribbleArea
from PyQt5.QtWidgets import QApplication, QPushButton, \
    QLabel, QVBoxLayout, QWidget, QBoxLayout, QMainWindow, QAction
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QPen
from PyQt5 import QtCore
import file
import edit
import image
import filter
from scribble_area import  ScribbleArea
class PhotoshopEditor(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 572)
        MainWindow.setMinimumSize(QtCore.QSize(800, 572))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_list = [None] * 9

        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("background:black\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNesssw")
        self.menuFile.addAction(self.actionNew)
        self.menubar.addAction(self.menuFile.menuAction())
        self.toolbar()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        main_menu = QtWidgets.QMenuBar(MainWindow)
        main_menu.setGeometry(QtCore.QRect(0, 0, 800, 24))
        MainWindow.setMenuBar(main_menu)
        file_menu = QtWidgets.QMenu(main_menu)
        edit_menu = QtWidgets.QMenu(main_menu)
        image_menu = QtWidgets.QMenu(main_menu)
        filter_menu = QtWidgets.QMenu(main_menu)
        _translate = QtCore.QCoreApplication.translate
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
        self.x = ScribbleArea()

        for key, value in dict_file.items():
            extractAction = QtWidgets.QAction(MainWindow)
            file_menu.addAction(extractAction)
            main_menu.addAction(file_menu.menuAction())
            extractAction.triggered.connect(functools.partial(value,self.x,self))
            extractAction.setText(_translate("MainWindow", key))


        for key, value in dict_edit.items():
            extractAction = QtWidgets.QAction(MainWindow)
            edit_menu.addAction(extractAction)
            main_menu.addAction(edit_menu.menuAction())
            extractAction.triggered.connect(functools.partial(value, self.x, self))
            extractAction.setText(_translate("MainWindow", key))

        for key, value in dict_image.items():
            extractAction = QtWidgets.QAction(MainWindow)
            image_menu.addAction(extractAction)
            main_menu.addAction(image_menu.menuAction())
            extractAction.triggered.connect(functools.partial(value, self.x, self))
            extractAction.setText(_translate("MainWindow", key))

        for key, value in dict_filter.items():
            extractAction = QtWidgets.QAction(MainWindow)
            filter_menu.addAction(extractAction)
            main_menu.addAction(filter_menu.menuAction())
            extractAction.triggered.connect(functools.partial(value, self.x, self))
            extractAction.setText(_translate("MainWindow", key))

        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        file_menu.setTitle(_translate("MainWindow", "File"))
        image_menu.setTitle(_translate("MainWindow", "Edit"))
        edit_menu.setTitle(_translate("MainWindow", "Image"))
        filter_menu.setTitle(_translate("MainWindow", "Filter"))

    def toolbar(self):
        """This function is responsible for create and design buttons of tool"""
        dict_buttons = {'../content/paint-brush.png': self.paint,
                        '../content/move.png': self.move1,
                        '../content/marquee.png': self.marquee,
                        '../content/lasso.png': self.lasso,
                        '../content/crop.png': self.crop,
                        '../content/eyedropper.png': self.eyedropper,
                        '../content/eraser.png': self.eraser,
                        '../content/font.png': self.type,
                        '../content/recovery.png': self.image_converter}
        y = 20
        i = 0
        for key, value in dict_buttons.items():
            self.button_list[i] = QtWidgets.QPushButton(self.centralwidget)

            self.button_list[i].setMaximumSize(QtCore.QSize(50, 50))
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.button_list[i].sizePolicy().hasHeightForWidth())
            self.button_list[i].setSizePolicy(sizePolicy)
            self.button_list[i].setMaximumSize(QtCore.QSize(50, 50))
            self.button_list[i].setIcon(QIcon(key))
            self.button_list[i].clicked.connect(value)
            #print(self.button_list[1])
            self.button_list[i].setStyleSheet("QPushButton:hover "
                                              "{background-color: lightgray}")
            self.verticalLayout.addWidget(self.button_list[i])
            i += 1


    def all_button_white(self):
        for i in range(9):
            self.button_list[i].setStyleSheet('background-color: white;')

    def paint(self):
        self.x.is_pressed(True)
        self.all_button_white()
        self.button_list[0].setStyleSheet('background-color: red;')


    def move1(self):
        self.scribbleArea.is_pressed(False)
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

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QMainWindow()
    ui = PhotoshopEditor()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())