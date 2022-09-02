import sys
from PyQt5.QtCore import QPoint, Qt, QDir, QSize
from PyQt5.QtGui import QImage, qRgb, QPainter, QPen
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QWidget, QMainWindow
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from source.scribble_area import ScribbleArea


class File(QMainWindow):
    def __init__(self):
        super(File, self).__init__()
        self.filename = ''
        #self.obj = PhotoshopEditor()


    def new(self, obj):
        if self.check:
            close = QMessageBox.question(obj,
                                         "QUIT",
                                         "Do you want to save changes?",
                                         QMessageBox.Yes | QMessageBox.No)
            if close == QMessageBox.Yes:
                print("File saved")
                self.scribbleArea.image = QImage()
                newSize = self.scribbleArea.image.size().expandedTo(obj.scribbleArea.size())
                self.resizeImage(obj.scribbleArea.image, newSize)
                self.update()
                self.check = False


            else:
                obj.scribbleArea.image = QImage()
                newSize = obj.scribbleArea.image.size().expandedTo(obj.scribbleArea.size())
                obj.scribbleArea.resizeImage(obj.scribbleArea.image, newSize)
                obj.scribbleArea.update()
                obj.scribbleArea.check = False

    def open(self, obj):
        self.filename, _ = QFileDialog.getOpenFileName(obj, "Open File", QDir.currentPath(),
                                                  "Image files (*.jpg *.png)")
        if self.filename:
            obj.scribbleArea.openImage(self.filename)
        self.check = True

    def save(self, obj):
        try:
            if self.filename == '':
                pass
        except:
            self.filename = 'C'
            fileFormat = 'png'
            initialPath = self.filename + f'/untitled.' + fileFormat
            fileName, _ = QFileDialog.getSaveFileName(obj, "Save", initialPath,
                    "%s Files (*.%s);;All Files (*)" % (fileFormat.upper(), fileFormat))
            if fileName:
                return obj.scribbleArea.saveImage(fileName, fileFormat)

        lst = str(self.filename).split('/')
        image_name = str(lst[-1])
        fileFormat = image_name[len(image_name) - 3:]
        #image_name = image_name[:len(image_name) - 4]
        #initialPath = self.filename + f'/{image_name}.' + fileFormat
        # fileName, _ = QFileDialog.getSaveFileName(obj, "Save", initialPath,
        #                     "%s Files (*.%s);;All Files (*)" % (fileFormat.upper(), fileFormat))

        if self.filename:
            return obj.scribbleArea.saveImage(self.filename, fileFormat)


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
            obj.scribbleArea.image.print_(printer)


    def close(self,obj_close):
        from source.photoshop_editor import PhotoshopEditor
        obj = PhotoshopEditor()
        close = QMessageBox.question(obj,
                                     "QUIT",
                                     "Are you sure want to close the program?",
                                     QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            exit()
