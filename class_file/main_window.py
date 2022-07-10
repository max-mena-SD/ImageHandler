from ctypes import alignment
from curses import panel
import os, glob
from os import path
from os.path import isfile, join
from re import A

from PySide6.QtWidgets import QMainWindow, QFileDialog, QVBoxLayout, QWidget, QLabel, QHBoxLayout
from PySide6.QtGui import QAction, QPixmap
from PySide6.QtCore import Qt
from PIL import Image
import json
import requests


class MainWindowClass(QMainWindow):
    main_window_wide = None
    main_window_tall = None
    task_bar= None
    task_bar_option = None
    image = None
    image_tag= None
    path = None
    route_images= "./images_downloaded/"
    route_thumbnail= "./images_downloaded/thumbnail/"
    panel= None

    image_tag2= None

    # constructor, title of the window and the size of the monitor, no return
    def __init__(self, title, monitor_size):
        super().__init__()

        self.path = os.path.expanduser('~')
        self.file_creation_clean()

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
        self.panel = QWidget()
        self.panel.setStyleSheet("background-color: #d1d1d1;")
        self.setCentralWidget(self.panel)

        # self.container_tag_test( panel )
        # self.container_tag(panel)

    #verifies that the folders exists and is empty, no parameters, no return
    def file_creation_clean (self):
        if not path.exists(self.route_images):
            os.mkdir(self.route_images)
            print ("Path created", self.route_images)
        else:
            try:
                for img in os.listdir(self.route_images ):
                    os.remove(self.route_images + img)
            except:
                print ("uncontrolled issue: ", self.route_images)
            print (self.route_images, "existed")

        if not path.exists(self.route_thumbnail):
            os.mkdir(self.route_thumbnail)
            # print ("Path created", self.route_thumbnail)
        else:
            try:
                for img in os.listdir(self.route_thumbnail ):
                    os.remove(self.route_thumbnail + img)
            except:
                print ("uncontrolled issue: ", self.route_thumbnail)
            # print (self.route_thumbnail, "existed")

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
        open_option.triggered.connect(self.image_downloader)
        menu_option.addAction(open_option)

    # enable pop-up window to select a file, do not takes arguments, does not return values
    def open_file(self): #verify file selected

        self.file_creation_clean ()

        image_list = None
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
            with open (selected_file, "r") as json_file:
                image_list = json_file.read()
                image_list = json.loads(image_list)
            return image_list
         
    # obtain images and name of it
    def image_downloader(self):
        
        image_list = self.open_file()
        size_thumbnail= (100,100)
        

        for image_data in image_list:
            try:
                params = {
                        "auto": "compress",
                        "cs": "tinysrgb",
                        "w": 1260,
                        "h": 750,
                        "dpr" : 1
                    }
                answer = requests.get(image_data['url'], params=params)
                image_name= self.route_images + image_data['nombre'] + ".jpg"                    
                with open(image_name, mode="wb") as imagen:
                    imagen.write(answer.content)

            except KeyError as e:
                print("Dictionary List error:", e.args)
            except:
                print("Unhandled error at image_downloader object")

        for img in os.listdir(self.route_images):
            file, ext = os.path.splitext(img)
            try:
                with Image.open(self.route_images + img) as im:
                    im.thumbnail(size_thumbnail)
                    im.save( self.route_thumbnail + file + "-thumbnail.jpg", "JPEG")
            except:
                print ("Catched directory opening as image")
        
        self.container_tag(self.panel)

    # adds images to the main window, receives the QWidget object and images information
    def container_tag(self, panel):
        
        format = """
                padding: 10px;
                border: 3px solid green; 
                """
        disposition_panel = QHBoxLayout()
        disposition_panel.setAlignment(Qt.AlignVCenter)#Qt.AlignLeft)#AlignHCenter)
        panel.setLayout(disposition_panel)

        for img in os.listdir(self.route_thumbnail):
            thumbnail_name, ext = os.path.splitext(img) 

            self.image_tag = QLabel()
            # self.image_tag.setFixedWidth(50)
            # self.image_tag.setFixedWidth(50)
            image_show = QPixmap(self.route_thumbnail + img)
            self.image_tag.setPixmap(image_show)
            disposition_panel.addWidget(self.image_tag )

            titulo = QLabel()
            titulo.setText(thumbnail_name)
            disposition_panel.addWidget(titulo )    
