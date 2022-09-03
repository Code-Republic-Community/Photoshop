import functools
import sys
from functools import partial
from source.scribble_area import ScribbleArea
from PyQt5.QtWidgets import QApplication, QPushButton, \
    QLabel, QVBoxLayout, QWidget, QBoxLayout, QMainWindow, QAction, QSizePolicy, QHBoxLayout, QMenuBar, QMenu
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QPen
from PyQt5 import QtCore, QtWidgets
import file
import edit
import image
import filter
import help
from scribble_area import ScribbleArea
from help import Help, Documentation
class PhotoshopEditor(QMainWindow):
    def __init__(self):
        super(PhotoshopEditor, self).__init__()
        self.scribbleArea = ScribbleArea()
        #QMainWindow.setCentralWidget(self,self.scribbleArea)
    def setupUi(self, MainWindow):

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

        dict_help = {'Help': self.help, 'Documentation': self.documentation
                       }

        for key, value in dict_file.items():
            extractAction = QAction(MainWindow)
            file_menu.addAction(extractAction)
            main_menu.addAction(file_menu.menuAction())
            extractAction.triggered.connect(functools.partial(value, self, self))
            extractAction.setText(_translate("MainWindow", key))


        for key, value in dict_edit.items():
            extractAction = QAction(MainWindow)
            edit_menu.addAction(extractAction)
            main_menu.addAction(edit_menu.menuAction())
            extractAction.triggered.connect(functools.partial(value, self.x, self))
            extractAction.setText(_translate("MainWindow", key))

        for key, value in dict_image.items():
            extractAction = QAction(MainWindow)
            image_menu.addAction(extractAction)
            main_menu.addAction(image_menu.menuAction())
            extractAction.triggered.connect(functools.partial(value, self.x, self))
            extractAction.setText(_translate("MainWindow", key))

        for key, value in dict_filter.items():
            extractAction = QAction(MainWindow)
            filter_menu.addAction(extractAction)
            main_menu.addAction(filter_menu.menuAction())
            extractAction.triggered.connect(functools.partial(value, self.x, self))
            extractAction.setText(_translate("MainWindow", key))

        for key, value in dict_help.items():
            extractAction = QAction(MainWindow)
            help_menu.addAction(extractAction)
            main_menu.addAction(help_menu.menuAction())
            extractAction.triggered.connect(functools.partial(value, self.x, self))
            extractAction.setText(_translate("MainWindow", key))

        file_menu.setTitle(_translate("MainWindow", "File"))
        image_menu.setTitle(_translate("MainWindow", "Edit"))
        edit_menu.setTitle(_translate("MainWindow", "Image"))
        filter_menu.setTitle(_translate("MainWindow", "Filter"))
        help_menu.setTitle(_translate("MainWindow", "Help"))

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
            #print(self.button_list[1])
            self.button_list[i].setStyleSheet("QPushButton:hover "
                                              "{background-color: lightgray}")
            self.verticalLayout.addWidget(self.button_list[i])
            i += 1


    def all_button_white(self):
        for i in range(9):
            self.button_list[i].setStyleSheet('background-color: white;')

    def paint(self):
        self.scribbleArea.is_pressed(True)
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

    def help(self,obj,obj2):
        self.window = QtWidgets.QDialog()
        self.ui = Help()
        self.ui.setupUi(self.window)
        self.window.show()
    def documentation(self,obj,obj2):
        self.window = QtWidgets.QDialog()
        self.ui = Documentation()
        self.ui.setupUi(self.window)
        self.window.show()

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    Frame = QMainWindow()
    ui = PhotoshopEditor()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())