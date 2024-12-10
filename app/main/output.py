from PySide6.QtWidgets import (QPushButton, QGridLayout, QLabel, QTextBrowser, 
                               QProgressBar, QSizePolicy, QSpacerItem)

import app.root

class Output(app.root.RootUi):
    def __init__(self, root):
        super().__init__()

        self.__root = root

    def setup_ui(self):
        self.__layout = QGridLayout()

        self.__label_output = QLabel("Вывод")

        self.__field_output = QTextBrowser()

        self.__progress_process = QProgressBar()

        self.__button_start = QPushButton("Начать")
        self.__button_stop = QPushButton("Остановить")

        self.setLayout(self.__layout)
    
    def add_ui(self):
        self.__layout.addWidget(self.__label_output, 0, 0, 1, 2)
        self.__layout.addWidget(self.__field_output, 1, 0, 2, 2)
        self.__layout.addWidget(self.__progress_process, 2, 0, 1, 2)
        self.__layout.addWidget(self.__button_start, 3, 0, 1, 1)
        self.__layout.addWidget(self.__button_stop, 3, 1, 1, 1)
    
    def customize_ui(self):
        self.__label_output.setSizePolicy(QSizePolicy().Policy.Fixed, QSizePolicy().Policy.Fixed)
        self.__label_output.setStyleSheet("font-weight: bold;")
