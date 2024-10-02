#!/us/bin/python3
"""__init__ file for the engine package"""
from models.engine.file_storage import FileStorage
from models.engine.settings_storage import SettingsStorage

storage = FileStorage()
storage.reload()
setting_storage = SettingsStorage()
setting_storage.reload()
