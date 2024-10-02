import unittest
import datetime
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

    def test_kwarg_init(self):
        """test kwargs that init uses"""
        date_str = "2021-01-01T00:00:00.000000"
        kwargs = {
            'id': '3489', 
            'created_at': date_str, 
            'updated_at': date_str
            }
        base = BaseModel(**kwargs)
        self.assertEqual(base.id, '3489')
        self.assertEqual(base.created_at.isoformat(), date_str)
        self.assertEqual(base.updated_at.isoformat(), date_str)

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
        self.assertIsInstance(my_model.created_at, datetime.datetime)
        self.assertIsInstance(my_model.updated_at, datetime.datetime)
        self.assertLessEqual(my_model.created_at, my_model.updated_at)


if __name__ == "__main__":
        unittest.main()
    