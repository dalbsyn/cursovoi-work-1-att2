from PySide6.QtWidgets import (QWidget, QPushButton, QLineEdit, QGridLayout,
                                QLabel, QComboBox, QCheckBox)

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

    # def add_elements(self):
    #    pass


class FileSelection(Root):
    """# Класс `FileSelection(Root)`
    Инициализирует элементы для выбора файла:
    - `__label_file_selection` - заголовок выбора файла;
    - `__field_file_selection` - текстовое поле, куда заполняется пользователем
    или программой путь до требуемого или выбранного файла соответственно;
    - `__button_file_selection` - кнопка, нажатие выводит диалог выбора файла.
    """
    
    def __init__(self):
        super().__init__()

    def ui(self):
        self.__layout = QGridLayout()

        self.__label_file_selection = QLabel("Select file")
        self.__field_file_selection = QLineEdit()
        self.__button_file_selection = QPushButton("Select file")
        
        self.__layout.addWidget(self.__label_file_selection, 0, 0)
        self.__layout.addWidget(self.__field_file_selection, 1, 0)
        self.__layout.addWidget(self.__button_file_selection, 1, 1)

        self.setLayout(self.__layout)

class ProcessSettings(Root):
    """# Класс `ProcessSettings(Root)`
    Инициализирует элементы для настройки обработки:
    - заголовки:
        - `__label_process_settings` - пункт всего настроек;
        - `__label_model` - пункт выбора модели;
        - `__label_language` - пункт выбора языка;
        - `__label_device` - пункт выбор устройства обработки;
        - `__label_quantization` - пункт выбора квантизации.
    - выпадающие меню:
        - `__combo_model` - пункты выбора модели;
        - `__combo_language` - пункты выбора языка;
        - `__combo_device` - пункты выбора устройства;
        - `__combo_quantization` -  пункты выбора квантизации.
    """
    def __init__(self):
        super().__init__()
    
    def ui(self):
        self.__layout = QGridLayout()

        self.__label_process_settings = QLabel("Process settings")
        self.__label_model = QLabel("Model")
        self.__label_language = QLabel("Language")
        self.__label_device = QLabel("Device")
        self.__label_quantization = QLabel("Quantization")

        self.__combo_model = QComboBox()
        self.__combo_language = QComboBox()
        self.__combo_device = QComboBox()
        self.__combo_quantization = QComboBox()

        self.__check_timestamp = QCheckBox("Insert timestamp beside every line of output")

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


class MainWindow(Root):
    """# Класс `MainWindow(Root)`
    Это класс, который собирает все элементы интерфейса и размещает их в окне.
    """

    def __init__(self):
        super().__init__()
    
    def ui(self):
        self.__layout = QGridLayout()

        self.__layout.addWidget(FileSelection(), 0, 0)
        self.__layout.addWidget(ProcessSettings(), 1, 0)

        self.setLayout(self.__layout)
        