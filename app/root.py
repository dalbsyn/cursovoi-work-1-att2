from PySide6.QtWidgets import QWidget

class Root:
    def __init__(self):
        super().__init__()

        self.__current_file_path = None
        self.__current_language = None
        self.__current_model = None
    
    def set_current_file_path(self, value: str):
        self.__current_file_path = value
    
    def set_current_language(self, value: str):
        self.__current_language = value

    def set_current_model(self, value: str):
        self.__current_model = value

    def get_current_file_path(self):
        return self.__current_file_path
    
    def get_current_language(self):
        return self.__current_language
    
    def get_current_model(self):
        return self.__current_model

class RootUi(QWidget):
    """# Класс `RootUI(Qwidget)`
    Предоставляет шаблон для создания элементов интерфейса с помощью следующих
    методов:
    - `setup_ui` - инициализация элементов интерфейса;
    - `add_ui` - добавление элементов интерфейса;
    - `customize_ui` - настройка элементов интерфейса;
    - `actions` - присваивание элементам интерфейса функций."""

    def __init__(self):
        super().__init__()

        self.setup_ui()
        self.add_ui()
        self.customize_ui()
        self.actions()

    def setup_ui(self):
        """# Метод `setup_ui()`
        Шаблон, в котором инициализируются элементы интерфейса, вроде
        заголовков, кнопок, выпадающих меню и т. п.
        Входные параметры: никакие."""

        pass

    def add_ui(self):
        """#  Метод `add_ui()`
        Шаблон, в котором добавляются элементы интерфейса к макету, который
        обычно инициализируется в `setup_ui()` (cм. "Метод `setup_ui()`).
        Входные параметры: никакие.
        """
        
        pass

    def customize_ui(self):
        """# Метод `customize_ui()`
        Шаблон, в котором настраивается внешний вид элементов интерфейса,
        которые были инициализированы в `setup_ui()` (см. "Метод `setup_ui()`)
        и уже добавлены в `add_ui()` (cм. "Метод `add_ui()`).
        Входные параметры: никакие."""

        pass

    def actions(self):
        """# Метод `actions()`
        Шаблон, в котором инициализируются функции элементам интерфейса.
        Например: выполнение функции (в собственном классе) при нажатии на
        кнопку, который был инициализирован в `setup_ui()` (см. "Метод 
        `setup_ui()`) и уже добавлен в `add_ui()` (см. "Метод `add_ui()`")
        Входные параметры: никакие."""

        pass