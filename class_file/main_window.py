# from ctypes import resize
# from turtle import width
from curses import panel
import os
from PySide6.QtWidgets import QMainWindow, QFileDialog, QVBoxLayout, QWidget, QLabel
from PySide6.QtGui import QAction, QPixmap
from PySide6.QtCore import Qt

# from .tool_bar import #BarraTareas # la clase aun no esta creada

from PIL import Image


class MainWindowClass(QMainWindow):
    main_window_wide = None
    main_window_tall = None
    task_bar= None
    task_bar_option = None
    image = None
    image_tag= None
    path = None

    #
    def __init__(self, title, monitor_size):
        super().__init__()

        self.path = os.path.expanduser('~')

        #gets the first size of the window
        self.main_window_wide = monitor_size.width()*.6
        self.main_window_tall = monitor_size.height()*.6
        
        #helps center the image
        axis_x = int((monitor_size.width() - self.main_window_wide)/2)
        axis_y = int((monitor_size.height() - self.main_window_tall)/2)

        self.setWindowTitle(title)

        self.setGeometry(
            axis_x, 
            axis_y,
            self.main_window_wide,
            self.main_window_tall
        )

        self.start_menu() #function of this class

        #allows to draw within the canvas
        disposition = QVBoxLayout()
        self.setLayout(disposition)
        panel = QWidget()
        panel.setStyleSheet("background-color: #d1d1d1;")
        self.setCentralWidget(panel)
        disposition_panel = QVBoxLayout()
        disposition_panel.setAlignment(Qt.AlignHCenter)
        panel.setLayout(disposition_panel)
        
        #Qlabel enables to place text in the main windows
        self.image_tag = QLabel()
        disposition_panel.addWidget(self.image_tag)

        
    # borrar
    def show_hide_task_bar(self):
        pass
    
    # enable pop-up window to select a file, do not takes arguments, does not return values
    def open_file(self):
        print("ingresa a open file")
        selected_file = QFileDialog.getOpenFileName(
            self,
            "Select a bdjson file: ",
            self.path,
            "Archivo bdJson (*.bdjson)"
        )
        selected_file = selected_file[0]

        if not selected_file:
            return
        else:
            self.image = Image.open(selected_file, 'r')
            self.refresh_image()

    #
    def start_menu(self):
        main_menu = self.menuBar()

        main_menu.setStyleSheet(
            """
            background-color: #213341; 
            color:white; 
            padding:10px;
            font-size:20px
            """
        )

        menu_option = main_menu.addMenu('Opciones')
        open_option = QAction("Abrir base de datos", menu_option)
        open_option.triggered.connect(self.open_file)
        menu_option.addAction(open_option)
        print("ultima linea Start Menu")

    #
    def resizeEvent():
        pass

    #
    def refresh_image(self):
        pass
