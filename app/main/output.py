from PySide6.QtWidgets import (QPushButton, QGridLayout, QLabel, QTextEdit, 
                               QProgressBar, QSizePolicy, QSpacerItem)
from PySide6.QtCore import (QObject)
from faster_whisper import WhisperModel
import threading
import app.root


class Output(app.root.RootUi):
    def __init__(self, root):
        super().__init__()

        self.__root = root

    def setup_ui(self):
        self.__layout = QGridLayout()

        self.__label_output = QLabel("Вывод")

        self.__field_output = QTextEdit()

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
    
    def actions(self):
        self.__button_start.clicked.connect(self.transcribe_thread)
    
    def customize_ui(self):
        self.__label_output.setSizePolicy(QSizePolicy().Policy.Fixed, QSizePolicy().Policy.Fixed)
        self.__label_output.setStyleSheet("font-weight: bold;")
        
        self.__field_output.setReadOnly(True)
        self.__field_output.setSizePolicy(QSizePolicy().Policy.Preferred, QSizePolicy().Policy.Expanding)
    
    def transcribe(self):
        self.__current_file_path = self.__root.get_current_file_path()
        self.__current_model = self.__root.get_current_model()
        self.__current_language = self.__root.get_current_language()
        self.__current_timestamp = self.__root.get_current_timestamp()
        self.__current_quantizaton = self.__root.get_current_quantization()
        self.__current_device = self.__root.get_current_device()

        self.__model = WhisperModel(self.__current_model, device=self.__current_device, compute_type=self.__current_quantizaton)

        self.__segments, self.__info = self.__model.transcribe(self.__current_file_path, beam_size=5, language=self.__current_language)

        if self.__current_timestamp[1] == True:
            for segment in self.__segments:
                self.__field_output.append("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
        else:
            for segment in self.__segments:
                self.__field_output.append("%s" % (segment.text))
        
        self.__field_output.append("КОНЕЦ")
    
    def transcribe_thread(self):
        var_transcribe = threading.Thread(target=self.transcribe)
        var_transcribe.start()
    

