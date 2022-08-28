import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, QAction, QMessageBox
from source import file
from source import edit
from source import image
from source import filter


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('&File')
        edit_menu = main_menu.addMenu('&Edit')
        image_menu = main_menu.addMenu('&Image')
        filter_menu = main_menu.addMenu('&Filter')

        dict_file = {'New': file.File.new, 'Open': file.File.open,
                     'Save': file.File.save, 'Save As': file.File.save_as,
                     'Print': file.File.print, 'Close': file.File.close}

        dict_edit = {'Undo': edit.undo, 'Redo': edit.redo, 'Cut': edit.cut,
                     'Copy': edit.copy, 'Paste': edit.paste,
                     'Clear screen': edit.clear_screen,
                     'Keyboard shortcuts': edit.keyboard_shortcuts}

        dict_image = {'Image size': image.image_size, 'Canvas size': image.canvas_size,
                      'Rotate left': image.rotate_left, 'Rotate right': image.rotate_right}

        dict_filter = {'Blur': filter.blur, 'Noise': filter.noise, 'Distort': filter.distort,
                       'Pixelate': filter.pixelate}

        for key, value in dict_file.items():
            extractAction = QAction(key, self)
            file_menu.addAction(extractAction)
            extractAction.triggered.connect(value)

        for key, value in dict_edit.items():
            extractAction = QAction(key, self)
            edit_menu.addAction(extractAction)
            extractAction.triggered.connect(value)

        for key, value in dict_image.items():
            extractAction = QAction(key, self)
            image_menu.addAction(extractAction)
            extractAction.triggered.connect(value)

        for key, value in dict_filter.items():
            extractAction = QAction(key, self)
            filter_menu.addAction(extractAction)
            extractAction.triggered.connect(value)

        # self.setMenuBar(self.menuBar())
        # self.show()
        # self.menu_and_actions = {
        #     QMenu("File", self): [QAction("New", self), QAction("Open", self), QAction("Save", self),
        #                           QAction("Save as", self), QAction("Print", self), QAction("Close", self)],
        #     QMenu("Edit", self): [QAction("Undo", self), QAction("Redo", self), QAction("Cut", self),
        #                           QAction("Copy", self), QAction("Paste", self), QAction("Clear screen", self),
        #                           QAction("Keyboard shortcuts", self)],
        #     QMenu("Image", self): [QAction("Image size", self), QAction("Canvas size", self),
        #                            QAction("Rotate left", self), QAction("Rotate right", self)],
        #     QMenu("Filter", self): [QAction("Blur", self), QAction("Noise", self), QAction("Distort", self),
        #                             QAction("Pixelate", self)]
        # }
        # self.add_menus()
        # self.key = list(self.menu_and_actions.keys())
        # self.connect_actions()
    #
    # def connect_actions(self):
    #     self.menu_and_actions[self.key[0]][5].triggered.connect(self.close)
    #
    # def close(self):
    #     close = QMessageBox.question(self,
    #                                  "QUIT",
    #                                  "Are you sure want to close the program?",
    #                                  QMessageBox.Yes | QMessageBox.No)
    #     if close == QMessageBox.Yes:
    #         exit()
    #
    # def add_menus(self):
    #     menubar = self.menuBar()
    #
    #     i = 0
    #     for name, actions in self.menu_and_actions.items():
    #         menubar.addMenu(name)
    #         for j in range(len(actions)):
    #             name.addAction(actions[j])
    #
    #         i += 1

# def main():
#     app = QApplication(sys.argv)
#     ex = MainWindow()
#     ex.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()
