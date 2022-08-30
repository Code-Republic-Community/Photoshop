import sys

from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QMessageBox, QFileDialog


class File():
    def __init__(self):
        super(File, self).__init__()

    def new(self):
        pass


    def open(self):
        from source.photoshop_editor import PhotoshopEditor
        from source.scribble_area import ScribbleArea
        scribble_area = ScribbleArea()
        obj = PhotoshopEditor()
        fileName, _ = QFileDialog.getOpenFileName(obj, "Open File",
                                                  QDir.currentPath(), "Image files (*.jpg *.gif)")
        print(fileName)
        if fileName:
            scribble_area.openImage(fileName)


    def save(self):
        pass


    def save_as(self):
        pass


    def print(self):
        pass


    def close(self):
        from source.photoshop_editor import PhotoshopEditor
        obj = PhotoshopEditor()
        close = QMessageBox.question(obj,
                                     "QUIT",
                                     "Are you sure want to close the program?",
                                     QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            exit()
