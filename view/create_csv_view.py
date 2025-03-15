import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QScrollArea, QVBoxLayout,
    QHBoxLayout, QSpinBox, QStackedWidget, QPushButton, QLineEdit
)
from PyQt6.QtCore import Qt

class SettingsOfParams(QWidget):
    def __init__(self, forward_callback):

        super().__init__()
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        self.input_name_file = QLineEdit()
        self.input_name_file.setPlaceholderText('Введите название файла')
        self.input_name_file.setFixedHeight(30)
        self.input_name_file.setFixedWidth(200)
        self.input_name_file.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.input_name_file, alignment=Qt.AlignmentFlag.AlignCenter)
        
        col_count_layout = QVBoxLayout()
        col_count_layout.setSpacing(10)
        
        self.label = QLabel('Введи количество столбцов')
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        col_count_layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.spin_box = QSpinBox()
        self.spin_box.setRange(1, 100)
        self.spin_box.setSingleStep(1)
        self.spin_box.setFixedHeight(30)
        self.spin_box.setFixedWidth(200)
        self.spin_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        col_count_layout.addWidget(self.spin_box, alignment=Qt.AlignmentFlag.AlignCenter)
        
        layout.addLayout(col_count_layout)
        
        self.forward_button = QPushButton('Вперед')
        self.forward_button.setFixedSize(100, 40)
        self.forward_button.clicked.connect(forward_callback)
        layout.addWidget(self.forward_button, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.setLayout(layout)

class WriteLine(QWidget):
    def __init__(self, col_count, headers_list, back_callback):

        super().__init__()
        self.col_count = col_count
        self.headers_list = headers_list
        self.back_callback = back_callback
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        container = QWidget()
        container_layout = QVBoxLayout(container)

        for i in range(self.col_count):
            line_edit = QLineEdit()
            line_edit.setPlaceholderText(self.headers_list[i])
            container_layout.addWidget(line_edit)
        
        scroll_area.setWidget(container)
        main_layout.addWidget(scroll_area)

        back_button = QPushButton("Назад")
        back_button.setFixedSize(100, 40)
        back_button.clicked.connect(self.back_callback)
        main_layout.addWidget(back_button, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.setLayout(main_layout)

class CreateCsvView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Создать csv-файл')
        self.setGeometry(250, 300, 300, 250)
        self.setFixedSize(300, 250)

        self.stack = QStackedWidget()
        
        self.settings_of_params = SettingsOfParams(self.show_write_line_page)
        self.stack.addWidget(self.settings_of_params)
        
        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)
        main_layout.addWidget(self.stack)
        self.setCentralWidget(central_widget)

    def show_write_line_page(self):
        col_count = self.settings_of_params.spin_box.value()
        headers_list = [f"Column {i+1}" for i in range(col_count)]
        
        self.write_line = WriteLine(col_count, headers_list, self.show_settings_page)
        
        if self.stack.count() < 2:
            self.stack.addWidget(self.write_line)
        else:
            self.stack.removeWidget(self.stack.widget(1))
            self.stack.addWidget(self.write_line)
        self.stack.setCurrentWidget(self.write_line)

    def show_settings_page(self):
        self.stack.setCurrentWidget(self.settings_of_params)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CreateCsvView()
    window.show()
    sys.exit(app.exec())
