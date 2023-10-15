#!/usr/bin/python3
"""
This is unit test for test Base model
"""

import unittest
from models.base_model import BaseModel
import datetime
import models


class Test_Base_Model(unittest.TestCase):
    """
    This is Test class
    """
    def test_base_model_id(self):
        """Check if to_dict method returned
        a dictionary that has the correct keys and values"""

        flag1 = False
        base = BaseModel()
        dic = base.to_dict()
        dic1 = base.__dict__
        for key in dic.keys():
            for key1 in dic1.keys():
                if key == '__class__':
                    flag = True
                    continue
                elif key == key1:
                    flag1 = True
        self.assertTrue(flag1 and flag)

    def test_base_to_dict_keys(self):
        """Check the key __class__ existence"""

        base = BaseModel()
        self.assertIn('__class__', base.to_dict())

    def test_base_serialise_desrialise1(self):
        """Test deserialization and reloading from JSON"""

        base = BaseModel()
        base.save()
        models.storage.save()
        key = f"BaseModel.{base.id}"
        models.storage.reload()
        obj = models.storage.all()[key]
        self.assertTrue(isinstance(obj, BaseModel))
