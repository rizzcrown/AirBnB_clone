from models.base_models import BaseModel

class State(BaseModel):
    name =""

    def __init__(self, *args, **kwarg):
        super().__init__(*args, **kwarg)
