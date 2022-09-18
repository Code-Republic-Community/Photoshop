from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog

class Help(QDialog):

    def setupUi(self, help):
        help.setObjectName("Help")
        help.setWindowIcon(QIcon('../content/photoshop.png'))
        help.resize(682, 556)
        help.setMinimumSize(QtCore.QSize(682, 556))
        vertical_layout = QtWidgets.QVBoxLayout(help)
        vertical_layout.setObjectName("verticalLayout")
        scroll_area = QtWidgets.QScrollArea(help)
        scroll_area.setWidgetResizable(True)
        scroll_area.setObjectName("scrollArea")
        scroll_area_widget_contents = QtWidgets.QWidget()
        scroll_area_widget_contents.setGeometry(QtCore.QRect(0, 0, 656, 530))
        scroll_area_widget_contents.setObjectName("scrollAreaWidgetContents")
        horizontal_layout = QtWidgets.QHBoxLayout(scroll_area_widget_contents)
        horizontal_layout.setObjectName("horizontalLayout")
        frame = QtWidgets.QFrame(scroll_area_widget_contents)
        frame.setMinimumSize(QtCore.QSize(613, 500))
        frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame.setFrameShadow(QtWidgets.QFrame.Raised)
        frame.setObjectName("frame")
        grid_layout = QtWidgets.QGridLayout(frame)
        grid_layout.setObjectName("gridLayout")
        label = QtWidgets.QLabel(frame)
        label.setText("")
        label.setObjectName("label")
        grid_layout.addWidget(label, 5, 0, 1, 1)
        spacer_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        grid_layout.addItem(spacer_item, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(frame)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("font: italic 18pt \"Gill Sans\";")
        self.label_3.setObjectName("label_3")
        grid_layout.addWidget(self.label_3, 1, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_2 = QtWidgets.QLabel(frame)
        self.label_2.setStyleSheet("font: italic 24pt \"Gill Sans\";")
        self.label_2.setObjectName("label_2")
        grid_layout.addWidget(self.label_2, 0, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        horizontal_layout.addWidget(frame)
        scroll_area.setWidget(scroll_area_widget_contents)
        vertical_layout.addWidget(scroll_area)
        self.retranslateUi(help)
        QtCore.QMetaObject.connectSlotsByName(help)

    def retranslateUi(self, Help):
        _translate = QtCore.QCoreApplication.translate
        Help.setWindowTitle(_translate("Help", "Help"))
        self.label_3.setText(
            _translate("Help", " It\'s a Photoshop alternative that you can use. Photoshop interface and \n"
                               " photo editing feature tools are available on it."))
        self.label_2.setText(_translate("Help", "HELP"))

class Documentation(QDialog):

    def setupUi(self, Documentation):
        Documentation.setObjectName("Help")
        Documentation.setWindowIcon(QIcon('../content/photoshop.png'))
        Documentation.resize(682, 556)
        Documentation.setMinimumSize(QtCore.QSize(682, 556))
        self.verticalLayout = QtWidgets.QVBoxLayout(Documentation)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(Documentation)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 656, 530))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(613, 500))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("font: italic 18pt \"Gill Sans\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setStyleSheet("font: italic 24pt \"Gill Sans\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.retranslateUi(Documentation)
        QtCore.QMetaObject.connectSlotsByName(Documentation)

    def retranslateUi(self, Documentation):
        _translate = QtCore.QCoreApplication.translate
        Documentation.setWindowTitle(_translate("Documentation", "Documentation"))
        self.label_3.setText(
            _translate("Documentation", " It\'s a Photoshop alternative that you can use. Photoshop interface and \n"
                               " photo editing feature tools are available on it."))
        self.label_2.setText(_translate("Help", "DOCUMENTATION"))

