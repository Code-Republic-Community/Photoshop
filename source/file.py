import os
import sys
from PIL import Image
from PyQt5.QtCore import QPoint, Qt, QDir, QSize
from PyQt5.QtGui import QImage, qRgb, QPainter, QPen, QPagedPaintDevice
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QWidget, QMainWindow
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog


class File(QMainWindow):
    def __init__(self):
        super(File, self).__init__()
        self.filename = ''

    def new(self, obj):
        from source.photoshop_editor import PhotoshopEditor
        self.ph_obj = PhotoshopEditor()
        if obj.scribbleArea.check:
            close = QMessageBox.question(self,
                                         "QUIT",
                                         "Do you want to save changes?",
                                         QMessageBox.Yes | QMessageBox.No)
            if close == QMessageBox.Yes:
                File.save_as(self, obj)
            else:
                obj.scribbleArea.image = QImage()
                newSize = obj.scribbleArea.image.size().expandedTo(obj.scribbleArea.size())
                obj.scribbleArea.resizeImage(obj.scribbleArea.image, newSize)
                obj.scribbleArea.update()
                obj.scribbleArea.check = False
    def open(self, obj):
        self.filename, _ = QFileDialog.getOpenFileName(obj, "Open File", QDir.currentPath(),
                                                       "Image files (*.jpg *.png)")

        im = Image.open(self.filename)
        #f, e = os.path.splitext(self.filename)
        imResize = im.resize((900, 600), Image.ANTIALIAS)
        imResize.save(self.filename, 'JPEG', quality=90)
        print(im)
        if self.filename:
            obj.scribbleArea.openImage(self.filename)
        self.check = True

    def save(self, obj):
        try:
            if self.filename == '':
                self.filename = 'C'
                fileFormat = 'png'
                initialPath = self.filename + f'/untitled.' + fileFormat
                fileName, _ = QFileDialog.getSaveFileName(obj, "Save", initialPath,
                                                          "%s Files (*.%s);;All Files (*)" % (
                                                              fileFormat.upper(), fileFormat))

                self.filename = fileName
                if fileName:
                    return obj.scribbleArea.saveImage(fileName, fileFormat)
        except:
            self.filename = 'C'
            fileFormat = 'png'
            initialPath = self.filename + f'/untitled.' + fileFormat
            fileName, _ = QFileDialog.getSaveFileName(obj, "Save", initialPath,
                                                      "%s Files (*.%s);;All Files (*)" % (
                                                          fileFormat.upper(), fileFormat))

            self.filename = fileName
            if fileName:
                return obj.scribbleArea.saveImage(fileName, fileFormat)
            self.filename = ''
            return

        lst = str(self.filename).split('/')
        image_name = str(lst[-1])
        fileFormat = image_name[len(image_name) - 3:]
        if self.filename:
            obj.scribbleArea.saveImage(self.filename, fileFormat)


    def save_as(self, obj):

        self.filename = 'C'
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self,
                                                  "Save File", "", "All Files(*);; PNG File(*.png) ;; JPG File(*.jpg)",
                                                  options=options)
        if fileName:
            return obj.scribbleArea.saveImage(fileName, fileName[-1:-4])

        lst = str(self.filename).split('/')
        image_name = str(lst[-1])
        fileFormat = image_name[len(image_name) - 3:]

        if self.filename:
            return obj.scribbleArea.saveImage(self.filename, fileFormat)


    def print(self, obj):
        from source.scribble_area import ScribbleArea
        obj_scribble = ScribbleArea()
        printer = QPrinter(QPrinter.HighResolution)
        printer.setResolution(1200)
        printer.setFullPage(True)
        printer.setPageSize(QPagedPaintDevice.Legal)

        dialog = QPrintDialog(printer)
        dialog.exec_()
        im = QImage("../content/nissan-gtr.jpg")
        im = im.scaledToWidth(printer.pageRect().width(), Qt.SmoothTransformation)

        painter = QPainter()
        painter.begin(printer)
        painter.drawImage(0, 0, im)
        painter.end()


    def close_window(self, obj1):
        from source.photoshop_editor import PhotoshopEditor
        obj = PhotoshopEditor()
        if not obj1.scribbleArea.check:
            close = QMessageBox.question(obj,
                                         "QUIT",
                                         "Are you sure want to close the program?",
                                         QMessageBox.Yes | QMessageBox.No)
            if close == QMessageBox.Yes:
                exit()
        elif obj1.scribbleArea.check:
            close = QMessageBox.question(self,
                                         "QUIT",
                                         "Do you want to save changes?",
                                         QMessageBox.Yes | QMessageBox.No)
            if close == QMessageBox.Yes:
                File.save(self, obj)
                exit()
            else:
                exit()
