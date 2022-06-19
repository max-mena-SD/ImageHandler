# Project description

### Objective:
#### Create a program that generates a graphical interface in which the menu has a single option:

* Abrir base de datos

When the button is pressed, the machine's file picker wil display and allow the user to select a file with the **.bdjson** extension. 

If the user clicks cancel, or does not select a valid file, the interface will do nothing. But if the user select a file with the indicated extension, the program will proceed with the following step. 

> Files with the *.bdjson* extension have the following form:

```json
[
    {
        "url" : "https://....",
        "nombre" "Imagen 1"
    },
    {
        "url" : "https://....",
        "nombre" "Imagen 2"
    }
    ...
]
```

It is a list of dictionaries, where each one of the dictionaries corresponds to the information of an image with the data of the URL, as well as the name of said image. 

When a valid file is selected, the program goes to the URL of each of the images and download the content of it. 

When you have successfully downloaded the image, the program should be able to display all the images horizontally, within the empty space of the graphical interface. 

Images must be displayed in a size of ***100(height) x 100(width)***. 

The name of the image will be displayed under the corresponding one, aligned to the center.
- The process of obtaining the images must be done with the ``` requests ``` library.
- Image processing should be done with the ``` Pillow ``` library in case it is necessary
- The file ***requirements.txt*** of your environment must be sent

### Unit tests
Unit tests must be generated for the method that downloads the image.

---

## Project setup

I recommend to stablish a virtual enviroment by using pyenv:

```bash
    $ pyenv exec python3 -m venv .venv
    $ source .venv/bin/activate
```

Update apt:

```bash
    $ apt update
```

Install *requeriments.txt* by using:

```python
    pip install -r requirements.txt
```

