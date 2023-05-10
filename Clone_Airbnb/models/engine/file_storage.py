import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)

            from models.user import User
            from models.place import Place
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.review import Review

            class_mappings = {

                'User': User,
                'Place': Place,
                'State': State,
                'City': City,
                'Amenity': Amenity,
                'Review': Review

            }

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
            