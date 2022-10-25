import functools
from PyQt5 import QtWidgets, QtCore, QtGui
import file
import edit
import image
import filter
import scribble_area
import buttons
import textinput
import help
from load_screen import app


class PhotoshopEditor(QtWidgets.QMainWindow):
    def __init__(self):
        super(PhotoshopEditor, self).__init__()
        self.scribble_area = scribble_area.ScribbleArea()
        self.scribble_area.get_photoshop_obj(self)
        self.buttons_obj = buttons.Buttons()
        self.is_clicked_move = False
        self.pressed_button = None
        self.main_window: QtWidgets.QMainWindow = None
        self.button_list = [None] * 10
        self.screen_width = 0
        self.screen_height = 0
        self.band = []
        self.button_clicked = [False] * 10

    def setupUi(self, main_window):
        screen = QtWidgets.QApplication.primaryScreen()
        rect = screen.availableGeometry()
        self.screen_width = rect.width()
        self.screen_height = rect.height()
        self.main_window = main_window
        main_window.setObjectName('MainWindow')
        main_window.setWindowTitle('Photoshop Clone')
        main_window.setGeometry((self.screen_width - 840) // 2,
                                (self.screen_height - 560) // 2, 900, 600)
        main_window.setFixedSize(900, 600)
        main_window.setWindowIcon(QtGui.QIcon('../content/logo.png'))

        main_window.setStyleSheet("background: #686868; color:white")

        self.choose_width_pen = QtWidgets.QSlider(QtCore.Qt.Horizontal, self.scribble_area)
        self.choose_width_pen.setAutoFillBackground(True)
        self.choose_width_pen.setMinimum(1)
        self.choose_width_pen.setMaximum(50)
        self.choose_width_pen.setSliderPosition(15)
        self.choose_width_pen.hide()

        self.choose_width_rubber = QtWidgets.QSlider(QtCore.Qt.Horizontal, self.scribble_area)
        self.choose_width_rubber.setAutoFillBackground(True)
        self.choose_width_rubber.setMinimum(1)
        self.choose_width_rubber.setMaximum(50)
        self.choose_width_rubber.setSliderPosition(15)
        self.choose_width_rubber.hide()

        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName('central_widget')

        horizontal_layout = QtWidgets.QHBoxLayout(self.central_widget)
        horizontal_layout.setObjectName('horizontalLayout')
        horizontal_layout_2 = QtWidgets.QHBoxLayout()
        horizontal_layout_2.setObjectName('horizontalLayout_2')
        # self.panel = QtWidgets.QFrame(self.central_widget)
        # self.panel.setStyleSheet("background: #686868;")
        self.vertical_layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.vertical_layout.setObjectName('verticalLayout')
        horizontal_layout_2.addLayout(self.vertical_layout)
        horizontal_layout_2.addWidget(self.scribble_area)
        horizontal_layout.addLayout(horizontal_layout_2)
        main_window.setCentralWidget(self.central_widget)

        menubar = QtWidgets.QMenuBar(main_window)
        menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))

        menubar.setObjectName('menubar')
        menu_file = QtWidgets.QMenu(menubar)
        menu_file.setObjectName('menuFile')
        main_window.setMenuBar(menubar)
        action_new = QtWidgets.QAction(main_window)
        action_new.setObjectName('action_new')
        menu_file.addAction(action_new)
        menubar.addAction(menu_file.menuAction())
        self.toolbar()
        self.re_translate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def re_translate_ui(self, main_window):
        main_menu = QtWidgets.QMenuBar(main_window)
        main_menu.setGeometry(QtCore.QRect(0, 0, 800, 24))
        main_window.setMenuBar(main_menu)
        file_menu = QtWidgets.QMenu(main_menu)
        edit_menu = QtWidgets.QMenu(main_menu)
        image_menu = QtWidgets.QMenu(main_menu)
        filter_menu = QtWidgets.QMenu(main_menu)
        help_menu = QtWidgets.QMenu(main_menu)
        translate = QtCore.QCoreApplication.translate

        dict_file = {'New': file.File.new, 'Open': file.File.open,
                     'Save': file.File.save, 'Save As': file.File.save_as,
                     'Print': file.File.print, 'Close': file.File.close_window}

        dict_edit = {'Undo': edit.Edit.undo, 'Redo': edit.Edit.redo,
                     'Cut': edit.Edit.cut, 'Copy': edit.Edit.copy,
                     'Paste': edit.Edit.paste, 'Clear screen': edit.Edit.clear_screen,
                     'Keyboard shortcuts': edit.Edit.keyboard_shortcuts}

        dict_image = {'Image size': image.Image.image_size,
                      'Canvas size': image.Image.canvas_size,
                      'Rotate left': image.Image.rotate_left,
                      'Rotate right': image.Image.rotate_right}

        dict_filter = {'Blur': filter.Filter.blur, 'Noise': filter.Filter.noise,
                       'Twirling spirals': filter.Filter.twirling_spirals,
                       'Pixelate': filter.Filter.pixelate}

        dict_help = {'Help': self.help, 'Documentation': self.documentation}

        lst_file_shortcut = ['Ctrl+N', 'Ctrl+O', 'Ctrl+S', 'Ctrl+Shift+S', 'Ctrl+P', 'Ctrl+W']
        i = 0
        for key, value in dict_file.items():
            extract_action = QtWidgets.QAction(main_window)
            extract_action.setShortcut(lst_file_shortcut[i])
            file_menu.addAction(extract_action)
            main_menu.addAction(file_menu.menuAction())
            extract_action.triggered.connect(functools.partial(value, self, self))
            extract_action.setText(translate('MainWindow', key))
            i += 1

        lst_edit_shortcut = ['Ctrl+Z', 'Ctrl+Y', 'Ctrl+X', 'Ctrl+C', 'Ctrl+V', 'Ctrl+L', 'Ctrl+K']
        i = 0
        for key, value in dict_edit.items():
            extract_action = QtWidgets.QAction(main_window)
            extract_action.setShortcut(lst_edit_shortcut[i])
            edit_menu.addAction(extract_action)
            main_menu.addAction(edit_menu.menuAction())
            extract_action.triggered.connect(functools.partial(value, self))
            extract_action.setText(translate('MainWindow', key))
            i += 1

        lst_image_shortcut = ['Ctrl+Alt+I', 'Ctrl+Alt+C', 'Shift+Ctrl+L', 'Shift+Ctrl+R']
        i = 0
        for key, value in dict_image.items():
            extract_action = QtWidgets.QAction(main_window)
            extract_action.setShortcut(lst_image_shortcut[i])
            image_menu.addAction(extract_action)
            main_menu.addAction(image_menu.menuAction())
            extract_action.triggered.connect(functools.partial(value, self))
            extract_action.setText(translate('MainWindow', key))
            i += 1

        lst_filter_shortcut = ['Shift+Ctrl+B', 'Shift+Ctrl+N', 'Shift+Ctrl+T', 'Shift+Ctrl+P']
        i = 0
        for key, value in dict_filter.items():
            extract_action = QtWidgets.QAction(main_window)
            extract_action.setShortcut(lst_filter_shortcut[i])
            filter_menu.addAction(extract_action)
            main_menu.addAction(filter_menu.menuAction())
            extract_action.triggered.connect(functools.partial(value, self))
            extract_action.setText(translate('MainWindow', key))
            i += 1

        lst_help_shortcut = ['Ctrl+H', 'Ctrl+D']
        i = 0
        for key, value in dict_help.items():
            extract_action = QtWidgets.QAction(main_window)
            extract_action.setShortcut(lst_help_shortcut[i])
            help_menu.addAction(extract_action)
            main_menu.addAction(help_menu.menuAction())
            extract_action.triggered.connect(value)
            extract_action.setText(translate("MainWindow", key))
            i += 1

        file_menu.setTitle(translate('MainWindow', 'File'))
        edit_menu.setTitle(translate('MainWindow', 'Edit'))
        image_menu.setTitle(translate('MainWindow', 'Image'))
        filter_menu.setTitle(translate('MainWindow', 'Filter'))
        help_menu.setTitle(translate('MainWindow', 'Help'))

    def toolbar(self):
        dict_buttons = {'../content/paint-brush.png': self.paint,
                        '../content/move.png': self.move_text,
                        '../content/marquee.png': self.marquee,
                        '../content/lasso.png': self.lasso,
                        '../content/crop.png': self.crop,
                        '../content/eyedropper.png': self.eyedropper,
                        '../content/eraser.png': self.eraser,
                        '../content/font.png': self.type,
                        '../content/recovery.png': self.image_converter,
                        '': functools.partial(self.scribble_area.set_pen_color, self)
                        }
        i = 0
        QtWidgets.QToolTip.setFont(QtGui.QFont('Arial', 14))
        lst_name_buttons = ['Pen', 'Move', 'Marquee', 'Lasso', 'Crop', 'Eyedropper'
                            , 'Eraser', 'Text', 'Image converter', 'Color']
        for key, value in dict_buttons.items():
            self.button_list[i] = QtWidgets.QPushButton(self.central_widget)

            self.button_list[i].setMaximumSize(QtCore.QSize(36, 36))
            size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                                QtWidgets.QSizePolicy.Preferred)
            size_policy.setHorizontalStretch(0)
            size_policy.setVerticalStretch(0)
            size_policy.setHeightForWidth(self.button_list[i].sizePolicy().hasHeightForWidth())
            self.button_list[i].clicked.connect(value, self.button_clicked[i])
            self.button_list[i].setToolTip(lst_name_buttons[i])
            self.button_list[i].setSizePolicy(size_policy)
            self.button_list[i].setIcon(QtGui.QIcon(key))
            self.button_list[i].setIconSize(QtCore.QSize(24, 24))
            self.button_list[i].setStyleSheet("""
                                                    QPushButton{
                                                        border-radius:8px;
                                                    }
                                                    QPushButton::hover{
                                                        background-color: #FF7DF7;
                                                    }
                                                    QToolTip{ 
                                                        border: 1px solid white; 
                                                        background-color: #D600C9 ; 
                                                        font: 12pt}
                                                    """)
            self.vertical_layout.addWidget(self.button_list[i])
            i += 1

        rubber_menu = QtWidgets.QMenu()
        rubber_menu.addAction('Rubber the scribble', functools.partial(self.eraser, 'transparent'))
        rubber_menu.addAction('Rubber all image', functools.partial(self.eraser, 'all image'))

        self.button_list[6].setMenu(rubber_menu)
        self.button_list[9].setMaximumSize(QtCore.QSize(36, 36))
        self.button_list[9].setStyleSheet("""
                                                    QPushButton{
                                                        border-radius:8px;
                                                        background: black
                                                    }
                                                    QPushButton::hover{
                                                        background-color: #FF7DF7;
                                                    }
                                                    """)

    def all_button_white(self):
        for i in range(9):
            self.button_list[i].setStyleSheet("""
                                                    QPushButton{
                                                        border-radius:8px;
                                                    }
                                                    QPushButton::hover{
                                                        background-color: #FF7DF7;
                                                    }
                                                    """)

    def paint(self):
        self.is_clicked_move = False
        self.scribble_area.pressed_button = 'paint'
        self.all_button_white()
        self.button_list[0].setStyleSheet('background:#D600C9; border-radius:8px')

        pixmap = QtGui.QPixmap('../content/dry-clean.png')
        if self.scribble_area.pen_width > 10:
            pixmap = pixmap.scaled(self.scribble_area.pen_width,
                                   self.scribble_area.pen_width,
                                   QtCore.Qt.IgnoreAspectRatio,
                                   QtCore.Qt.SmoothTransformation)
        else:
            pixmap = pixmap.scaled(10, 10,
                                   QtCore.Qt.IgnoreAspectRatio,
                                   QtCore.Qt.SmoothTransformation)

        cursor = QtGui.QCursor(pixmap)
        app.setOverrideCursor(cursor)

    def move_text(self):
        self.is_clicked_move = True
        self.scribble_area.pressed_button = 'move'
        self.all_button_white()
        self.button_list[1].setStyleSheet('background:#D600C9; border-radius:8px')
        for i in self.band:
            i.draggable = True

        pixmap = QtGui.QPixmap('../content/move_black.png')
        pixmap = pixmap.scaled(20, 20,
                               QtCore.Qt.IgnoreAspectRatio,
                               QtCore.Qt.SmoothTransformation)
        cursor = QtGui.QCursor(pixmap)
        app.setOverrideCursor(cursor)

    def marquee(self):
        self.is_clicked_move = False
        self.scribble_area.pressed_button = 'marquee'
        self.all_button_white()
        self.button_list[2].setStyleSheet('background:#D600C9; border-radius:8px')
        for i in self.band:
            i.draggable = False

        pixmap = QtGui.QPixmap('../content/crop_black.png')
        pixmap = pixmap.scaled(20, 20,
                               QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)

        cursor = QtGui.QCursor(pixmap)
        app.setOverrideCursor(cursor)

    def lasso(self):
        self.is_clicked_move = False
        self.scribble_area.pressed_button = 'lasso'
        self.all_button_white()
        self.button_list[3].setStyleSheet('background:#D600C9; border-radius:8px')
        for i in self.band:
            i.draggable = False

        pixmap = QtGui.QPixmap('../content/dry-clean.png')
        pixmap = pixmap.scaled(20, 20,
                               QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)

        cursor = QtGui.QCursor(pixmap)
        app.setOverrideCursor(cursor)

    def crop(self):
        self.is_clicked_move = False
        self.scribble_area.pressed_button = 'crop'
        self.all_button_white()
        self.button_list[4].setStyleSheet('background:#D600C9; border-radius:8px')
        self.buttons_obj.crop(self)
        for i in self.band:
            i.draggable = False

    def eyedropper(self):
        self.is_clicked_move = False
        self.scribble_area.pressed_button = 'eyedropper'
        self.all_button_white()
        self.button_list[5].setStyleSheet('background:#D600C9; border-radius:8px')
        for i in self.band:
            i.draggable = False
        pixmap = QtGui.QPixmap('../content/eyedropper_black.png')
        pixmap = pixmap.scaled(20, 20,
                               QtCore.Qt.IgnoreAspectRatio,
                               QtCore.Qt.SmoothTransformation)
        cursor = QtGui.QCursor(pixmap)
        app.setOverrideCursor(cursor)

    def eraser(self, rubber_type):
        self.is_clicked_move = False
        if rubber_type == 'transparent':
            self.scribble_area.pressed_button = 'transparent'
        else:
            self.scribble_area.pressed_button = 'all image'

        self.all_button_white()
        self.button_list[6].setStyleSheet('background:#D600C9; border-radius:8px')

        for i in self.band:
            i.draggable = False

        pixmap = QtGui.QPixmap('../content/dry-clean.png')
        if self.scribble_area.rubber_width > 10:
            pixmap = pixmap.scaled(self.scribble_area.rubber_width,
                                   self.scribble_area.rubber_width,
                                   QtCore.Qt.IgnoreAspectRatio,
                                   QtCore.Qt.SmoothTransformation)
        else:
            pixmap = pixmap.scaled(10, 10,
                                   QtCore.Qt.IgnoreAspectRatio,
                                   QtCore.Qt.SmoothTransformation)

        mask = pixmap.createMaskFromColor(QtCore.Qt.red)
        pixmap.setMask(mask)
        cursor = QtGui.QCursor(pixmap)
        app.setOverrideCursor(cursor)

    def type(self):
        self.scribble_area.rotated = 'None'
        self.is_clicked_move = False
        self.scribble_area.check = True
        self.scribble_area.pressed_button = 'type'
        self.all_button_white()
        self.button_list[7].setStyleSheet('background:#D600C9; border-radius:8px')
        textinput.Ui_Dialog(self.scribble_area).exec()
        if self.scribble_area.text != '':
            obj = buttons.MoveText(self.scribble_area.text, self.scribble_area.width_text,
                                   self.scribble_area.text_font, self.scribble_area.color_text,
                                   self.scribble_area.bold, self.scribble_area.italic,
                                   self.scribble_area.underline, self.scribble_area,
                                   self, dragable=False)
            self.band.append(obj)
            self.move_text()
        else:
            self.all_button_white()

    def image_converter(self):
        self.is_clicked_move = False
        self.scribble_area.pressed_button = 'image_converter'
        self.all_button_white()
        self.button_list[8].setStyleSheet('background:#D600C9; border-radius:8px')
        self.buttons_obj.image_converter(self)
        for i in self.band:
            i.draggable = False

    def help(self):
        self.is_clicked_move = False
        self.window = QtWidgets.QDialog()
        self.ui = help.Help()
        self.ui.setupUi(self.window)
        self.window.show()

    def documentation(self):
        self.is_clicked_move = False
        self.window = QtWidgets.QDialog()
        self.ui = help.Documentation()
        self.ui.setupUi(self.window)
        self.window.show()

    def set_window_size(self, width, height):
        screen = app.primaryScreen()
        rect = screen.availableGeometry()
        bigger = False
        if height > rect.height() - 30:
            height = rect.height() - 30
            bigger = True

        if width > rect.width():
            width = rect.width()
        self.scribble_area.image_width = width
        self.scribble_area.image_height = height

        self.main_window.setFixedSize(width, height)
        if bigger:
            self.main_window.setGeometry((self.screen_width - width) // 2,
                                         (self.screen_height - height + 20) // 2, width, height)
        else:
            self.main_window.setGeometry((self.screen_width - width) // 2,
                                         (self.screen_height - height) // 2, width, height)
