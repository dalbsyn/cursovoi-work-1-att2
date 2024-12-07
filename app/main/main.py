from PySide6.QtWidgets import (QWidget, QPushButton, QLineEdit, QGridLayout,
                                QLabel, QComboBox, QCheckBox, QTextBrowser,
                                QProgressBar, QSpacerItem, QSizePolicy)
from PySide6.QtCore import QObject


class Root(QWidget):
    """# Класс Root
    Это что-то вроде абстрактного класса, который служит основой для размещения
    элементов интерфейса. Наследование от него уже вызывает функцию, которая 
    размещает интерфейс.

    Методы:
    - ui(self) - основа, в которую записываются элементы интерфейса.
    """
    def __init__(self):
        super().__init__()
        self.ui()
    
    def ui(self):
        pass


class FileSelection(Root):
    """# Класс `FileSelection(Root)`
    Инициализирует элементы для выбора файла:
    - заголовок выбора файла: `__label_file_selection`;
    - текстовое поле, куда пользователь может вставить путь до файла
    или отобразится выбранный через диалог выбора файла: `__field_file_selection`;
    - кнопка, нажатие выводит диалог выбора файла: `__button_file_selection`.
    - 
    """
    
    def __init__(self):
        super().__init__()

    def ui(self):
        self.__layout = QGridLayout()

        self.__label_file_selection = QLabel("Выбор файл")
        self.__field_file_selection = QLineEdit()
        self.__button_file_selection = QPushButton("Выбрать файл")

        self.__layout.addItem(QSpacerItem(1, 2, QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Expanding), 0, 0)
        self.__layout.addWidget(self.__label_file_selection, 1, 0, 1, 2)
        self.__layout.addWidget(self.__field_file_selection, 2, 0)
        self.__layout.addWidget(self.__button_file_selection, 2, 1)

        self.setLayout(self.__layout)

class Output(Root):
    """# Класс `Output(Root)`
    Инициализирует элементы для вывода результатов обработки и управления
    процессом:
    - `__label_output` - заголовок вывода;
    - `__field_output` - поле для вывода;
    - `__progress_output` - прогресс обработки;
    - `__button_begin` - кнопка начала обработки;
    - `__button_stop` - кнопка остановки обработки.
    """

    def __init__(self):
        super().__init__()

    def ui(self):
        self.__layout = QGridLayout()

        self.__label_output = QLabel("Вывод")
        self.__field_output = QTextBrowser()
        self.__progress_output = QProgressBar()
        self.__button_begin = QPushButton("Начать")
        self.__button_stop = QPushButton("Остановить")

        self.__layout.addWidget(self.__label_output, 0, 0, 1, 2)
        self.__layout.addWidget(self.__field_output, 1, 0, 1, 2)
        self.__layout.addWidget(self.__progress_output, 2, 0, 1, 2)
        self.__layout.addWidget(self.__button_begin, 3, 0)
        self.__layout.addWidget(self.__button_stop, 3, 1)

        self.setLayout(self.__layout)


class ProcessSettings(Root):
    """# Класс `ProcessSettings(Root)`
    Инициализирует элементы для настройки обработки:
    - заголовки-пункты: `__label_*`;
    - выпадающие меню: `__combo_model_*`.
    """

    def __init__(self):
        super().__init__()
    
    def ui(self):
        self.__layout = QGridLayout()

        self.__label_process_settings = QLabel("Настройки обработки")
        self.__label_model = QLabel("Модель")
        self.__label_language = QLabel("Язык")
        self.__label_device = QLabel("Устройство")
        self.__label_quantization = QLabel("Квантизация")

        self.__combo_model = QComboBox()
        self.__combo_language = QComboBox()
        self.__combo_device = QComboBox()
        self.__combo_quantization = QComboBox()

        self.__check_timestamp = QCheckBox("Вставить временную напротив каждой строки")

        self.__label_list = (self.__label_process_settings,
                             self.__label_model,
                             self.__label_language,
                             self.__label_device,
                             self.__label_quantization,
                             self.__check_timestamp)
        
        self.__combo_list = (self.__combo_model,
                             self.__combo_language,
                             self.__combo_device,
                             self.__combo_quantization)
        
        for i in range(0, len(self.__label_list)):
            self.__layout.addWidget(self.__label_list[i], i, 0)
        
        for i in range(0, len(self.__combo_list)):
            self.__layout.addWidget(self.__combo_list[i], i+1, 1)
                
        self.setLayout(self.__layout)

class ProcessValues(Root):
    """# Класс `ProcessValues(Root)`
    Инициализирует элементы, которые показывают выбранные значения на текущий 
    момент для дальнейшей обработки:
    - заголовки пунктов: `__label_*`;
    - заголовки-значения: `__label_value_*`.
    """

    def __init__(self):
        super().__init__()
    
    def ui(self):
        self.__layout = QGridLayout(self)

        self.__label_process_values = QLabel("Установленные настройки обработки")
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

        self.__label_list = (self.__label_process_values,
                             self.__label_selected_language, 
                             self.__label_selected_model, 
                             self.__label_selected_device, 
                             self.__label_selected_quantization,
                             self.__label_selected_timestamp, 
                             self.__label_available_ram_vram)
        
        self.__label_value_list = (self.__label_value_selected_language,
                                   self.__label_value_selected_model,
                                   self.__label_value_selected_device,
                                   self.__label_value_selected_quantization,
                                   self.__label_value_selected_timestamp,
                                   self.__label_value_available_ram_vram)
        
        for i in range(0, len(self.__label_list)):
            self.__layout.addWidget(self.__label_list[i], i, 0)

        for i in range(0, len(self.__label_value_list)):
            self.__layout.addWidget(self.__label_value_list[i], i+1, 1)

        self.__layout.addItem(QSpacerItem(1, 2, QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Expanding), 7, 0)

        self.setLayout(self.__layout)

class MainWindow(Root):
    """# Класс `MainWindow(Root)`
    Это класс, который собирает все элементы интерфейса и размещает их в окне.
    """

    def __init__(self):
        super().__init__()
    
    def ui(self):
        self.__layout = QGridLayout()

        self.__file_selection = FileSelection()
        self.__process_settings = ProcessSettings()
        self.__process_values = ProcessValues()
        self.__output = Output()

        self.__layout.addWidget(self.__file_selection, 0, 0)
        self.__layout.addWidget(self.__process_settings, 1, 0)
        self.__layout.addWidget(self.__process_values, 2, 0)
        self.__layout.addWidget(self.__output, 0, 1, 3, 1)


        self.setLayout(self.__layout)
        