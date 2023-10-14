#!/usr/bin/python3
"""Test for Place class"""
import os
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Tests for amenity class"""

    def test_attrib(self):
        """Tests for public attrib"""
        place = Place()
        self.assertEqual("", place.city_id)
        self.assertEqual("", place.user_id)
        self.assertEqual("", place.name)
        self.assertEqual("", place.description)
        self.assertEqual(0, place.number_rooms)
        self.assertEqual(0, place.number_bathrooms)
        self.assertEqual(0, place.max_guest)
        self.assertEqual(0, place.price_by_night)
        self.assertEqual(0.0, place.latitude)
        self.assertEqual(0.0, place.longitude)
        self.assertEqual([], place.amenity_ids)


if __name__ == '__main__':
    unittest.main()
