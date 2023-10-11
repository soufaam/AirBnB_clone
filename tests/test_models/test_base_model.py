#!/usr/bin/python3
"""This is unist test for test Base model"""

import unittest
import models.base_model

class Test_Base_Model(unittest.TestCase):
    def test_base_model(self):
        self.assertEqual()


my_model = models.base_model.BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
