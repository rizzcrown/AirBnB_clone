#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = "file.json"
    __objects = {}#stores the classname.id :object/instance name as the key value pairs

    def all(self, cls=None):
        """returns a dictionary of models currently in storage """
        if cls:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls.__name__ == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return FileStorage.__objects
    
    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes the __objects to json file(__file_path)"""
        obj_dict = {}
        for key, obj in self.__objects.items():
            # converts instances/objects in __objects to dictionaries 
            # the key represents the object id 
            obj_dict[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
    

    """
    def reload(self):
        # deserializes the json file to __objects 
        
        #Loads storage dictionary from file
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        class_mappings = {

                'BaseModel': BaseModel,
                'User': User,
                'Place': Place,
                'State': State,
                'City': City,
                'Amenity': Amenity,
                'Review': Review

            }

        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)

            for key, value in obj_dict.items():
                class_name, obj_id = key.split('.')
                if class_name in class_mappings:
                    cls = class_mappings[class_name]
                    obj = cls(**value)
                    self.__objects[key] = obj
            else:
                module = __import__('models.' + class_name, fromlist=[class_name])
                cls = getattr(module, class_name)
                obj = cls(**value)
                self.__objects[key] = obj

        except FileNotFoundError:
            pass
            
        """
            