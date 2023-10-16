#!/usr/bin/python3
"""
This is unit test for test Base model
"""

import unittest
from models.place import Place
from models.base_model import BaseModel
import datetime
import models


class Test_Base_Model(unittest.TestCase):
    """
    This is unittest class
    """
    def test_place_id(self):
        """
        Check if the id is string
        """

        place = Place()
        self.assertTrue(isinstance(place.id, str))

    def test_place_len_of_id(self):
        """
        Ensure id is a uuid4 string (len == 36)
        """

        place1 = Place()
        self.assertEqual(len(place1.id), 36)

    def place_ids(self):
        """
        Inequality of two different objects ids
        """

        place1 = Place()
        place2 = Place()
        self.assertTrue(place1.id != place2.id)

    def test_place_basemodels_instance(self):
        """
        Inequality of two different objects ids
        """

        place1 = Place()
        self.assertTrue(isinstance(place1, BaseModel))

    def test_place_tow_diff_ids2(self):
        """
        Inequality of two different objects ids
        """

        place = Place()
        place.first_name = "ALX"
        models.storage.new(place)
        place.save()
        key = f"{Place.__name__}.{place.id}"
        models.storage.reload()
        dic = models.storage.all()
        self.assertTrue(key in dic.keys())

    def test_place_subclass(self):
        """
        Inequality of two different objects ids
        """

        self.assertTrue(issubclass(Place, BaseModel))

    def test_place_id(self):
        """
        Inequality of two different objects ids
        """

        self.assertEqual("", Place.city_id)

    def test_place_id(self):
        """
        Inequality of two different objects ids
        """

        self.assertEqual("", Place.city_id)

    def test_user_id(self):
        """
        Inequality of two different objects ids
        """

        self.assertEqual("", Place.user_id)

    def test_name(self):
        """
        Inequality of two different objects ids
        """

        self.assertEqual("", Place.name)

    def test_description(self):
        """
        Inequality of two different objects ids
        """

        self.assertEqual("", Place.description)

    def test_description(self):
        """
        Inequality of two different objects ids
        """

        self.assertEqual("", Place.description)

    def test_number_rooms(self):
        """
        Inequality of two different objects ids
        """

        self.assertEqual(0, Place.number_rooms)

    def test_number_bathrooms(self):
        """
        Inequality of two different objects ids
        """

        self.assertEqual(0, Place.number_bathrooms)

    def test_max_guest(self):
        """
        Inequality of two different objects ids
        """

        self.assertEqual(0, Place.max_guest)

    def test_price_by_night(self):
        """
        Inequality of two different objects ids
        """

        self.assertEqual(0, Place.price_by_night)

    def test_latitude(self):
        """
        Inequality of two different objects ids
        """

        self.assertEqual(0.0, Place.latitude)

    def test_longitude(self):
        """
        Inequality of two different objects ids
        """

        self.assertEqual(0.0, Place.longitude)

    def test_amenity_ids(self):
        """
        Inequality of two different objects ids
        """

        self.assertEqual([], Place.amenity_ids)
