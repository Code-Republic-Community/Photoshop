import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, QAction


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setGeometry(300, 150, 900, 600)
        # Initial size, user can maximize the window
        self.setMinimumSize(900, 600)
        self.setMenuBar(self.menuBar())
        self.setWindowTitle('Photoshop Clone')
        self.add_menus()
        self.show()

    def add_menus(self):
        menubar = self.menuBar()
        menu__and_actions = {
            QMenu("File",self): [QAction("New",self), QAction("Open",self), QAction("Save",self), QAction("Save as",self), QAction("Print",self), QAction("Close",self)],
            QMenu("Edit",self): [QAction("Undo",self), QAction("Redo",self), QAction("Cut",self), QAction("Copy",self), QAction("Paste",self), QAction("Clear screen",self), QAction("Keyboard shortcuts",self)],
            QMenu("Image",self): [QAction("Image size",self), QAction("Canvas size",self), QAction("Rotate left",self), QAction("Rotate right",self)],
            QMenu("Filter",self): [QAction("Blur",self), QAction("Noise",self), QAction("Distort",self), QAction("Pixelate",self)]
        }
        i = 0
        for name,actions in menu__and_actions.items():
            menubar.addMenu(name)
            for j in range(len(actions)):
                name.addAction(actions[j])

            i += 1



def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
