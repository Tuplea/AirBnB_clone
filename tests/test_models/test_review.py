#!/usr/bin/python3
"""Test for Review class"""
import os
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Tests for review class"""

    def test_attrib(self):
        """Tests for public attrib"""
        review = Review()
        self.assertEqual("", review.place_id)
        self.assertEqual("", review.user_id)
        self.assertEqual("", review.text)


if __name__ == '__main__':
    unittest.main()
