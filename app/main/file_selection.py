from PySide6.QtWidgets import QGridLayout, QLabel, QPushButton, QLineEdit, QFileDialog
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
        self.__layout.addWidget(self.__label_file, 0, 0)
        self.__layout.addWidget(self.__field_file, 1, 0)
        self.__layout.addWidget(self.__button_file, 1, 1)
    
    def actions(self):
        self.__button_file.clicked.connect(self.file_dialog)
    
    def file_dialog(self):
        self.__file_dialog = QFileDialog().getOpenFileName()
        self.__root.set_current_file_path(self.__file_dialog[0])
        print(self.__root.get_current_file_path())
        self.__field_file.setText(self.__root.get_current_file_path())