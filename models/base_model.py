#!/usr/bin/python3
"""Base Model Class"""

import uuid
from datetime import datetime


class BaseModel():
    """Base model class definition"""

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        updated_at = datetime.now()

    def __str__(self):
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()

        return inst_dict
