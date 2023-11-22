import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Simple Calculator')
        self.setGeometry(100, 100, 300, 300)

        self.layout = QVBoxLayout()

        self.result_display = QLineEdit()
        self.result_display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.layout.addWidget(self.result_display)

        buttons_layout = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]

        for row in buttons_layout:
            row_layout = QHBoxLayout()
            for button_text in row:
                button = QPushButton(button_text)
                button.clicked.connect(self.on_button_clicked)
                row_layout.addWidget(button)
            self.layout.addLayout(row_layout)

        self.setLayout(self.layout)

    def on_button_clicked(self):
        button = self.sender()
        if button.text() == '=':
            expression = self.result_display.text()
            try:
                result = eval(expression)
                self.result_display.setText(str(result))
            except Exception as e:
                self.result_display.setText('Error')
        elif button.text() == 'C':
            self.result_display.clear()
        else:
            self.result_display.setText(self.result_display.text() + button.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())