#!/usr/bin/python3
"""class for testing the storage"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """test the file storage"""

    def test_base_init_(self):
        """test the base init"""
        exp = {
            'id': '3423',
            'created_at': '2021-02-03T13:52:46.957343',
            'updated_at': '2021-02-03T13:52:46.957343'
        }
        tmp = BaseModel(**exp)
        self.assertEqual(tmp.id, '3423')
        self.assertEqual(tmp.created_at.isoformat(timespec='seconds'))
        

    def test_all(self):
        """test the all method"""
        storage = FileStorage()
        self.assertIsNotNone(storage.all())

    def test_new(self):
        """test the new method"""
        tmp = BaseModel()
        storage = FileStorage()
        storage.new(tmp)
        self.assertIn(type(tmp).__name__, storage.all())
        self.assertEqual(storage.all()[type(tmp).__name__].id, tmp.id)

    def test_save(self):
        """test the save method"""
        storage = FileStorage()
        tmp = BaseModel()
        storage.new(tmp)
        storage.save()
        self.assertIn(type(tmp).__name__, storage.all())
        storage.reload()

if __name__ == "__main__":
    unittest.main()
