#!/usr/bin/python3
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """test class for user"""

    def test__init__(self):
        """test __init__"""

        user = User()
        self.assertIsInstance(User(), User)
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

