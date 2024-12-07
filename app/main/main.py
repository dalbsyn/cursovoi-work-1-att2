from PySide6.QtWidgets import (QWidget, QPushButton, QLineEdit, QGridLayout,
                                QLabel, QComboBox, QCheckBox, QTextBrowser,
                                QProgressBar, QSpacerItem, QSizePolicy, 
                                QHBoxLayout)
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

        self.add_horizontal_widgets()

        self.setLayout(self.__layout)

    def add_horizontal_widgets(self):

        self.__methods_horizontal_widgets = (self.language(),
                                             self.model(),
                                             self.device(),
                                             self.quantization())
        
        for i in range(0, 3):
            self.__methods_horizontal_widgets[i]
        
        self.__list_horizontal_widgets = (self.__language,
                                          self.__model,
                                          self.__device,
                                          self.__quantization)
        
        
        for i in range(0, 3):
            self.__layout.addLayout(self.__list_horizontal_widgets[i], i, 0)
    
    def language(self):
        self.__language = QHBoxLayout()
        self.__language.addWidget(self.__label_language, 0)
        self.__language.addWidget(self.__combo_language, 1)

    def model(self):
        self.__model = QHBoxLayout()
        self.__model.addWidget(self.__label_model, 0)
        self.__model.addWidget(self.__combo_model, 1)

    def device(self):
        self.__device = QHBoxLayout()
        self.__device.addWidget(self.__label_device, 0)
        self.__device.addWidget(self.__combo_device, 1)
    
    def quantization(self):
        self.__quantization = QHBoxLayout()
        self.__quantization.addWidget(self.__label_quantization, 0)
        self.__quantization.addWidget(self.__combo_quantization, 1)

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

        self.__label_value_selected_language = QLabel("a")
        self.__label_value_selected_model = QLabel("a")
        self.__label_value_selected_device = QLabel("a")
        self.__label_value_selected_quantization = QLabel("a")
        self.__label_value_selected_timestamp = QLabel("a")
        self.__label_value_available_ram_vram = QLabel("a")

        self.add_horizontal_widgets()
        self.__layout.addItem(QSpacerItem(1, 2, QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Expanding), 7, 0)
        self.setLayout(self.__layout)
        
    def add_horizontal_widgets(self):
        self.__methods_horizontal_widgets = (self.selected_language(),
                                             self.selected_model(),
                                             self.selected_device(),
                                             self.selected_quantization(),
                                             self.selected_timestamp(),
                                             self.available_ram_vram())
        
        self.__methods_length = len(self.__methods_horizontal_widgets)

        for i in range(self.__methods_length):
            self.__methods_horizontal_widgets[i]

        self.__list_horizontal_widgets  = (self.__e_selected_language,
                                           self.__e_selected_model,
                                           self.__e_selected_device,
                                           self.__e_selected_quantization,
                                           self.__e_timestamp,
                                           self.__e_available_ram_vram)
        
        self.__list_length_horizontal_widgets = len(self.__list_horizontal_widgets)

        for i in range(self.__list_length_horizontal_widgets):
            self.__layout.addLayout(self.__list_horizontal_widgets[i], i, 0)


    def selected_language(self):
        self.__e_selected_language = QHBoxLayout()
        self.__e_selected_language.addWidget(self.__label_selected_language, 0)
        self.__e_selected_language.addWidget(self.__label_value_selected_language, 1)
    
    def selected_model(self):
        self.__e_selected_model = QHBoxLayout()
        self.__e_selected_model.addWidget(self.__label_selected_model, 0)
        self.__e_selected_model.addWidget(self.__label_value_selected_model, 1)
    
    def selected_device(self):
        self.__e_selected_device = QHBoxLayout()
        self.__e_selected_device.addWidget(self.__label_selected_device, 0)
        self.__e_selected_device.addWidget(self.__label_value_selected_device, 1)

    def selected_quantization(self):
        self.__e_selected_quantization = QHBoxLayout()
        self.__e_selected_quantization.addWidget(self.__label_selected_quantization, 0)
        self.__e_selected_quantization.addWidget(self.__label_value_selected_quantization, 1)
    
    def selected_timestamp(self):
        self.__e_timestamp = QHBoxLayout()
        self.__e_timestamp.addWidget(self.__label_selected_timestamp, 0)
        self.__e_timestamp.addWidget(self.__label_value_selected_timestamp, 1)
    
    def available_ram_vram(self):
        self.__e_available_ram_vram = QHBoxLayout()
        self.__e_available_ram_vram.addWidget(self.__label_available_ram_vram, 0)
        self.__e_available_ram_vram.addWidget(self.__label_value_available_ram_vram, 1)

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
        