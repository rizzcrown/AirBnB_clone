from models.base_models import BaseModel

class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)