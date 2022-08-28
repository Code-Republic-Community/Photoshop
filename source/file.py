import sys
from PyQt5.QtWidgets import QMessageBox

class File():
    def __init__(self):
        super(File, self).__init__()

    def new(self):
        pass


    def open(self):
        pass


    def save(self):
        pass


    def save_as(self):
        pass


    def print(self):
        pass


    def close(self):
        from source.photoshop_editor import PhotoshopEditor
        obj = PhotoshopEditor()
        close = QMessageBox.question(id(obj),
                                     "QUIT",
                                     "Are you sure want to close the program?",
                                     QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            exit()
