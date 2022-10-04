import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import load_screen
import photoshop_editor
import file

COUNTER = 0


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.photoshop_obj = photoshop_editor.PhotoshopEditor()
        self.photoshop_obj.setupUi(self)

    def closeEvent(self, event):
        if not file.CLOSED:
            file.File.close_window(file.File(), self.photoshop_obj, event)


class SplashScreen(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.load_screen_obj = load_screen.LoadScreen()
        self.load_screen_obj.setup_ui(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 60))

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)

        self.load_screen_obj.label_description.setText("<strong>WELCOME</strong> TO PHOTOSHOP CLONE")

        QtCore.QTimer.singleShot(1500, lambda: self.load_screen_obj.label_description.
                                 setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000, lambda: self.load_screen_obj.label_description.
                                 setText("<strong>LOADING</strong> USER INTERFACE"))

        self.show()

    def progress(self):
        global COUNTER

        self.load_screen_obj.progress_bar.setValue(COUNTER)
        if COUNTER > 100:
            self.timer.stop()

            main = MainWindow()
            main.show()
            self.close()
        COUNTER += 1


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
