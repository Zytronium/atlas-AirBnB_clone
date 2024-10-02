#!/usr/bin/python3
"""class for testing state"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """class for testing state"""
    
    def setUp(self):  
        """setup for testing"""
        
        self.state = State()
        self.state.name = 'Texas'
  
    def test__init__(self):
        """test __init__"""
      
        self.assertEqual(self.state.name, 'Texas')


if __name__ == "__main__":
  unittest.main()