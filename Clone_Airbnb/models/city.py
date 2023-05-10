from models.base_models import BaseModel

class City(BaseModel):
    state_id = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
