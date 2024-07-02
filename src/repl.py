from calculator import CalculatorFacade
from plugin_manager import PluginManager

class REPL:
    def __init__(self):
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
            'plugins': self.list_plugins
        }
        self.load_plugin_commands()

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

    def load_plugin_commands(self):
        for name, plugin in self.plugin_manager.get_plugins().items():
            self.commands[name] = plugin.main

    def add(self, a, b):
        result = self.calculator.perform_operation('add', float(a), float(b))
        print(result)

    def subtract(self, a, b):
        result = self.calculator.perform_operation('subtract', float(a), float(b))
        print(result)

    def multiply(self, a, b):
        result = self.calculator.perform_operation('multiply', float(a), float(b))
        print(result)

    def divide(self, a, b):
        result = self.calculator.perform_operation('divide', float(a), float(b))
        print(result)

    def save_history(self, filename):
        self.calculator.calculator.save_history(filename)
        print(f"History saved to {filename}")

    def load_history(self, filename):
        self.calculator.calculator.load_history(filename)
        print(f"History loaded from {filename}")

    def exit(self):
        print("Exiting the calculator.")
        exit()

    def list_plugins(self):
        print("Available plugins:")
        for plugin in self.plugin_manager.get_plugins():
            print(f"- {plugin}")

if __name__ == "__main__":
    repl = REPL()
    repl.start()
