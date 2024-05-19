#!/usr/bin/python3
"""Unittest for User class"""

import unittest
from models.user import User
from datetime import datetime
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Check cases for User class"""

    def setUp(self):
        """Set up for all tests"""
        self.user = User()
        self.user.email = "San Francisco"
        self.user.password = "CA"
        self.user.first_name = "San Francisco"
        self.user.last_name = "San Francisco"

    def tearDown(self):
        """Tear down for all tests"""
        del self.user

    def test_docstring(self):
        """Check docstring"""
        self.assertIsNotNone(User.__doc__)

    def test_attributes(self):
        """Check attributes"""
        self.assertTrue("id" in self.user.__dict__)
        self.assertTrue("created_at" in self.user.__dict__)
        self.assertTrue("updated_at" in self.user.__dict__)
        self.assertTrue("email" in self.user.__dict__)
        self.assertTrue("password" in self.user.__dict__)
        self.assertTrue("first_name" in self.user.__dict__)
        self.assertTrue("last_name" in self.user.__dict__)

    def test_subclass(self):
        """Check if User is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_type(self):
        """Check type of User"""
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.last_name), str)


if __name__ == "__main__":
    unittest.main()
