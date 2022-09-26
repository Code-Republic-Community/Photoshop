from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QLabel


class Help(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(665, 585)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 639, 559))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setScaledContents(False)
        self.label_4.setWordWrap(False)
        self.label_4.setOpenExternalLinks(False)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Help"))
        self.label_2.setText(_translate("Dialog", "Help"))
        self.label_4.setText(_translate("Dialog", "It\'s a Photoshop alternative that you can use. Photoshop interface and \n"
"photo editing feature tools are available on it."))

        dictionary_shortcuts = [
            'New : New blank window', 'Open : Open an image file.' , 'Save : Replace the uploaded image with a new image' ,
            'Save as : Save the image on screen into the selected file format' , 'Print : Print the picture that you are currently viewing',
            'Close : Quit the program' , 'Undo : It erases the last change done to the image' , 'Redo : Restores something undone' ,
            'Cut : The removal of unwanted outer areas from a image' , 'Copy : Copying part of an image' , 'Paste a copied area on your image',
            'Clear screen : Clears the scribble area' , 'Keyboard shortcuts : Show the list of shortcuts' , 'Image size : Changes the image size' ,
            'Canvas size : Changes the canvas size' , 'Rotate left : Rotates the image 90 degrees to the left', 'Rotate right : Rotates the image 90 degrees to the right',
            'Blur : Blur refers to the part of an image that is out of focus', 'Noise : Random variation of brightness or color information in images',
            'Twirling spirals :  Applies a swirling pattern to the image', 'Pixelate : Cause an image to break up into pixels, as by oversizing the image',
            'Help : Help window', 'Documentation : Software documentation', 'Paint : Paint on the image, also you can choose the width and color',
            'Move : Move the text or a copied image', 'Select : Select a part of an image', 'Lasso : Lasso select erases the selected area',
            'Crop : Crops the image and keeps only the selected part', 'Eyedropper : Click a point in the image to identify and select its color',
            'Eraser : You can choose the transparent eraser or the rubber', 'Text : Put a text to the image' ,
            'Convert : Convert any image to a different format'


        ]

        for key in dictionary_shortcuts:
            my_font = QtGui.QFont()
            my_font.setFamily("Arial")
            my_font.setPointSize(14)
            my_font.setItalic(True)
            my_font.setBold(True)
            label = QLabel(self)
            label.setText(key)
            label.setFont(my_font)
            self.verticalLayout_3.addWidget(label)



class Documentation(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(665, 585)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 639, 559))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setScaledContents(False)
        self.label_4.setWordWrap(False)
        self.label_4.setOpenExternalLinks(False)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Documentation"))
        self.label_2.setText(_translate("Dialog", "Documentation"))
        self.label_4.setText(_translate("Dialog", "It\'s a Photoshop alternative that you can use. Photoshop interface and \n"
"photo editing feature tools are available on it."))

        dictionary_shortcuts = {'New': 'Ctrl+N', 'Open': 'Ctrl+O', 'Save': 'Ctrl+S',
                                'Save As': 'Ctrl+Shift+S', 'Print': 'Ctrl+P', 'Close': 'Ctrl+W',
                                'Undo': 'Ctrl+Z', 'Redo': 'Ctrl+Y', 'Cut': 'Ctrl+X', 'Copy': 'Ctrl+C',
                                'Paste': 'Ctrl+V', 'Clear screen': 'Ctrl+L',
                                'Keyboard shortcuts': 'Ctrl+K', 'Image size': 'Ctrl+Alt+I',
                                'Canvas size': 'Ctrl+Alt+C', 'Rotate left': 'Shift+Ctrl+L',
                                'Rotate right': 'Shift+Ctrl+R', 'Blur': 'Shift+Ctrl+B',
                                'Noise': 'Shift+Ctrl+N', 'Twirling spirals': 'Shift+Ctrl+P',
                                'Pixelate': 'Shift+Ctrl+P', 'Help': 'Ctrl+H', 'Documentation': 'Ctrl+D'}

        for key in dictionary_shortcuts.keys():
            my_font = QtGui.QFont()
            my_font.setFamily("Arial")
            my_font.setPointSize(14)
            my_font.setItalic(True)
            my_font.setBold(True)
            label = QLabel(self)
            label.setText(key)
            label.setFont(my_font)
            self.verticalLayout_3.addWidget(label)

