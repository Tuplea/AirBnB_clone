#!/usr/bin/python3
"""Test for User class"""
import os
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Tests for User class"""

    def test_attrib(self):
        """Tests for public attrib"""
        user = User()
        self.assertEqual("", user.email)
        self.assertEqual("", user.password)
        self.assertEqual("", user.first_name)
        self.assertEqual("", user.last_name)


if __name__ == '__main__':
    unittest.main()
