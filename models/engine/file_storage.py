#!/usr/bin/python3
"""File storage class"""
import json
from os import path
from models.base_model import BaseModel


class FileStorage:
    """File storage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns the dictionary __objects"""
        if cls is None:
            return FileStorage.__objects
        return {
            k: v for k,
            v in FileStorage.__objects.items() if isinstance(v, cls)}

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serial_dict = {
            k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(
                FileStorage.__file_path,
                mode="w", encoding="utf-8") as f:
            json.dump(serial_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        try:
            with open(
                    FileStorage.__file_path,
                    mode="r", encoding="utf-8") as f:
                deserial_dict = json.load(f)
                for k, v in deserial_dict.items():
                    print(f"Key: {k}, Value: {v}")
                    class_name = k.split(".")[0]
                    obj = eval(class_name + "(**v)")
                    FileStorage.__objects[k] = obj
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside"""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]
                self.save()

    def close(self):
        """Deserializes the JSON file to objects"""
        self.reload()


# if __name__ == "__main__":
#     fs = FileStorage()

#     # All States
#     all_states = fs.all(State)
#     print("All States: {}".format(len(all_states.keys())))
#     for state_key in all_states.keys():
#         print(all_states[state_key])

#     # Create a new State
#     new_state = State()
#     new_state.name = "California"
#     fs.new(new_state)
#     fs.save()
#     print("New State: {}".format(new_state))

#     # All States
#     all_states = fs.all(State)
#     print("All States: {}".format(len(all_states.keys())))
#     for state_key in all_states.keys():
#         print(all_states[state_key])

#     # Create another State
#     another_state = State()
#     another_state.name = "Nevada"
#     fs.new(another_state)
#     fs.save()
#     print("Another State: {}".format(another_state))

#     # All States
#     all_states = fs.all(State)
#     print("All States: {}".format(len(all_states.keys())))
#     for state_key in all_states.keys():
#         print(all_states[state_key])

#     # Delete the new State
#     fs.delete(new_state)

#     # All States
#     all_states = fs.all(State)
#     print("All States: {}".format(len(all_states.keys())))
#     for state_key in all_states.keys():
#         print(all_states[state_key])
