import io
import sys

from PyQt5.QtCore import QPoint, Qt, QSize, QBuffer, QRect
from PyQt5.QtGui import QImage, qRgb, QPainter, QPen, QColor, QIcon, QTextCharFormat, QFont, qRgba, qRed, qGreen, qBlue, \
    QPixmap, QCursor
from PyQt5.QtWidgets import QWidget, QColorDialog, QInputDialog, QUndoStack, QApplication
import numpy as np
import cv2 as cv
from source.edit import UndoCommand
from source.buttons import Buttons
from source.buttons import TextTypeCheckbox
from source.test import Test


class ScribbleArea(QWidget):
    def __init__(self):
        super(ScribbleArea, self).__init__()

        self.setAttribute(Qt.WA_StaticContents)
        self.image = QImage(self.size(), QImage.Format_ARGB32)
        self.image_draw = QImage(self.size(), QImage.Format_ARGB32)
        # self.image_draw.fill(Qt.transparent)
        self.buttons = Buttons()
        self.pressed_button = None

        newSize = self.image.size().expandedTo(self.size())
        self.resizeImage(self.image, QSize(newSize))

        # newSize = self.image_draw.size().expandedTo(self.size())
        # self.resizeImageDraw(self.image_draw, newSize)

        # self.image_draw.fill(Qt.red)
        self.update()
        self.lastPoint = QPoint()
        self.check = False
        self.color_pen = (0, 0, 255, 255)
        self.color_text = (0, 0, 0, 255)
        self.width_pen = 3
        self.width_text = 15
        self.bold = False
        self.italic = False
        self.underline = False
        self.text = None
        self.image_width = 0
        self.image_height = 0
        self.app = None
        self.painter = QPainter()

        self.mUndoStack = QUndoStack(self)
        self.mUndoStack.setUndoLimit(20)

        self.coords = ()
        self.shape = QRect()
        self.coordinates = []
        # self.mUndoStack.canUndo()
        # self.mUndoStack.canRedo()

    def current_window_size(self):
        return self.width(), self.height()

    def openImage(self, img):
        # newSize = img.size().expandedTo(self.size())
        newSize = QSize(img.shape[0], img.shape[1])
        self.resizeImage(img, newSize)
        self.image = self.cv_to_qimage(img)
        self.update()
        return True

    def openImageDraw(self, img):
        # newSize = img.size().expandedTo(self.size())
        newSize = QSize(img.shape[0], img.shape[1])
        #Test(self.cv_to_qimage1(img)).exec()
        self.resizeImageDraw(img, newSize)
        self.image_draw = self.cv_to_qimage1(img)
        self.update()
        return True

    def resizeImage(self, image, newSize):
        # if image.size() == newSize:
        # return
        newImage = QImage(newSize, QImage.Format_ARGB32)
        newImage.fill(qRgb(255, 255, 255))
        painter = QPainter(newImage)
        image = self.cv_to_qimage(image)
        painter.drawImage(QPoint(0, 0), image)
        self.image = newImage

    def resizeImageDraw(self, image, newSize):
        newImage = QImage(newSize, QImage.Format_ARGB32)
        painter = QPainter(newImage)
        image = self.cv_to_qimage1(image)
        painter.drawImage(QPoint(0, 0), image)
        self.image_draw = newImage

    def resizeEvent(self, event):
        img = cv.resize(self.qimage_to_cv(self.image), self.current_window_size())
        img_draw = cv.resize(self.qimage_to_cv1(self.image_draw), self.current_window_size())
        self.openImage(img)
        self.openImageDraw(img_draw)
        self.image = self.cv_to_qimage(img)
        self.image_draw = self.cv_to_qimage1(img_draw)
        self.update()

        super(ScribbleArea, self).resizeEvent(event)

    def saveImage(self, fileName, fileFormat):
        visibleImage = self.image
        self.resizeImage(visibleImage, self.size())

        if visibleImage.save(fileName, fileFormat):
            return True
        return False

    def paintEvent(self, event):
        painter = QPainter(self)
        painter1 = QPainter(self)
        dirtyRect = event.rect()
        painter.drawImage(dirtyRect, self.cv_to_qimage(self.image), dirtyRect)
        #painter.setOpacity(0.1)
        # painter1.drawImage(dirtyRect, self.cv_to_qimage(self.image_text), dirtyRect)
        # self.image_draw.fill(Qt.transparent)
        painter.drawImage(dirtyRect, self.cv_to_qimage1(self.image_draw), dirtyRect)
        if self.pressed_button == "marquee":
            painter.setPen(QPen(Qt.black, 1, Qt.DotLine))
            painter.drawImage(dirtyRect, self.cv_to_qimage(self.image), dirtyRect)
            painter.drawText(150, 250, self.text)
            if not self.begin.isNull() and not self.end.isNull():
                self.shape = QRect(self.begin,self.end)
                #self.coords = self.shape.getCoords()
                #painter.drawRect(self.shape.normalized())
                painter.drawRect(QRect(self.begin, self.end).normalized())
        # myFont = QFont()
        # myFont.setBold(self.bold)
        # myFont.setItalic(self.italic)
        # myFont.setUnderline(self.underline)
        # myFont.setPointSize(self.width_text)
        # painter.setFont(myFont)
        # painter.drawText(350, 280, self.text)
        # if self.text != None:

    def mousePressEvent(self, event):
        self.make_undo_command()
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()
            # self.buttons.pos_x = event.pos().x()
            # self.buttons.pos_y = event.pos().y()
            if self.pressed_button == 'eyedropper':
                self.buttons.get_color(self, event.pos().x(), event.pos().y())
            if self.pressed_button == 'type':
                pass
            if self.pressed_button == 'paint':
                pass
            if self.pressed_button == 'marquee':
                self.begin = self.end = event.pos()
                self.update()
                super().mousePressEvent(event)
                # img_text = cv.resize(self.qimage_to_cv(self.image_draw), self.current_window_size())
                # self.image_draw = self.cv_to_qimage(img_text)

    def mouseMoveEvent(self, event):
        if self.pressed_button == 'paint':
            painter = QPainter(self.image_draw)
            painter.setPen(QPen(
                QColor(self.color_pen[0], self.color_pen[1], self.color_pen[2], self.color_pen[3]),
                self.width_pen, Qt.SolidLine))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()
            self.check = True

        if self.pressed_button == "marquee":
            self.end = event.pos()
            self.update()
            super().mouseMoveEvent(event)


        if self.pressed_button == 'eraser':
            painter1 = QPainter(self.image_draw)
            r = QRect(QPoint(), 20 * QSize())
            r.moveCenter(event.pos())
            painter1.save()
            painter1.setCompositionMode(QPainter.CompositionMode_Clear)
            painter1.eraseRect(r)
            painter1.restore()

    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            pass

    def pen_color(self):
        color_dialog = QColorDialog(self)
        color_dialog.setWindowIcon(QIcon('../content/photoshop.png'))
        self.color_pen = color_dialog.getColor().getRgb()

    def pen_width(self):
        num, ok = QInputDialog.getInt(self, "Pen width", "Choose the pen width")
        self.width_pen = num

    def make_undo_command(self):
        self.mUndoStack.push(UndoCommand(self))

    def qimage_to_cv(self, img: QImage):
        buffer = QBuffer()
        buffer.open(QBuffer.ReadWrite)
        img.save(buffer, "PNG")
        img_stream = io.BytesIO((buffer.data()))
        img = cv.imdecode(np.frombuffer(img_stream.read(), np.uint8), 1)
        return img

    def cv_to_qimage(self, img):
        if not isinstance(img, QImage):
            is_success, buffer = cv.imencode(".jpg", img)
            io_buf = io.BytesIO(buffer)
            qimg = QImage()
            qimg.loadFromData(io_buf.getvalue())
            return qimg
        return img

    def cv_to_qimage1(self, img):
        if not isinstance(img, QImage):
            # tmp = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            # _, alpha = cv.threshold(tmp, 0, 255, cv.THRESH_BINARY)
            # b, g, r = cv.split(img)
            # rgba = [b, g, r, alpha]
            # img = cv.merge(rgba, 4)
            #print(type(img))
            #cv.imwrite("my_png.png", img)
            # is_success, buffer = cv.imencode(".jpg", img)
            # io_buf = io.BytesIO(buffer)
            # qimg = QImage(self.size(), QImage.Format_ARGB32)
            # qimg.loadFromData(io_buf.getvalue())

            # RGBImg = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            # qimg = QImage(RGBImg, RGBImg.shape[1], RGBImg.shape[0], QImage.Format_RGB888)
            if self.pressed_button != 'paint':
                imgDown = cv.pyrDown(img)
                imgDown = np.float32(imgDown)
                cvRGBImg = cv.cvtColor(imgDown, cv.COLOR_RGB2BGR)
                a, b = self.current_window_size()
                print(b)
                print(cvRGBImg.shape[0])
                qimg = QImage(cvRGBImg.data, a, b - 150, QImage.Format_RGBA8888)
            else:
                is_success, buffer = cv.imencode(".jpg", img)
                io_buf = io.BytesIO(buffer)
                qimg = QImage(self.size(), QImage.Format_ARGB32)
                qimg.loadFromData(io_buf.getvalue())

            # qimg = QImage(img, img.shape[1], \
            #                      img.shape[0], img.shape[1] * 3, QImage.Format_RGB888)

            # alpha = cv.CreateMat(img.height, img.width, cv.CV_8UC1)
            # cv.Rectangle(alpha, (0, 0), (img.width, img.height), cv.ScalarAll(255), -1)
            # rgba = cv.CreateMat(img.height, img.width, cv.CV_8UC4)
            # cv.Set(rgba, (1, 2, 3, 4))
            # cv.MixChannels([img, alpha], [rgba], [
            #     (0, 0),  # rgba[0] -> bgr[2]
            #     (1, 1),  # rgba[1] -> bgr[1]
            #     (2, 2),  # rgba[2] -> bgr[0]
            #     (3, 3)  # rgba[3] -> alpha[0]
            # ])
            # self.__imagedata = rgba.tostring()
            # qimg = QImage(self.__imagedata, img.width, img.height, QImage.Format_RGB32)

            #Test(qimg).exec()
            return qimg
        return img

    def qimage_to_cv1(self, img: QImage):
        if self.pressed_button == 'paint':
            print("A")
            img = img.convertToFormat(4)
            width = img.width()
            height = img.height()
            ptr = img.bits()
            ptr.setsize(img.byteCount())
            arr = np.array(ptr).reshape(height, width, 4)
            cv.imwrite("my_png.png", arr)
            return arr
        buffer = QBuffer()
        buffer.open(QBuffer.ReadWrite)
        img.save(buffer, "PNG")
        img_stream = io.BytesIO((buffer.data()))
        img = cv.imdecode(np.frombuffer(img_stream.read(), np.uint8), 1)
        tmp = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        _, alpha = cv.threshold(tmp, 0, 255, cv.THRESH_BINARY)
        b, g, r = cv.split(img)
        rgba = [b, g, r, alpha]
        img = cv.merge(rgba, 4)
        cv.imwrite("test.png", img)
        return img

        # Create an empty image using numpy
        # cv_image = np.zeros((img.height(), img.width(), 3), dtype=np.uint8)
        # cv.imwrite('b.png', cv_image)
        # print('begin cv_image type:', type(cv_image))
        # for row in range(0, img.height()):
        #     for col in range(0, img.width()):
        #         r = qRed(img.pixel(col, row))
        #         g = qGreen(img.pixel(col, row))
        #         b = qBlue(img.pixel(col, row))
        #         # cv_image[row, col, 0] = r
        #         # cv_image[row, col, 1] = g
        #         # cv_image[row, col, 2] = b
        #         cv_image[row, col, 0] = b
        #         cv_image[row, col, 1] = g
        #         cv_image[row, col, 2] = r
        #
        # return cv_image
        pass

    def QimageToCVMat(self, img: QImage):
        # if img.format() == QImage.Format_ARGB32:
        #     print("a")
        #     #cv.Mat mat()
        #     cv_image = np.zeros((img.height(), img.width(), 3), dtype=np.uint8)
        #     mat = cv.Mat(cv_image)
        #     print(type(cv_image))
        #     print(type(mat))
        #     cv.imwrite('my_png.png', mat.clone())
        #img = QImage('../content/nissan-gtr.jpg')
        # print("A")
        # img = img.convertToFormat(4)
        # width = img.width()
        # height = img.height()
        # ptr = img.bits()
        # ptr.setsize(img.byteCount())
        # arr = np.array(ptr).reshape(height, width, 4)
        # cv.imwrite('test.png', arr)
        # return arr
        pass

    def qimage_to_pixmap(self, img: QImage):
        pix = QPixmap(600, 600)
        pix = pix.fromImage(img)
        pix.fill(Qt.transparent)
        return pix

    def pixmap_to_qimage(self, img):
        qimage = img.toImage().convertToFormat(QImage().Format_ARGB32)
        return qimage


