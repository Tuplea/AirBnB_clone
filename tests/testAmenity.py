#!/usr/bin/python3
"""Test for Amenity class"""
import os
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests for amenity class"""

    def test_name(self):
        """tests the name attrib"""
        amenity = Amenity()
        self.assertEqual("", amenity.name)


if __name__ == '__main__':
    unittest.main()
