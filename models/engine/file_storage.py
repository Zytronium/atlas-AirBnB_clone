#!/usr/bin/env python3
"""the FileStorage class."""
import json



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
      dict = FileStorage.__objects
      with open(FileStorage.__file_path, 'w') as f:
        json.dump(dict, f)
