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
        central_widget = QtWidgets.QWidget(self)
        central_widget.resize(self.width(), self.height())

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        radius = 30
        central_widget.setStyleSheet(
            """
            background:#686868;
            border-top-left-radius:{0}px;
            border-bottom-left-radius:{0}px;
            border-top-right-radius:{0}px;
            border-bottom-right-radius:{0}px;
            """.format(radius)
        )
        vertical_layout_2 = QtWidgets.QVBoxLayout(self)
        vertical_layout_2.setObjectName("verticalLayout_2")
        vertical_layout = QtWidgets.QVBoxLayout()
        vertical_layout.setObjectName("verticalLayout")
        horizontal_layout_2 = QtWidgets.QHBoxLayout()
        horizontal_layout_2.setObjectName("horizontalLayout_2")

        self.font = QtWidgets.QFontComboBox(self)
        self.font.setObjectName("font")
        horizontal_layout_2.addWidget(self.font)
        self.font.activated[str].connect(functools.partial(self.set_font, 'text_font'))

        self.fontsize = QtWidgets.QSlider(self)
        self.fontsize.setOrientation(QtCore.Qt.Horizontal)
        self.fontsize.setObjectName("fontsize")
        self.fontsize.setMaximum(50)
        self.fontsize.setSliderPosition(15)
        self.fontsize.valueChanged.connect(functools.partial(self.set_font, 'size'))
        horizontal_layout_2.addWidget(self.fontsize)

        self.bold = QtWidgets.QPushButton(self)
        self.bold.setMaximumSize(QtCore.QSize(24, 24))
        self.bold.setStyleSheet("border-radius:8px\n")
        self.bold.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../content/bold.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bold.setIcon(icon)
        self.bold.setObjectName("bold")
        self.bold.clicked.connect(functools.partial(self.set_font, 'bold'))
        horizontal_layout_2.addWidget(self.bold)
        icon.addPixmap(QtGui.QPixmap("../content/italic.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.italic = QtWidgets.QPushButton(self)
        self.italic.setMaximumSize(QtCore.QSize(24, 24))
        self.italic.setStyleSheet("border-radius:8px\n")
        self.italic.setText("")
        self.italic.setIcon(icon)
        self.italic.setObjectName("italic")
        self.italic.clicked.connect(functools.partial(self.set_font, 'italic'))
        horizontal_layout_2.addWidget(self.italic)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../content/underline.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.underline = QtWidgets.QPushButton(self)
        self.underline.setMaximumSize(QtCore.QSize(24, 24))
        self.underline.setStyleSheet("border-radius:8px\n")
        self.underline.setText("")
        self.underline.setIcon(icon)
        self.underline.setObjectName("underline")
        self.underline.clicked.connect(functools.partial(self.set_font, 'underline'))
        horizontal_layout_2.addWidget(self.underline)
        icon.addPixmap(QtGui.QPixmap("../content/color.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        color = QtWidgets.QPushButton(self)
        color.setMaximumSize(QtCore.QSize(24, 24))
        color.setStyleSheet("border-radius:8px\n")
        color.setText("")
        color.setIcon(icon)
        color.setObjectName("color")
        color.clicked.connect(functools.partial(self.set_font, 'color'))
        horizontal_layout_2.addWidget(color)
        vertical_layout.addLayout(horizontal_layout_2)

        self.text_edit = QtWidgets.QTextEdit(self)
        self.text_edit.setObjectName("textEdit")
        font = QtGui.QFont()
        font.setPointSize(self.scribble_obj.width_text)
        self.text_edit.setFont(font)
        vertical_layout.addWidget(self.text_edit)
        horizontal_layout = QtWidgets.QHBoxLayout()
        horizontal_layout.setObjectName("horizontalLayout")
        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacer_item)

        btn_cancel = QtWidgets.QPushButton(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                            QtWidgets.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(110)
        size_policy.setVerticalStretch(35)
        size_policy.setHeightForWidth(btn_cancel.sizePolicy().hasHeightForWidth())
        btn_cancel.setSizePolicy(size_policy)
        btn_cancel.setMinimumSize(QtCore.QSize(110, 35))
        btn_cancel.setMaximumSize(QtCore.QSize(110, 35))
        btn_cancel.setAcceptDrops(False)
        btn_cancel.setToolTipDuration(-1)
        btn_cancel.setAutoFillBackground(False)
        btn_cancel.setStyleSheet("border-radius:8px;\n"
                                 "background: White;color: #D600C9\n"
                                 ""
                                 "\n"
                                 "                                                    ")
        btn_cancel.setAutoRepeat(False)
        btn_cancel.setAutoDefault(True)
        btn_cancel.setDefault(False)
        btn_cancel.setFlat(False)
        btn_cancel.setObjectName("cancel")
        btn_cancel.clicked.connect(self.reject_window)
        horizontal_layout.addWidget(btn_cancel)

        btn_accept = QtWidgets.QPushButton(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                            QtWidgets.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(110)
        size_policy.setVerticalStretch(35)
        size_policy.setHeightForWidth(btn_accept.sizePolicy().hasHeightForWidth())
        btn_accept.setSizePolicy(size_policy)
        btn_accept.setMinimumSize(QtCore.QSize(110, 35))
        btn_accept.setMaximumSize(QtCore.QSize(110, 35))
        btn_accept.setAcceptDrops(False)
        btn_accept.setToolTipDuration(-1)
        btn_accept.setAutoFillBackground(False)
        btn_accept.setStyleSheet("QPushButton{\n"
                                 "       border-radius:8px;\n"
                                 "       background:#D600C9;color: white\n"
                                 "       \n"
                                 "         }\n"
                                 "\n"
                                 "                                                    ")
        btn_accept.setAutoRepeat(False)
        btn_accept.setAutoDefault(True)
        btn_accept.setDefault(False)
        btn_accept.setFlat(False)
        btn_accept.setObjectName("accept")
        btn_accept.clicked.connect(self.accept_window)

        horizontal_layout.addWidget(btn_accept)
        vertical_layout.addLayout(horizontal_layout)
        vertical_layout_2.addLayout(vertical_layout)
        action_bold = QtWidgets.QAction(self)
        action_bold.setCheckable(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../content/bold.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        action_bold.setIcon(icon1)
        action_bold.setObjectName("actionbold")

        translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(translate("Dialog", "Text"))
        btn_cancel.setText(translate("Dialog", "Cancel"))
        btn_accept.setText(translate("Dialog", "OK"))
        action_bold.setText(translate("Dialog", "bold"))
        QtCore.QMetaObject.connectSlotsByName(self)

    def set_font(self, font_type):
        font = QtGui.QFont(self.scribble_obj.text_font)
        font.setBold(self.scribble_obj.bold)
        font.setItalic(self.scribble_obj.italic)
        font.setUnderline(self.scribble_obj.underline)
        font.setPointSize(self.scribble_obj.width_text)
        self.text_edit.setStyleSheet(f'color: rgb{self.scribble_obj.color_text};')
        # font.sty(self.scribble_obj.text_font)
        icon = QtGui.QIcon()

        if font_type == 'bold':
            if not self.scribble_obj.bold:
                self.scribble_obj.bold = True
                icon.addPixmap(QtGui.QPixmap("../content/bold_black.png"),
                               QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.bold.setIcon(icon)
                font.setBold(self.scribble_obj.bold)
            else:
                self.scribble_obj.bold = False
                icon.addPixmap(QtGui.QPixmap("../content/bold.png"),
                               QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.bold.setIcon(icon)
                font.setBold(self.scribble_obj.bold)
            self.text_edit.setFont(font)

        elif font_type == 'italic':
            if not self.scribble_obj.italic:
                self.scribble_obj.italic = True
                icon.addPixmap(QtGui.QPixmap("../content/italic_black.png"),
                               QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.italic.setIcon(icon)
                font.setItalic(self.scribble_obj.italic)
            else:
                self.scribble_obj.italic = False
                icon.addPixmap(QtGui.QPixmap("../content/italic.png"),
                               QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.italic.setIcon(icon)
                font.setItalic(self.scribble_obj.italic)
            self.text_edit.setFont(font)

        elif font_type == 'underline':
            if not self.scribble_obj.underline:
                self.scribble_obj.underline = True
                icon.addPixmap(QtGui.QPixmap("../content/underline_black.png"),
                               QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.underline.setIcon(icon)
                font.setUnderline(self.scribble_obj.underline)

            else:
                self.scribble_obj.underline = False
                icon.addPixmap(QtGui.QPixmap("../content/underline.png"),
                               QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.underline.setIcon(icon)
                font.setUnderline(self.scribble_obj.underline)
            self.text_edit.setFont(font)

        elif font_type == 'color':
            self.scribble_obj.color_text = QtWidgets.QColorDialog.getColor().getRgb()
            self.text_edit.setStyleSheet(f'color: rgb{self.scribble_obj.color_text};')
        elif font_type == 'text_font':
            self.scribble_obj.text_font = self.font.currentText()
            self.text_edit.setFont(QtGui.QFont(self.scribble_obj.text_font,
                                               self.scribble_obj.width_text))
        else:
            self.scribble_obj.width_text = int(self.fontsize.value())
            self.text_edit.setFont(QtGui.QFont(self.scribble_obj.text_font,
                                               self.scribble_obj.width_text))

    def accept_window(self):
        if self.text_edit.toPlainText():
            self.scribble_obj.text = self.text_edit.toPlainText()
            self.close()

    def reject_window(self):
        self.scribble_obj.text = ''
        self.close()
