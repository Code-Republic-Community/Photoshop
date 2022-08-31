import sys
from PyQt5.QtCore import QPoint, Qt, QDir, QSize
from PyQt5.QtGui import QImage, qRgb, QPainter, QPen
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QWidget, QMainWindow
from scribble_area import ScribbleArea
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog


class File(QMainWindow):
    def __init__(self):
        super(File, self).__init__()
        #self.obj = PhotoshopEditor()


    def new(self,obj):
        from photoshop_editor import PhotoshopEditor
        pht_obj = PhotoshopEditor()
        if obj.scribbleArea.check:
            close = QMessageBox.question(pht_obj,
                                         "QUIT",
                                         "Do you want to save changes?",
                                         QMessageBox.Yes | QMessageBox.No)
            if close == QMessageBox.Yes:
                print("File saved")
                obj.scribbleArea.image = QImage()
                newSize = obj.scribbleArea.image.size().expandedTo(obj.scribbleArea.size())
                obj.scribbleArea.resizeImage(obj.scribbleArea.image, newSize)
                obj.scribbleArea.update()
                obj.scribbleArea.check = False

            else:
                obj.scribbleArea.image = QImage()
                newSize = obj.scribbleArea.image.size().expandedTo(obj.scribbleArea.size())
                obj.scribbleArea.resizeImage(obj.scribbleArea.image, newSize)
                obj.scribbleArea.update()
                obj.scribbleArea.check = False

    def open(self,obj):
        fileName, _ = QFileDialog.getOpenFileName(obj, "Open File", QDir.currentPath(),
                                                  "Image files (*.jpg *.png)")
        if fileName:
            obj.scribbleArea.openImage(fileName)



    def save(self, obj):
        pass

    def save_as(self,obj):
        filename = QFileDialog.getSaveFileName(self,
                                               self.tr("Save project as..."),
                                               ".",
                                               self.tr("PNG Image (*.png), JPG Image (*jpg)"))[0]
        if filename:
            pass

    def print(self,obj):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.scribbleArea.image.print_(printer)


    def close(self,obj):
        from source.photoshop_editor import PhotoshopEditor
        obj = PhotoshopEditor()
        close = QMessageBox.question(obj,
                                     "QUIT",
                                     "Are you sure want to close the program?",
                                     QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            exit()
