from curses import panel
import os
from os.path import isfile, join
from re import A
from PySide6.QtWidgets import QMainWindow, QFileDialog, QVBoxLayout, QWidget, QLabel
from PySide6.QtGui import QAction, QPixmap
from PySide6.QtCore import Qt
from PIL import Image
import bdjson
import requests
from .file_manager import file_handler


class MainWindowClass(QMainWindow):
    main_window_wide = None
    main_window_tall = None
    task_bar= None
    task_bar_option = None
    image = None
    image_tag= None
    path = None
    file_manager=None

    # constructor, title of the window and the size of the monitor, no return
    def __init__(self, title, monitor_size):
        super().__init__()

        # self.path = os.path.expanduser('~')

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

        # self.file_manager = file_handler()
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

    # change appearence of the main menu bar, no parameters, no return
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
        open_option.triggered.connect(self.process_loads_downloads_images())
        menu_option.addAction(open_option)
        
    def process_loads_downloads_images(self):
        self.file_manager = file_handler()
        
        list_files= self.file_manager.open_file()

        return self.file_manager.image_downloader(list_files)
    
            