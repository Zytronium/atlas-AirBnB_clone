#!/usr/bin/python3
import unittest, models, datetime
from uuid import uuid4
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
"""test module for the BaseModel class"""


class TestBaseModel(unittest.TestCase):
    """test class for the BaseModel class"""

    def setUp(self):
        """setup the test class"""
        self.storage = FileStorage
        class_file = 'file.json'

    @classmethod
    def teardown(cls):
        """teardown the test class"""
        cls.self.storage.all.clear()
        
    def test_to_dict(self):
        """test to_dict method"""
        my_model = BaseModel()
        dict = my_model.to_dict()
        self.assertEqual(dict['__class__'], 'BaseModel')
        self.assertEqual(dict['id' ], str(uuid4()))
        self.assertEqual(dict['created_at'], datetime.datetime.today().isoformat())
        self.assertEqual(dict['updated_at'], datetime.datetime.today().isoformat())

    
    def test_save(self):
        """test save method"""
        base = BaseModel()
        base.save()
        self.assertEqual(base.updated_at, datetime.datetime.today())
        
        

    def test__str__(self):
        """test __str__ method"""
        base = BaseModel()
        self.assertEqual(str(base), "[BaseModel] ({}) {}".format(
            base.id, base.__dict__))

    def test_kwarg_init(self):
        """test kwargs that init uses"""
        date = "1971-01-01T00:00:00.000000"
        split = {'user': '3489', 'created_at': date, 'updated_at': date}



    def test_base_id(self):
        """test the id attribute"""
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsInstance(my_model.id, str)

    def test_initializaton(self):
        """test the __init__ method"""
        
        my_model = BaseModel()
        self.assertEqual(my_model.id, str(uuid.uuid4()))
        self.assertEqual(my_model.__class__.__name__, "BaseModel")
        self.assertIsInstance(my_model.created_at, datetime.datetime)
        self.assertIsInstance(my_model.updated_at, datetime.datetime)
        self.assertGreater(my_model.created_at, my_model.updated_at)
        self.assertNotEqual(my_model.created_at, my_model.updated_at)

    def (self):
        """test the datetime attributes"""

        pass


if __name__ == "__main__":
    unittest.main()
    
    
    
    

  
  
