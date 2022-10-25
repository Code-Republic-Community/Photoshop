import sys
from PyQt5 import QtWidgets, QtCore, QtGui

app = QtWidgets.QApplication(sys.argv)


class LoadScreen(object):
    def setup_ui(self, main_obj):
        if main_obj.objectName():
            main_obj.setObjectName('SplashScreen')
        main_obj.resize(680, 400)
        main_obj.setWindowIcon(QtGui.QIcon('../content/logo.png'))
        central_widget = QtWidgets.QWidget(main_obj)
        central_widget.setObjectName('central_widget')
        vertical_layout = QtWidgets.QVBoxLayout(central_widget)
        vertical_layout.setSpacing(0)
        vertical_layout.setObjectName('vertical_Layout')
        vertical_layout.setContentsMargins(10, 10, 10, 10)
        drop_shadow_frame = QtWidgets.QFrame(central_widget)
        drop_shadow_frame.setObjectName('dropShadowFrame')
        drop_shadow_frame.setStyleSheet('QFrame {	\n'
                                        '	background-color: rgb(56, 58, 89);	\n'
                                        '	color: rgb(220, 220, 220);\n'
                                        '	border-radius: 10px;\n'
                                        '}')
        drop_shadow_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        drop_shadow_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        label_title = QtWidgets.QLabel(drop_shadow_frame)
        label_title.setObjectName('label_title')
        label_title.setGeometry(QtCore.QRect(0, 90, 661, 61))
        font = QtGui.QFont()
        font.setFamily('Segoe UI')
        font.setPointSize(40)
        label_title.setFont(font)
        label_title.setStyleSheet('color: rgb(254, 121, 199);')
        label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_description = QtWidgets.QLabel(drop_shadow_frame)
        self.label_description.setObjectName('label_description')
        self.label_description.setGeometry(QtCore.QRect(0, 150, 661, 31))
        font1 = QtGui.QFont()
        font1.setFamily('Segoe UI')
        font1.setPointSize(14)
        self.label_description.setFont(font1)
        self.label_description.setStyleSheet('color: rgb(98, 114, 164);')
        self.label_description.setAlignment(QtCore.Qt.AlignCenter)
        self.progress_bar = QtWidgets.QProgressBar(drop_shadow_frame)
        self.progress_bar.setObjectName('progressBar')
        self.progress_bar.setGeometry(QtCore.QRect(50, 280, 561, 23))
        self.progress_bar.setStyleSheet('QProgressBar {\n'
                                        '	\n'
                                        '	background-color: rgb(98, 114, 164);\n'
                                        '	color: rgb(200, 200, 200);\n'
                                        '	border-style: none;\n'
                                        '	border-radius: 10px;\n'
                                        '	text-align: center;\n'
                                        '}\n'
                                        'QProgressBar::chunk{\n'
                                        '	border-radius: 10px;\n'
                                        '	background-color: '
                                        '   qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, '
                                        '   y2:0.523, stop:0 rgba(254, 121, 199, 255), '
                                        '   stop:1 rgba(170, 85, 255, 255));\n'
                                        '}')
        self.progress_bar.setValue(24)
        label_loading = QtWidgets.QLabel(drop_shadow_frame)
        label_loading.setObjectName('label_loading')
        label_loading.setGeometry(QtCore.QRect(0, 320, 661, 21))
        font2 = QtGui.QFont()
        font2.setFamily('Segoe UI')
        font2.setPointSize(12)
        label_loading.setFont(font2)
        label_loading.setStyleSheet('color: rgb(98, 114, 164);')
        label_loading.setAlignment(QtCore.Qt.AlignCenter)
        label_credits = QtWidgets.QLabel(drop_shadow_frame)
        label_credits.setObjectName('label_credits')
        label_credits.setGeometry(QtCore.QRect(20, 350, 621, 21))
        font3 = QtGui.QFont()
        font3.setFamily('Segoe UI')
        font3.setPointSize(10)
        label_credits.setFont(font3)
        label_credits.setStyleSheet('color: rgb(98, 114, 164);')
        label_credits.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)

        vertical_layout.addWidget(drop_shadow_frame)
        main_obj.setCentralWidget(central_widget)
        QtCore.QMetaObject.connectSlotsByName(main_obj)

        main_obj.setWindowTitle(QtCore.QCoreApplication.translate(
            'SplashScreen', 'Photoshop Clone', None))
        label_title.setText(QtCore.QCoreApplication.translate(
            'SplashScreen', '<strong>Photoshop</strong> Clone', None))
        self.label_description.setText(QtCore.QCoreApplication.translate(
            'SplashScreen', '<strong>Photo Editing</strong> Application', None))
        label_loading.setText(QtCore.QCoreApplication.translate(
            'SplashScreen', 'loading...', None))
        label_credits.setText(QtCore.QCoreApplication.translate(
            'SplashScreen', '<strong>Created</strong>: G.Nersisyan & M.Davitavyan', None))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    frame = QtWidgets.QMainWindow()
    ui = LoadScreen()
    ui.setup_ui(frame)
    frame.show()
    sys.exit(app.exec_())
