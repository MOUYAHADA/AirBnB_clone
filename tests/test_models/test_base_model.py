#!/usr/bin/python3
"""Module for testing the BaseModel class"""
from models.base_model import BaseModel
import unittest
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Class for testing the BaseModel class"""
    def setUp(self):
        self.baseModel = BaseModel()

    def test_id_is_string(self):
        """Check if id is a string"""
        self.assertIsInstance(self.baseModel.id, str)

    def test_id_is_unique(self):
        """Check if id is unique"""
        baseModel1 = BaseModel()
        baseModel2 = BaseModel()
        self.assertNotEqual(baseModel1, baseModel2)

    def test_created_at(self):
        """Check if creatied_at date is a datetime object"""
        self.assertIsInstance(self.baseModel.created_at, datetime)

    def test_updated_at(self):
        """Check if updated_at date is a datetime object"""
        self.assertIsInstance(self.baseModel.updated_at, datetime)

    def test_save_updates(self):
        """Check if save function changes update date"""
        old_date = self.baseModel.updated_at
        self.baseModel.save()
        self.assertNotEqual(old_date, self.baseModel.updated_at)

    def test_str_format(self):
        """Check __str__ format"""
        self.assertEqual(
            str(self.baseModel),
            "[BaseModel] ({}) {}".format(self.baseModel.id,
                                         self.baseModel.__dict__),)

    def tearDown(self):
        del self.baseModel


if __name__ == "__main__":
    unittest.main()
