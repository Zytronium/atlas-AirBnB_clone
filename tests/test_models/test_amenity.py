#!/usr/bin/python3
"""test_amenity class"""
import unittest 
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """test case"""

    def test__init__(self):
        """test __init__"""

        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertEqual(amenity.name, "")


if __name__ == "__main__":
  unittest.main()