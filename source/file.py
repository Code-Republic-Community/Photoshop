import sys

from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QWidget, QMainWindow
#from source.photoshop_editor import PhotoshopEditor


class File(QMainWindow):
    def __init__(self):
        super(File, self).__init__()
        #self.obj = PhotoshopEditor()


    def new(self,obj):
        pass


    def open(self,obj):
        fileName, _ = QFileDialog.getOpenFileName(obj, "Open File", QDir.currentPath(),
                                                  "Image files (*.jpg *.png)")
        if fileName:
            obj.scribbleArea.openImage(fileName)



    def save(self, obj):
        #from source.photoshop_editor import PhotoshopEditor
        #obj = PhotoshopEditor()
        print(obj)
        obj.button_list[1].setStyleSheet('background-color: blue;')

    def save_as(self,obj):
        pass


    def print(self,obj):
        pass


    def close(self,obj):
        from source.photoshop_editor import PhotoshopEditor
        obj = PhotoshopEditor()
        close = QMessageBox.question(obj,
                                     "QUIT",
                                     "Are you sure want to close the program?",
                                     QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            exit()
