import sys

from PIL import Image
from PyQt5.QtCore import QPoint, Qt, QDir, QSize, QBuffer
from PyQt5.QtGui import QImage, qRgb, QPainter, QPen, QPagedPaintDevice
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QWidget, QMainWindow
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
import cv2 as cv

closed = False


class File(QMainWindow):
    def __init__(self):
        super().__init__()
        self.filename = ''

    def new(self, obj):
        obj.is_clicked_move = False
        if obj.scribble_area.check:
            close = QMessageBox.question(self,
                                         "QUIT",
                                         "Do you want to save changes?",
                                         QMessageBox.Yes | QMessageBox.No)
            if close == QMessageBox.Yes:
                if obj.scribble_area.open:
                    File.save(self, obj)
                else:
                    File.save_as(self, obj)
            else:
                obj.scribble_area.check = False

            width, height = obj.scribble_area.current_window_size()
            obj.scribble_area.image = QImage(QSize(width, height), QImage.Format_ARGB32)
            newSize = obj.scribble_area.image.size().expandedTo(obj.scribble_area.size())
            obj.scribble_area.resizeImage(obj.scribble_area.image, newSize)

            obj.scribble_area.image_draw = QImage(QSize(width, height), QImage.Format_ARGB32)
            # newSize = obj.scribble_area.image_draw.size().expandedTo(obj.scribble_area.size())
            obj.scribble_area.resizeImageDraw(obj.scribble_area.image_draw, newSize)

            obj.scribble_area.update()

    def open(self, obj):
        obj.is_clicked_move = False
        self.filename, _ = QFileDialog.getOpenFileName(obj, "Open File", QDir.currentPath(),
                                                       "Image files (*.jpg *.png *.gif)")

        if self.filename != '':
            # if self.filename[-3:] == 'gif':
            #     point_index = self.filename.rindex('.')
            #     Image.open(self.filename).convert('RGB'). \
            #         save(f'{self.filename[:point_index + 1]}png')

            img = cv.resize(cv.imread(self.filename), obj.scribble_area.current_window_size())
            if self.filename:
                obj.scribble_area.openImage(img)
            obj.scribble_area.check = True

    def save(self, obj):
        obj.is_clicked_move = False
        try:
            if self.filename == '':
                self.filename = 'C'
                file_format = 'png'
                initial_path = self.filename + f'/untitled.' + file_format
                filename, _ = QFileDialog.getSaveFileName(obj, "Save", initial_path,
                                                          "%s Files (*.%s);;All Files (*)" % (
                                                              file_format.upper(), file_format))

                self.filename = filename
                if filename:
                    return obj.scribble_area.saveImage(filename, file_format)
        except:
            self.filename = 'C'
            file_format = 'png'
            initial_path = self.filename + f'/untitled.' + file_format
            filename, _ = QFileDialog.getSaveFileName(obj, "Save", initial_path,
                                                      "%s Files (*.%s);;All Files (*)" % (
                                                          file_format.upper(), file_format))

            self.filename = filename
            if filename:
                return obj.scribble_area.saveImage(filename, file_format)
            self.filename = ''
            return

        lst = str(self.filename).split('/')
        image_name = str(lst[-1])
        file_format = image_name[len(image_name) - 3:]
        if self.filename:
            obj.scribble_area.saveImage(self.filename, file_format)

    def save_as(self, obj):
        obj.is_clicked_move = False
        self.filename = 'C'
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self,
                                                  "Save File", "", "All Files(*);; PNG File(*.png) ;; JPG File(*.jpg)",
                                                  options=options)
        if filename:
            return obj.scribble_area.saveImage(filename, filename[-1:-4])

        lst = str(self.filename).split('/')
        image_name = str(lst[-1])
        file_format = image_name[len(image_name) - 3:]

        if self.filename:
            return obj.scribble_area.saveImage(self.filename, file_format)

    @classmethod
    def print(cls, obj, obj1=None):
        obj.is_clicked_move = False
        printer = QPrinter(QPrinter.HighResolution)
        printer.setResolution(1200)
        printer.setFullPage(True)
        printer.setPageSize(QPagedPaintDevice.Legal)

        dialog = QPrintDialog(printer)
        dialog.exec_()
        im = QImage(obj.scribble_area.image)
        im = im.scaledToWidth(printer.pageRect().width(), Qt.SmoothTransformation)

        painter = QPainter()
        painter.begin(printer)
        painter.drawImage(0, 0, im)
        painter.end()

    def close_window(self, obj, event):
        obj.is_clicked_move = False
        if not obj.scribble_area.check:
            close1 = QMessageBox.question(self,
                                          "QUIT",
                                          "Are you sure want to close the program?",
                                          QMessageBox.Yes | QMessageBox.No)
            if close1 == QMessageBox.Yes:
                global closed
                closed = True
                obj.main_window.close()
            else:
                if str(type(event)) == "<class 'PyQt5.QtGui.QCloseEvent'>":
                    event.ignore()
        else:
            close = QMessageBox.question(self,
                                         "QUIT",
                                         "Do you want to save changes?",
                                         QMessageBox.Yes | QMessageBox.No)
            if close == QMessageBox.Yes:
                if obj.scribble_area.open:
                    File.save(self, obj)
                else:
                    File.save_as(self, obj)
            else:
                obj.main_window.close()
