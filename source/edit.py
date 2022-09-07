from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QUndoCommand, QWidget


class Edit():
    def __init__(self):
        super().__init__()

    def undo(self, object):
        self.undo = UndoCommand(object.scribbleArea)
        self.undo.undo()
        object.scribbleArea.mUndoStack.undo()
        object.scribbleArea.update()

    def redo(self, obj):
        obj.scribbleArea.mUndoStack.redo()
        from scribble_area import ScribbleArea
        obj = ScribbleArea()
        self.redo = UndoCommand(obj)
        self.redo.redo()

    def cut(self):
        pass

    def copy(self):
        pass

    def paste(self):
        pass

    def clear_screen(self, obj):
        obj.scribbleArea.image = QImage()
        newSize = obj.scribbleArea.image.size().expandedTo(obj.scribbleArea.size())
        obj.scribbleArea.resizeImage(obj.scribbleArea.image, QSize(newSize))
        obj.scribbleArea.update()

    def keyboard_shortcuts(self):
        pass


class UndoCommand(QUndoCommand):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.mPrevImage = parent.image.copy()
        self.mCurrImage = parent.image.copy()

    def undo(self):
        self.mCurrImage = self.parent.image.copy()
        self.parent.image = self.mPrevImage
        self.parent.update()

    def redo(self):
        self.parent.image = self.mCurrImage
        self.parent.update()
