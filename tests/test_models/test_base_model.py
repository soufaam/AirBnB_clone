#!/usr/bin/python3
"""
This is unit test for test Base model
"""

import unittest
from models.base_model import BaseModel
import datetime
import os
import json
from models.engine.file_storage import FileStorage


class Test_Base_Model(unittest.TestCase):
    """
    This is unittest class
    """
    def test_base_model_id(self):
        """
        Check if the id is string
        """

        base_model = BaseModel()
        self.assertTrue(isinstance(base_model.id, str))

    def test_base_mode_len_of_id(self):
        """
        Ensure id is a uuid4 string (len == 36)
        """

        base_model1 = BaseModel()
        self.assertEqual(len(base_model1.id), 36)

    def test_base_model_tow_diff_ids(self):
        """
        Inequality of two different objects ids
        """

        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertTrue(base_model1.id != base_model2.id)

    def test_base_model_tow_diff_ids2(self):
        """
        Inequality of two different objects ids
        """

        base_model1 = BaseModel(name="hlim")
        base_model2 = BaseModel()
        self.assertTrue(base_model1.id != base_model2.id)

    def test_base_model_tow_diff_ids3(self):
        """
        Inequality of two different objects ids
        """

        base_model1 = BaseModel(name="hlim")
        base_model2 = BaseModel(name="hlim")
        self.assertTrue(base_model1.id != base_model2.id)

    def test_base_model_tow_diff_instances(self):
        """
        Inequality of two instances of BaseModel
        """

        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertTrue(base_model1 != base_model2)

    def test_base_model_if_instance(self):
        """
        Inequality of two instances of BaseModel
        """

        base_model1 = BaseModel()
        self.assertTrue(isinstance(base_model1, BaseModel))

    def test_base_model_datetime_created_at(self):
        """
        test the type of created_at attr
        """

        base_model = BaseModel()
        self.assertTrue(isinstance(base_model.created_at, datetime.datetime))

    def test_base_model_datetime_now_(self):
        """
        Check if the created time is always less than the current time.
        """

        base_model = BaseModel()
        self.assertLess(base_model.created_at.timestamp(),
                        datetime.datetime.now().timestamp())

    def test_base_model_datetime_updated_at(self):
        """
        test the type of update_at attr
        """

        base_model = BaseModel()
        self.assertTrue(isinstance(base_model.updated_at, datetime.datetime))

    def test_base_model_new_attr1(self):
        """
        test new attr
        """

        base_model = BaseModel()
        base_model.name = "AIRBnb console"
        self.assertEqual(base_model.name, "AIRBnb console")

    def test_base_model_modify_datetime(self):
        """
        modify create_at and update_at
        """

        base_model = BaseModel(name="ALX", )
        now = datetime.datetime.now()
        base_model.created_at = now
        base_model.updated_at = now
        self.assertEqual(base_model.created_at, base_model.updated_at)

    def test_base_model_new_attr2(self):
        """
        create object using the class with kwargs
        """

        base_model = BaseModel(name="ALX")
        self.assertEqual(base_model.name, "ALX")

    def test_base_model_dict(self):
        """
        test to_dic method
        """

        base_model = BaseModel(name="ALX")
        dic = base_model.to_dict()
        self.assertTrue(isinstance(dic, dict))

    def test_base_model_dict2(self):
        """
        test key value of the return value of to_dic
        """

        base_model = BaseModel(name="ALX")
        dic = base_model.to_dict()
        self.assertTrue(dic['__class__'] == BaseModel.__name__)

    def test_base_model_str_(self):
        """
        test key value of the return value of to_dic
        """

        base_model = BaseModel(name="ALX")
        result1 = base_model.__str__()
        result2 = f"[{BaseModel.__name__}] \
({base_model.id}) {base_model.__dict__}"
        self.assertEqual(result1, result2)

    def test_base_model_save_method1(self):
        """
        Check the inequality of created_at and updated_at
        attributes after using the save(self) method
        """

        base_model = BaseModel(name="ALX")
        base_model.save()
        self.assertLess(base_model.created_at.timestamp(),
                        base_model.updated_at.timestamp())

    def test_base_model_save_method2(self):
        """
        Check the inequality of created_at and updated_at
        attributes after using the save(self) method
        """

        base_model = BaseModel(name="ALX")
        base_model.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_base_model_iso_format(self):
        """
        Check the inequality of created_at and updated_at
        attributes after using the save(self) method
        """

        base_model = BaseModel(name="ALX")
        base_model.save()
        self.assertLess(base_model.created_at.timestamp(),
                        base_model.updated_at.timestamp())

    def test_base_model_from_iso(self):
        """
        Check if the created_at and updated_at are in the
        “%Y-%m-%dT%H:%M:%S.%f” ISO format in the dictionary
        returned from to_dict method
        """

        base_model = BaseModel(name="ALX")
        dic = base_model.to_dict()
        self.assertIsNotNone(
            datetime.datetime.fromisoformat(dic['created_at']))

    def test__file_path(self):
        """_summary_
        Check if the model key in the
        __objects attribute after using
        the new method
        """

        test_storage = FileStorage()
        with self.assertRaises(Exception) as context:
            file = test_storage.__file_path
        self.assertTrue("object has no attribute " in str(context.exception))

    def test__object(self):
        """_summary_
        Check if the model key in the
        __objects attribute after using
        the new method
        """

        test_storage = FileStorage()
        with self.assertRaises(Exception) as context:
            file = test_storage.__objects
        self.assertTrue("object has no attribute " in str(context.exception))

    def test__save(self):
        """_summary_
        Check if the model key in the
        __objects attribute after using
        the new method
        """

        base = BaseModel()
        base.save()
        key = f"{BaseModel.__name__}.{base.id}"
        with open("file.json") as file:
            data = json.load(file)
            self.assertTrue(key in data.keys())
