"""Plugin manager for the advanced calculator."""

import importlib
import os

class PluginManager:
    """Manager for loading and handling plugins."""
    def __init__(self, plugin_folder='plugins'):
        """Initialize the plugin manager with the given folder."""
        self.plugin_folder = plugin_folder
        self.plugins = {}

    def load_plugins(self):
        """Load all plugins from the plugin folder."""
        for filename in os.listdir(self.plugin_folder):
            if filename.endswith('.py') and filename != '__init__.py':
                plugin_name = filename[:-3]
                module = importlib.import_module(plugin_name)
                self.plugins[plugin_name] = module

    def get_plugins(self):
        """Get the loaded plugins."""
        return self.plugins
