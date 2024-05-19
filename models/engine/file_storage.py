#!/usr/bin/python3
"""
The FileStorage class
"""
import json


class FileStorage:
    """A class dedicated to saving instances as JSON files"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets new object"""
        self.__class__.__objects[
            f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes dictionary of objects and saves it to file"""
        new_dict = {}
        for key, value in self.__class__.__objects.items():
            new_dict[key] = value.to_dict()
        objects_json = json.dumps(new_dict)
        with open(self.__class__.__file_path, 'w', encoding="utf-8") as f:
            f.write(objects_json)

    def reload(self):
        """Deserializes JSON file to objects"""
        try:
            with open(self.__class__.__file_path, 'r', encoding="utf-8") as f:
                dict_contents = json.load(f)
                for key, value in dict_contents.items():
                    self.__class__.__objects[key] \
                        = eval(value['__class__'])(**value)

        except FileNotFoundError:
            return
