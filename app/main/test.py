from PySide6.QtWidgets import (QGridLayout, QPushButton)
import app.root

class Test(app.root.RootUi):
    def __init__(self, root):
        super().__init__()
        self.__root = root
    
    def setup_ui(self):
        self.__layout = QGridLayout()
        self.__button = QPushButton("ТЕСТОВАЯ КНОПКА ТОЧНО ИЗ ДРУГОГО КЛАССА")
        self.setLayout(self.__layout)
    
    def add_ui(self):
        self.__layout.addWidget(self.__button)
    
    def actions(self):
        self.__button.clicked.connect(self.get)
    
    def get(self):
        print("====")
        print("Путь до файла: {0};".format(self.__root.get_current_file_path()))
        print("Текущий язык: {0};".format(self.__root.get_current_language()))
        print("Текущая модель: {0}".format(self.__root.get_current_model()))
        print("====")