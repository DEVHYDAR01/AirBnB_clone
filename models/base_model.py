#!/usr/bin/python3
"""Type module of BaseModel"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Type class of BaseModel"""

    def __init__(self, *args, **kwargs):
        """Type method initialized"""
        timeformat = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(val, timeformat))
                elif key != '__class__':
                    setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def save(self):
        """Type method for saving"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Type method for the to_dict"""
        rt_dict = self.__dict__.copy()
        rt_dict["created_at"] = self.created_at.isoformat()
        rt_dict["updated_at"] = self.updated_at.isoformat()
        rt_dict["__class__"] = self.__class__.__name__
        return rt_dict

    def __str__(self):
        """Type method for __str__"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
