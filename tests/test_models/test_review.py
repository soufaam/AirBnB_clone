#!/usr/bin/python3
"""
This is unit test for test Base model
"""

import unittest
from models.user import User
from models.review import Review
from models.base_model import BaseModel
import datetime
import models


class Test_Base_Model(unittest.TestCase):
    """
    This is unittest class
    """
    def test_review_id(self):
        """
        Check if the id is string
        """

        review = Review()
        self.assertTrue(isinstance(review.id, str))

    def test_review_len_of_id(self):
        """
        Ensure id is a uuid4 string (len == 36)
        """

        review1 = Review()
        self.assertEqual(len(review1.id), 36)

    def review_ids(self):
        """
        Inequality of two different objects ids
        """

        review1 = Review()
        review2 = Review()
        self.assertTrue(review1.id != review2.id)

    def test_review_basemodels_instance(self):
        """
        Inequality of two different objects ids
        """

        review1 = Review()
        self.assertTrue(isinstance(review1, BaseModel))

    def test_review_tow_diff_ids2(self):
        """
        Inequality of two different objects ids
        """

        review = Review()
        review.first_name = "ALX"
        models.storage.new(review)
        review.save()
        key = f"{Review.__name__}.{review.id}"
        models.storage.reload()
        dic = models.storage.all()
        self.assertTrue(key in dic.keys())

    def test_review_subclass(self):
        """
        Inequality of two different objects ids
        """

        self.assertTrue(issubclass(Review, BaseModel))

    def test_review_text(self):
        """
        Inequality of two different objects ids
        """

        self.assertEqual("", Review.text)

    def test_review_user_id(self):
        """
        Inequality of two different objects ids
        """

        self.assertEqual("", Review.user_id)

    def test_place_id(self):
        """
        Inequality of two different objects ids
        """

        self.assertEqual("", Review.place_id)
