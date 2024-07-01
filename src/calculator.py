import pandas as pd

class Calculator:
    def __init__(self):
        self.history = pd.DataFrame(columns=['operation', 'a', 'b', 'result'])

    def add(self, a, b):
        result = a + b
        self._save_history('add', a, b, result)
        return result

    def subtract(self, a, b):
        result = a - b
        self._save_history('subtract', a, b, result)
        return result

    def multiply(self, a, b):
        result = a * b
        self._save_history('multiply', a, b, result)
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        result = a / b
        self._save_history('divide', a, b, result)
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

    def load_history(self, filename):
        self.history = pd.read_csv(filename)

