#!/usr/bin/python3
"""Test for BaseModel class"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_no_args_instantiates(self):
        """tests init with no args"""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        """tests existance of an instance in storage"""
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        """test id is a public str"""
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        """test if created_at is public datetime obj"""
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        """test if updated_at is public datetime obj"""
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        """test unique ids"""
        base_model_1 = BaseModel()
        base_model_2 = BaseModel()
        self.assertNotEqual(base_model_1.id, base_model_2.id)

    def test_two_models_different_created_at(self):
        """test if created_at is assigned correctly"""
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_two_models_different_updated_at(self):
        """test if updated_at is assigned correctly"""
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.updated_at, bm2.updated_at)

    def test_str_representation(self):
        """tests str repr conformity"""
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)

    def test_args_unused(self):
        """test unused args"""
        base_model = BaseModel(None)
        self.assertNotIn(None, base_model.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """test initiation with **kargs"""
        date_t = datetime.today()
        date_t_iso = date_t.isoformat()
        base_model = BaseModel(id="00001285", created_at=date_t_iso,
                               updated_at=date_t_iso)
        self.assertEqual(base_model.id, "00001285")
        self.assertEqual(base_model.created_at, date_t)
        self.assertEqual(base_model.updated_at, date_t)

    def test_instantiation_with_None_kwargs(self):
        """test init without **kargs"""
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        """test init with args and **kargs"""
        date_time = datetime.today()
        d_t_iso = date_time.isoformat()
        base_model = BaseModel("12", id="00001285", created_at=d_t_iso,
                               updated_at=d_t_iso)
        self.assertEqual(base_model.id, "00001285")
        self.assertEqual(base_model.created_at, date_time)
        self.assertEqual(base_model.updated_at, date_time)


class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    @classmethod
    def setUp(self):
        """sets up test env"""
        try:
            os.rename("memory.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        """cleans up for test env"""
        try:
            os.remove("memory.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "memory.json")
        except IOError:
            pass

    def test_one_save(self):
        """tests for the saving one time"""
        base_model = BaseModel()
        sleep(0.05)
        first_updated_at = base_model.updated_at
        base_model.save()
        self.assertLess(first_updated_at, base_model.updated_at)

    def test_two_saves(self):
        """test for saving two times"""
        base_model = BaseModel()
        sleep(0.05)
        first_updated_at = base_model.updated_at
        base_model.save()
        second_updated_at = base_model.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        base_model.save()
        self.assertLess(second_updated_at, base_model.updated_at)

    def test_save_with_arg(self):
        """test calling save with args"""
        base_model = BaseModel()
        with self.assertRaises(TypeError):
            base_model.save(None)

    def test_save_updates_file(self):
        """test for updates after calling save"""
        base_model = BaseModel()
        base_model.save()
        base_model_id = "BaseModel." + base_model.id
        with open("memory.json", "r") as f:
            self.assertIn(base_model_id, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class"""

    def test_to_dict_type(self):
        """test for the method return type"""
        base_model = BaseModel()
        self.assertTrue(dict, type(base_model.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """test for methode return values"""
        base_model = BaseModel()
        self.assertIn("id", base_model.to_dict())
        self.assertIn("created_at", base_model.to_dict())
        self.assertIn("updated_at", base_model.to_dict())
        self.assertIn("__class__", base_model.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """test for attributes returned"""
        base_model = BaseModel()
        base_model.name = "Betty"
        base_model.my_number = 98
        self.assertIn("name", base_model.to_dict())
        self.assertIn("my_number", base_model.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """test for date related attributes type"""
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertEqual(str, type(base_model_dict["created_at"]))
        self.assertEqual(str, type(base_model_dict["updated_at"]))

    def test_to_dict_output(self):
        """test method output"""
        date_time = datetime.today()
        base_model = BaseModel()
        base_model.id = "00001285"
        base_model.created_at = base_model.updated_at = date_time
        test_dict = {
            'id': '00001285',
            '__class__': 'BaseModel',
            'created_at': date_time.isoformat(),
            'updated_at': date_time.isoformat()
        }
        self.assertDictEqual(base_model.to_dict(), test_dict)

    def test_diff_dict_and__dict(self):
        """test for diffrences between .to_dict and .__dict__"""
        base_model = BaseModel()
        self.assertNotEqual(base_model.to_dict(), base_model.__dict__)

    def test_to_dict_with_arg(self):
        """test calling the methode with args"""
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)


if __name__ == "__main__":
    unittest.main()
