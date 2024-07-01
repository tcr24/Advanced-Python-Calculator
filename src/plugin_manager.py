import importlib
import os

class PluginManager:
    def __init__(self, plugin_folder='plugins'):
        self.plugin_folder = plugin_folder
        self.plugins = {}

    def load_plugins(self):
        for filename in os.listdir(self.plugin_folder):
            if filename.endswith('.py'):
                plugin_name = filename[:-3]
                module = importlib.import_module(f'{self.plugin_folder}.{plugin_name}')
                self.plugins[plugin_name] = module

    def get_plugins(self):
        return self.plugins
