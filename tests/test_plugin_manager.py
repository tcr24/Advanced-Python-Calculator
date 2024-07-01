from src.plugin_manager import PluginManager

def test_load_plugins():
    manager = PluginManager(plugin_folder='plugins')
    manager.load_plugins()
    plugins = manager.get_plugins()
    assert 'sample_plugin' in plugins

def test_plugin_execution(capsys):
    from plugins import sample_plugin
    sample_plugin.main()
    captured = capsys.readouterr()
    assert "This is a sample plugin" in captured.out
