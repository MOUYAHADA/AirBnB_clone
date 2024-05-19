#!/usr/bin/python3

""" Test Review Unittest module

"""

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview_Object_Instance(unittest.TestCase):

    """ Test review class object instance

    """

    def setUp(self):
        print("Testing Review Object Instance")

    def test_review_is_subclass_basemodel(self):
        r1 = Review()
        self.assertIsInstance(r1, BaseModel)

    def test_review_unique_ids(self):
        r1 = Review()
        r2 = Review()
        self.assertNotEqual(r1.id, r2.id)

    def test_review_placeid_default_value(self):
        r1 = Review()
        self.assertEqual(r1.place_id, "")

    def test_review_userid_default_value(self):
        r1 = Review()
        self.assertEqual(r1.user_id, "")

    def test_review_text_default_value(self):
        r1 = Review()
        self.assertEqual(r1.text, "")

    def test_review_id_type(self):
        r1 = Review()
        self.assertEqual(type(r1.id), str)

    def test_review_place_id_type(self):
        r1 = Review()
        self.assertEqual(type(r1.place_id), str)

    def test_review_user_id_type(self):
        r1 = Review()
        self.assertEqual(type(r1.user_id), str)

    def test_review_object_creation_time(self):
        r1 = Review()
        r2 = Review()
        self.assertNotEqual(r1.created_at, r2.created_at)


class TestReview_Has_Attributes_BaseModel(unittest.TestCase):

    """ Check if Review has attributes of BaseModel

    """

    def test_review_has_id_attr(self):
        r1 = Review()
        self.assertTrue(r1.id)

    def test_review_has_created_at_attr(self):
        r1 = Review()
        self.assertTrue(r1.created_at)

    def test_review_has_updated_at_attr(self):
        r1 = Review()
        self.assertTrue(r1.updated_at)

    def test_review_has___str__(self):
        r1 = Review()
        self.assertTrue(r1.__str__)

    def test_review_has_save_attr(self):
        r2 = Review()
        self.assertTrue(r2.save)

    def test_review_has_to_dict_attr(self):
        r1 = Review()
        self.assertTrue(r1.to_dict)

    def test_review_can_take_kwargs(self):
        r2 = Review(name="Al-Areef")
        self.assertEqual(r2.name, "Al-Areef")

    def test_review_object_str_representation(self):
        r1 = Review()
        self.assertIn("[Review]", r1.__str__())


if __name__ == "__main__":
    unittest.main()
