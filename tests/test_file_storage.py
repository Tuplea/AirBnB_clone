#!/usr/bin/python3
"""Test for FileStorage class"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_init(unittest.TestCase):
    """Unittests for testing initialisation of the FileStorage class"""

    def test_FileStorage_init_zero_args(self):
        """initalizing the class withouts args"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_init_with_args(self):
        """initalizing the class with args"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        """make sure that the path is private str"""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_FileStorage_objects_is_private_dict(self):
        """make sure that the __objects is private dict"""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_init_success(self):
        """test correct initialization"""
        self.assertEqual(type(models.storage), FileStorage)


class Test_FileStorage_methods(unittest.TestCase):
    """Unittests for testing FileStorage class methods"""

    @classmethod
    def setUp(self):
        """sets up test env"""
        try:
            os.rename("memory.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        """cleans up test env"""
        try:
            os.remove("memory.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "memory.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all_no_args(self):
        """test all func without args"""
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_args(self):
        """test all func with args"""
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_create_new_no_args(self):
        """test creating new instances without args"""
        base_model = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()
        models.storage.new(base_model)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(amenity)
        models.storage.new(review)
        self.assertIn("BaseModel." + base_model.id,
                      models.storage.all().keys())
        self.assertIn(base_model, models.storage.all().values())
        self.assertIn("User." + user.id, models.storage.all().keys())
        self.assertIn(user, models.storage.all().values())
        self.assertIn("State." + state.id, models.storage.all().keys())
        self.assertIn(state, models.storage.all().values())
        self.assertIn("Place." + place.id, models.storage.all().keys())
        self.assertIn(place, models.storage.all().values())
        self.assertIn("City." + city.id, models.storage.all().keys())
        self.assertIn(city, models.storage.all().values())
        self.assertIn("Amenity." + amenity.id, models.storage.all().keys())
        self.assertIn(amenity, models.storage.all().values())
        self.assertIn("Review." + review.id, models.storage.all().keys())
        self.assertIn(review, models.storage.all().values())

    def test_create_new_with_args(self):
        """test creating new instances with args"""
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_create_new_with_None(self):
        """test creating new instances with arg None"""
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save_no_args(self):
        """test save without args"""
        base_model = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()
        models.storage.new(base_model)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(amenity)
        models.storage.new(review)
        models.storage.save()
        save_text = ""
        with open("memory.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + base_model.id, save_text)
            self.assertIn("User." + user.id, save_text)
            self.assertIn("State." + state.id, save_text)
            self.assertIn("Place." + place.id, save_text)
            self.assertIn("City." + city.id, save_text)
            self.assertIn("Amenity." + amenity.id, save_text)
            self.assertIn("Review." + review.id, save_text)

    def test_save_with_args(self):
        """test save with args"""
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload_no_args(self):
        """test reload fun without args"""
        base_model = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()
        models.storage.new(base_model)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(amenity)
        models.storage.new(review)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + base_model.id, objs)
        self.assertIn("User." + user.id, objs)
        self.assertIn("State." + state.id, objs)
        self.assertIn("Place." + place.id, objs)
        self.assertIn("City." + city.id, objs)
        self.assertIn("Amenity." + amenity.id, objs)
        self.assertIn("Review." + review.id, objs)

    def test_reload_no_file(self):
        """test reload fun without a file"""
        self.assertEqual(None, models.storage.reload())

    def test_reload_with_args(self):
        """test reload fun with args"""
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
