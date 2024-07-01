# src/repl.py
from calculator import Calculator

class REPL:
    def __init__(self):
        self.calculator = Calculator()
        self.commands = {
            'add': self.add,
            'subtract': self.subtract,
            'multiply': self.multiply,
            'divide': self.divide,
            'exit': self.exit
        }

    def start(self):
        while True:
            user_input = input("calc> ").strip().split()
            command = user_input[0]
            args = user_input[1:]
            if command in self.commands:
                try:
                    self.commands[command](*args)
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print(f"Unknown command: {command}")

    def add(self, a, b):
        result = self.calculator.add(float(a), float(b))
        print(result)

    def subtract(self, a, b):
        result = self.calculator.subtract(float(a), float(b))
        print(result)

    def multiply(self, a, b):
        result = self.calculator.multiply(float(a), float(b))
        print(result)

    def divide(self, a, b):
        result = self.calculator.divide(float(a), float(b))
        print(result)

    def exit(self):
        print("Exiting the calculator.")
        exit()
