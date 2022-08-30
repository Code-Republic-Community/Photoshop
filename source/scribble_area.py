from PyQt5.QtCore import QPoint, Qt, QDir
from PyQt5.QtGui import QImage, qRgb, QPainter, QPen
from PyQt5.QtWidgets import QWidget, QLabel


class ScribbleArea(QWidget):
    def __init__(self):
        super(ScribbleArea, self).__init__()

        self.setAttribute(Qt.WA_StaticContents)
        self.modified = False
        self.scribbling = False
        self.myPenWidth = 1
        #self.resize(850, 580)
        #self.move(50, 20)
        self.myPenColor = Qt.blue
        self.image = QImage()
        self.lastPoint = QPoint()

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

    def paintEvent(self, event):
        painter = QPainter(self)
        dirtyRect = event.rect()
        painter.drawImage(dirtyRect, self.image, dirtyRect)

    def resizeImage(self, image, newSize):
        if image.size() == newSize:
            return

        newImage = QImage(newSize, QImage.Format_RGB32)
        newImage.fill(qRgb(255, 255, 255))
        painter = QPainter(newImage)
        painter.drawImage(QPoint(0, 0), image)
        self.image = newImage



    # def mousePressEvent(self, event):
    #     if event.button() == Qt.LeftButton:
    #         self.drawing = True
    #         self.lastPoint = event.pos()
    #
    # def mouseMoveEvent(self, event):
    #     painter = QPainter(self.image)
    #     painter.setPen(QPen(Qt.red, 3, Qt.SolidLine))
    #     painter.drawLine(self.lastPoint, event.pos())
    #     self.lastPoint = event.pos()
    #     self.update()
    #
    # def mouseReleaseEvent(self, event):
    #     if event.button == Qt.LeftButton:
    #         self.drawing = False