#!/usr/bin/python3
"""Defines 'FileStorage' class"""

import os
import json
from models.base_model import BaseModel


class FileStorage():
    """Class methods"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        cls_name = obj.__class__.__name__
        obj_id = obj.id
        key = f"{cls_name}.{obj_id}"
        FileStorage.__objects[key] = obj

    def save(self):
        obj_dict = {}

        for obj in FileStorage.__objects.keys():
            obj_dict[obj] = FileStorage.__objects[obj].to_dict()

        with open(FileStorage.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="UTF-8") as f:
                try:
                    obj_dict = json.load(file)
                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        cls = classes[class_name]
                        new_obj = cls(**value)
                        self.new(new_obj)
                except Exception:
                    pass
