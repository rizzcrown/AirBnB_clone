from models.engine.file_storage import storage 
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4)
            self.create_at = datetime.now()
            self.update_at = self.create_at
            storage.new(self) # add a cal to the new() method on storage for new instances

    def save(self):
        self.update_at = datetime.now()
        storage.save() # call the save method on storage to serialize __objects

    
    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['udpated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    