#!/usr/bin/python3
"""places test class for testing"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """test class for testing"""

    def test__init__(self):
        """test for __init__"""
        self.assertEqual(Place.city_id, "")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(Place.name, "")
        self.assertEqual(Place.description, "")
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(Place.number_bathrooms, 0)

if __name__ == "__main__":
  unittest.main()