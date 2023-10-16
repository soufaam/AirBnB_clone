#!/usr/bin/python3
"""
This is unit test for test Base model
"""

import unittest
from models.user import User
from models.base_model import BaseModel
import datetime
import models


class Test_Base_Model(unittest.TestCase):
    """
    This is unittest class
    """
    def test_user_id(self):
        """
        Check if the id is string
        """

        user = User()
        self.assertTrue(isinstance(user.id, str))

    def test_user_len_of_id(self):
        """
        Ensure id is a uuid4 string (len == 36)
        """

        user1 = User()
        self.assertEqual(len(user1.id), 36)

    def user_ids(self):
        """
        Inequality of two different objects ids
        """

        user1 = User()
        user2 = User()
        self.assertTrue(user1.id != user2.id)

    def test_user_basemodels_instance(self):
        """
        Inequality of two different objects ids
        """

        user1 = User()
        self.assertTrue(isinstance(user1, BaseModel))

    def test_user_tow_diff_ids2(self):
        """
        Inequality of two different objects ids
        """

        user = User()
        user.first_name = "ALX"
        models.storage.new(user)
        user.save()
        key = f"{User.__name__}.{user.id}"
        models.storage.reload()
        dic = models.storage.all()
        self.assertTrue(key in dic.keys())

    def test_user_subclass(self):
        """
        Inequality of two different objects ids
        """

        self.assertTrue(issubclass(User, BaseModel))

    def test_user_first_name(self):
        """
        Inequality of two different objects ids
        """

        User.first_name = ""
        self.assertEqual("", User.first_name)

    def test_user_last_name(self):
        """
        Inequality of two different objects ids
        """
        User.last_name = ""
        self.assertEqual("", User.last_name)

    def test_user_passowrd(self):
        """
        Inequality of two different objects ids
        """

        User.password = ""
        self.assertEqual("", User.password)

    def test_user_email(self):
        """
        Inequality of two different objects ids
        """

        self.assertEqual("", User.email)
