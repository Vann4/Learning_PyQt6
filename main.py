import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton
from PyQt6.QtGui import QLinearGradient, QColor, QFont

app = QApplication(sys.argv)

font = QFont('Arial', 12) #Текст и размер шрифта


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Изучение PyQt6')
        self.setFixedSize(400, 100)
        self.move(800, 350)

        self.layout = QVBoxLayout()
        self.label = QLabel('Введите ваше имя: ')
        self.label.setStyleSheet('color: blue;')
        self.label.setFont(font)

        self.line_edit = QLineEdit()
        self.line_edit.setFont(font)

        self.button = QPushButton('Ввод')
        self.button.setStyleSheet('color: purple;')
        self.button.setStyleSheet('background-color: pink;')
        self.button.setFont(font)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.get_user_data)
        self.setLayout(self.layout)

        self.gradient = QLinearGradient(0, 0, 0, self.height())
        self.gradient.setColorAt(0, QColor(255, 150, 255))  # Начальный цвет градиента
        self.gradient.setColorAt(1, QColor(148, 100, 255))  # Конечный цвет градиента
        self.setAutoFillBackground(True)
        self.p = self.palette()
        self.p.setBrush(self.backgroundRole(), self.gradient)
        self.setPalette(self.p)

    def get_user_data(self):
        self.user_name = self.line_edit.text() #Получение данных

        self.layout.removeWidget(self.label)
        self.label.deleteLater()
        self.layout.removeWidget(self.line_edit)
        self.line_edit.deleteLater()
        self.layout.removeWidget(self.button)
        self.button.deleteLater()

        self.label = QLabel(f'Приятно познакомиться {self.user_name}!')
        self.label.setFont(font)
        self.label.setStyleSheet('color: blue;')
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)


window = MainWindow()
window.show()

sys.exit(app.exec())
