import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QSpinBox,
    QLabel, QLineEdit, QStackedWidget, QScrollArea
)


class ParameterPage(QWidget):
    def __init__(self, switch_callback):
        """
        switch_callback: функция, вызываемая при нажатии кнопки OK
        """
        super().__init__()
        self.switch_callback = switch_callback
    
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        label = QLabel("Выберите количество QLineEdit:")
        self.spinBox = QSpinBox()
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(50)  # увеличил максимальное значение для демонстрации
        okButton = QPushButton("OK")
        okButton.clicked.connect(self.on_ok)

        layout.addWidget(label)
        layout.addWidget(self.spinBox)
        layout.addWidget(okButton)
        self.setLayout(layout)

    def on_ok(self):
        count = self.spinBox.value()
        self.switch_callback(count)


class LineEditPage(QWidget):
    def __init__(self, count, back_callback):
        """
        count: количество QLineEdit для создания
        back_callback: функция, вызываемая при нажатии кнопки "Назад"
        """
        super().__init__()
        self.count = count
        self.back_callback = back_callback

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # Создаем область с прокруткой для QLineEdit
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        # Контейнер для виджетов внутри области прокрутки
        container = QWidget()
        container_layout = QVBoxLayout()
        for i in range(self.count):
            le = QLineEdit()
            le.setPlaceholderText(f"LineEdit {i+1}")
            container_layout.addWidget(le)
        container.setLayout(container_layout)
        scroll_area.setWidget(container)

        # Добавляем область прокрутки в основной layout
        main_layout.addWidget(scroll_area)

        # Кнопка "Назад", которая всегда видна
        backButton = QPushButton("Назад")
        backButton.clicked.connect(self.back_callback)
        main_layout.addWidget(backButton)

        self.setLayout(main_layout)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.stack = QStackedWidget()

        self.init_ui()

    def init_ui(self):
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.stack)

        # Страница с выбором параметров
        self.paramPage = ParameterPage(self.show_lineedit_page)
        self.stack.addWidget(self.paramPage)

        self.setLayout(mainLayout)
        self.setWindowTitle("Переключение страниц в одном окне")

    def show_lineedit_page(self, count):
        # Создаем новую страницу с QLineEdit
        self.lineEditPage = LineEditPage(count, self.show_param_page)
        # Если на стеке уже есть страница LineEditPage, заменяем её
        if self.stack.count() < 2:
            self.stack.addWidget(self.lineEditPage)
        else:
            self.stack.removeWidget(self.stack.widget(1))
            self.stack.addWidget(self.lineEditPage)
        self.stack.setCurrentWidget(self.lineEditPage)

    def show_param_page(self):
        self.stack.setCurrentWidget(self.paramPage)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
