#!/usr/bin/python3
"""
A module that include the parent class Basemodel
"""

import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    class BaseModel that defines all common attributes/methods
    for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        __init__ method to initise the an object during its creation
        Args:
        *args: tuple of arguments
        **kwags: key value variables
        """

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        fformat = '%Y-%m-%dT%H:%M:%S.%f'
                        """convert the string values to datetime objects"""
                        value = datetime.strptime(value, fformat)
                    setattr(self, key, value)
                    """ ^^^this is like self.key = value
                    and this line solves the purpose of
                    each value of this dictionary is the value of
                    this attribute name
                    """
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        __str__: should print: [<class name>] (<self.id>) <self.__dict__>
        """

        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        save(self): updates the public instance attribute
        updated_at with the current datetime
        """

        self.updated_at = datetime.now()
        models.storage.save()

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
