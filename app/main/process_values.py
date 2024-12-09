from PySide6.QtWidgets import (QGridLayout, QLabel, QComboBox, QHBoxLayout)
import app.root

class ProcessValues(app.root.RootUi):
    def __init__(self, root):
        super().__init__()

        self.__root = root

    def setup_ui(self):
        self.__layout = QGridLayout(self)

        self.__label_process_values = QLabel("Значения обработки")
        self.__label_selected_language = QLabel("Выбранный язык:")
        self.__label_selected_model = QLabel("Выбранная модель:")
        self.__label_selected_device = QLabel("Выбранное устройство:")
        self.__label_selected_quantization = QLabel("Выбранная квантизация:")
        self.__label_selected_timestamp = QLabel("Наличие временной метки:")
        self.__label_available_ram_vram = QLabel("Доступно ОЗУ/видеопамяти:")

        self.__label_value_selected_language = QLabel(None)
        self.__label_value_selected_model = QLabel(None)
        self.__label_value_selected_device = QLabel(None)
        self.__label_value_selected_quantization = QLabel(None)
        self.__label_value_selected_timestamp = QLabel(None)
        self.__label_value_available_ram_vram = QLabel(None)

        
        self.setLayout(self.__layout)
    
    def add_ui(self):
        self.__list_methods = (self.selected_language(),
                               self.selected_model(),
                               self.selected_device(),
                               self.selected_quantization(),
                               self.selected_timestamp(),
                               self.available_ram_vram())
        
        self.__list_entries = (self.__selected_language,
                               self.__selected_model,
                               self.__selected_device,
                               self.__selected_quantization,
                               self.__selected_timestamp,
                               self.__available_ram_vram)
        
        self.__amount_methods = len(self.__list_methods)
        self.__amount_entries = len(self.__list_entries)

        for i in range(self.__amount_methods):
            self.__list_methods[i]
        
        self.__layout.addWidget(self.__label_process_values, 0, 0, 1, 2)
        for i in range(self.__amount_entries):
            self.__layout.addLayout(self.__list_entries[i], i+1, 0, 1, 2)
    
    def selected_language(self):
        self.__selected_language = QHBoxLayout()
        self.__selected_language.addWidget(self.__label_selected_language, 0)
        self.__selected_language.addWidget(self.__label_value_selected_language, 1)
    
    def selected_model(self):
        self.__selected_model = QHBoxLayout()
        self.__selected_model.addWidget(self.__label_selected_model, 0)
        self.__selected_model.addWidget(self.__label_value_selected_model, 1)
    
    def selected_device(self):
        self.__selected_device = QHBoxLayout()
        self.__selected_device.addWidget(self.__label_selected_device, 0)
        self.__selected_device.addWidget(self.__label_value_selected_device, 1)
    
    def selected_quantization(self):
        self.__selected_quantization = QHBoxLayout()
        self.__selected_quantization.addWidget(self.__label_selected_quantization, 0)
        self.__selected_quantization.addWidget(self.__label_value_selected_quantization, 1)

    def selected_timestamp(self):
        self.__selected_timestamp = QHBoxLayout()
        self.__selected_timestamp.addWidget(self.__label_selected_timestamp, 0)
        self.__selected_timestamp.addWidget(self.__label_value_selected_timestamp, 1)
    
    def available_ram_vram(self):
        self.__available_ram_vram = QHBoxLayout()
        self.__available_ram_vram.addWidget(self.__label_available_ram_vram, 0)
        self.__available_ram_vram.addWidget(self.__label_value_available_ram_vram, 1)