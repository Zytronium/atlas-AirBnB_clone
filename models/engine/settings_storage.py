#!/usr/bin/env python3
"""the SettingsStorage class."""
import json
import os


class SettingsStorage:
    """the SettingsStorage class"""

    __file_path = "settings.json"
    __objects = {}

    def all(self):
        """return the dictionary of all settings"""
        return SettingsStorage.__objects

    def new(self, name, default_value):
        """add a new setting to the dictionary"""
        SettingsStorage.__objects[name] = default_value

    def save(self):
        """save the settings to the file"""
        try:
            with open(SettingsStorage.__file_path, 'w') as f:
                json.dump(SettingsStorage.__objects, f)
        except Exception as e:
            print(e)

    def reload(self):
        """deserializes the file to __object"""
        if os.path.isfile(SettingsStorage.__file_path):
            try:
                with open(SettingsStorage.__file_path, 'r') as f:
                    SettingsStorage.__objects = json.load(f)
            except Exception as e:
                print(e)

        if 'show_warnings' not in SettingsStorage.__objects:
            SettingsStorage.__objects['show_warnings'] = True
        if 'sound' not in SettingsStorage.__objects:
            SettingsStorage.__objects['sound'] = True

        self.save()
