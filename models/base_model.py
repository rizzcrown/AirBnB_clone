#!/usr/bin/python3
from models import storage 
import uuid
from datetime import datetime

class BaseModel:
    """ Defines all common attributes/methods for other classes of Hbnb"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                """If the values passed to datetime.strptime() in init is not 
                    string it is assigned dirrectly without conversion otherwise,
                    it is first converted to a datetime object
                """
                if key == 'created_at' or key == 'updated_at':
                    if isinstance(value, datetime):
                        setattr(self, key, value)
                    else:
                        setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        storage.new(self) # add a call to the new() method on storage for new instances

    def save(self):
        """ Update the current instance attribute 'update_at' with 
            current datetime
        """
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save() # call the save method on storage to serialize __objects

    
    def to_dict(self):
        """ Convert instance into dict format
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
    
    def delete(self):
        """delete the current instance"""
        from models import storage
        storage.delete(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    