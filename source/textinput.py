
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(530, 415)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("background: #686868")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.font = QtWidgets.QFontComboBox(Dialog)
        self.font.setObjectName("font")
        self.horizontalLayout_2.addWidget(self.font)
        self.fontsize = QtWidgets.QSlider(Dialog)
        self.fontsize.setOrientation(QtCore.Qt.Horizontal)
        self.fontsize.setObjectName("fontsize")
        self.horizontalLayout_2.addWidget(self.fontsize)
        self.bold = QtWidgets.QPushButton(Dialog)
        self.bold.setMaximumSize(QtCore.QSize(24, 24))
        self.bold.setStyleSheet("background-color: #FF7DF7;\n"
"border-radius:8px\n"
"")
        self.bold.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../content/font.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bold.setIcon(icon)
        self.bold.setObjectName("bold")
        self.horizontalLayout_2.addWidget(self.bold)
        self.italic = QtWidgets.QPushButton(Dialog)
        self.italic.setMaximumSize(QtCore.QSize(24, 24))
        self.italic.setStyleSheet("background-color: #FF7DF7;\n"
"border-radius:8px\n"
"")
        self.italic.setText("")
        self.italic.setIcon(icon)
        self.italic.setObjectName("italic")
        self.horizontalLayout_2.addWidget(self.italic)
        self.underline = QtWidgets.QPushButton(Dialog)
        self.underline.setMaximumSize(QtCore.QSize(24, 24))
        self.underline.setStyleSheet("background-color: #FF7DF7;\n"
"border-radius:8px\n"
"")
        self.underline.setText("")
        self.underline.setIcon(icon)
        self.underline.setObjectName("underline")
        self.horizontalLayout_2.addWidget(self.underline)
        self.color = QtWidgets.QPushButton(Dialog)
        self.color.setMaximumSize(QtCore.QSize(24, 24))
        self.color.setStyleSheet("background-color: #FF7DF7;\n"
"border-radius:8px\n"
"")
        self.color.setText("")
        self.color.setIcon(icon)
        self.color.setObjectName("color")
        self.horizontalLayout_2.addWidget(self.color)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancel = QtWidgets.QPushButton(Dialog)
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
        self.horizontalLayout.addWidget(self.cancel)
        self.accept = QtWidgets.QPushButton(Dialog)
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
        self.horizontalLayout.addWidget(self.accept)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.actionbold = QtWidgets.QAction(Dialog)
        self.actionbold.setCheckable(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../content/bold.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionbold.setIcon(icon1)
        self.actionbold.setObjectName("actionbold")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Text"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.accept.setText(_translate("Dialog", "OK"))
        self.actionbold.setText(_translate("Dialog", "bold"))
