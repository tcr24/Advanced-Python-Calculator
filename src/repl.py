"""REPL for the advanced calculator."""

import sys
import os

from calculator import CalculatorFacade
from plugin_manager import PluginManager

# Add the src and plugins directories to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'plugins'))

class REPL:
    """Read-Eval-Print Loop (REPL) for the advanced calculator."""
    def __init__(self):
        """Initialize the REPL with calculator and plugin manager."""
        self.calculator = CalculatorFacade()
        self.plugin_manager = PluginManager()
        self.plugin_manager.load_plugins()
        self.commands = {
            'add': self.add,
            'subtract': self.subtract,
            'multiply': self.multiply,
            'divide': self.divide,
            'save': self.save_history,
            'load': self.load_history,
            'exit': self.exit,
            'plugins': self.list_plugins,
            'menu': self.menu  # Add the menu command
        }
        self.load_plugin_commands()

    def start(self):
        """Start the REPL."""
        while True:
            user_input = input("calc> ").strip().split()
            command = user_input[0]
            args = user_input[1:]
            if command in self.commands:
                try:
                    self.commands[command](*args)
                except ValueError as ve:
                    print(f"Error: {ve}")
                except Exception as e:  # pylint: disable=broad-except
                    print(f"Unexpected error: {e}")
            else:
                print(f"Unknown command: {command}")

    def load_plugin_commands(self):
        """Load commands from plugins."""
        for name, plugin in self.plugin_manager.get_plugins().items():
            self.commands[name] = plugin.main

    def add(self, a, b):
        """Add two numbers."""
        result = self.calculator.perform_operation('add', float(a), float(b))
        print(result)

    def subtract(self, a, b):
        """Subtract two numbers."""
        result = self.calculator.perform_operation('subtract', float(a), float(b))
        print(result)

    def multiply(self, a, b):
        """Multiply two numbers."""
        result = self.calculator.perform_operation('multiply', float(a), float(b))
        print(result)

    def divide(self, a, b):
        """Divide two numbers."""
        result = self.calculator.perform_operation('divide', float(a), float(b))
        print(result)

    def save_history(self, filename):
        """Save calculation history to a file."""
        self.calculator.calculator.save_history(filename)
        print(f"History saved to {filename}")

    def load_history(self, filename):
        """Load calculation history from a file."""
        self.calculator.calculator.load_history(filename)
        print(f"History loaded from {filename}")

    def exit(self):
        """Exit the REPL."""
        print("Exiting the calculator.")
        sys.exit()

    def list_plugins(self):
        """List available plugins."""
        print("Available plugins:")
        for plugin in self.plugin_manager.get_plugins():
            print(f"- {plugin}")

    def menu(self):
        """List all available commands."""
        print("Available commands:")
        for command in self.commands:
            print(f"- {command}")

if __name__ == "__main__":
    repl = REPL()
    repl.start()
