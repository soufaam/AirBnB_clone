#!/usr/bin/python3
"""
This is unit test for test Base model
"""

import unittest
from models.state import State
from models.base_model import BaseModel
import datetime
import models


class Test_Base_Model(unittest.TestCase):
    """
    This is unittest class
    """
    def test_state_id(self):
        """
        Check if the id is string
        """

        state = State()
        self.assertTrue(isinstance(state.id, str))

    def test_state_len_of_id(self):
        """
        Ensure id is a uuid4 string (len == 36)
        """

        state1 = State()
        self.assertEqual(len(state1.id), 36)

    def state_ids(self):
        """
        Inequality of two different objects ids
        """

        state1 = State()
        state2 = State()
        self.assertTrue(state1.id != state2.id)

    def test_state_basemodels_instance(self):
        """
        Inequality of two different objects ids
        """

        state1 = State()
        self.assertTrue(isinstance(state1, BaseModel))

    def test_state_tow_diff_ids2(self):
        """
        Inequality of two different objects ids
        """

        state = State()
        state.first_name = "ALX"
        models.storage.new(state)
        state.save()
        key = f"{State.__name__}.{state.id}"
        models.storage.reload()
        dic = models.storage.all()
        self.assertTrue(key in dic.keys())

    def test_state_subclass(self):
        """
        Inequality of two different objects ids
        """

        self.assertTrue(issubclass(State, BaseModel))
