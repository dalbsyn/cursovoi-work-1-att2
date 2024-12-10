from PySide6.QtWidgets import (QGridLayout, QLabel, QPushButton, QLineEdit, 
                               QFileDialog, QSizePolicy)
from PySide6.QtGui import (QFont)
import app.root

class FileSelection(app.root.RootUi):
    def __init__(self, root):
        super().__init__()

        self.__root = root

    def setup_ui(self):
        self.__layout = QGridLayout()
        self.__label_file = QLabel("Выберите файл")
        self.__field_file = QLineEdit()
        self.__button_file = QPushButton("Выбрать файл")
        self.setLayout(self.__layout)

    def add_ui(self):
        self.__layout.addWidget(self.__label_file, 0, 0, 1, 2)
        self.__layout.addWidget(self.__field_file, 1, 0, 1, 1)
        self.__layout.addWidget(self.__button_file, 1, 1, 1, 1)
    
    def actions(self):
        self.__button_file.clicked.connect(self.file_dialog)
    
    def customize_ui(self):
        self.__label_file.setSizePolicy(QSizePolicy().Policy.Maximum, QSizePolicy().Policy.Fixed)
        self.__label_file.setStyleSheet("font-weight: bold;")
        
        self.__field_file.setSizePolicy(QSizePolicy().Policy.Minimum, QSizePolicy().Policy.Fixed)

        self.__button_file.setSizePolicy(QSizePolicy().Policy.Maximum, QSizePolicy().Policy.Fixed)
    
    def file_dialog(self):
        self.__file_dialog = QFileDialog().getOpenFileName()
        self.__root.set_current_file_path(self.__file_dialog[0])
        self.__field_file.setText(self.__root.get_current_file_path())
        print("Путь до файла: {0};".format(self.__root.get_current_file_path()))