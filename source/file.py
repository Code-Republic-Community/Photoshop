from PyQt5 import QtWidgets, QtCore, QtGui, QtPrintSupport
import cv2 as cv

CLOSED = False


class File(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.filename = ''

    def new(self, photoshop_obj):
        photoshop_obj.is_clicked_move = False
        if photoshop_obj.scribble_area.check:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle('Photoshop Clone')
            msg_box.setWindowIcon(QtGui.QIcon('../content/logo.png'))
            msg_box.setText("The image has been modified.")
            msg_box.setInformativeText("Do you want to save your changes?")
            msg_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            msg_box.button(QtWidgets.QMessageBox.No).setMinimumSize(QtCore.QSize(60, 25))
            msg_box.button(QtWidgets.QMessageBox.No).setStyleSheet(
                "border-radius:8px;"
                "background: White;color: #D600C9"
            )
            msg_box.button(QtWidgets.QMessageBox.Yes).setMinimumSize(QtCore.QSize(60, 25))
            msg_box.button(QtWidgets.QMessageBox.Yes).setStyleSheet(
                "border-radius:8px;"
                "background:#D600C9;color: white"

            )
            return_value = msg_box.exec_()
            if return_value == msg_box.Yes:
                File.save(self, photoshop_obj)

        photoshop_obj.scribble_area.check = False

        width, height = photoshop_obj.scribble_area.get_current_window_size()
        photoshop_obj.scribble_area.image = QtGui.QImage(QtCore.QSize(width, height),
                                                         QtGui.QImage.Format_ARGB32)

        new_size = photoshop_obj.scribble_area.image.size(). \
            expandedTo(photoshop_obj.scribble_area.size())
        photoshop_obj.scribble_area.image.fill(QtCore.Qt.white)

        photoshop_obj.scribble_area.image_draw.fill(QtCore.Qt.transparent)

        photoshop_obj.scribble_area.resize_image_draw(photoshop_obj.scribble_area.image_draw,
                                                      'image_draw', new_size)

        photoshop_obj.scribble_area.update()

    def open(self, photoshop_obj):
        photoshop_obj.is_clicked_move = False
        self.filename, _ = QtWidgets.QFileDialog.getOpenFileName(photoshop_obj, 'Open File',
                                                                 QtCore.QDir.currentPath(),
                                                                 'Image files (*.jpg *.png)')

        if self.filename != '':
            img = cv.resize(cv.imread(self.filename),
                            photoshop_obj.scribble_area.get_current_window_size())
            photoshop_obj.scribble_area.open_image(img)

    def save(self, photoshop_obj):
        photoshop_obj.is_clicked_move = False
        try:
            if self.filename == '':
                pass
        except:
            self.filename = 'C'
            file_format = 'png'
            initial_path = self.filename + '/untitled.' + file_format
            filename, _ = QtWidgets.QFileDialog.getSaveFileName(photoshop_obj,
                                                                'Save', initial_path,
                                                                '%s Files (*.%s);;'
                                                                'All Files (*)' % (
                                                                    file_format.upper(),
                                                                    file_format))

            self.filename = filename
            if filename:
                photoshop_obj.scribble_area.check = False
                return photoshop_obj.scribble_area.save_image(filename, file_format)
            self.filename = ''
            return

        lst = str(self.filename).split('/')
        image_name = str(lst[-1])
        file_format = image_name[len(image_name) - 3:]
        if self.filename:
            photoshop_obj.scribble_area.check = False
            photoshop_obj.scribble_area.save_image(self.filename, file_format)

    def save_as(self, photoshop_obj):
        photoshop_obj.is_clicked_move = False
        self.filename = 'C'
        options = QtWidgets.QFileDialog.Options()
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self,
                                                            'Save File', '',
                                                            'All Files(*);; '
                                                            'PNG File(*.png) ;; '
                                                            'JPG File(*.jpg)',
                                                            options=options)
        if filename:
            photoshop_obj.scribble_area.check = False
            return photoshop_obj.scribble_area.save_image(filename, filename[-1:-4])

        lst = str(self.filename).split('/')
        image_name = str(lst[-1])
        file_format = image_name[len(image_name) - 3:]

        if self.filename:
            return photoshop_obj.scribble_area.save_image(self.filename, file_format)

    def print(self, photoshop_obj):
        photoshop_obj.is_clicked_move = False
        printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
        printer.setResolution(1200)
        printer.setFullPage(True)
        printer.setPageSize(QtGui.QPagedPaintDevice.Legal)

        dialog = QtPrintSupport.QPrintDialog(printer)
        dialog.exec_()
        img = photoshop_obj.scribble_area.merge_two_images(photoshop_obj.scribble_area.image_draw,
                                                           photoshop_obj.scribble_area.image)
        img = img.scaledToWidth(printer.pageRect().width(), QtCore.Qt.SmoothTransformation)

        painter = QtGui.QPainter()
        painter.begin(printer)
        painter.drawImage(0, 0, img)
        painter.end()

    def close_window(self, photoshop_obj, event):
        photoshop_obj.is_clicked_move = False
        global CLOSED

        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle('Photoshop Clone')
        msg_box.setWindowIcon(QtGui.QIcon('../content/logo.png'))
        msg_box.setInformativeText('Are you sure want to close the program?')
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        msg_box.button(QtWidgets.QMessageBox.No).setMinimumSize(QtCore.QSize(60, 25))
        msg_box.button(QtWidgets.QMessageBox.No).setStyleSheet(
            "border-radius:8px;"
            "background: White;color: #D600C9"
        )
        msg_box.button(QtWidgets.QMessageBox.Yes).setMinimumSize(QtCore.QSize(60, 25))
        msg_box.button(QtWidgets.QMessageBox.Yes).setStyleSheet(
            "border-radius:8px;"
            "background:#D600C9;color: white"
        )

        if not photoshop_obj.scribble_area.check:
            return_value = msg_box.exec_()
            if return_value == msg_box.Yes:
                CLOSED = True
                photoshop_obj.main_window.close()
            elif str(type(event)) == "<class 'PyQt5.QtGui.QCloseEvent'>":
                event.ignore()
        else:
            msg_box.setText("The image has been modified.")
            msg_box.setInformativeText("Do you want to save your changes?")
            return_value = msg_box.exec_()
            if return_value == msg_box.Yes:
                if photoshop_obj.scribble_area.open:
                    File.save(self, photoshop_obj)
                else:
                    File.save_as(self, photoshop_obj)
            elif type(event) == QtGui.QCloseEvent:
                event.accept()
            elif return_value == msg_box.No:
                CLOSED = True
                photoshop_obj.main_window.close()
