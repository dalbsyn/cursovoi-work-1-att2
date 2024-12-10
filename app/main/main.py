from PySide6.QtWidgets import QGridLayout 

import app.root
import app.main.file_selection
import app.main.process_settings
import app.main.process_values
import app.main.output
import app.main.test
    
class MainWindow(app.root.RootUi):
    def __init__(self):
        self.__root = app.root.Root()
        super().__init__()
        
    
    def setup_ui(self):
        self.__layout = QGridLayout()
        self.__file_selection = app.main.file_selection.FileSelection(self.__root)
        self.__process_settings = app.main.process_settings.ProcessSettings(self.__root)
        self.__process_values = app.main.process_values.ProcessValues(self.__root)
        self.__output = app.main.output.Output(self.__root)
        self.__test = app.main.test.Test(self.__root)
        self.setLayout(self.__layout)
    
    def add_ui(self):
        self.__layout.addWidget(self.__file_selection, 0, 0)
        self.__layout.addWidget(self.__process_settings, 1, 0)
        #self.__layout.addWidget(self.__process_values, 2, 0)
        #self.__layout.addWidget(self.__test, 3, 0)
        self.__layout.addWidget(self.__output, 0, 1, 4, 1)
