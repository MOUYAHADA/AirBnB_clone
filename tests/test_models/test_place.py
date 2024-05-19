#!/usr/bin/python3

"""Unittests for Place class"""

import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlaceInstance(unittest.TestCase):

    """Check Place instance"""

    def setUp(self):
        print("Testing Place instance...")

    def test_subclass(self):
        """Check Place subclass of BaseModel"""
        p = Place()
        self.assertIsInstance(p, BaseModel)

    def test_id_diff(self):
        """Check Place ids are different"""
        p1 = Place()
        p2 = Place()
        self.assertNotEqual(p1.id, p2.id)

    def test_created_updated_diff(self):
        """Check created and updated are different"""
        p = Place()
        self.assertNotEqual(p.created_at, p.updated_at)

    def test_attrs_init_empty(self):
        """Check attrs init empty/zero"""
        p = Place()
        self.assertEqual(p.city_id, "")
        self.assertEqual(p.user_id, "")
        self.assertEqual(p.name, "")
        self.assertEqual(p.number_rooms, 0)


class TestPlaceAttrs(unittest.TestCase):

    """Check Place attributes inheritance"""

    def setUp(self):
        print("Testing Place attributes...")

    def test_place_has_id(self):
        """Check Place has id attribute"""
        self.assertTrue(Place().id)

    def test_place_has_created_at(self):
        """Check Place has created_at attribute"""
        self.assertTrue(Place().created_at)

    def test_place_has_updated_at(self):
        """Check Place has updated_at attribute"""
        self.assertTrue(Place().updated_at)

    def test_place_has_str(self):
        """Check Place has __str__ attribute"""
        self.assertTrue(Place().__str__)


if __name__ == "__main__":
    unittest.main()
