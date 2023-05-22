# Calculator

This is a simple calculator application built using PyQt5. It provides basic arithmetic operations and supports number conversion between different number systems such as decimal, binary, octal, and hexadecimal.

## Requirements
- Python 3.x
- PyQt5

## Installation
1. Clone the repository or download the source code files.
2. Install the required dependencies using the following command:
```pip install pyqt5```

## Usage
Run the following command to start the calculator application:
```python calculator.py```

## Features
- Arithmetic operations: Addition, subtraction, multiplication, and division.
- Number conversion: Convert numbers between decimal, binary, octal, and hexadecimal.
- Keyboard support: The calculator can be used with the keyboard. The Enter key is used to evaluate the expression, and Backspace key is used to delete characters.

## Interface
The calculator interface consists of the following components:
- Convert from: A drop-down menu to select the number system to convert from (decimal, binary, octal, or hexadecimal).
- Convert to: A drop-down menu to select the number system to convert to.
- Result: A text input field to display the result or user input.
- Calculator buttons: Buttons for numbers (0-9), operators (+, -, *, /), decimal point (.), and special buttons like clear (C) and equals (=).

## Styling
The calculator interface is styled using CSS. The style sheet is defined within the code.

## Examples
To perform an arithmetic operation, enter the expression using the calculator buttons or the keyboard and press the equals (=) button or the Enter key. The result will be displayed in the result field.

To convert a number from one number system to another, select the number system to convert from in the "Convert from" drop-down menu and the number system to convert to in the "Convert to" drop-down menu. Enter the number in the result field, and the converted number will be displayed in the result field.

Note: The calculator supports only basic arithmetic operations and may display an error message for complex or invalid expressions.

## License
This project is licensed under the [MIT License](LICENSE).

Feel free to explore and use the calculator application for your calculations and number conversions!
