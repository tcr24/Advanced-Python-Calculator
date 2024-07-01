import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Calculator:
    def __init__(self):
        self.history = pd.DataFrame(columns=['operation', 'a', 'b', 'result'])

    def add(self, a, b):
        result = a + b
        self._save_history('add', a, b, result)
        logging.info(f"Added {a} and {b} to get {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self._save_history('subtract', a, b, result)
        logging.info(f"Subtracted {b} from {a} to get {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self._save_history('multiply', a, b, result)
        logging.info(f"Multiplied {a} with {b} to get {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            logging.error("Attempted to divide by zero")
            raise ValueError("Cannot divide by zero.")
        result = a / b
        self._save_history('divide', a, b, result)
        logging.info(f"Divided {a} by {b} to get {result}")
        return result

    def _save_history(self, operation, a, b, result):
        self.history = self.history.append({
            'operation': operation,
            'a': a,
            'b': b,
            'result': result
        }, ignore_index=True)

    def save_history(self, filename):
        self.history.to_csv(filename, index=False)
        logging.info(f"History saved to {filename}")

    def load_history(self, filename):
        self.history = pd.read_csv(filename)
        logging.info(f"History loaded from {filename}")

class CalculatorFacade:
    def __init__(self):
        self.calculator = Calculator()

    def perform_operation(self, operation, a, b):
        if operation == 'add':
            return self.calculator.add(a, b)
        elif operation == 'subtract':
            return self.calculator.subtract(a, b)
        elif operation == 'multiply':
            return self.calculator.multiply(a, b)
        elif operation == 'divide':
            return self.calculator.divide(a, b)
        else:
            logging.error(f"Unknown operation: {operation}")
            raise ValueError(f"Unknown operation: {operation}")
