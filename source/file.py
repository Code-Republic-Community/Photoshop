import sys

from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QWidget, QMainWindow
#from source.photoshop_editor import PhotoshopEditor


class File(QMainWindow):
    def __init__(self):
        super(File, self).__init__()
        self.filename = ''
        #self.obj = PhotoshopEditor()


    def new(self,obj):
        pass


    def open(self,obj):
        self.fileName, _ = QFileDialog.getOpenFileName(obj, "Open File", QDir.currentPath(),
                                                  "Image files (*.jpg *.png)")
        if self.fileName:
            obj.scribbleArea.openImage(self.fileName)



    def save(self, obj):
        try:
            if self.fileName == '':
                self.fileName = 'C:/Users/m_sor/Desktop/untitled.png'
        except:
            self.fileName = 'C:/Users/m_sor/Desktop/untitled.png'
        print(self.fileName)
        fileFormat = self.fileName[len(self.fileName) - 4:]
        initialPath = self.fileName
        print(self.fileName)
        fileName, _ = QFileDialog.getSaveFileName(obj, "Save", initialPath,
                "%s Files (*.%s);;All Files (*)" % (fileFormat.upper(), fileFormat))
        if fileName:
            return obj.scribbleArea.saveImage(fileName, fileFormat)

        return False

    def save_as(self, obj):
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
