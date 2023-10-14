#!/usr/bin/python3
"""Test for State class"""
import os
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Tests for amenity class"""

    def test_attrib(self):
        """Tests for public attrib"""
        state = State()
        self.assertEqual("", state.name)


if __name__ == '__main__':
    unittest.main()
