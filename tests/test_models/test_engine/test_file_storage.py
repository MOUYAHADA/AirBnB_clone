#!/usr/bin/python3
"""Unittest for file_storage.py"""
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test_FileStorage_instantiation_arg(self):
        """Test instantiation of FileStorage class with arguments"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_instantiation_no_args(self):
        """Test instantiation of FileStorage class without arguments"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_file_path_is_private_str(self):
        """Test if __file_path is a private string attribute."""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        """Test if __objects is a private dictionary attribute."""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))


class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    def setUp(self):
        """Set up test environment."""
        self.storage = FileStorage()
        self.storage._FileStorage__objects = {}
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """Tear down test environment."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        self.storage._FileStorage__objects = {}

    def test_all(self):
        """Test the all method."""
        # Test scenarios for the all method...

    def test_all_with_arg(self):
        """Test the all method with arguments."""
        with self.assertRaises(TypeError):
            self.storage.all(None)

    def test_new(self):
        """Test the new method."""
        # Test scenarios for the new method...

    def test_new_with_args(self):
        """Test the new method with arguments."""
        with self.assertRaises(TypeError):
            self.storage.new(BaseModel(), 1)

    def test_save(self):
        """Test the save method."""
        # Test scenarios for the save method...

    def test_save_with_arg(self):
        """Test the save method with arguments."""
        with self.assertRaises(TypeError):
            self.storage.save(None)

    def test_reload(self):
        """Test the reload method."""
        # Test scenarios for the reload method...

    def test_reload_with_arg(self):
        """Test the reload method with arguments."""
        with self.assertRaises(TypeError):
            self.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
