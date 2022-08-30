from PyQt5.QtCore import QPoint, Qt, QDir, QSize
from PyQt5.QtGui import QImage, qRgb, QPainter, QPen
from PyQt5.QtWidgets import QWidget, QLabel


class ScribbleArea(QWidget):
    def __init__(self):
        super(ScribbleArea, self).__init__()

        self.setAttribute(Qt.WA_StaticContents)
        self.modified = False
        self.scribbling = False
        self.myPenWidth = 1
        self.myPenColor = Qt.blue
        self.image = QImage()
        self.pressed = False
        newSize = self.image.size().expandedTo(self.size())
        self.resizeImage(self.image, newSize)
        self.lastPoint = QPoint()

    def is_pressed(self, value):
        self.pressed = value
        return self.pressed

    def openImage(self, fileName):
        loadedImage = QImage()
        if not loadedImage.load(fileName):
            return False
        newSize = loadedImage.size().expandedTo(self.size())
        self.resizeImage(loadedImage, newSize)
        self.image = loadedImage
        self.modified = False
        self.update()
        return True

    def resizeImage(self, image, newSize):
        if image.size() == newSize:
            return

        newImage = QImage(newSize, QImage.Format_RGB32)
        newImage.fill(qRgb(255, 255, 255))
        painter = QPainter(newImage)
        painter.drawImage(QPoint(40, 0), image)
        self.image = newImage

    def paintEvent(self, event):
        painter = QPainter(self)
        dirtyRect = event.rect()
        painter.drawImage(dirtyRect, self.image, dirtyRect)


    def resizeEvent(self, event):
        if self.width() > self.image.width() or self.height() > self.image.height():
            newWidth = max(self.width(), self.image.width())
            newHeight = max(self.height(), self.image.height())
            self.resizeImage(self.image, QSize(newWidth, newHeight))
            self.update()

        super(ScribbleArea, self).resizeEvent(event)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        if self.pressed:
            painter = QPainter(self.image)
            painter.setPen(QPen(Qt.red, 3, Qt.SolidLine))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            self.drawing = False