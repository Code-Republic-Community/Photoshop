from PyQt5 import QtCore, QtGui, QtWidgets


class Help(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(624, 441)
        Dialog.setStyleSheet("background: #686868")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(2)
        font.setKerning(False)
        self.scrollArea.setFont(font)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setMidLineWidth(1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 596, 1328))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_2.setMaximumSize(QtCore.QSize(70, 400))
        self.line_2.setStyleSheet("background: #FF7DF7;")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_3.addWidget(self.line_3)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setEnabled(True)
        self.line.setMaximumSize(QtCore.QSize(80, 70))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.line.setFont(font)
        self.line.setStyleSheet("background: #FF7DF7;\n"
                                "border-radius:20px\n"
                                "")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(0)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.line_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_3.addWidget(self.line_4)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.line_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_5.setMaximumSize(QtCore.QSize(90, 90))
        self.line_5.setStyleSheet("background: #FF7DF7")
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_3.addWidget(self.line_5)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.line_6 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_3.addWidget(self.line_6)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.line_7 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_7.setMaximumSize(QtCore.QSize(100, 100))
        self.line_7.setStyleSheet("background: #FF7DF7")
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_3.addWidget(self.line_7)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.line_8 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_3.addWidget(self.line_8)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.line_9 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_9.setMaximumSize(QtCore.QSize(90, 90))
        self.line_9.setStyleSheet("background: #FF7DF7")
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.verticalLayout_3.addWidget(self.line_9)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.line_10 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.verticalLayout_3.addWidget(self.line_10)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.line_11 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_11.setMaximumSize(QtCore.QSize(60, 60))
        self.line_11.setStyleSheet("background: #FF7DF7")
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.verticalLayout_3.addWidget(self.line_11)
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_3.addWidget(self.label_13)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Help"))
        self.label_2.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-size:18pt; "
                                        "color:#ffffff;\">HELP</span></p></body></html>"))
        self.label.setText(_translate("Dialog",
                                      "<html><head/><body><p><span style=\" font-style:italic; "
                                      "color:#fefdfc;\">FILE MENU</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" "
                                        "font-family:\'Helvetica Neue\'; "
                                        "font-size:14pt; font-weight:600; "
                                        "font-style:italic; color:#fdf8f8;\">New</span><span "
                                        "style=\" font-family:\'Helvetica Neue\'; "
                                        "font-size:14pt; font-style:italic; color:#fdf8f8;\"> : "
                                        "New blank window</span></p><p><span style=\" "
                                        "font-family:\'Helvetica Neue\'; font-size:14pt; "
                                        "font-weight:600; font-style:italic; "
                                        "color:#fdf8f8;\">Open</span><span style=\" "
                                        "font-family:\'Helvetica Neue\'; font-size:14pt; "
                                        "font-style:italic; color:#fdf8f8;\"> : "
                                        "Open an image file. </span></p><p><span "
                                        "style=\" font-family:\'Helvetica Neue\'; "
                                        "font-size:14pt; font-weight:600; font-style:italic; "
                                        "color:#fdf8f8;\">Save</span><span "
                                        "style=\" font-family:\'Helvetica Neue\'; "
                                        "font-size:14pt; font-style:italic; "
                                        "color:#fdf8f8;\"> : "
                                        "Replace the uploaded image with a new image</span></p>"
                                        "<p><span style=\" font-family:\'Helvetica Neue\'; "
                                        "font-size:14pt; font-weight:600; font-style:italic; "
                                        "color:#fdf8f8;\">Save as</span><span style=\" "
                                        "font-family:\'Helvetica Neue\'; font-size:14pt; "
                                        "font-style:italic; color:#fdf8f8;\"> : "
                                        "Save the image on screen into the selected file format "
                                        "</span></p><p><span style=\" font-family:\'Helvetica Neue\'; "
                                        "font-size:14pt; font-weight:600; font-style:italic; "
                                        "color:#fdf8f8;\">Print</span><span style=\" "
                                        "font-family:\'Helvetica Neue\'; font-size:14pt; "
                                        "font-style:italic; color:#fdf8f8;\"> : "
                                        "Print the picture that you are currently viewing</span></p>"
                                        "<p><span style=\" font-family:\'Helvetica Neue\'; "
                                        "font-size:14pt; font-weight:600; font-style:italic; "
                                        "color:#fdf8f8;\">Close</span><span style=\" "
                                        "font-family:\'Helvetica Neue\'; font-size:14pt; "
                                        "font-style:italic; color:#fdf8f8;\"> : "
                                        "Quit the program</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-size:14pt; font-style:italic; color:#ffffff;\">EDIT MENU</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">Undo</span><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-style:italic; color:#ffffff;\"> : It erases the last change done to the image </span></p><p><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">Redo</span><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-style:italic; color:#ffffff;\"> : Restores something undone</span></p><p><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">Cut</span><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-style:italic; color:#ffffff;\"> : The removal of unwanted outer areas from a image </span></p><p><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">Copy</span><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-style:italic; color:#ffffff;\"> : Copying part of an image</span></p><p><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">Paste</span><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-style:italic; color:#ffffff;\"> : Paste a copied area on your image</span></p><p><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">Clear screen</span><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-style:italic; color:#ffffff;\"> : Clears the scribble area</span></p><p><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">Keyboard shortcuts</span><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-style:italic; color:#ffffff;\"> : Show the list of shortcuts</span></p></body></html>"))
        self.label_6.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-size:14pt; font-style:italic; color:#fefdfb;\">IMAGE MENU</span></p></body></html>"))
        self.label_7.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">Image size</span><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-style:italic; color:#ffffff;\"> : Changes the image size</span></p><p><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">Canvas size</span><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-style:italic; color:#ffffff;\"> : Changes the canvas size</span></p><p><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">Rotate left</span><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-style:italic; color:#ffffff;\"> : Rotates the image 90 degrees to the left</span></p><p><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">Rotate right</span><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-style:italic; color:#ffffff;\"> : Rotates the image 90 degrees to the right</span></p></body></html>"))
        self.label_8.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-size:14pt; font-style:italic; color:#ffffff;\">FILTER MENU</span></p></body></html>"))
        self.label_9.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">Blur</span><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-style:italic; color:#ffffff;\"> : Blur refers to the part of an image that is out of focus</span></p><p><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">Noise</span><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-style:italic; color:#ffffff;\"> : Random variation of brightness or color information in images</span></p><p><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">Twirling spirals </span><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-style:italic; color:#ffffff;\">:  Applies a swirling pattern to the image</span></p><p><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">Pixelate</span><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-style:italic; color:#ffffff;\"> : Cause an image to break up into pixels, as by oversizing the image</span><span style=\" font-size:14pt; font-style:italic; color:#ffffff;\"/></p></body></html>"))
        self.label_10.setText(_translate("Dialog",
                                         "<html><head/><body><p><span style=\" font-size:14pt; font-style:italic; color:#ffffff;\">HELP MENU</span></p></body></html>"))
        self.label_11.setText(_translate("Dialog",
                                         "<html><head/><body><p><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">Help</span><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-style:italic; color:#ffffff;\"> : Help window</span></p><p><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">Documentation</span><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-style:italic; color:#ffffff;\"> : Software documentation</span><span style=\" font-size:14pt; font-style:italic; color:#ffffff;\"/></p></body></html>"))
        self.label_12.setText(_translate("Dialog",
                                         "<html><head/><body><p><span style=\" font-size:14pt; font-style:italic; color:#ffffff;\">TOOLS</span></p></body></html>"))
        self.label_13.setText(_translate("Dialog",
                                         "<html><head/><body><p><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">Paint</span><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-style:italic; color:#ffffff;\"> : Paint on the image, also you can choose the width and color</span></p><p><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">Move</span><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-style:italic; color:#ffffff;\"> : Move the text or a copied image </span></p><p><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">Select</span><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-style:italic; color:#ffffff;\"> : Select a part of an image</span></p><p><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">Lasso</span><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-style:italic; color:#ffffff;\"> : Lasso select erases the selected area</span></p><p><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">Crop</span><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-style:italic; color:#ffffff;\"> : Crops the image and keeps only the selected part </span></p><p><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">Eyedropper</span><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-style:italic; color:#ffffff;\"> : Click a point in the image to identify and select its color</span></p><p><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">Eraser</span><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-style:italic; color:#ffffff;\"> : You can choose the transparent eraser or the rubber</span></p><p><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">Text</span><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-style:italic; color:#ffffff;\"> : Put a text to the image</span></p><p><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">Convert</span><span style=\" font-family:\'Helvetica Neue\'; font-size:14pt; font-style:italic; color:#ffffff;\"> : Convert any image to a different format</span></p></body></html>"))


class Documentation(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(624, 413)
        Dialog.setStyleSheet("background: #686868")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(2)
        font.setKerning(False)
        self.scrollArea.setFont(font)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setMidLineWidth(1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -169, 596, 554))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_2.setMaximumSize(QtCore.QSize(70, 400))
        self.line_2.setStyleSheet("background: #FF7DF7;")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_3.addWidget(self.line_3)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setEnabled(True)
        self.line.setMaximumSize(QtCore.QSize(140, 70))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.line.setFont(font)
        self.line.setStyleSheet("background: #FF7DF7;\n"
                                "border-radius:20px\n"
                                "")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(0)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Help"))
        self.label_2.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" "
                                        "font-size:18pt; color:#ffffff;\">"
                                        "DOCUMENTATION</span></p></body></html>"))
        self.label.setText(_translate("Dialog",
                                      "<html><head/><body><p><span style=\" font-size:14pt; "
                                      "font-style:italic; color:#fefdfc;\">"
                                      "FEATURES</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog",
                                        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                        "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" "
                                        "/><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" "
                                        "font-family:\'.AppleSystemUIFont\'; "
                                        "font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; "
                                        "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                        "text-indent:0px;\"><span style=\" "
                                        "font-family:\'-apple-system,BlinkMacSystemFont,"
                                        "Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,"
                                        "Segoe UI Emoji\'; font-size:14pt; font-style:italic; "
                                        "color:#ffffff;\">Draw</span></p>\n"
                                        "<p style=\" margin-top:12px; margin-bottom:12px; "
                                        "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                        "text-indent:0px;\"><span style=\" "
                                        "font-family:\'-apple-system,BlinkMacSystemFont,"
                                        "Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,"
                                        "Segoe UI Emoji\'; font-size:14pt; font-style:italic; "
                                        "color:#ffffff;\">Image resizing</span></p>\n"
                                        "<p style=\" margin-top:12px; margin-bottom:12px; "
                                        "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                        "text-indent:0px;\"><span style=\" "
                                        "font-family:\'-apple-system,BlinkMacSystemFont,"
                                        "Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,"
                                        "Segoe UI Emoji\'; font-size:14pt; font-style:italic; "
                                        "color:#ffffff;\">Image rotating</span></p>\n"
                                        "<p style=\" margin-top:12px; margin-bottom:12px; "
                                        "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                        "text-indent:0px;\"><span style=\" "
                                        "font-family:\'-apple-system,BlinkMacSystemFont,"
                                        "Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,"
                                        "Segoe UI Emoji\'; font-size:14pt; font-style:italic; "
                                        "color:#ffffff;\">Image filters such as blur, noise, "
                                        "twirling spirals and pixelate</span></p>\n"
                                        "<p style=\" margin-top:12px; margin-bottom:12px; "
                                        "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                        "text-indent:0px;\"><span style=\" "
                                        "font-family:\'-apple-system,BlinkMacSystemFont,"
                                        "Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,"
                                        "Segoe UI Emoji\'; font-size:14pt; font-style:italic; "
                                        "color:#ffffff;\">Adding a text</span></p>\n"
                                        "<p style=\" margin-top:12px; margin-bottom:12px; "
                                        "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                        "text-indent:0px;\"><span style=\" "
                                        "font-family:\'-apple-system,BlinkMacSystemFont,"
                                        "Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,"
                                        "Segoe UI Emoji\'; font-size:14pt; font-style:italic; "
                                        "color:#ffffff;\">Converting any image to a "
                                        "different format</span></p>\n"
                                        "<p style=\" margin-top:12px; margin-bottom:12px; "
                                        "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                        "text-indent:0px;\"><span style=\" "
                                        "font-family:\'-apple-system,BlinkMacSystemFont,"
                                        "Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,"
                                        "Segoe UI Emoji\'; font-size:14pt; font-style:italic; "
                                        "color:#ffffff;\">Eraser, transparent eraser</span></p>\n"
                                        "<p style=\" margin-top:12px; margin-bottom:12px; "
                                        "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                        "text-indent:0px;\"><span style=\" "
                                        "font-family:\'-apple-system,BlinkMacSystemFont,"
                                        "Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,"
                                        "Segoe UI Emoji\'; font-size:14pt; font-style:italic; "
                                        "color:#ffffff;\">Removal of unwanted outer areas</span></p>\n"
                                        "<p style=\" margin-top:12px; margin-bottom:12px; "
                                        "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                        "text-indent:0px;\"><span style=\" "
                                        "font-family:\'-apple-system,BlinkMacSystemFont,"
                                        "Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,"
                                        "Segoe UI Emoji\'; font-size:14pt; font-style:italic; "
                                        "color:#ffffff;\">Lasso tool</span></p>\n"
                                        "<p style=\" margin-top:12px; margin-bottom:12px; "
                                        "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                        "text-indent:0px;\"><span style=\" "
                                        "font-family:\'-apple-system,BlinkMacSystemFont,"
                                        "Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,"
                                        "Segoe UI Emoji\'; font-size:14pt; font-style:italic; "
                                        "color:#ffffff;\">Paste a copied area on your "
                                        "image</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" "
                                        "font-size:14pt; font-style:italic; color:#ffffff;\">"
                                        "PACKAGES WE USED</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-size:14pt; "
                                        "font-style:italic; color:#ffffff;\">PyQt5</span></p><p>"
                                        "<span style=\" font-size:14pt; font-style:italic; "
                                        "color:#ffffff;\">OpenCV</span></p><p><span style=\" "
                                        "font-size:14pt; font-style:italic; color:#ffffff;\">"
                                        "PIL</span></p><p><span style=\" font-size:14pt; "
                                        "font-style:italic; color:#ffffff;\">Functools</span></p>"
                                        "<p><span style=\" font-size:14pt; font-style:italic; "
                                        "color:#ffffff;\">Numpy</span></p></body></html>"))
