import sys
from PySide6.QtWidgets import QApplication
from class_file.main_window import MainWindowClass


def main():
    
    app = QApplication([])

    monitor_size = app.screens()[len(app.screens())-1].size()#funciones
    # print(len(app.screens())-1)

    main_window= MainWindowClass("Mi aplicacion de imagenes desde la web", monitor_size)

    main_window.show()

    app.exec()

if __name__ == '__main__':
    main()