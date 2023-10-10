#!/usr/bin/python3
import models
from datetime import datetime
from uuid import uuid4
"""
class BaseModel that defines all common attributes/methods
for other classes.
"""


class BaseModel:
    """base"""

    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """

        c_dict = self.__dict__.copy()
        c_dict['__class__'] = self.__class__.__name__
        c_dict['created_at'] = self.created_at.isoformat()
        c_dict['updated_at'] = self.updated_at.isoformat()
        return c_dict
