from PySide6.QtWidgets import (QGridLayout, QLabel, QComboBox, QCheckBox)
import faster_whisper.tokenizer
import faster_whisper.utils
import app.root

class ProcessSettings(app.root.RootUi):
    def __init__(self, root):
        super().__init__()

        self.__root = root

        self.fill_combo_language()
        self.fill_combo_models()

    def setup_ui(self):
        self.__layout = QGridLayout()

        self.__label_process_settings = QLabel("Настройки обработки")
        self.__label_language = QLabel("Язык")
        self.__label_model = QLabel("Модель")
        self.__label_device = QLabel("Устройство")
        self.__label_quantization = QLabel("Квантизация")

        self.__checkbox_timestamp = QCheckBox("Вставлять временную метку рядом с каждой строкой")

        self.__combo_language = QComboBox()
        self.__combo_model = QComboBox()
        self.__combo_device = QComboBox()
        self.__combo_quantization = QComboBox()

        self.setLayout(self.__layout)
    
    def add_ui(self):
        self.__list_labels = (self.__label_process_settings,
                              self.__label_language,
                              self.__label_model,
                              self.__label_device,
                              self.__label_quantization,
                              self.__checkbox_timestamp)
        
        self.__list_combos = (self.__combo_language,
                              self.__combo_model,
                              self.__combo_device,
                              self.__combo_quantization)
        
        self.__amount_labels = len(self.__list_labels)
        self.__amount_combos = len(self.__list_combos)

        for i in range(self.__amount_labels-1):
            self.__layout.addWidget(self.__list_labels[i], i, 0)
        
        self.__layout.addWidget(self.__checkbox_timestamp, self.__amount_combos+1, 0, 1, 2)
        
        for i in range(self.__amount_combos):
            self.__layout.addWidget(self.__list_combos[i], i+1, 1)
    
    def actions(self):
        self.__combo_language.activated.connect(self.current_combo_language)
        self.__combo_model.activated.connect(self.current_combo_model)

    def current_combo_language(self):
        self.__current_combo_language = self.__combo_language.currentText()
        self.__root.set_current_language(self.__current_combo_language)
    
    def current_combo_model(self):
        self.__current_combo_model = self.__combo_model.currentText()
        self.__root.set_current_model(self.__current_combo_model)
    
    def fill_combo_language(self):
        for i in faster_whisper.tokenizer._LANGUAGE_CODES:
            self.__combo_language.addItem(i)
    
    def fill_combo_models(self):
        for i in faster_whisper.utils._MODELS:
            self.__combo_model.addItem(i)