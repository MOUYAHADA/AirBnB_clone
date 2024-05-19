#!/usr/bin/python3
"""
Module for the FileStorage class which takes care of storing objects as json
"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """A class dedicated to saving instances as JSON files"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets new object"""
        self.__objects[
            f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes dictionary of objects and saves it to file"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes JSON file to objects"""
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r', encoding="utf-8") as f:
                    dict_contents = json.load(f)
                    for key, value in dict_contents.items():
                        self.__objects[key] \
                            = eval(value['__class__'])(**value)

            except FileNotFoundError:
                pass
