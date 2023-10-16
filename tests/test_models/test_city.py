#!/usr/bin/python3
"""
This is unit test for test Base model
"""

import unittest
from models.city import City
from models.base_model import BaseModel
import datetime
import models


class Test_Base_Model(unittest.TestCase):
    """
    This is unittest class
    """
    def test_city_id(self):
        """
        Check if the id is string
        """

        city = City()
        self.assertTrue(isinstance(city.id, str))

    def test_city_len_of_id(self):
        """
        Ensure id is a uuid4 string (len == 36)
        """

        city1 = City()
        self.assertEqual(len(city1.id), 36)

    def city_ids(self):
        """
        Inequality of two different objects ids
        """

        city1 = City()
        city2 = City()
        self.assertTrue(city1.id != city2.id)

    def test_city_basemodels_instance(self):
        """
        Inequality of two different objects ids
        """

        city1 = City()
        self.assertTrue(isinstance(city1, BaseModel))

    def test_city_tow_diff_ids2(self):
        """
        Inequality of two different objects ids
        """

        city = City()
        city.first_name = "ALX"
        models.storage.new(city)
        city.save()
        key = f"{City.__name__}.{city.id}"
        models.storage.reload()
        dic = models.storage.all()
        self.assertTrue(key in dic.keys())

    def test_city_subclass(self):
        """
        Inequality of two different objects ids
        """

        self.assertTrue(issubclass(City, BaseModel))

    def test_city(self):
        """
        Inequality of two different objects ids
        """

        self.assertEqual('', City.name)

    def test_state_id(self):
        """
        Inequality of two different objects ids
        """

        self.assertEqual('', City.state_id)
