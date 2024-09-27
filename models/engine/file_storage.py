#!/usr/bin/env python3
"""the FileStorage class."""
import json
import os
from models.base_model import BaseModel



class FileStorage:
    """the FileStorage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dictionary of all objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sdd a new object to the dictionary"""
        key = obj.id
        obj_name = obj.__class__.__name__
        FileStorage.__objects[f"{obj_name}.{key}"] = obj

    def save(self):
      """save the dict to the file"""
      dict = FileStorage.__objects.copy()
      with open(FileStorage.__file_path, 'w') as f:


    def reload(self):
        """deserializes the file to __object"""
        json_deco = {}
        if (os.path.isfile(FileStorage.__file_path)):
            with open(FileStorage.__file_path, 'r') as f:
                json_deco = json.load(f).copy()
        for key in json_deco.keys():
            obj_name = key.split(".")[0]
            obj_id = key.split(".")[1]
            obj_dict = json_deco[key]
            obj_dict["__class__"] = obj_name
            obj_dict["id"] = obj_id
            obj = BaseModel(**obj_dict)
                
            
                