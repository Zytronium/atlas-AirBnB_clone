#!/usr/bin/python3
"""classs for testing Review"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """testing for the __init__"""


    def test_init(self):
        """__init__"""

        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

if __name__ == "__main__":
    unittest.main()