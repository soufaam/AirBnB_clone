#!/usr/bin/python3
"""
This is unit test for test File_storge
"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import datetime
import models


class Test_FileStorage(unittest.TestCase):
    """
    This is Test class for the
    Test of FileStorage class
    """

    def test_test_file_storage_new(self):
        """_summary_
        Check the equality of the created model
        and the model in the __objects attribute
        """

        base1 = BaseModel()
        base2 = BaseModel()
        """models.storage.save()"""
        test_stoge = FileStorage()
        test_stoge.new(base1)
        test_stoge.new(base2)
        test_stoge.save()
        test_stoge.reload()
        key1 = f"BaseModel.{base1.id}"
        obj1 = test_stoge.all()[key1]
        self.assertTrue(isinstance(obj1, BaseModel))
