from curses import panel
import os
from os.path import isfile, join
from re import A
from PySide6.QtWidgets import QMainWindow, QFileDialog, QVBoxLayout, QWidget, QLabel
from PySide6.QtGui import QAction, QPixmap
from PySide6.QtCore import Qt
from PIL import Image
import requests
import json

class file_handler(QMainWindow):

    path= None
    def __init__(self):
        super().__init__()
        self.path = os.path.expanduser('~')


    # enable pop-up window to select a file, do not takes arguments, does not return values
    def open_file(self): #verify file selected
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
            ## llamar una funcion que devuelva la imagen o la direccion
            content = None
            with open(selected_file, "r") as json_file:
                content= json_file.read()
                content= json.loads(content)
            
            return content
            # print (content)
         
    # obtain images and name of it
    def image_downloader(self, image_dict):
        # image_dict = {}
        # image_dict = self.open_file()
        url = ''
        for image_url in image_dict:
            try:
                if image_url['url']:
                    url = image_url['url']
                    parms = {
                        "auto": "compress",
                        "cs": "tinysrgb",
                        "w": 1260,
                        "h": 750,
                        "dpr" : 1
                    }
                    answer = requests.get(url, params=parms)
            except KeyError as e:
                image_name= "./images_downloaded/" + image_url['nombre'] + ".jpg"
                with open(image_name, mode="wb") as imagen:
                    imagen.write(answer.content)
                # print("Error:", e.args ) #I have the feeling that this is not the proper way but I will investigate later
                # self.open_image()# loads the image but just one
                continue
            except:
                print("Unhandled error at image_downloader object")
            
    #
    def open_image(self):
        images_path = "./images_downloaded"
        image_list = []

        # files_within = [img for img in os.listdir(images_path) if isfile(join(images_path,"/", img))] #seems unnecesary
        # for img in files_within:

        for img in os.listdir(images_path):
            img_route= images_path+ "/" + img
            image_list.append(Image.open(img_route))
            # image_show = QPixmap(img_route)
            # self.image_tag.setPixmap(image_show)
        print (len(image_list))
        # return image_list
        

        #
    def image_resize(self, images):
        tall= images.height
        wide= images.width
        a, b,c,d = ((wide/2)*.5, (tall/2)*.5, wide*.5, tall*.5)
        images = images.transform(size=(100,100), method= Image.EXTENT, data=(a,b,c,d))

