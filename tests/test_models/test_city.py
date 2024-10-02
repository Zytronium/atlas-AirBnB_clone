#!/usr/bin/python3
"""testing class for City"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """testing class for City"""


    def test__init__(self):
      """test for __init__"""

      my_city = City()
      self.assertEqual(my_city.name, "")
      self.assertEqual(my_city.state_id, "")

if __name__ == "__main__":
  unittest.main()