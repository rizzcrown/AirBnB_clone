from models.base_models import BaseModel

class Place(BaseModel):
    city_id = ""
    user_id = ""
    name = ""
    decription = ""
    number_rooms = 0
    number_bathrooms = 0
    namx_guest = 0
    prince_by_night = 0
    latitude = float()
    longitude = float()
    amenity_id = ""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
