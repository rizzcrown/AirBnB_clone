#!/usr/bin/bash
from models.base_model import BaseModel

class State(BaseModel):
    name =""

    def __init__(self, *args, **kwarg):
        super().__init__(*args, **kwarg)
