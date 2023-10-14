#!/usr/bin/python3
"""Test for City class"""
import os
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Tests for amenity class"""

    def test_attrib(self):
        """Tests for public attrib"""
        city = City()
        self.assertEqual("", city.state_id)
        self.assertEqual("", city.name)


if __name__ == '__main__':
    unittest.main()
