#!/usr/bin/python3
"""
This is unit test for test Base model
"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import datetime
import models


class Test_Base_Model(unittest.TestCase):
    """
    This is unittest class
    """
    def test_amenity_id(self):
        """
        Check if the id is string
        """

        amenity = Amenity()
        self.assertTrue(isinstance(amenity.id, str))

    def test_amenity_len_of_id(self):
        """
        Ensure id is a uuid4 string (len == 36)
        """

        amenity1 = Amenity()
        self.assertEqual(len(amenity1.id), 36)

    def amenity_ids(self):
        """
        Inequality of two different objects ids
        """

        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertTrue(amenity1.id != amenity2.id)

    def test_amenity_basemodels_instance(self):
        """
        Inequality of two different objects ids
        """

        amenity1 = Amenity()
        self.assertTrue(isinstance(amenity1, BaseModel))

    def test_amenity_tow_diff_ids2(self):
        """
        Inequality of two different objects ids
        """

        amenity = Amenity()
        amenity.first_name = "ALX"
        models.storage.new(amenity)
        amenity.save()
        key = f"{Amenity.__name__}.{amenity.id}"
        models.storage.reload()
        dic = models.storage.all()
        self.assertTrue(key in dic.keys())

    def test_amenity_subclass(self):
        """
        Inequality of two different objects ids
        """

        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_amenity_name(self):
        """
        Inequality of two different objects ids
        """

        self.assertEqual('', Amenity.name)
