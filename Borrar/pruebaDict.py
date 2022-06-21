# from os import listdir
# from os.path import isfile, join
# from PIL import Image

# images_path = "./images_downloaded"
# mi_imagen = []

# files_within = [img for img in listdir(images_path) if isfile(join(images_path, img))]
# for img in files_within:
#     mi_imagen.append(Image.open(images_path+ "/" + img))
    
# mi_imagen[0].show()

import os
from os.path import isfile, join
from PySide6.QtGui import QAction, QPixmap
from PIL import Image

images_path = "./images_downloaded"
image_list = []

files_within = [img for img in os.listdir(images_path) if isfile(join(images_path, img))]
for img in files_within:
    img_route= images_path+ "/" + img

    ruta = img_route
    mi_imagen = Image.open(ruta)

    #image resized
    tall= mi_imagen.height
    wide= mi_imagen.width
    percent= (100/wide)#because is taller
    a, b,c,d = ((wide/2)*.5, (tall/2)*.5, wide*.5, tall*.5)
    image_resized = mi_imagen.transform(size=(100,100), method= Image.EXTENT, data=(a,b,c,d))
    image_resized.save(img_route, 'PNG')
    mi_imagen.close()
    #image resized 

    image_list.append(Image.open(img_route))
    # image_show = QPixmap(img_route)
    print(image_list)


    