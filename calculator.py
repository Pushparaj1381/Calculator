import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QComboBox,
    QLineEdit,
    QPushButton,
    QGridLayout,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QSizePolicy,
)

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setStyleSheet('''
           QMainWindow {
                background-color: #f2f2f2;
            }
            
            QLabel {
                font-size: 22px;
                color: #1e90ff;
                margin-top: 0;
                margin-bottom: 5px;
            }

            QLineEdit {
                margin-bottom: 10px;
                padding: 10px;
                font-size: 24px;
                text-align: right;
                background-color: #d6d6d6;
                color: #363636;
                border-radius: 5px;
                width: 350px;
            }

            QComboBox {
                margin-bottom: 10px;
                padding: 10px;
                font-size: 24px;
                background-color: #d6d6d6;
                color: #363636;
                border-radius: 5px;
                width: 350px;
            }

            QPushButton {
                height: 40px;
                padding: 10px;
                margin-bottom: 5px;
                font-size: 18px;
                border: none;
                border-radius: 5px;
                width: 120px;
            }

            QPushButton.operator {
                background-color: #e65037;
                color: #ffffff;
            }

            QPushButton.operator:hover {
                background-color: #c43e29;
            }

            QPushButton.delete {
                background-color: #eb8934;
                color: #ffffff;
                height: 60px;
                padding: 0;
            }

            QPushButton.delete:hover {
                background-color: #d77631;
            }

            QPushButton.equals {
                background-color: #009f4d;
                color: #ffffff;
                width: 120px;
            }

            QPushButton.equals:hover {
                background-color: #007d3b;
            }
        ''')

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        convert_layout = QVBoxLayout()
        main_layout.addLayout(convert_layout)

        from_layout = QHBoxLayout()
        convert_layout.addLayout(from_layout)

        convert_from_label = QLabel("Convert from:")
        convert_from_label.setFixedWidth(185)
        self.from_combo_box = QComboBox()
        self.from_combo_box.addItems(["Decimal", "Binary", "Octal", "Hexadecimal"])
        self.from_combo_box.currentIndexChanged.connect(self.update_to_number_system_options)
        self.from_combo_box.setFixedWidth(165)

        from_layout.addWidget(convert_from_label)
        from_layout.addWidget(self.from_combo_box)

        to_layout = QHBoxLayout()
        convert_layout.addLayout(to_layout)

        convert_to_label = QLabel("Convert to:")
        convert_to_label.setFixedWidth(185)
        self.to_combo_box = QComboBox()
        self.to_combo_box.setFixedWidth(165)

        to_layout.addWidget(convert_to_label)
        to_layout.addWidget(self.to_combo_box)

        self.result_line_edit = QLineEdit()
        self.result_line_edit.setFixedWidth(335)

        buttons_layout = QGridLayout()
        button_values = [
            ['7', '8', '9', '+'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '*'],
            ['0', '.', 'C', '/'],
            ['\u232b', '\u003d']
        ]

        for row, button_row in enumerate(button_values):
            for col, value in enumerate(button_row):
                button = QPushButton(value)
                if value == '\u232b':
                    button.clicked.connect(self.handle_backspace)
                    button.setProperty('class', 'delete')
                    button.setFixedWidth(150)  # Set fixed width for backspace button
                    buttons_layout.addWidget(button, row, col, 1, 2)  # Span two columns
                elif value == '\u003d':
                    button.clicked.connect(self.handle_equals)
                    button.setProperty('class', 'equals')
                    button.setFixedWidth(150)  # Set fixed width for equals button
                    buttons_layout.addWidget(button, row, col+1)  # Place in the second column
                else:
                    button.clicked.connect(lambda _, val=value: self.append_value(val))
                    button.setProperty('class', 'operator')
                    buttons_layout.addWidget(button, row, col)

        self.calculator_widget = QWidget(self)
        self.calculator_widget.setStyleSheet('''
            /* Rest of the style definitions */
        ''')
        self.calculator_widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.calculator_widget.setMaximumWidth(350)
        self.calculator_widget.setLayout(buttons_layout)

        main_layout.addStretch()  # Add stretchable space to center the calculator
        main_layout.addLayout(from_layout)  # Moved from_layout to main_layout
        main_layout.addLayout(to_layout)  # Moved to_layout to main_layout
        main_layout.addWidget(self.result_line_edit)  # Moved result_line_edit above calculator_widget
        main_layout.addWidget(self.calculator_widget)
        main_layout.addStretch()  # Add stretchable space to center the calculator

        central_widget.setFixedWidth(350)

    def update_to_number_system_options(self):
        from_number_systems = {
            'Decimal': 10,
            'Binary': 2,
            'Octal': 8,
            'Hexadecimal': 16
        }
        from_number_system = self.from_combo_box.currentText()
        from_base = from_number_systems.get(from_number_system)
        self.to_combo_box.clear()

        for to_number_system, to_base in from_number_systems.items():
            if to_base != from_base:
                self.to_combo_box.addItem(to_number_system)

    def handle_backspace(self):
        current_text = self.result_line_edit.text()
        if current_text:
            self.result_line_edit.setText(current_text[:-1])
        else:
            self.result_line_edit.clear()

    def append_value(self, value):
        current_text = self.result_line_edit.text()
        self.result_line_edit.setText(current_text + value)

    def append_value(self, value):
        current_text = self.result_line_edit.text()
        if value == 'C':
            self.result_line_edit.clear()
        else:
            self.result_line_edit.setText(current_text + value)


    def handle_equals(self):
        expression = self.result_line_edit.text()
        try:
            result = eval(expression)
            self.result_line_edit.setText(str(result))
        except Exception as e:
            self.result_line_edit.setText("Error")

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Return or key == Qt.Key_Enter:
            self.handle_equals()
        elif key == Qt.Key_Backspace:
            if self.result_line_edit.hasFocus():
                self.handle_backspace()
            else:
                current_text = self.result_line_edit.text()
                self.result_line_edit.setText(current_text[:-1])
        elif key == Qt.Key_0:
            self.append_value('0')
        elif key == Qt.Key_1:
            self.append_value('1')
        elif key == Qt.Key_2:
            self.append_value('2')
        elif key == Qt.Key_3:
            self.append_value('3')
        elif key == Qt.Key_4:
            self.append_value('4')
        elif key == Qt.Key_5:
            self.append_value('5')
        elif key == Qt.Key_6:
            self.append_value('6')
        elif key == Qt.Key_7:
            self.append_value('7')
        elif key == Qt.Key_8:
            self.append_value('8')
        elif key == Qt.Key_9:
            self.append_value('9')
        elif key == Qt.Key_Plus:
            self.append_value('+')
        elif key == Qt.Key_Minus:
            self.append_value('-')
        elif key == Qt.Key_Asterisk:
            self.append_value('*')
        elif key == Qt.Key_Slash:
            self.append_value('/')
        elif key == Qt.Key_Period:
            self.append_value('.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = CalculatorApp()
    calculator.show()
    sys.exit(app.exec_())
