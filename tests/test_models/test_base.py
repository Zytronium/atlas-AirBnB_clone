import unittest
from uuid import uuid4
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_to_dict(self):
        """test to_dict method"""
        my_model = BaseModel()
        dict_rep = my_model.to_dict()
        self.assertEqual(dict_rep['__class__'], 'BaseModel')
        self.assertEqual(dict_rep['id'], my_model.id)
        self.assertEqual(dict_rep['created_at'],
                        my_model.created_at.isoformat())
        self.assertEqual(dict_rep['updated_at'],
                        my_model.updated_at.isoformat())

    def test_save(self):
        """test save method"""
        base = BaseModel()
        old_updated_at = base.updated_at
        base.save()
        self.assertNotEqual(base.updated_at, old_updated_at)

    def test__str__(self):
        """test __str__ method"""
        base = BaseModel()
        self.assertEqual(str(base), "[BaseModel] ({}) {}".format(
                base.id, base.__dict__))

    def test_base__init__kwargs(self):
        time = datetime.now().isoformat()
        base_id = str(uuid4())
        kwargs = {'id': base_id, 'created_at': time, 'updated_at': time}
        base = BaseModel(**kwargs)
        self.assertEqual(base.id, base_id)
        self.assertEqual(base.created_at.isoformat(), time)
        self.assertEqual(base.updated_at.isoformat(), time)

    def test_base_id(self):
        """test the id attribute"""
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsInstance(my_model.id, str)

    def test_initializaton(self):
        """test the __init__ method"""
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)
        self.assertEqual(my_model.__class__.__name__, "BaseModel")
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)
        self.assertLessEqual(my_model.created_at, my_model.updated_at)


if __name__ == "__main__":
        unittest.main()
    