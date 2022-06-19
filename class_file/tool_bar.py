import faulthandler
from typing_extensions import Self
from PySide6.QtWidgets import  QToolBar
from PySide6.QtGui  import QAction

class tool_bar(QToolBar):
    father = None

    # initalize variables and adds the functionality to the menu, 
    def __init__(self, father):
        super().__init__()

        self.father = father

        open_database = QAction("Open DataBase", self)
        open_database.triggered.connect(self.open_database)
        self.addAction(open_database)

    # shows the window to locate the file .bdjson, do not recieve parameters, do not returns
    def open_database(self):
        self.father.bdjson_file

