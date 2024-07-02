"""Calculator module for advanced calculator."""

import logging
import pandas as pd

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Calculator:
    """Calculator for performing basic arithmetic operations with history tracking."""
    def __init__(self):
        """Initialize the calculator with an empty history."""
        self.history = pd.DataFrame(columns=['operation', 'a', 'b', 'result'])

    def add(self, a, b):
        """Add two numbers and save to history."""
        result = a + b
        self._save_history('add', a, b, result)
        logging.info("Added %s and %s to get %s", a, b, result)
        return result

    def subtract(self, a, b):
        """Subtract two numbers and save to history."""
        result = a - b
        self._save_history('subtract', a, b, result)
        logging.info("Subtracted %s from %s to get %s", b, a, result)
        return result

    def multiply(self, a, b):
        """Multiply two numbers and save to history."""
        result = a * b
        self._save_history('multiply', a, b, result)
        logging.info("Multiplied %s with %s to get %s", a, b, result)
        return result

    def divide(self, a, b):
        """Divide two numbers and save to history. Raise error if divide by zero."""
        if b == 0:
            logging.error("Attempted to divide by zero")
            raise ValueError("Cannot divide by zero.")
        result = a / b
        self._save_history('divide', a, b, result)
        logging.info("Divided %s by %s to get %s", a, b, result)
        return result

    def _save_history(self, operation, a, b, result):
        """Save the operation to the calculation history."""
        new_entry = pd.DataFrame({
            'operation': [operation],
            'a': [a],
            'b': [b],
            'result': [result]
        })

        # Ensure the new entry and history are not all-NA or empty before concatenation
        if not new_entry.dropna(how='all').empty:
            if self.history.empty:
                self.history = new_entry
            else:
                self.history = pd.concat([self.history, new_entry.dropna(how='all')], ignore_index=True)

    def save_history(self, filename):
        """Save the calculation history to a CSV file."""
        self.history.to_csv(filename, index=False)
        logging.info("History saved to %s", filename)

    def load_history(self, filename):
        """Load the calculation history from a CSV file."""
        self.history = pd.read_csv(filename)
        logging.info("History loaded from %s", filename)

class CalculatorFacade:
    """Facade for Calculator to provide a simplified interface."""
    def __init__(self):
        """Initialize the CalculatorFacade with a Calculator instance."""
        self.calculator = Calculator()

    def perform_operation(self, operation, a, b):
        """Perform the specified operation with the given operands."""
        if operation == 'add':
            return self.calculator.add(a, b)
        if operation == 'subtract':
            return self.calculator.subtract(a, b)
        if operation == 'multiply':
            return self.calculator.multiply(a, b)
        if operation == 'divide':
            return self.calculator.divide(a, b)
        logging.error("Unknown operation: %s", operation)
        raise ValueError(f"Unknown operation: {operation}")
