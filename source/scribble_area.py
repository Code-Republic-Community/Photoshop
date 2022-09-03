from PyQt5.QtCore import QPoint, Qt, QSize
from PyQt5.QtGui import QImage, qRgb, QPainter, QPen, QColor
from PyQt5.QtWidgets import QWidget


class ScribbleArea(QWidget):
    def __init__(self):
        super(ScribbleArea, self).__init__()

        self.setAttribute(Qt.WA_StaticContents)
        self.image = QImage()
        self.pressed = False
        self.lastPoint = QPoint()
        self.check = False
        self.color = (0, 0, 0, 255)

    def is_pressed(self, value):
        self.pressed = value
        return self.pressed

    def current_window_size(self):
        return self.width(), self.height()

    def openImage(self, fileName):
        loadedImage = QImage()
        if not loadedImage.load(fileName):
            return False
        newSize = loadedImage.size().expandedTo(self.size())
        self.resizeImage(loadedImage, newSize)
        self.image = loadedImage
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
        # if self.width() > self.image.width() or self.height() > self.image.height():
        newWidth = max(self.width() + 128, self.image.width())
        newHeight = max(self.height() + 128, self.image.height())
        self.resizeImage(self.image, QSize(self.width(), self.height()))
        self.update()

        super(ScribbleArea, self).resizeEvent(event)

    def saveImage(self, fileName, fileFormat):
        visibleImage = self.image
        self.resizeImage(visibleImage, self.size())

        if visibleImage.save(fileName, fileFormat):
            return True
        return False

    def foo(self):
        return self.image

    def paintEvent(self, event):
        painter = QPainter(self)
        dirtyRect = event.rect()
        painter.drawImage(dirtyRect, self.image, dirtyRect)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        from photoshop_editor import PhotoshopEditor
        if self.pressed:
            painter = QPainter(self.image)
            painter.setPen(QPen(
                QColor(self.color[0], self.color[1], self.color[2], self.color[3]),
                3, Qt.SolidLine))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()
            self.check = True

    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            pass
