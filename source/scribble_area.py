from PyQt5.QtCore import QPoint, Qt, QSize
from PyQt5.QtGui import QImage, qRgb, QPainter, QPen
from PyQt5.QtWidgets import QWidget


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
        self.check = False

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
        painter.drawImage(QPoint(0, 0), image)
        self.image = newImage

    def resizeEvent(self, event):
        #if self.width() > self.image.width() or self.height() > self.image.height():
        newWidth = max(self.width() + 128, self.image.width())
        newHeight = max(self.height() + 128, self.image.height())
        self.resizeImage(self.image, QSize(self.width(), self.height()))
        self.update()

        super(ScribbleArea, self).resizeEvent(event)

    def saveImage(self, fileName, fileFormat):
        visibleImage = self.image
        self.resizeImage(visibleImage, self.size())

        if visibleImage.save(fileName, fileFormat):
            self.modified = False
            return True
        else:
            return False

    def foo(self):
        return self.image

    def paintEvent(self, event):
        painter = QPainter(self)
        dirtyRect = event.rect()
        #print(self.foo())
        painter.drawImage(dirtyRect, self.image, dirtyRect)

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
            self.check = True

    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            self.drawing = False