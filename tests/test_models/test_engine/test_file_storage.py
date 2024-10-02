#!/usr/bin/python3
"""class for testing the storage"""
import unittest, os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """test the file storage"""

    def test_all(self):
        """test the all method"""
        storage = FileStorage()
        self.assertIsNotNone(storage.all())

if __name__ == "__main__":
    unittest.main()
