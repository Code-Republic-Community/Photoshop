import functools
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self, scribble_obj):
        super().__init__()
        self.scribble_obj = scribble_obj
        self.is_bold = False
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(530, 415)
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.setAutoFillBackground(False)
        #self.setStyleSheet("background: #686868")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.font = QtWidgets.QFontComboBox(self)
        self.font.setObjectName("font")
        self.horizontalLayout_2.addWidget(self.font)
        self.font.activated[str].connect(functools.partial(self.set_font, 'text_font'))

        self.fontsize = QtWidgets.QSlider(self)
        self.fontsize.setOrientation(QtCore.Qt.Horizontal)
        self.fontsize.setObjectName("fontsize")
        self.fontsize.setMaximum(50)
        self.fontsize.valueChanged.connect(functools.partial(self.set_font, 'size'))
        self.horizontalLayout_2.addWidget(self.fontsize)

        self.bold = QtWidgets.QPushButton(self)
        self.bold.setMaximumSize(QtCore.QSize(24, 24))
        self.bold.setStyleSheet("background-color: #FF7DF7;\n"
                                "border-radius:8px\n"
                                "")
        self.bold.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../content/font.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bold.setIcon(icon)
        self.bold.setObjectName("bold")
        self.bold.clicked.connect(functools.partial(self.set_font, 'bold'))
        self.horizontalLayout_2.addWidget(self.bold)

        self.italic = QtWidgets.QPushButton(self)
        self.italic.setMaximumSize(QtCore.QSize(24, 24))
        self.italic.setStyleSheet("background-color: #FF7DF7;\n"
                                  "border-radius:8px\n"
                                  "")
        self.italic.setText("")
        self.italic.setIcon(icon)
        self.italic.setObjectName("italic")
        self.italic.clicked.connect(functools.partial(self.set_font, 'italic'))
        self.horizontalLayout_2.addWidget(self.italic)

        self.underline = QtWidgets.QPushButton(self)
        self.underline.setMaximumSize(QtCore.QSize(24, 24))
        self.underline.setStyleSheet("background-color: #FF7DF7;\n"
                                     "border-radius:8px\n")
        self.underline.setText("")
        self.underline.setIcon(icon)
        self.underline.setObjectName("underline")
        self.underline.clicked.connect(functools.partial(self.set_font, 'underline'))
        self.horizontalLayout_2.addWidget(self.underline)

        self.color = QtWidgets.QPushButton(self)
        self.color.setMaximumSize(QtCore.QSize(24, 24))
        self.color.setStyleSheet("background-color: #FF7DF7;\n"
                                 "border-radius:8px\n"
                                 "")
        self.color.setText("")
        self.color.setIcon(icon)
        self.color.setObjectName("color")
        self.color.clicked.connect(functools.partial(self.set_font, 'color'))
        self.horizontalLayout_2.addWidget(self.color)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setObjectName("textEdit")
        font = QtGui.QFont()
        font.setPointSize(self.scribble_obj.width_text)
        self.textEdit.setFont(font)
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.cancel = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(110)
        sizePolicy.setVerticalStretch(35)
        sizePolicy.setHeightForWidth(self.cancel.sizePolicy().hasHeightForWidth())
        self.cancel.setSizePolicy(sizePolicy)
        self.cancel.setMinimumSize(QtCore.QSize(110, 35))
        self.cancel.setMaximumSize(QtCore.QSize(110, 35))
        self.cancel.setAcceptDrops(False)
        self.cancel.setToolTipDuration(-1)
        self.cancel.setAutoFillBackground(False)
        self.cancel.setStyleSheet("border-radius:8px;\n"
                                  "background: White\n"
                                  "\n"
                                  "\n"
                                  "                                                    ")
        self.cancel.setAutoRepeat(False)
        self.cancel.setAutoDefault(True)
        self.cancel.setDefault(False)
        self.cancel.setFlat(False)
        self.cancel.setObjectName("cancel")
        self.cancel.clicked.connect(self.reject_window)
        self.horizontalLayout.addWidget(self.cancel)

        self.accept = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(110)
        sizePolicy.setVerticalStretch(35)
        sizePolicy.setHeightForWidth(self.accept.sizePolicy().hasHeightForWidth())
        self.accept.setSizePolicy(sizePolicy)
        self.accept.setMinimumSize(QtCore.QSize(110, 35))
        self.accept.setMaximumSize(QtCore.QSize(110, 35))
        self.accept.setAcceptDrops(False)
        self.accept.setToolTipDuration(-1)
        self.accept.setAutoFillBackground(False)
        self.accept.setStyleSheet("QPushButton{\n"
                                  "       border-radius:8px;\n"
                                  "       background:#D600C9\n"
                                  "       \n"
                                  "         }\n"
                                  "\n"
                                  "                                                    ")
        self.accept.setAutoRepeat(False)
        self.accept.setAutoDefault(True)
        self.accept.setDefault(False)
        self.accept.setFlat(False)
        self.accept.setObjectName("accept")
        self.accept.clicked.connect(self.accept_window)

        self.horizontalLayout.addWidget(self.accept)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.actionbold = QtWidgets.QAction(self)
        self.actionbold.setCheckable(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../content/bold.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionbold.setIcon(icon1)
        self.actionbold.setObjectName("actionbold")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Text"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.accept.setText(_translate("Dialog", "OK"))
        self.actionbold.setText(_translate("Dialog", "bold"))

    def set_font(self, font_type):
        font = QtGui.QFont(self.scribble_obj.text_font)
        font.setBold(self.scribble_obj.bold)
        font.setItalic(self.scribble_obj.italic)
        font.setUnderline(self.scribble_obj.underline)
        font.setPointSize(self.scribble_obj.width_text)
        self.textEdit.setStyleSheet(f'color: rgb{self.scribble_obj.color_text};')
        #font.sty(self.scribble_obj.text_font)

        if font_type == 'bold':
            if not self.scribble_obj.bold:
                self.scribble_obj.bold = True
                font.setBold(self.scribble_obj.bold)
            else:
                self.scribble_obj.bold = False
                font.setBold(self.scribble_obj.bold)
            self.textEdit.setFont(font)
        elif font_type == 'italic':
            if not self.scribble_obj.italic:
                self.scribble_obj.italic = True
                font.setItalic(self.scribble_obj.italic)
            else:
                self.scribble_obj.italic = False
                font.setItalic(self.scribble_obj.italic)
            self.textEdit.setFont(font)
        elif font_type == 'underline':
            if not self.scribble_obj.underline:
                self.scribble_obj.underline = True
                font.setUnderline(self.scribble_obj.underline)
            else:
                self.scribble_obj.underline = False
                font.setUnderline(self.scribble_obj.underline)
            self.textEdit.setFont(font)
        elif font_type == 'color':
            self.scribble_obj.color_text = QtWidgets.QColorDialog.getColor().getRgb()
            self.textEdit.setStyleSheet(f'color: rgb{self.scribble_obj.color_text};')
        elif font_type == 'text_font':
            self.scribble_obj.text_font = self.font.currentText()
            self.textEdit.setFont(QtGui.QFont(self.scribble_obj.text_font, self.scribble_obj.width_text))
        else:
            self.scribble_obj.width_text = int(self.fontsize.value())
            self.textEdit.setFont(QtGui.QFont(self.scribble_obj.text_font, self.scribble_obj.width_text))

    def accept_window(self):
        if self.textEdit.toPlainText():
            self.scribble_obj.text = self.textEdit.toPlainText()
            self.close()

    def reject_window(self):
        self.scribble_obj.text = ''
        self.close()