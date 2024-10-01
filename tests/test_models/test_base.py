#!/usr/bin/python3
import unittest
import models
import datetime
from models.base_model import BaseModel

"""test module for the BaseModel class"""


class TestBase(unittest.TestCase):

    def test_base_model(self):
        obj = BaseModel()
        obj.name = "Atlas"
        obj.my_number = 98
        obj.save()
        obj_dict = obj.to_dict()  
        self.assertEqual(obj_dict["name"], "Atlas")
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertEqual(obj_dict["my_number"], 98)
        self.assertEqual(isinstance(obj_dict["created_at"], datetime.datetime), True)
        self.assertEqual(isinstance(obj_dict["updated_at"], datetime.datetime), True)

if __name__ == "__main__":
    unittest.main()
    
    
    
    

  
  
