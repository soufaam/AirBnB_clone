#!/usr/bin/python3
"""This is unist test for test Base model"""

import unittest
from models.base_model import BaseModel
import datetime


class Test_Base_Model(unittest.TestCase):
    """This is Test class"""

    def test_base_model_datetime_created_at(self):
        """test the type of created_at attr"""

        base_model = BaseModel()
        self.assertTrue(isinstance(base_model.created_at, datetime.datetime))

    def test_base_model_datetime_updated_at(self):
        """test the type of update_at attr"""

        base_model = BaseModel()
        self.assertTrue(isinstance(base_model.updated_at, datetime.datetime))

    def test_base_model_id(self):
        """test the type of id"""

        base_model = BaseModel()
        self.assertTrue(isinstance(base_model.id, str))

    def test_base_model_new_attr1(self):
        """test new attr"""

        base_model = BaseModel()
        base_model.name = "AIRBnb console"
        self.assertEqual(base_model.name, "AIRBnb console")

    def test_base_model_modify_datetime(self):
        """modify create_at and update_at"""

        base_model = BaseModel(name="ALX", )
        now = datetime.datetime.now()
        base_model.created_at = now
        base_model.updated_at = now
        self.assertEqual(base_model.created_at, base_model.updated_at)

    def test_base_model_new_attr2(self):
        """create object using the class with kwargs"""

        base_model = BaseModel(name="ALX")
        self.assertEqual(base_model.name, "ALX")

    def test_base_model_dict(self):
        """test to_dic method"""

        base_model = BaseModel(name="ALX")
        dic = base_model.to_dict()
        self.assertTrue(isinstance(dic, dict))

    def test_base_model_dict2(self):
        """test key value of the return value of to_dic"""

        base_model = BaseModel(name="ALX")
        dic = base_model.to_dict()
        self.assertTrue(dic['__class__'] == BaseModel.__name__)
