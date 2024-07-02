import sys
import os
import pytest
from plugin_manager import PluginManager

# Add the plugins directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'plugins'))

def test_load_plugins():
    manager = PluginManager(plugin_folder='plugins')
    manager.load_plugins()
    assert 'sample_plugin' in manager.get_plugins()
