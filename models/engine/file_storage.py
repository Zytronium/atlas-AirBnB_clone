#!/usr/bin/env python3
"""the FileStorage class."""
import json
import os
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.user import User
from models.review import Review


class FileStorage:
    """the FileStorage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dictionary of all objects"""
        return FileStorage.__objects

    def new(self, obj):
        """add a new object to the dictionary"""
        key = obj.id
        obj_name = obj.__class__.__name__
        FileStorage.__objects[f"{obj_name}.{key}"] = obj

    def save(self):
        """save the dict to the file"""
        dict = {}
        for nattr, vattr in FileStorage.__objects.items():
            if vattr:
                dict[nattr] = vattr.to_dict()
                with open(FileStorage.__file_path, 'w') as f:
                    json.dump(dict, f)

    def reload(self):
        """deserializes the file to __object"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        try:
            if os.path.isfile(FileStorage.__file_path):
                with open(FileStorage.__file_path, 'r') as f:
                    content = json.load(f)
                    for k, v in content.items():
                        class_name = v.pop('__class__', None)
                        if class_name:
                            obj = eval(f"{class_name}(**v)")
                            FileStorage.__objects[k] = obj
        except Exception as e:
            print(e)

