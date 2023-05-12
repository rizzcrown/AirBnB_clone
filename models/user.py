#!/usr/bin/python3
from models.base_model import BaseModel

class User(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.firstname = ""
        self.lastname = ""

        