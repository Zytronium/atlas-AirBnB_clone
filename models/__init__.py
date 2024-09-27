#!/us/bin/python3
"""__init__ file for the engine package"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()